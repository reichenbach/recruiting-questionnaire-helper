Read AGENTS.md section 0 before intake. Quietly reuse the open package folder
without replacing saved work; request file access only if needed.
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

Resume check: quietly, after the browser check passes and before any
question, look for an existing `profile.json` from this package. Its folder
must also contain `profile.template.json` or `AGENTS.md`. Search in this order:

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

When changing working folders, copy (never move or delete) `profile.json`,
`reports/` and the saved approvals log (including `reports/approvals.log`)
into the working folder. Never overwrite anything already there that is newer;
retain conflicting older copies in timestamped local backups, including any
answered profile before replacing it with another saved profile. Preserve
reviewed copies, hashes and log history; do not silently merge answers or
rewrite approvals. Leave older folders untouched. Work and save family data
only in the selected non-synced package folder after this check.

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

Use START_PROMPT.md's source or an existing local/bundled copy. For EVERY
runtime repo/file fetch, try once only with a bounded timeout and handle errors.
If private, 404, offline or blocked, say:
"I couldn't open the online package, so I'll use a local copy or ask you to share it."
No retry loops, alternate download methods/endpoints or sign-in attempts after
failure. Continue from the open folder, bundled copy or supplied ZIP/folder,
without more network attempts after failure. If none is usable, ask the family
to paste or share the package and explain what is missing; never crash or stall.
Save no family data during setup. Never invent missing package instructions.

Tool-permission or app-access clicks (granting computer-use, screen recording
or browser access) are NOT family approval for any form action, Submit, consent,
upload or account creation.

For brand-new real-family runs: five groups -> one summary -> one Yes -> fill ->
one fresh Yes per Submit. The summary lists what will be entered into which
official form, including any specific ARMS profile-creation action. Do not add a
separate disclosure approval step, profile versions such as "v1" or "v2", or
whole-profile re-approvals. Separate live-rehearsal disclosure approval applies
only to deliberate dry-run tests on live forms, with fake data and no Submit.
Required consent, file, contact and other item-specific safety gates still
apply.

## Quiet setup

Check actual computer-use capabilities, not app or subscription names. Handle
necessary free setup from official sources within app permissions; never ask
the parent to use a terminal or buy anything. The parent grants system
permissions and handles sign-in; never type, request or save passwords or
bypass system/administrator prompts. Never create accounts without approval.
Use official app help if setup is needed. Explain permissions and device
troubleshooting ONLY if a permission prompt appears or the check fails.

For Codex / ChatGPT desktop, if needed: Plugins > Computer Use > Install plugin
or Enable; both server and skill toggles, Try now, and browser access in
Settings > Computer use. Explain that permission allows seeing/operating
approved apps when the parent is asked to grant it.

For Cursor, if needed: Settings > Tools & MCP > Browser Automation > Browser
Tab. Fully restart and open a new Agent chat in this project if required;
review/approve browser actions rather than auto-run. The headless cursor-agent
CLI has no Browser tool; use desktop. If blocked, check tool approval settings.

## Browser test

Use the real computer-use tool to open https://example.com and inspect the
actual browser. Pass if the tab title OR displayed page text contains
"Example Domain", OR displayed page text contains "This domain is for use in"
(the documentation examples notice). No heading element is needed. Record what
the tool actually saw quietly in reports/. Expected text, web search, HTTP fetch
or shell commands cannot pass. Never ask the parent to accept a variant,
approve a changed test or choose how to pass. Troubleshoot with the parent only
if the page fails to load or the tool cannot read anything. On success say at
most "Browser check passed." Pause intake until the real check passes.

After passing, complete the resume check above before any question,
then follow prompts/start.md for the recap or new intake.
Do not narrate successful setup.

Only if the page fails to load or the tool cannot read anything, explain what
happened in plain words; check tool installation,
enablement, components, browser access and internet. Explain only the relevant
permission/device steps:

- Mac: older Intel Macs may not be supported; Apple menu > About This Mac shows
  the chip. In System Settings > Privacy & Security, the parent enables Screen
  Recording and Accessibility for the component named by the permission prompt.
  These let it see the browser and click/type. Reopen the app if prompted.
- Windows: computer-use takes over the foreground, pointer and keyboard. Keep
  the browser visible and PC unlocked/connected; do not use it meanwhile. The
  parent can stop or take over anytime.

Retry the same harmless page after fixing the issue. If tools need a new
session, explain how to reopen this project and retry. If unavailable or blocked
by account, region or device policy, explain and pause intake. Never promise an
upgrade fixes access or replace computer-use with scripted form entry.
