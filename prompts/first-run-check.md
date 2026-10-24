Read AGENTS.md section 0 before intake. Quietly reuse the open package folder
without replacing saved work; request file access only if needed.
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

For real-family runs: five groups -> one summary -> one Yes -> fill -> one
fresh Yes per Submit. The summary lists what will be entered into which
official form, including any specific ARMS profile-creation action. Do not add
a separate disclosure approval step, profile versions such as "v1" or "v2", or
whole-profile re-approvals. Separate live-rehearsal disclosure approval applies
only to deliberate dry-run tests on live forms, with fake data and no Submit.
Required consent, file, contact and other item-specific safety gates still apply.

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

Continue with prompts/start.md after passing. Do not narrate successful setup.

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
