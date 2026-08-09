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