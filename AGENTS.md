# Website agent instructions

## Purpose
Help improve joemarkland.co.uk as Joe Markland's personal coaching website.
Keep GAP Profile (https://gapprofile.co.uk) distinct as the linked self-reflection product.
Optimise for visitor understanding, justified trust and a working next step.

## Read first
Read WEBSITE_TEAM.md, the current index.html, CNAME and deployment workflow before edits.
Current implementation: static index.html with React 18 loaded from CDN; no package manifest or build pipeline.
Home, About and Parents are hash-based routes. Preserve direct links, refresh and back/forward navigation.
Keep the existing stack unless a specific requirement justifies a change.

## Working rules
- Use plain British English. Be specific, warm and credible; avoid generic coaching promises.
- Never add source=chatgpt or other unrequested attribution parameters to links.
- Keep GAP Profile as the primary homepage CTA. Preserve secondary contact routes.
- Never invent testimonials, qualifications, client results, validation or scientific support.
- Treat existing website claims as copy to verify, not evidence that they are true.
- Do not describe GAP Profile as a diagnosis or a validated instrument without evidence.
- Confirm current commercial terms from Joe's approved brief before changing prices; old site copy may be stale.
- Do not put private conversations, coaching notes, client data, credentials or personal business plans in this public repository.
- Work on a separate branch. Inspect the diff before committing.
- Prepare reversible changes and reviewable drafts autonomously within the requested scope.
- Ask Joe before merging/publishing, spending money, contacting people or making irreversible changes.
- main deploys to GitHub Pages automatically. A merge is a publication action.
- Do not run workflow_dispatch as a preview mechanism.
- Do not add automation, dependencies, analytics or paid services merely to run the team.
- State what was actually tested. Never mark browser, payment or delivery checks passed from code inspection alone.

## Team workflow
Use the role prompts and handoff format in WEBSITE_TEAM.md.
The lead owns scope; researcher owns evidence; writer owns words; builder owns implementation; reviewer owns acceptance.
Roles may be run sequentially in one session. These files do not create background agents or scheduled tasks.
Use separately delegated agents only where the user/runtime authorises them; otherwise label review as a separate review pass, not an independent agent.
Only the builder edits site implementation during a task. The lead coordinates documentation.
Return failed checks to their owner, then review the updated diff.

## Definition of done
Deliver a focused diff, evidence for the change, applicable test results, known limitations and a reviewable PR.
For website changes, check affected routes, mobile/desktop layouts, keyboard operation, assets, external destinations and browser console.
For documentation-only changes, check consistency and links/paths; no application test suite is needed.
