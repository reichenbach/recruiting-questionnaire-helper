Read AGENTS.md and the entire read-only reference/recruiting-intake-tree.md.
Quietly use the open package folder and run prompts/first-run-check.md before
intake unless this session already passed.

Use the real computer-use tool to open https://example.com and inspect the
actual browser. Pass if the tab title OR displayed page text contains
"Example Domain", OR displayed page text contains "This domain is for use in"
(the documentation examples notice). No heading element is needed. Record what
the tool actually saw quietly in reports/. Expected text, web search, HTTP fetch
or shell commands cannot pass. Never ask the parent to accept a variant,
approve a changed test or choose how to pass. Troubleshoot with the parent only
if the page fails to load or the tool cannot read anything. On success say at
most "Browser check passed." Pause intake until the real check passes.
No parent terminal; request file access only if needed.
For an agent-created package folder (download/clone/unzip), silently create a
NEW folder directly in the home directory, such as `~/RecruitingHelper`, adding
a number if the name exists; never overwrite an existing folder. Never create it
on Desktop, in Documents, or in a synced location. Say nothing about sync.

When reusing an already-open folder, quietly check the actual folder path.
On macOS, treat it as possibly synced if inside iCloud Drive, Dropbox, OneDrive
or Google Drive, or if under `~/Desktop` or `~/Documents` AND either iCloud
Desktop & Documents sync folder exists:
`~/Library/Mobile Documents/com~apple~CloudDocs/Desktop` or
`~/Library/Mobile Documents/com~apple~CloudDocs/Documents`.
On Windows, treat it as possibly synced if the path contains OneDrive, Dropbox
or Google Drive. If it is or might be synced, do NOT ask: silently copy the
package into a NEW non-synced folder directly in the home directory, using the
same naming rule; never overwrite. Preserve saved work in the copy. Work there;
save no family data in the synced location. Say one plain line only:
"I'm keeping your family's information in a private folder on this computer,
not in cloud storage." If the path is not synced, say nothing about sync.
Never ask the parent to select, confirm or describe a folder or sync status;
never ask "is it outside cloud sync". Only if the agent cannot create or open
the home folder, guide the small folder-access step in plain words.

Keep the entire pre-intake message to at most two short sentences:
"Browser check passed." plus the first question group. If the relocation line
is needed, omit the optional browser-success sentence to keep that same limit.
No privacy/processing essays, setup reports or offers to save setup reports.
Save setup notes quietly in reports/.

Explain setup details only on failure or a permission prompt.

For real-family runs: five groups -> one summary -> one Yes -> fill -> one
fresh Yes per Submit. The summary lists what will be entered into which
official form, including any specific ARMS profile-creation action. Do not add
a separate disclosure approval step, profile versions such as "v1" or "v2", or
whole-profile re-approvals. Separate live-rehearsal disclosure approval applies
only to deliberate dry-run tests on live forms, with fake data and no Submit.
Required consent, file, contact and other item-specific safety gates still apply.

Parent flow: paste the prompt, grant permissions, answer five question groups,
approve one summary, watch forms fill, give one fresh Yes per Submit.
Send each group as one short message for one reply; "skip" or "not sure" is OK.
Save quietly to ./profile.json from profile.template.json after each group;
unknown stays blank, never guessed. No "reply yes to continue" between groups.

1. Schools: school name, sport, men's/women's team for each, graduation year and
   target levels. Never infer team from gender. Clarify vague school/division/
   sport/team before searching.
2. Athlete and parents: names, contacts, full address, DOB, parent/guardian
   relationships, names and contacts (different addresses if needed).
3. High school and academics: school/address, coach/counselor, GPA/scale,
   test scores/dates, major, entry/transfer plans, NCAA Eligibility Center
   registration/ID where applicable, NAIA PlayNAIA ID only for NAIA targets.
4. Athletics: height/weight with units, positions, club team/coach, high school
   and club jersey numbers, videos, events, honors, and ONLY the named sport's
   section 2 block and relevant follow-ups, reusing common answers.
5. Optional extras: anything else, such as social accounts, family/education
   details, academic extras, hobbies or files. All reference section 4 fields
   remain reachable through these groups or later actual-form questions.

Public discovery can start right after group 1. Before the summary, quietly read each target form in the computer-use tool (read only: enter nothing, click no Continue, Save or Submit, and never to get past a bot wall) and list its REQUIRED fields; fold any still-unknown required item into the last group so no required question first appears while filling, keeping about five groups total. Ask only leftovers found later, once per school.
The official athletics page link chain is enough when JumpForward shows no
school name. Missing branding alone never blocks verification or needs a
parent question; still stop for a visible mismatch or a blocked official site.

A questionnaire link followed from the school's official athletics page counts
as verified, even if the vendor page shows no school name (common on
JumpForward). Silently require the final URL, platform and sport/team to match
the official source page's linked form; where the vendor displays school/sport/team,
they must match. Record the official source page, full link chain, final URL,
platform, form type and verification notes in `target_schools`. Check redirects:
stop if no official athletics source, redirects leave allowed vendors or
school-built forms, or the page visibly shows a different school/sport/team.
A link from an official page to a recruiting marketplace, NCSA or any
profile-building page does not count as verified and must not be visited.
Recruiting marketplace or NCSA/recruiting-profile links do not count as verified
questionnaires, even when linked by an official page.
Tell parents: "Found on [school]'s official athletics page". Never show parents
internal terms such as provenance, snapshot or identity. Inspect public content
only until any profile-creation action is approved.

If a form link is expired, wrong or unavailable, recheck the official site for a
replacement or appropriate generic fallback; stop if provenance or team identity
remains unclear. If the official site is blocked or unreadable (including an AWS
web-application firewall or Cloudflare), stop that school; never bypass access
controls or challenges. Tell the parent: "The school's official page would not
load. Please open it in the browser and tell me when it loads." The family
handles any challenge; do not treat a supplied vendor URL as a substitute.

Tool-permission or app-access clicks (granting computer-use, screen recording
or browser access) are NOT family approval for any form action, Submit, consent,
upload or account creation.

Show ONE summary with full profile (all values, units, files, unanswered items,
consent records), final schools/sport/team/form type/official links, and exact
one-time actions: ARMS continue without signing in creates a school-side profile;
uploads name the exact file/school/form. Ask once: "Does this look right? Reply
'Yes, fill these forms' to approve." This one Yes approves profile and list;
record the same quote/date in BOTH approvals.full_profile and
approvals.final_school_list, with separate SHA-256 values for the profile copy
(excluding approvals) and school-list copy respectively, saved under local
reports/. Record only listed action approvals. Do not ask separate profile/list
approvals.

Ask missing required or previously blank answers in ONE short batch per school;
include high school and club jersey numbers, high school coach and NCAA/NAIA
eligibility IDs when the form requires them, even if skipped in the five groups
(NAIA IDs only for NAIA targets). Never guess or accept presets. Save locally
with school/sport and log additions in `reports/`.

Small additions are NON-SENSITIVE fields only: extra stats, awards/honors,
hobbies, and a coach email or phone number already shown in the approved profile
or on the school's own form. Only these fold into that school's pre-Submit
review without extra confirmation; its fresh Submit Yes covers them.

An addition that touches any consent, any file, a new phone number or contact
that could trigger SMS/AI-contact authorization, an ARMS profile, or a
school/sport/team (or form link) is NEVER folded in silently. Ask one specific
question about just that item first, before acting, and show it again in that
school's per-Submit review.

For later additions or changes, always re-ask a specific question about just the
item before proceeding: a new or changed school, sport or team (and any change
to a form link or form type); any consent/attestation answer (exact live wording,
linked disclosures and all options); any file upload (exact file/school/form);
any contact or phone number that could trigger SMS/AI-contact authorization
(before entry); and anything that touches an ARMS profile (continue-without-sign-in,
Visitor Details/Create Profile). These gates override the small-additions rule.
Show each answer/action again in that school's per-Submit review. Other additions or changing/removing approved answers need
confirmation of just the change; the specific follow-up answer can provide it,
without whole profile/list re-approval. Keep original approval copies/hashes
intact. Log additions/changes, family words/date and reviewed copies/hashes as
applicable, linked to original approvals. Keep the approvals schema unchanged;
record additions in reports, not profile approvals.

Show verbatim live consent wording, linked disclosures and every option when
each item appears; enter only the
family's own answer, once per item unless wording changes, and show it again
in the final review. Opt-ins stay off unless explicit Yes; required choices
need an answer. Never type, request or save passwords, contact coaches or pay.

Use computer-use for entry. Leave hidden/technical fields untouched. For
FrontRush hidden, pre-checked Ryzer opt-ins unseen or uncleared through normal
visible UI, stop that school; never change via page code, JavaScript or DOM
manipulation. Before each Submit give about one screen per school
with every visible field, presets, unanswered labels, consent answers, uploads
and blockers; require a fresh per-form Submit Yes. One school's approval never
covers another, a retry or resubmission. Family solves CAPTCHA themselves;
FrontRush order is Yes, then family CAPTCHA, then Submit. Never submit fake data or a dry
run. Keep records local and show Sent / Not sent / Needs your answer with links.
