Help my family fill college recruiting questionnaires. I am using Claude:
computer use in the Claude desktop app, or Claude in Chrome, whichever my plan
and app offer. Claude Code is optional. I never use a terminal; do the setup
yourself. For a new family: paste this, grant permissions, answer five groups,
approve one summary, watch forms fill, give one fresh Yes before each Submit.

Package source:
https://github.com/reichenbach/recruiting-questionnaire-helper
Quietly reuse the package folder this app has open, or a bundled copy, without
overwriting saved work. Otherwise make one fetch with a bounded timeout and
handled errors. For EVERY runtime repo/file fetch, try once only. If private,
404, offline or blocked, say: "I couldn't open the online package, so I'll use
a local copy or ask you to share it." No retry loops, other download methods or
sign-in attempts after a failure; use a local or bundled copy, or ask me to
share the package and say what is missing. Never crash or stall.

Prompt-resident rule: the pasted START_PROMPT.md / CHATGPT_PROMPT.md text is the
source of truth for the Resume check, relocation rule, "Anything changed?" recap
and never-blank rule. It wins over stale package files (AGENTS.md, README.md or
prompts) that lack the Resume check section. Never fall back to starting a fresh
intake because a package copy is stale. Keep these prompt-resident rules even if
every available package copy is stale.

Package choice: if the opened folder has no AGENTS.md (for example,
`~/Documents/projects`), search one and two levels down for package copies:
folders with both AGENTS.md and profile.template.json. Prefer a copy whose
AGENTS.md contains "Resume check"; among those, choose the newest AGENTS.md
modification time. Never silently pick a copy lacking it when one with it
exists. If none has it, use the newest copy and still apply the prompt-resident
rules. Keep the original opened path for the saved-profile search and include
all discovered package copies as profile candidates, not just the chosen copy.
Do not tell the parent about package selection or stale copies.

Defer creating or relocating a working folder until the browser check and
resume check below; use the available open/local package for setup. Do not
collect new family answers during setup. Search before making any home folder.
For an agent-created package folder (download/clone/unzip), silently create a
NEW folder directly in the home directory only if no saved folder can be reused
or relocation is required, such as `~/RecruitingHelper`, adding a number if the
name exists; never overwrite an existing folder. Never create it on Desktop,
in Documents, or in a synced location. Say nothing about sync.

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

Resume check: quietly, after the browser check passes and before any question,
look for an existing `profile.json` from this package. Its folder must also
contain `profile.template.json` or `AGENTS.md`, except that every
`~/RecruitingHelper*` folder holding a profile with answers is a candidate even
if its package files are stale or missing. Do the resume check BEFORE copying a
package into any numbered home folder. Copying a package copy, which may contain
a stale or blank profile.json, into a new numbered folder is only allowed when
no saved profile with answers exists. Never create RecruitingHelperN when one
with data exists in a non-synced folder; reuse it directly. Relocating saved
work from a synced folder is still allowed under the relocation rules, after
this search; this is not permission to copy a package-only folder first.
Search in this order:

- The folder the agent was opened from (remember its original path).
- `~/RecruitingHelper*`, including `~/RecruitingHelper`,
  `~/RecruitingHelper2`, `~/RecruitingHelper3` and later numbered folders.
- Sibling folders one level up from the opened folder, then folders directly
  under `~/Desktop`, `~/Documents` and `~/Documents/projects`; in this last
  search include folders whose name contains "recruit" (case-insensitive) or
  that contain `profile.template.json`.

Inspect all candidates; ignore profiles equal to the blank template or with
no answers. Metadata, approvals and `intake.dry_run` alone are not answers;
explicit false/zero answers count. Pick the profile with answers whose
`profile.json` has the newest modification time across all locations (search
order breaks ties). If several have answers, mention only the newest one.

Reuse that profile. Never replace, blank, reset or overwrite a profile that
has answers with the template. Never start a fresh intake over it unless the
parent says in their own words to start over; first keep a timestamped backup
under local ignored `reports/`. Do not interpret `intake.dry_run=true` as a
reason to discard answers. If the selected folder is non-synced, work in it
directly; do not create another folder. If the selected source or opened folder
needs relocation under the sync rules, silently copy the selected package to a
NEW non-synced home folder under the existing naming rule. A non-synced folder
with saved answers takes precedence over relocating the opened folder.
Never create an empty duplicate home folder when one with data exists.

Refresh stale package files in the selected saved folder from the
opened/selected newest package only after selecting the saved profile. Compare
only this allowlist: AGENTS.md, README.md, prompts/, reference/, test/,
.cursor/, CLAUDE.md, CLAUDE_PROMPT.md, CURSOR_PROMPT.md, CHATGPT_PROMPT.md,
START_PROMPT.md and profile.template.json. If they differ, first copy the old
versions to `reports/package-backup-<timestamp>/`, preserving relative paths;
then update ONLY those package files from the newest package. Do not delete
other files or copy the whole package over the saved folder. NEVER touch
profile.json, existing reports/ contents, approvals logs or any family data. The
only reports/ changes are adding the backup folder and a one-line note in
reports/ recording the refresh. Do not overwrite an existing backup or follow
symlinks into family data. Say nothing to the parent. If the selected source
must be relocated, copy saved work under the rules below before refreshing in
the private folder.

When changing working folders, copy (never move or delete) `profile.json`,
`reports/` and the saved approvals log (including `reports/approvals.log`)
into the working folder. Never overwrite anything already there that is newer;
retain conflicting older copies in timestamped local backups, including any
answered profile before replacing it with another saved profile. Preserve
reviewed copies, hashes and log history; do not silently merge answers or
rewrite approvals. Leave older folders untouched. Work and save family data
only in the selected non-synced package folder after this check.

The recap must be the first parent message after "Browser check passed." when an
answered profile exists anywhere in the search (with only the required
relocation line allowed before it). A first message asking a question group
while an answered profile exists is a failure. Matt's regression scenario:
opened in `~/Documents/projects` without AGENTS.md, stale package copies there
and in `~/RecruitingHelper*`, saved dry_run profile in
`~/RecruitingHelper2/profile.json` -> recap labeled
"Test profile (made-up athlete)" + "Anything changed?", never group 1.

Show ONE short recap, about six lines maximum: athlete, graduation year,
sport/team, target schools and levels, parent contact names, and what is still
blank. Then ask exactly one question: "Anything changed?" Do not restart the
five groups or re-ask any answer already in the profile. After that reply, ask
only what is blank AND required, once in one batch per school, and only items
the parent says changed. Previously asked blanks stay Needs-your-answer; do
not ask them again. Keep all item-specific safety gates for proposed actions.

Name the athlete in the recap's first line. If the parent says it is a different
athlete or family, or the reply is unclear, do not use the profile: ask once,
and for a different athlete or family run the five groups in a NEW numbered home
folder, leaving the saved folder untouched. A real-family profile
(`intake.dry_run` false) beats a newer test profile. Approvals on a
`dry_run=true` profile never authorize a real form. The reviewed school-list
copy must list every one-time action still wanted (ARMS profile creation,
uploads, accounts); any action not listed there needs its own question.

For `intake.dry_run=true`, reuse the answers for rehearsals with the recap's
first line labeled "Test profile (made-up athlete)". Keep `dry_run=true` and
never present it as the real family. Prefer offline rehearsal; live rehearsal
needs separate disclosure approval before fake data goes to any real form,
plus specific ARMS/profile, consent, contact and upload approvals as applicable.
Never submit a dry run or fake data. If the parent says this is a real family
or wants to start fresh, save a timestamped backup of the test profile first,
then create a new blank profile in the working folder and run the normal five
groups. Never silently convert test answers into real-family answers.

Saved approvals alone never carry over as permission to fill or Submit.
If the recap shows no change, the existing summary approval applies only after
verifying BOTH recorded SHA-256 values still match the current profile
(excluding approvals) and school list against the saved reviewed copies.
Missing approvals/copies or a hash mismatch means show the one summary again
and obtain its Yes before filling. Keep original approval copies/hashes intact;
record a renewed review separately in local `reports/`. Every Submit still
needs a fresh per-school Yes; never resend confirmed forms. Consent wording,
exact-file uploads, contact authorizations, ARMS profile actions, family-only
passwords/CAPTCHAs and the FrontRush Ryzer stop retain every existing gate.

If no profile with answers exists anywhere in the search, use the unchanged
brand-new-family flow: create `profile.json` from `profile.template.json`,
five groups, one summary, one Yes to fill, one fresh Yes per Submit.

Keep the entire pre-intake message to at most two short sentences plus the
recap block on resume: optional "Browser check passed." and "Anything changed?"
For a brand-new family, "Browser check passed." plus the first question group;
if the relocation line is needed, omit the optional browser-success sentence.
On resume the relocation line may be one more sentence before the recap.
No privacy/processing essays, setup reports or offers to save setup reports.
Save setup notes quietly in reports/.
Read CLAUDE.md, AGENTS.md, README.md, prompts/ and all of reference/recruiting-
intake-tree.md; AGENTS.md wins. The ChatGPT/Codex menu steps do not apply to
Claude. Never edit the reference or template, use the test fixture for my
family, commit or publish.

Use the real computer-use tool to open https://example.com and inspect the
actual browser. Pass if the tab title OR displayed page text contains
"Example Domain", OR displayed page text contains "This domain is for use in"
(the documentation examples notice). No heading element is needed. Record what
the tool actually saw quietly in reports/. Expected text, web search, HTTP fetch
or shell commands cannot pass. Never ask the parent to accept a variant,
approve a changed test or choose how to pass. Troubleshoot with the parent only
if the page fails to load or the tool cannot read anything. On success say at
most "Browser check passed." Pause intake until the real check passes.

Use the same tool for forms (computer use or Claude in Chrome). Playwright or
other scripts never count. Explain permission prompts (Screen Recording,
Accessibility, Chrome extension site access) only when they appear or something
fails. I grant permissions and handle every sign-in; never type, request or
save passwords, bypass a prompt or buy anything. If it cannot work, explain and
pause. Collect no family information until the check passes.

For brand-new real-family runs: five groups -> one summary -> one Yes -> fill ->
one fresh Yes per Submit. The summary lists what will be entered into which
official form, including any specific ARMS profile-creation action. Do not add a
separate disclosure approval step, profile versions such as "v1" or "v2", or
whole-profile re-approvals. Separate live-rehearsal disclosure approval applies
only to deliberate dry-run tests on live forms, with fake data and no Submit.
Required consent, file, contact and other item-specific safety gates still
apply.

For a new profile only, ask five short question groups, one reply each: schools; athlete and
parents; high school and academics; athletics (only the named sport's
questions); optional extras. "Skip" or "not sure" is fine; unknown stays blank.
Save quietly to profile.json (from profile.template.json) after each group; no
"reply yes" between groups. Never infer team from gender. Before the summary,
quietly read each target form in the interactive browser tool (never to get past
a bot wall) and list its REQUIRED fields; fold any still-unknown required item
into the last group so no required question first appears while filling, keeping
about five groups total. Ask only leftovers found later, once per school.

The official athletics page link chain is enough when JumpForward shows no
school name. Missing branding alone never blocks verification or needs a
parent question; still stop for a visible mismatch or a blocked official site.

Find forms from each school's official athletics page. A link followed from that
page counts as verified even if the vendor shows no school name (JumpForward);
tell me "Found on [school]'s official athletics page". Quietly check the final
URL, platform and sport/team match the link text. Stop if a redirect leaves the
allowed vendors or school forms, or the page shows a different school, sport or
team. A link to a recruiting marketplace, NCSA or other profile-building page is
not verified; do not use it. If a bot wall blocks the official site, ask me to
load it; never bypass it.

Before entering family data show ONE summary: my full profile, the final school
list (school, sport/team, form type, official link) and one-time actions: ARMS
"continue without signing in, which creates a profile on the school's side",
exact file uploads (file, school, form), any account and any Personal Contacts
Save. Ask: "Does this look right? Reply 'Yes, fill these forms' to approve."
That one Yes approves the profile, list and listed actions only. Save reviewed
copies in reports/; record the same quote and date with separate SHA-256 values
in approvals.full_profile and approvals.final_school_list. It never approves
Submit. Ask missing or blank answers in one short batch per school. Ask each
blank once; after "not sure" or no answer, keep it as Needs-your-answer and do
not repeat it in later replies. Small additions are non-sensitive fields only:
extra stats, awards/honors, hobbies, and a coach email or phone number already
shown in the approved profile or on the school's own form. Only these fold into
that school's pre-Submit review without extra confirmation; its fresh Submit
Yes covers them. No whole-summary re-approval. Always ask
again, in just the change, for: a new or changed school, sport, team or form
link; changing or removing an approved answer; any consent answer; any file;
any new phone or contact that could trigger SMS or AI-contact authorization;
anything involving an ARMS profile.

Fill only with computer use or Claude in Chrome, in a new tab. A tool-permission
click or "always allow" is never approval. Never guess, convert units or invent
digits; for a format error, re-enter the same phone digits only. Ask high
school and club jersey numbers, high school coach name and NCAA ID (NAIA ID only
for NAIA targets) when a form needs them. Confirm every preset. Show every
consent word for word with all options and linked disclosures; enter only my
answer. For NCSA/IMG Academy propose "No thanks" and wait. Show any SMS/AI
contact authorization BEFORE entering a mobile number. If the FrontRush Ryzer
opt-in is hidden or can't be cleared in the normal visible UI, stop that school
and explain; never change it via code, JavaScript or the page's DOM. I solve
every CAPTCHA and sign-in myself. No passwords, payments, coach contact or
marketplaces.

Before each Submit show about one screen for that school: link, every visible
field and value, presets with confirmed answers, consent answers, uploads and
Needs-your-answer items. Ask "Approve submitting this reviewed questionnaire to
[school/team] at [URL] now?" and wait for my fresh Yes for that school. For
FrontRush: my Yes, then I solve the CAPTCHA, then Submit. Never submit a dry
run or fake data. Never retry an uncertain submit. Report each school in one
line with its link: Sent / Not sent: why / Needs your answer: what. On resume
re-read saved records and ask again before Submit; never resend.

If you cannot save local files, follow the no-local-files rules in
CHATGPT_PROMPT.md with these Claude steps. Chat is processed by Anthropic, not
offline storage; a form may save data before Submit. Usage limits may change;
see https://support.anthropic.com and the app's usage display. Never buy extra
usage; if it runs out, save progress and explain how to resume. Start now.
