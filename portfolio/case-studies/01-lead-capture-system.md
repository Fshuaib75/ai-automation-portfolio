# AI-Powered Lead Capture & Enrichment System

**Tech Stack:** Python · n8n · OpenAI API · SQL/Airtable · JSON

---

## Problem
How can incoming lead messages be automatically converted into structured, usable records — without manual data entry?

Real estate agents (and similar client-facing businesses) lose deals simply because they can't respond to inbound leads fast enough. Every message — from a website form, WhatsApp, or a lead feed — has to be read, interpreted, and manually logged into a CRM before any follow-up can happen. That delay costs real business.

## Architecture
 **Webhook** — a live endpoint that any external system (form, WhatsApp, lead feed) can send a message to, triggering the pipeline instantly
2. **OpenAI (few-shot prompted)** — reads the raw, unstructured message and extracts structured fields: name, phone, property of interest, budget, timeline
3. **Code node** — parses the AI's JSON response, with a try/catch safety net for malformed output
4. **Conditional branch (IF node)** — routes clean, validated data to storage; routes failed/invalid data to a separate path instead of silently breaking or corrupting the database
5. **Airtable** — the extracted lead lands as a permanent, organized record, ready for follow-up

## Tech Stack
| Layer | Tools |
|---|---|
| Orchestration | n8n |
| AI / Extraction | OpenAI API (GPT-4o-mini), few-shot prompt engineering |
| Data parsing | JavaScript (Code node) |
| Storage | Airtable |
| Version control | Git / GitHub |

## Features
- ✓ Structured data extraction from unstructured text
- ✓ Prompt engineering with few-shot examples for edge-case reliability
- ✓ Input/output validation
- ✓ Error handling (try/catch parsing)
- ✓ Conditional workflow branching (clean vs. failed data)
- ✓ Persistent database storage

## Example Input
> "hi its dave, interested in the maple street listing, budget 400k, my number is 555-0192"

## Example Output
| Name | Phone | Property Interest | Budget | Timeline |
|---|---|---|---|---|
| dave | 555-0192 | maple street listing | 400k | — |

## What I Learned
- **Prompt reliability requires examples, not just instructions.** An early version of this prompt correctly extracted data but occasionally confused two people mentioned in the same message (e.g., a lead and their sibling). Adding few-shot examples showing the correct behavior fixed this — instructions alone left too much room for interpretation.
- **Real systems fail in unpredictable ways.** The AI occasionally wrapped its JSON output in markdown code fences, breaking strict JSON parsing — an edge case I hadn't anticipated. The try/catch handling caught it exactly as intended instead of crashing the pipeline, and I fixed the root cause at two layers: tightening the prompt and making the parser more defensive.
- **Debugging environment issues is a real, transferable skill.** Working through Docker/WSL networking quirks, lost credentials, and file-location mixups during development built genuine troubleshooting instincts, not just "the happy path."

## How I'd Explain This to a Client
"Right now, when a lead messages you through a channel, the lead info traditionally has to be extracted manually and typed into a CRM — which takes time and can result in that lead going cold or not being converted efficiently. This system does all of that automatically: the second a message comes in, it reads it, pulls out their name, phone, what property they're interested in, their budget, and their timeline — and saves it straight into an organized database."

## Repository
[github.com/Fshuaib75/ai-automation-portfolio](https://github.com/Fshuaib75/ai-automation-portfolio)