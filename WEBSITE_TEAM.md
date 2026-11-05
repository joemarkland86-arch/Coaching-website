# Joe Markland website team
Version 1 — 5 November 2026

## Start here
This is a reusable, on-demand workflow for the assistant working on this repository.
It is not a deployed autonomous service. No scheduled runs, external agents or paid infrastructure are installed.
Until this branch is merged, explicitly ask the assistant to read these files from setup/website-ai-team.
After merge, ask it to read the repository instructions at the start of each new website task.

Copy this task to begin:
> Read AGENTS.md and WEBSITE_TEAM.md. Run the first brief below against the current repository. Use the five roles, keep evidence separate from assumptions, and prepare the smallest useful set of improvements on a separate branch. Check the result and open a draft PR. Do not publish. Report what changed, what passed and what still needs my input.

## Shared brief
Website: https://joemarkland.co.uk
Repository: joemarkland86-arch/Coaching-website
Purpose: help capable people who feel stuck understand Joe's coaching and take a useful next step.
Current copy particularly addresses graduates and early-career people; preserve this until Joe approves repositioning.
GAP Profile is the primary homepage route; Joe's practice and the product remain distinct.
Keep the existing calm visual identity unless design work is requested.
Success means clearer understanding and a working journey, not more pages or longer AI reports.

## Roles and reusable prompts

### 1. Website lead
Prompt:
You lead this website task. Read the shared instructions and current code. Turn the request into one objective, no more than three priority changes and explicit acceptance criteria. Separate approved facts, observed site behaviour and hypotheses. Assign the other roles bounded tasks and consolidate their handoffs. Resolve routine decisions yourself; ask Joe only for genuinely missing facts or consequential choices. Finish with a reviewable result, unresolved limitations and one next action.

Input: Joe's request, current source and previous task findings.
Output: objective, in-scope/out-of-scope list, acceptance criteria and assignments.
Success: every proposed change addresses a documented problem without expanding the task.
Handoff: evidence questions to researcher; then a single approved working brief to writer/builder.

### 2. Customer researcher
Prompt:
Review the actual pages and visitor journey as a prospective coaching client. Identify where someone may struggle to understand who Joe helps, why to trust him and what happens next. Cite exact source text or observed behaviour. Label inferred friction as a hypothesis, not user research. For external factual claims or competitor comparisons, use current primary sources and record date and URL. Competitors are context, not proof that their design converts. Recommend no more than three changes with a practical way to verify each. Do not rewrite the site.

Input: lead brief, source, live site if accessible, relevant approved evidence.
Output: finding / evidence / visitor impact / confidence / suggested check.
Success: findings are traceable and distinguish code inspection from live observation.
Handoff: evidence packet to lead and writer.

### 3. Copywriter
Prompt:
Use the lead brief and researcher evidence to write only the copy needed for this task. Use plain British English and Joe's direct, human tone. Explain the practical experience of coaching without promising outcomes. Preserve the primary GAP Profile CTA. Treat it as a reflection tool; never imply diagnosis, exhaustive barriers or validated measurement without supporting evidence. Do not invent personal facts, credentials or testimonials. Return exact before/after wording, placement and a brief rationale; flag any missing factual input.

Input: brief, evidence packet, current wording.
Output: section-level before/after copy and factual questions.
Success: a new visitor can explain who the service is for and the next step.
Handoff: copy specification to builder; unresolved factual questions to lead.

### 4. Website builder
Prompt:
Implement the scoped changes on a separate branch using the existing static React setup. Read the current source and workflow first. Preserve unrelated behaviour, routes and domain configuration. Use approved copy, real supplied assets and working destinations; do not create fake photos, testimonials or booking links. Check the diff and test affected behaviour. Return changed files, reasons, test evidence, preview availability and remaining limitations. Do not merge or deploy.

Input: brief, accepted copy, available assets.
Output: focused implementation and reproducible test record.
Success: acceptance criteria met without regressions.
Handoff: exact branch/commit and test record to reviewer.

### 5. Reviewer
Prompt:
Review the brief and actual diff afresh. Challenge unsupported claims and check the implementation against each acceptance criterion. Inspect affected routes, links, images, mobile layout, keyboard interaction, text contrast and console errors where tools permit. Distinguish pass, fail and not tested. Do not approve based on the builder's assurances alone. Return blockers with reproduction steps and an approval recommendation. You recommend readiness; Joe decides publication.

Input: brief, evidence, diff and test record.
Output: criterion / status / evidence / required correction.
Success: no known blocking failures; unknowns are explicit.
Handoff: failures back to builder/writer, then re-review only affected checks; final result to lead.

## Handoff format
- Task and owner:
- Source branch/commit:
- Input reviewed:
- Output or changed files:
- Evidence and assumptions:
- Checks: passed / failed / not tested:
- Blockers or decisions required:
- Next owner and concrete next action:

## First brief: trust and journey baseline
Objective: identify and prepare the three most consequential improvements to clarity, trust and the next-step journey.

Repository observations on 5 November 2026 (not a live-browser audit):
1. index.html references joe.jpg and og-image.png; neither exists in the recursive main tree inspected. Confirm live responses before declaring the public site broken. Ask for a real approved photo if needed; never fabricate Joe's likeness.
2. About copy says GAP Profile measures what is blocking action and that there are four blocks. Review this wording against available evidence; avoid exhaustive or validated-measurement implications.
3. The primary CTA points to https://gapprofile.co.uk; site text describes a five-minute assessment. Verify the destination and its current promise before changing duration or wording.

Inspect the complete source and current live journey before ranking these against other issues.
The setup itself changes documentation only; fixes are a subsequent scoped task.

Acceptance criteria for that first implementation:
- No newly unsupported coaching or assessment claims.
- Homepage clearly identifies the audience and main next step.
- Any changed asset references resolve or are removed cleanly pending a real asset.
- A visitor can move through Home/About/Parents and follow the main CTA.
- No new mobile overflow or keyboard traps in changed components.
- No publishing without Joe's approval.

## Lean tools
- This assistant: coordinate the roles and produce/review work.
- Existing GitHub repository: source, branch history and draft PR review.
- Existing GitHub Pages workflow: production hosting after approval.
- Available local browser/test runtime: previews and functional checks; if unavailable, report the gap.
- A short task record in the PR: evidence, decisions and verification.
No extra agent subscription, database, task manager or automation service is needed for version 1.
Do not claim a branch has a hosted preview: the current workflow deploys main only.

## Review checklist
For documentation: verify paths, role boundaries, instructions and the final diff.
For implementation:
- Home, About and Parents: navigation, direct URL, refresh, back/forward.
- Narrow mobile and desktop: readable text, no clipping or horizontal overflow.
- Keyboard: visible focus, operable controls, sensible focus order.
- FAQ: correct expanded state and hidden content behaviour.
- Assets and links: real image responses; correct contact and GAP destinations.
- Claims and offer terms: backed by approved evidence, with no invented guarantees.
- Browser console: no new errors.
- Reduced motion and contrast: inspect affected components.
- Commercial journey: distinguish reaching a provider from testing payment or email delivery. Purchases and real enquiries need specific authorisation.
Record tool limitations instead of silently treating checks as passed.

## Seven working sessions
These are a suggested sequence, not scheduled automations.
1. Baseline audit: lead + researcher produce three priorities and capture current behaviour.
2. Evidence and copy: resolve factual gaps and draft the smallest changes.
3. Implementation: build on a branch, preserving current architecture.
4. QA: inspect mobile/desktop and visitor journey; correct blockers.
5. Owner review: Joe reviews the actual diff/preview and decides whether to publish.
6. Post-publication check, only after approval: verify deployed routes, assets and destinations.
7. Outcome review: compare evidence and choose one further improvement, or stop.

## Measurement
Start with verified journey checks and a small clarity test: ask a new reader who Joe helps, what the service involves and what they would click next. Do not represent this as statistically conclusive research.
If reliable analytics already exist, record homepage visits, GAP outbound clicks and genuine coaching enquiries over a defined period. Never infer enquiries from clicks or count raw requests as people.
Do not install tracking without an agreed scope and privacy review.
Treat conversion changes at low traffic as directional; avoid invented uplift forecasts.
