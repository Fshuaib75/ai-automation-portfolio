# AI-Powered Lead Capture & Enrichment System

## The Problem
Real estate agents lose a significant share of leads simply because they can't respond fast enough. When a buyer or seller reaches out — through a website form, WhatsApp, or a Zillow-style lead feed — even a few hours of delay can mean the lead moves on to a competitor. Manually reading, categorizing, and logging every incoming message into a CRM also eats hours agents don't have.

## The Solution
I built an automated pipeline that instantly captures, understands, and stores incoming leads with zero manual work:

1. **Webhook trigger** — any external system (a website form, WhatsApp, a lead feed) can send a message to a live endpoint, triggering the automation instantly, 24/7.
2. **AI extraction** — an LLM (GPT-4o-mini), guided by a carefully engineered prompt with few-shot examples, reads the raw, messy message and extracts structured data: name, phone number, property of interest, budget, and timeline.
3. **Data parsing** — a lightweight processing step converts the AI's structured JSON response into clean, individual fields.
4. **Database storage** — the parsed lead is automatically saved as a new record in an Airtable database, ready for the agent to review, sort, or follow up on.

## Technical Details
- **Stack**: n8n (workflow orchestration), OpenAI API (GPT-4o-mini), Airtable (data storage)
- **Prompt engineering**: uses few-shot examples to handle edge cases reliably — for example, correctly distinguishing a lead's own information from other people they mention in the same message (e.g. "my brother might also be interested...")
- **Tested with**: realistic, messy, casually-written lead messages simulating real customer behavior

## Example
**Input** (raw message):
> "hi its dave, interested in the maple street listing, budget 400k, my number is 555-0192"

**Output** (automatically saved to database):
| Name | Phone | Property Interest | Budget | Timeline |
|---|---|---|---|---|
| dave | 555-0192 | maple street listing | 400k | — |

## Result
A real estate agent using this system would have every inbound lead automatically captured, categorized, and stored — with zero manual data entry, and response times limited only by how fast they check their database, not how fast they can parse a messy text message.

## What's Next
- Connect to a real, public-facing form (in progress — currently tested via webhook simulation, pending cloud deployment)
- Add automatic lead scoring/prioritization (e.g. flagging urgent language)
- Add automatic follow-up sequencing for leads that go quiet