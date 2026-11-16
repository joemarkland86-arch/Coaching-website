#!/usr/bin/env python3
"""Write the rendered homepage into index.html so it can be read without JavaScript.

The homepage is a React page. Search engines and AI assistants that do not run
JavaScript would otherwise see an empty page. This script opens index.html in
Chrome, copies what React renders, and stores it inside <div id="root"> between
the prerender markers. React replaces it with the live page when it loads.

Run it after ANY change to the homepage copy or layout in index.html:

    python3 .github/prerender.py            # update index.html
    python3 .github/prerender.py --check    # exit 1 if index.html is out of date

Needs: pip install playwright, plus Chrome or `playwright install chromium`.
With no internet access, pass --react-dir pointing at a folder holding
react.production.min.js and react-dom.production.min.js (React 18.3.1).
"""
import argparse, functools, http.server, pathlib, re, sys, threading

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
START, END = "<!--prerender:start-->", "<!--prerender:end-->"


def render(react_dir, chrome):
    from playwright.sync_api import sync_playwright
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass
    handler = functools.partial(Quiet, directory=str(ROOT))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=chrome, args=["--no-sandbox"]) if chrome else p.chromium.launch()
            page = browser.new_page(viewport={"width": 1280, "height": 900})
            if react_dir:
                d = pathlib.Path(react_dir)
                page.route("**/umd/react.production.min.js", lambda r: r.fulfill(path=str(d / "react.production.min.js"), content_type="application/javascript"))
                page.route("**/umd/react-dom.production.min.js", lambda r: r.fulfill(path=str(d / "react-dom.production.min.js"), content_type="application/javascript"))
            page.goto(f"http://127.0.0.1:{server.server_address[1]}/", wait_until="load")
            page.wait_for_selector("#root main h1")
            html = page.evaluate("document.getElementById('root').innerHTML")
            browser.close()
    finally:
        server.shutdown()
    if START in html or END in html or len(html) < 5000:
        sys.exit("Render looks wrong; index.html not changed.")
    return html


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--react-dir")
    ap.add_argument("--chrome", help="path to a Chrome or Chromium binary")
    a = ap.parse_args()
    src = INDEX.read_text(encoding="utf-8")
    m = re.search(re.escape(START) + r".*?" + re.escape(END), src, re.S)
    if not m:
        sys.exit("Prerender markers not found inside <div id=\"root\"> in index.html.")
    new = src[: m.start()] + START + render(a.react_dir, a.chrome) + END + src[m.end():]
    if a.check:
        sys.exit(0 if new == src else "index.html prerender is out of date. Run: python3 .github/prerender.py")
    INDEX.write_text(new, encoding="utf-8")
    print("index.html prerender updated" if new != src else "index.html prerender already up to date")


if __name__ == "__main__":
    main()
