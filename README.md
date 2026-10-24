# Recruiting questionnaire helper for families

1. **Get ChatGPT Plus or higher** using your personal account. This package is
   intended for ChatGPT Plus or higher; the first-run check confirms whether
   Computer Use works for your account and device.
2. **Install the ChatGPT desktop app** from [OpenAI's download
   page](https://openai.com/chatgpt/download/).
3. **Open Codex in the desktop app and paste all of
   [START_PROMPT.md](START_PROMPT.md)**. Codex normally gets the package from
   https://github.com/reichenbach/recruiting-questionnaire-helper using git
   clone or a ZIP download. You never need to use a terminal or install Git
   yourself. The repository is private for now and will become public later.
4. **If the download is unavailable, use the ZIP or folder you received**.
   Codex helps unzip it and open its folder, then checks Computer Use before
   asking questions. Keep it in a private local folder outside cloud sync or
   shared storage. If you have no copy, share or paste the package when asked.

**Using Claude instead?** Paste all of [CLAUDE_PROMPT.md](CLAUDE_PROMPT.md)
into the Claude desktop app with computer use, or into Claude in Chrome, if your
Claude plan and app offer them. Claude Code is optional. The same check, review
and per-Submit approvals apply; see [CLAUDE.md](CLAUDE.md) and
https://support.anthropic.com for setup help.

This folder helps a parent and athlete prepare one local profile, find official
college recruiting questionnaires, and fill them using Computer Use. You review
the answers, final school list, live consent wording and each completed form
before approving a submission.

The helper fills forms only. It never contacts coaches, sends emails or
messages, makes calls, pays fees, or buys services. It cannot promise admission,
eligibility, recruiting interest or a scholarship. It asks before creating an
account or school profile and before each specific file upload. Never type,
request or save passwords; the family signs in themselves. It stops a school
when required information is missing rather than making up an answer. All opt-in
decisions follow the [Opt-in rule in AGENTS.md](AGENTS.md#opt-in-rule).

## What happens after you paste the prompt

Codex reuses an existing package without replacing saved work; otherwise it
tries once to clone or download the package from the URL above. Every runtime
repo or repo-file fetch uses a bounded timeout and handles errors. If the repo
or any file cannot be opened (private, 404, offline or blocked), it says:
"I couldn't open the online package, so I'll use a local copy or ask you to
share it." It then uses the folder Codex is opened in, a bundled copy, or a
ZIP/folder you point to. Try once only: no retry loops, alternate download
methods/endpoints after failure, or sign-in attempts to bypass it; after a
failure, use available copies without more network attempts. If no usable copy
exists, Codex asks you to paste or share the package and explains what is
missing; a failed fetch must never crash or stall the workflow.

If the app asks you to choose a project folder, choose the folder containing
`AGENTS.md`, `profile.template.json`, `prompts/` and `reference/`. Codex
confirms it can read them before collecting family information and handles
necessary free installs.

Codex guides you through **Plugins > Computer Use > Install plugin** or
**Enable**, both the **Computer Use server** and **skill** toggles, and **Try
now**. Review browser access in **Settings > Computer use** and grant any app
access you approve. On Mac, you handle **Screen Recording** and
**Accessibility** in **System Settings > Privacy & Security** when prompted. If
the first-run check fails on an older Intel Mac, it may not be supported. On
Windows, Computer Use moves the pointer, types and takes over the foreground.
Keep the browser visible and the computer unlocked and connected; do not use it
while the task runs. You can stop or take over at any time.

Before intake, Codex follows [the first-run check](prompts/first-run-check.md),
opens `https://example.com` using Computer Use and reads back **Example Domain**
from the actual page. If the test fails, it helps troubleshoot in plain words
and pauses intake until the test works. Account, region, device policy and
permissions can affect access; a plan name alone does not establish capability.
The setup guidance follows [OpenAI's Computer Use
guide](https://learn.chatgpt.com/docs/computer-use).

For an already-open package, the stage prompts are [start](prompts/start.md),
[find forms](prompts/find-forms.md), [fill forms](prompts/fill-forms.md) and
[report](prompts/report.md). They all follow [AGENTS.md](AGENTS.md).

## Intake, review and submission

The helper first asks for each school's name, sport and men's or women's team.
It then asks the common questions in small batches, followed by only the named
sport's questions. For vague names, confirm the exact school, division and
sport/team before searching. Intake includes high school and club jersey
numbers, NCAA Eligibility Center ID where applicable or required, and NAIA
Eligibility Center ID only for NAIA targets. Say "unknown" or "skip" when
needed. Unknown answers stay empty; a missing required answer stops that school.
Eligibility identifiers for the National Association of Intercollegiate
Athletics are requested only when that association is among your target levels.

Review the full profile, including every number, unit, test score, file,
unanswered question and consent record. Separately review and approve the final
school list with each school's sport, team, form type and verified form URL.
These are two explicit approvals. Changed answers, consent wording or form URLs
require renewed review and the affected approvals. The helper never substitutes
a school, team, sport or competition level without your approval.

Stay available for questions specific to each form. The helper shows every live
consent, attestation, certification, signature or terms request with its
complete wording, options and necessary disclosures. Provide your own answer.
Opt-ins follow the [Opt-in rule](AGENTS.md#opt-in-rule); unanswered required
requests stop the form. Handle any verification challenge yourself. Required
NCSA and IMG Academy choices also need your answer to the complete live wording
and all options; the helper proposes "No thanks" but never picks for you. If a
new required question appears during filling, it asks you.

The helper uses the same phone number in the format a field requests, such as
digits only. It searches high schools by name plus city; if yours is absent, it
uses the form's add-school path with your address, asking for missing details.
It never chooses a different school. It checks every preset dropdown, radio and
checkbox against your answers and lists the final choices before sending.
Unknown answers are asked, not accepted from a form's defaults. A FrontRush
Personal Contacts Save needs your approval as part of filling, and unusual
position choices need your confirmation.

Some actions send data before Submit. ARMS offers "Continue without one of these
accounts" as its route without social sign-in; the helper always chooses that
route after separate approval for profile creation. ARMS "Visitor Details" or
"Verify Your Details to Create a Profile" asks for profile information. It needs
full-profile and school-list approvals before proceeding, as well as
profile-creation approval. Some forms authorize text messages or artificial
intelligence contact when a mobile number is entered. The helper shows the live
notice and obtains your approval before that action, following the Opt-in rule.

After reviewing each completed form, give a fresh, school-specific Yes
immediately before its Submit. Profile and school-list approval do not authorize
submission. You see one short line per school and its form link: **Sent** only
after confirmation, **Not sent: why**, or **Needs your answer: what**. Detailed
evidence and times stay in local `reports/`. If sending is uncertain, it tells
you it may already have gone through and does not automatically try again.
Confirmed schools are not sent again.

Usage limits may apply and can change; see the OpenAI Help Center and the app's
usage display. Help Center: https://help.openai.com. No fixed message count is
promised, and don't buy extra usage. If you reach a limit, the helper saves
local progress. To resume, reopen the folder and ask it to continue. It checks
saved answers, approvals and the page, then asks again before Submit.

## Backup option without the local package

Copy all of [CHATGPT_PROMPT.md](CHATGPT_PROMPT.md) into the ChatGPT desktop
app's **Work** mode with **Computer Use**. This is one self-contained paste
covering the common intake, every sport branch, form verification and approval
boundaries, with four volleyball examples included. It may try once to read
reference files from the same GitHub URL as an optional source. If that fails,
it explains in one sentence and continues with the instructions and examples
inlined in the prompt; it never blocks on a download or requires a local copy.
It runs the Computer Use check before asking for a saved profile summary or new
family information. Without working Computer Use, it pauses intake and form
entry.

The backup keeps its working record in the conversation and prints one compact,
complete **SAVED PROFILE SUMMARY** to keep privately. Paste that summary with
the backup prompt in a later conversation to resume after the Computer Use
check. The helper confirms saved answers, asks for missing items, and rechecks
live wording, links and approvals. It does not maintain `profile.json` or local
reports or create additional remote documents. Chat is still processed by
ChatGPT and is not offline storage.

## Privacy and package contents

On the Codex path, family data is saved only in local `profile.json` and ignored
files inside `reports/`, plus `screenshots/` if needed. Never commit or share
these files, documents or family information. The `.gitignore` helps prevent
accidental Git inclusion; it does not encrypt files or prevent sharing.
Information provided in chat or displayed through Computer Use is not a promise
of offline processing. Entering data into an approved form discloses it to the
school and its provider, and the form may save entries before Submit.

- [AGENTS.md](AGENTS.md) defines the workflow, boundaries and approval gates.
- [START_PROMPT.md](START_PROMPT.md) gets or checks the package and starts the
  Codex path, with a local-copy fallback if downloading fails.
- [CHATGPT_PROMPT.md](CHATGPT_PROMPT.md) provides the self-contained Work
  backup.
- [profile.template.json](profile.template.json) contains blank common fields
  and all 14 sport blocks. Unused sport blocks stay empty.
- [prompts/first-run-check.md](prompts/first-run-check.md) and the other stage
  prompts guide setup, intake, discovery, filling and reporting.
- [The reference tree](reference/recruiting-intake-tree.md) is read-only field
  research. [Sample forms](reference/sample-forms.md) copies its section 5
  exactly, including coverage gaps. Historical links are candidates requiring
  official verification and may be expired or blocked.
- [Verified forms](reference/verified-forms.md) records four women's volleyball
  examples verified on 2026-10-23. Recheck every link live from the official
  athletics site before use; these notes do not grant filling approval.
- [test/README.md](test/README.md) explains the offline checks and dry runs. The
  [baseball fixture](test/dry-run-profile.json) and
  [volleyball fixture](test/dry-run-profile-volleyball.json) contain invented
  data only. A dry run never submits and may stop earlier at an approval gate.

## Notes for someone sharing this package

Keep a ZIP or folder containing the package and START_PROMPT.md available as a
fallback while the repository is private or if a download fails. Package source:
https://github.com/reichenbach/recruiting-questionnaire-helper

The repository stays private for now and will become public later; do not change
its visibility as part of setup. A parent never needs repository access to run
the package you give them. Send only the instructions, blank template, prompts,
references and synthetic `test/` files. Inspect the folder first and exclude all
private profiles, reports, documents, screenshots, passwords and secrets. Never
substitute real family information into the shareable test fixture.
