# Recruiting questionnaire helper for families

**Paste the prompt → grant permissions → answer about five groups of questions
→ approve one summary → watch it fill the forms → give one Yes per Submit.**

Paste all of [START_PROMPT.md](START_PROMPT.md) into Codex in the ChatGPT desktop
app. The helper uses the package folder already open, checks browser access,
and starts the questions. You never need a terminal. It handles necessary free
setup and only explains extra steps if access fails or a permission prompt
appears. Grant the app permissions you approve; handle sign-in yourself.
Tool-permission or app-access clicks (granting computer-use, screen recording
or browser access) are NOT family approval for any form action, Submit, consent,
upload or account creation.

The public package is at
https://github.com/reichenbach/recruiting-questionnaire-helper
An existing local or bundled copy works too.
Quietly check the actual folder path, including whether Desktop/Documents
syncs to iCloud/OneDrive. If inside iCloud Drive, Dropbox, OneDrive or Google
Drive (or a Desktop/Documents folder syncing to iCloud/OneDrive), do not ask the
parent: copy the package to a NEW non-synced folder in the home directory, such
as `~/RecruitingHelper`, adding a number if the name exists; never overwrite an
existing folder. Say only: "I'm keeping your family's information in a private
folder on this computer, not in cloud storage." Work there; save no family data
in a synced location. If the app cannot open that folder, guide the small
folder-access step. If the folder is not synced, say nothing about sync.

**Other apps:** [CHATGPT_PROMPT.md](CHATGPT_PROMPT.md) is a self-contained rules
backup for ChatGPT Work with Computer Use; local file access is still needed to
save family data. [CLAUDE_PROMPT.md](CLAUDE_PROMPT.md) supports Claude computer
use; see [CLAUDE.md](CLAUDE.md) and https://support.anthropic.com.
[CURSOR_PROMPT.md](CURSOR_PROMPT.md) supports Cursor's built-in Browser; open the
package in Cursor Agent chat. Those app-specific launchers may describe extra
steps; the current package workflow is in [AGENTS.md](AGENTS.md).

## Setup and access

The helper checks actual access rather than relying on a subscription name.
Before asking family questions it uses the computer-use tool to open
`https://example.com` and inspect the browser. Displayed page text must contain
**Example Domain**; a search or fetch cannot pass. Success needs at most
"Browser check passed." If it fails, intake pauses while the helper explains
the relevant fix. You never need to run commands or buy extra access.

If setup is needed, see [first-run check](prompts/first-run-check.md). In
Codex/ChatGPT desktop this may involve Plugins > Computer Use, server and skill
toggles, Try now and Settings > Computer use browser access. Mac permissions may
include Screen Recording and Accessibility; older Intel Macs may not be
supported. On Windows the tool uses the foreground, pointer and keyboard: keep
the browser visible, PC unlocked and connected, and do not use it meanwhile.
The helper explains those details only on failure or a permission prompt. You
can stop or take over at any time. Official setup help:
https://learn.chatgpt.com/docs/computer-use and https://help.openai.com.

If a package download is needed, every runtime repo/file fetch uses a bounded
timeout and handled errors. If private, 404, offline or blocked, the helper says:
"I couldn't open the online package, so I'll use a local copy or ask you to share it."
Try once only: no retry loops, alternate download methods/endpoints or sign-in
attempts after failure. It uses the open folder, bundled copy or supplied
ZIP/folder without more network attempts after failure. If none is usable, it
asks for a pasted/shared package and explains what's missing; it must never
crash or stall. The backup's inline rules and examples remain available after
an optional reference fetch fails, but family data still needs local storage.

## Questions and one summary

Each group is one short message you answer in one reply. Say "skip" or "not
sure" for anything you cannot answer. The helper saves quietly after each group;
there are no "reply yes to continue" steps.

1. **Schools:** school, sport, men's/women's team for each, graduation year and
   target levels. Vague names are clarified before searching.
2. **Athlete and parents:** names, contacts, full address, date of birth and
   parent/guardian relationships, names and contacts.
3. **High school and academics:** school/address, coach/counselor, GPA/scale,
   test scores/dates, major, entry/transfer plans and eligibility center details
   where applicable. NAIA IDs are requested only for NAIA targets.
4. **Athletics:** height/weight with units, positions, club team/coach, high
   school and club jersey numbers, videos, honors, events and only your sport's
   questions.
5. **Optional extras:** anything else you want to add, such as social accounts,
   family/education details, academic extras, hobbies or files.

All reference fields remain available; optional or sensitive questions can be
skipped. Unknown answers stay blank. The helper never guesses, invents numbers,
calculates missing statistics, converts units or chooses a different school to
get past a field. It can retry digits only after a phone format error (CMU
requires this), changing punctuation, never the number; it asks if that still fails.

It may find public forms after the schools group. A questionnaire link followed
from the school's official athletics page counts as verified, even if the vendor
shows no school name. You see "Found on [school]'s official athletics page". The
helper checks that the final URL, platform and sport/team match the official
page's linked form and records the link chain and form type locally. Any school,
sport or team shown by the vendor must match. Recruiting marketplace or
NCSA/recruiting-profile links do not count as questionnaires and must not be
visited. Supplied video/social/profile links are form data, not browsing targets.
If the official site is blocked or unreadable, that school stops. The helper
says the school's official page would not load and asks you to open it in the
browser and say when it loads; it never bypasses a firewall or challenge.

Before entry you see ONE summary: all profile values, units, files, unanswered
items and consent records; each school's sport/team, form type and official
form link; and any specific one-time actions requested. Reply **"Yes, fill these
forms"** once to approve the profile and school list together. The helper saves
copies under local `reports/` and records that one Yes in BOTH
`approvals.full_profile` and `approvals.final_school_list`, with the same quote
and date and separate SHA-256 values for the profile copy (excluding approvals)
and school-list copy respectively. You approve them together.

The same Yes can approve actions explicitly listed there: for example ARMS
"continue without signing in, which creates a profile on the school's side",
Visitor Details/Create Profile disclosure, a named account creation or Personal
Contacts Save, or an exact file uploaded to a named school/form. Unlisted actions
still need specific approval. This Yes never authorizes Submit.

Missing required answers are asked in one short batch per school, including
high school and club jersey numbers, high school coach and NCAA/NAIA eligibility
IDs when required, even if skipped earlier (NAIA IDs only for NAIA targets).
Small additions are non-sensitive fields only: extra stats, awards/honors,
hobbies, and a coach email or phone number already shown in the approved profile
or on the school's own form. Only these fold into that school's per-Submit
review without extra confirmation, covered by its fresh Yes.

For later additions or changes, the helper always re-asks about just the item:
a new or changed school, sport or team, any form link or form type change; any
consent/attestation answer, with exact live wording, linked disclosures and all
options; any file upload, naming the exact file/school/form; any contact or
phone number that could trigger SMS/AI-contact authorization, before entry; and
anything that touches an ARMS profile, including continue-without-sign-in and
Visitor Details/Create Profile. These gates override the small-additions rule.
Other additions or changes/removals need brief confirmation of just the change. Your specific follow-up answer can provide it.
Each answer/action appears again in that school's per-Submit review; the whole
summary is not repeated. Original reviewed copies stay intact and additions and
changes are logged locally.

## Filling and sending

Stay available for form questions. Every consent, attestation, signature or
terms request is shown with verbatim live wording, all options and needed
linked disclosures. Only you answer, once per item unless wording changes; the
answer appears again in the final review. Implicit phone/SMS/AI-contact notices
need approval before entering the number. Opt-ins stay off unless you explicitly
say Yes; required choices need your answer. For NCSA/IMG Academy the helper
proposes "No thanks" and waits for your own answers. See the
[Opt-in rule](AGENTS.md#opt-in-rule).

The helper verifies high-school lookup matches, asks for missing details and
never selects a different school or bypasses disabled fields. JumpForward uses
school name only and has no not-listed option. Every preset must match your
answer. If unknown, it stops and labels it, for example: "Site preset Yes - NOT
the family's answer; needs your answer". FrontRush relationship "Other" needs
confirmation; unusual position mappings do too. Personal Contacts Save needs
specific approval as part of filling. If a pre-checked opt-in such as FrontRush
Ryzer cannot be seen or cleared through normal visible UI, that school stops;
it is never changed through code. Coalinga's not-listed checkbox erases School
Name, so the helper re-types and verifies it.

Before **each Submit**, review about one screen per school: school/team/link,
every visible field/value or blank, presets and confirmed answers, unanswered
labels, new answers, consents, uploads and blockers. Hidden/technical fields
stay untouched and are omitted; hidden consent blockers are explained plainly.
Resolve blockers, then give a fresh per-form Yes. Approval for one school never
covers another, a retry or resubmission. FrontRush order: **your Yes, you solve
the CAPTCHA, then Submit**. The helper never solves/bypasses CAPTCHAs. Fake data
and dry runs never submit, even if later asked.

Results show one line per school with sport/team and link: **Sent** only after
confirmation, **Not sent: why**, or **Needs your answer: what**. Detailed evidence,
actions and times stay in local `reports/`. An uncertain send may already have
gone through; the helper does not retry automatically or resend confirmed forms.
After a pause it reads local records, checks the page and asks again before
Submit. Usage limits may change; use the app's usage display. No message count
is promised and no extra usage is purchased.

The helper never contacts coaches by email, message, call or any channel; never
makes payments; and never types, requests or saves passwords. You handle sign-in.
It cannot promise admission, eligibility, recruiting interest or scholarships.

## Privacy and package contents

Family data is saved only in local `profile.json` and ignored `reports/`, plus
`screenshots/` if needed. Never commit/share profiles, reports, documents,
screenshots, passwords or secrets. `.gitignore` helps prevent accidental Git
inclusion; it does not encrypt files or prevent sharing. Chat/computer-use is
not an offline-processing promise. Approved form entry discloses data to the
school/provider, and a form may save before Submit. No additional cloud
summaries, remote profiles, documents or reporting are created.

- [AGENTS.md](AGENTS.md) defines the current rules. Stage prompts:
  [start](prompts/start.md), [find](prompts/find-forms.md),
  [fill](prompts/fill-forms.md), [report](prompts/report.md).
- [profile.template.json](profile.template.json) has blank common fields and
  all 14 sport blocks; unused blocks stay blank.
- [Reference tree](reference/recruiting-intake-tree.md) is read-only research;
  [sample forms](reference/sample-forms.md) copies section 5 including gaps.
- [reference/verified-forms.md](reference/verified-forms.md) has four women's
  volleyball examples dated 2026-10-23; recheck official links live. Dated notes
  never authorize filling or submission.
- [test/README.md](test/README.md) covers offline checks and synthetic fixtures.
  Dry runs never submit; real forms may save even before Submit.

## Notes for someone sharing this package

The repository is public. Package source:
https://github.com/reichenbach/recruiting-questionnaire-helper
Keep a ZIP/folder fallback available for offline or blocked downloads. Do not
change repository visibility during setup. Share only instructions, blank
template, prompts, references and synthetic test files. Inspect first and exclude
private profiles, reports, documents, screenshots, passwords and secrets. Never
put real family data in the shareable fixtures.
