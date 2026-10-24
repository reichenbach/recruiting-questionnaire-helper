Read AGENTS.md section 0 before intake. Quietly reuse the package folder the
app is opened in, without overwriting saved work. No folder-picker or "where
should I save it" questions. Only if files cannot be read, guide the small
folder-access step. Check the actual path; only if inside iCloud Drive, Dropbox,
OneDrive or Google Drive, say so in one plain sentence and ask permission to use
a local folder instead before saving data. Otherwise do not ask about sync.

Use START_PROMPT.md's source or an existing local/bundled copy. For EVERY
runtime repo/file fetch, try once only with a bounded timeout and handle errors.
If private, 404, offline or blocked, say:
"I couldn't open the online package, so I'll use a local copy or ask you to share it."
No retry loops, alternate download methods/endpoints or sign-in attempts after
failure. Continue from the open folder, bundled copy or supplied ZIP/folder,
without more network attempts after failure. If none is usable, ask the family
to paste or share the package and explain what is missing; never crash or stall.
Save no family data during setup. Never invent missing package instructions.

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

Using the actual computer-use tool, open https://example.com and inspect the
browser. Pass only if displayed page text contains "Example Domain". Expected
text, web search, HTTP fetch or a shell command cannot pass. Do not collect
family information until it works. On success say at most "Browser check
passed." and continue with prompts/start.md. Do not narrate successful setup.

On failure, explain what happened in plain words; check tool installation,
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
