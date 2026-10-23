# Recruiting questionnaire helper for families

1. **Get ChatGPT Plus or higher** using your personal account. This package is
   intended for ChatGPT Plus or higher; the first-run check confirms whether
   Computer Use works for your account and device.
2. **Install the ChatGPT desktop app** from [OpenAI's download
   page](https://openai.com/chatgpt/download/).
3. **Paste all of [START_PROMPT.md](START_PROMPT.md) into Codex** in the desktop
   app. Codex gets the package, explains setup, checks Computer Use, then asks
   questions. You never need a terminal or commands.

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

Codex retrieves the package into a private local folder, or reuses an existing
copy without replacing saved work. It can download the ZIP if Git is missing.
Keep the folder outside cloud sync and shared storage. If the app asks you to
choose a project folder, choose the folder containing `AGENTS.md`,
`profile.template.json`, `prompts/` and `reference/`. Codex confirms it can read
them before collecting family information and handles necessary free installs.

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
sport's questions. Say "unknown" or "skip" when needed. Unknown answers stay
empty; a missing required answer stops that school. Eligibility identifiers for
the National Association of Intercollegiate Athletics are requested only when
that association is among your target levels.

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
requests stop the form. Handle any verification challenge yourself.

Some actions send data before Submit. ARMS offers "Continue without one of these
accounts" as its route without social sign-in; the helper always chooses that
route after separate approval for profile creation. Illinois Wesleyan's "Visitor
Details" step asks for a name and email "to Create a Profile". It requires
full-profile and school-list approvals before proceeding, as well as
profile-creation approval. Some forms authorize text messages or artificial
intelligence contact when a mobile number is entered. The helper shows the live
notice and obtains your approval before that action, following the Opt-in rule.

After reviewing each completed form, give a fresh, school-specific Yes
immediately before its Submit. Profile and school-list approval do not authorize
submission. The helper records **submitted** only after observed confirmation,
**failed** with the specific reason, or **needs-info** with exact missing fields
or approvals. It shows the form link and evidence/time in chat and local
`reports/`. Uncertain submissions are not retried automatically, and confirmed
schools are not resubmitted.

Usage limits may apply and can change; see the OpenAI Help Center and the app's
usage display. Help Center: https://help.openai.com. No fixed message count is
promised, and don't buy extra usage. If you reach a limit, the helper saves
local progress. After a pause, ask it to resume from the profile and reports,
verify the current form and approvals, and get a fresh confirmation before
Submit.

## Backup option without the local package

Copy all of [CHATGPT_PROMPT.md](CHATGPT_PROMPT.md) into the ChatGPT desktop
app's **Work** mode with **Computer Use**. This is one self-contained paste
covering the common intake, every sport branch, form verification and approval
boundaries. It runs the Computer Use check before asking for a saved profile
summary or new family information. Without working Computer Use, it pauses
intake and form entry.

The backup keeps its working record in the conversation and prints a complete
**SAVED PROFILE SUMMARY** for you to keep privately. Paste that summary with the
backup prompt in a later conversation to resume after the Computer Use check.
The helper confirms saved answers, asks for missing items, and rechecks live
wording, links and approvals. It does not maintain `profile.json` or local
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
- [START_PROMPT.md](START_PROMPT.md) retrieves the package and starts the Codex
  path.
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
- [test/README.md](test/README.md) explains the offline checks and dry run. [The
  dry-run profile](test/dry-run-profile.json) contains invented baseball data
  only. A dry run never submits and may stop earlier at an approval gate.

## Notes for someone sharing this package

Share https://github.com/reichenbach/recruiting-questionnaire-helper together
with [START_PROMPT.md](START_PROMPT.md). If this link doesn't open as a public
repo, send the recipient the correct link. Send only the instructions, blank
template, prompts, references and synthetic `test/` files. Inspect the folder
first and exclude all private profiles, reports, documents, screenshots,
passwords and secrets. Never substitute real family information into the
shareable test fixture.
