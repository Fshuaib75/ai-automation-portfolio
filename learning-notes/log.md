# Learning Log

## Day 1
- Built: dev environment (WSL2, Docker, n8n, Git/GitHub, Python venv) + first AI script that extracts structured lead data from messy text
- Broke: OpenAI key auth failed at first (copied key incompletely)
- Learned: system prompt vs user prompt, .env/.gitignore secrets pattern, git push with token auth
## Day 2
- Built: few-shot prompt engineering test (deliberately broke a prompt, then fixed it), rebuilt the same lead-extraction logic in n8n using the "Message a model" node
- Broke: original prompt confused two people in one message (Dave vs. his brother) — picked the wrong person's budget and dropped a valid phone number entirely
- Learned: the failure wasn't the AI being "dumb" — it was a gap in my instructions. Plain instructions rely on the AI interpreting wording correctly; few-shot examples remove that ambiguity by showing the exact input→output pattern I want. Also confirmed the same prompt logic works identically whether run through Python code or n8n's no-code interface — the reliability comes from the prompt itself, not the tool.
## Day 3
- Built: first fully automated pipeline — webhook trigger → AI extraction → structured JSON output, no manual clicking required. Tested with curl simulating a real form submission.
- Broke: nothing major today, first clean run
- Learned: webhooks give an automation a real "address" other systems can call. Currently running on localhost (only reachable from my own machine) — public hosting (cloud deployment) is what would make this reachable by a real website, which comes later in the curriculum.
## Day 3 (continued)
- Built: a real Tally form (title + text field) and attempted to connect it directly to my n8n webhook
- Broke: Tally rejected my webhook URL ("please enter a valid link") because it's running on localhost — only reachable from my own machine, not from Tally's servers out on the internet
- Learned: this is the exact "public hosting" gap I predicted earlier — webhooks need a real, internet-reachable address to be usable by external services. My automation logic itself is fully proven (curl → webhook → AI → correct JSON output), the only missing piece is deployment, which comes later in the curriculum (Week 12-13, Docker/cloud hosting). Also learned tools like ngrok exist as a temporary workaround for this exact problem during local development.
## Day 4 — First AI Agent
- Built: a real AI Agent in n8n (not just a fixed prompt) with an OpenAI Chat Model as its reasoning engine and an HTTP Request Tool (weather API) it can choose to call
- Broke: kept confusing OpenAI's internal action-search panel with n8n's main node search — wasted time searching for "Agent" inside the wrong menu before realizing it was in the main "+" search all along
- Learned: the core difference between a workflow and an agent — a workflow always does the same fixed steps, an agent reasons about what to do based on the question, then decides whether to answer directly or call a tool. Proved this by asking a weather question: the agent correctly chose to call the weather tool on its own (never told to), then translated the raw JSON response into a natural sentence, even inferring "clear" and "nighttime" from numeric codes I never explained to it.
## Day 4 (continued) — Multiple tools & tool selection
- Built: added a second Tool to the AI Agent (a fake "property lookup" alongside the weather tool), tested whether the agent picks the right one based on the question
- Result: agent correctly selected the property tool over the weather tool for a listing-related question, based purely on the tool's written description — proven visually since only that tool node executed
- Learned: an agent is only as reliable as its tools' data and descriptions. When the "property" tool returned irrelevant placeholder data, the agent correctly said it couldn't find real info instead of making something up — this is the behavior you want, since a hallucinated fake property answer would be a real problem in a client-facing tool.
## Day 5 — Full Lead Capture & Enrichment System (complete pipeline)
- Built: end-to-end lead capture automation — Webhook → AI extraction (few-shot prompt) → Code node (parses AI's JSON string into real fields) → Airtable (permanent database storage). Tested with a realistic curl-simulated lead and confirmed a real row landed correctly in Airtable.
- Broke: multiple things today — added the Airtable node to the wrong workflow at first, hit a 403 permissions error on the Airtable token (missing schema.bases:read scope), and the AI's output came back as a single JSON string rather than usable fields, which needed a Code node to parse.
- Learned: real automations are rarely just "connect two nodes" — there's usually a data-shape mismatch somewhere (a string vs. real fields) that needs an intermediate step. Also learned Airtable's permission scopes are granular and specific errors (401 vs 403) mean genuinely different things — 401 is bad credentials, 403 is correct credentials but insufficient permissions.
## Day 6 — Error Handling & Robustness
- Built: added a try/catch safety net in the Code node (handles malformed AI output instead of crashing), plus an IF node that routes clean data to Airtable and error data to a separate branch, so failures are caught rather than silently lost
- Broke: hit a real, unpredictable edge case immediately — the AI occasionally wrapped its JSON response in markdown code fences (```json ... ```), which broke JSON.parse(). This wasn't something I could have anticipated in advance; the try/catch caught it exactly as intended instead of crashing the whole workflow.
- Learned: real automations fail in ways you don't expect, and the goal isn't to prevent every possible failure — it's to make sure failures are visible and contained instead of silent. Fixed this specific issue at two layers: tightened the system prompt (explicitly forbidding markdown formatting) and made the parsing code more resilient (strips markdown fences before parsing) as defense in depth.
## Day 7 — Mini CRM Automation (Status Tracking + Notifications)
- Built: added a Status field to the Airtable leads table (New/Contacted/Won/Lost), and a separate n8n workflow using an Airtable Trigger + IF node that detects when a lead's status changes to "Won" and automatically sends a Slack notification
- Broke: Slack OAuth login didn't work directly in n8n, requiring a manual Bot Token setup via api.slack.com/apps instead; also hit a "channel not found" error because the bot hadn't been added to the target channel yet — fixed via Slack's "Add apps" integration menu
- Learned: outgoing webhooks/notifications (n8n calling OUT to another service) are a different skill from incoming webhooks (receiving data) — this closes that gap from the curriculum. Also learned that connecting a bot/app to a workspace isn't enough on its own; it also needs explicit channel-level access before it can post there.