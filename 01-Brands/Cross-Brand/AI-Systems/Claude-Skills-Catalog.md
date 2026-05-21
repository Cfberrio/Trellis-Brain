---
brand: Cross-Brand
area: ai-systems
note_type: reference
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-15837 (Claude/SKILLS) — multiple pages"
owner: Luis Torres
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# Claude Skills Catalog

## Parent
- [[01-Brands/Cross-Brand/AI-Systems/AI-Systems-Home|AI Systems Home]]

## Related
- [[01-Brands/Cross-Brand/AI-Systems/Agents-Method|Agents Method (OpenClaw)]]
- [[00-Trellis-Core/Strategy-Models/01-100M-Offers/Hormozi-100M-Offers-Source-Map|Hormozi 100M Offers Source Map]]
- [[00-Trellis-Core/Strategy-Models/15-Closing/Hormozi-Closing-Source-Map|Hormozi Closing Source Map]]
- [[00-Trellis-Core/Strategy-Models/14-Retention/Hormozi-Retention-Source-Map|Hormozi Retention Source Map]]
- [[00-Trellis-Core/Strategy-Models/08-GOATed-Ads/Hormozi-GOATed-Ads-Source-Map|Hormozi GOATed Ads Source Map]]

## Purpose

Catalog of Claude skills, MCP connections, and workflows used across Trellis brands. Also includes the format used to document new AI tools / skills (mandatory for Cristian + dev team).

## What is a Skill

A **skill** is a reusable instruction Claude can execute when called with a slash command.

Examples:
```
/meta
/dr
/hormozi
/ads
```

**Skill** = how Claude should work
**MCP** = with what tool Claude can work
**Workflow** = combines skills + connections + steps to complete a task

## Trellis structure

```
Claude
├── Skills
│   ├── Meta
│   ├── DR
│   ├── Hormozi
│   └── Ads
│
├── MCP / Connections
│   ├── Notion
│   ├── Go High Level
│   ├── Obsidian
│   ├── ClickUp
│   └── Gmail
│
└── Workflows
    ├── Website Motion Graphics
    ├── SMS Draft Agent
    ├── Email Draft Agent
    └── Repo Update
```

## Decision rule

| If… | It's… |
|---|---|
| Executes with slash + only changes how Claude thinks/responds | **Skill** |
| Connects Claude to external tool to read/write/execute | **MCP / Connection** |
| Combines several things to complete a task | **Workflow** |

## 19 Hormozi Skills

Full catalog mapped to Trellis Brain `00-Trellis-Core/Strategy-Models/` source vaults.

### Wave 1 — Offers, Pricing, Branding (8 skills)

| # | Skill | Source vault | What it does |
|---|---|---|---|
| 1 | `offers` | `01-100M-Offers/` | Build/audit ONE offer. Grand Slam Offer, Value Equation, 5 enhancement levers (Scarcity, Urgency, Bonuses, Guarantees, Naming). |
| 2 | `pricing` (router) | — | Does NOT load notes. Diagnoses intent + routes to 1 of 5 subskills. Anti junk-drawer. |
| 3 | `pricing-posture` | `01-Pricing-Power/` | Premium pricing philosophy. Commodity trap, virtuous cycle. |
| 4 | `pricing-model` | `13-Pricing/` (3 notes) | Choose model (cost-plus vs value-based), 13 rules, profit-leverage. Initial price new product. |
| 5 | `pricing-plays` | `13-Instant-Profit-Plays` | 10 instant-profit tactics (28-day billing, processing fees, anchor display). Quick wins this week. |
| 6 | `price-test` | `09-Price-Testing-Method` | Structured test loop. Cadence, step-size, formula Price × Conv × Churn × LTV. |
| 7 | `price-raise` | `11-Price-Raise/` (4 notes) | Raise prices on EXISTING clients. Math, RAISE letter, rollout. |
| 8 | `branding` | `05-Branding/` (6 notes) | Brand pairing, R/I/D measurement, brand economics, 4-step build, authority, bouquet. |

### Wave 2 — Domain Coverage (10 skills)

| # | Skill | Source vault | What it does |
|---|---|---|---|
| 9 | `retention` | `14-Retention/` (15 notes) | Reduce churn. 9-lever Churn Checklist + customer-journey discipline. Includes onboarding subset (Levers 1-3) when scope first-30-days. |
| 10 | `avatar` | `01-Starving-Crowd` + `04-Avatar-Selection` | Pick/refine target. GMEP indicators. Avatar-selection method from existing clients. |
| 11 | `money-models` | `03-100M-Money-Models/` (6 notes) | Sequence multiple offers first 30 days. Attract → Upsell → Downsell → Continuity. CFA economics. |
| 12 | `hooks` | `07-Hooks/` (4 notes) | Hook engineering. 2-part anatomy, 8-format palette, 70-20-10 process, 121-hook swipe library. |
| 13 | `ads` | `08-GOATed-Ads/` (5 notes) | Produce paid ads at scale. Hook × Meat × CTA assembly. Schwartz awareness continuum. 5 meat formats. |
| 14 | `marketing-machine` | `12-Marketing-Machine/` (9 notes) | Continuous UGC / testimonial ads system. Lifecycle ads. Social / event / comms scrape. Testimonial competition. 6-point script. |
| 15 | `ltv` | `09-Crazy-Eight` + `09-Cost-Reduction` | Lift LTV via 8 levers. CFA math (LTGP / CAC / PPD). Delegates churn → `/retention`; price-test → `/price-test`. |
| 16 | `lead-nurture` | `10-Lead-Nurture/` (7 notes) | Convert opted-in leads to shows/closes. 4 pillars (Availability, Speed, Personalization, Volume) + BAMFAM. |
| 17 | `fast-cash` | `06-Fast-Cash/` (5 notes) | Immediate cash from warm audiences. 7-day promo. 10x-the-10% rule. Push-to-Consult / Push-to-Automated-Checkout. 90-day cadence. |
| 18 | `team` | `04-Lead-Getting-Employees` + `04-Maker-vs-Manager` | Hire (Internal Core Four, 3Ds, Performance Diamond) + founder calendar. |

### Wave 3 — Closing (1 skill)

| # | Skill | Source vault | What it does |
|---|---|---|---|
| 19 | `sales` | `15-Closing/` (7 notes) | Close deals in live call. Blame Onion + 28 rules + 7 All-Purpose closes + 3 branch-specific close libraries (Time/Money/Decision-Makers/Bad-Experiences/Preferences/Rushed/Guarantee) + Training System. |

## Documentation format — mandatory for new AI tools

Every new AI functionality / skill / workflow / API / prompt / automation must be documented in this format.

### 1. Name format
**Problem + Solution + Tool**

Examples:
- `Google Ads - Extract metrics without doing it manually - Claude Skill + API`
- `Meta Metrics - Token expired and blocked workflow - API Token + Claude`
- `Obsidian Offers - Improve offers using brand brain - Claude Skill`
- `Remotion - Replicate video editing faster - Claude Code + Remotion`

### 2. Mandatory 1–3 min screen-recorded video

Must explain:
1. What real problem they had
2. What solution they found
3. What tool they used
4. Where the process starts
5. How it's used
6. What result it generates
7. How it applies inside Trellis or a brand

### 3. Video rule
**Why it matters + how it's used.** Not only the result. Not only the technical step-by-step.

### 4. Problem
Specific, not generic.
- ❌ "We wanted to automate something."
- ✅ "Luis didn't understand how the Google Ads skill extracted metrics because where the API connected wasn't documented."

Questions:
- What was happening?
- Who was affected?
- What time, energy, or clarity was it costing?
- Why was it important to resolve?

### 5. Solution
Technical in simple words:
- Tool used
- Skill, agent, or workflow
- API connected
- Prompt used
- File / folder / repo where it lives
- Dependencies needed
- Final result

### 6. Initial setup
What does a person need ready before using it:
- Needs Claude?
- Needs Claude Code?
- Needs Cursor?
- Needs Node.js?
- Needs repo cloned?
- Needs API keys?
- Needs token?
- Needs account access?
- Needs to install skill manually?
- Does skill live in a repo or get copied/installed locally?
- Where are outputs saved?

### 7. Skill explanation
- **What it does**
- **When it's used**
- **What it needs to receive**
- **What it delivers**
- **Where it lives** (path)
- **How it's executed** (slash command)

### 8. Step-by-step
Format: `Opened ___ → Entered ___ → Connected ___ → Configured ___ → Copied ___ → Pasted ___ → Executed ___ → Reviewed ___ → Result: ___`

### 9. Things that can fail
Mandatory section. Common errors:
- Meta token can expire
- API key may not be configured
- `.env` file may be incomplete
- User may not have admin permissions
- Skill may be installed only locally and not appear to another person
- Output may be saved to a different folder
- Button or route may change accidentally if workflow touches frontend

How to know it worked:
- File ___ generated
- Claude confirms ___
- Dashboard shows ___
- Button redirects correctly to ___

### 10. Security + access
Never upload passwords, private tokens, API keys visibly. Document:
- Where to get them
- Type of access needed
- Variable names
- Who's responsible for updating
- If they expire

Example:
```
Variables needed:
- GOOGLE_ADS_CLIENT_ID
- GOOGLE_ADS_CLIENT_SECRET
- GOOGLE_ADS_REFRESH_TOKEN
- META_ACCESS_TOKEN

Note: do not paste real values in ClickUp.
```

For expiring tokens:
- Duration of token
- Responsible person to renew
- Where it's renewed
- How to confirm it's still active

### 11. Trellis application
Which brands does this serve? Trellis / DR / CTS / OEV / content / metrics / dev / editing? Who should use it?

### 12. Content value
- Would this serve someone else?
- What can a person learn from seeing this?
- Why is this not just "generic AI"?

### 13. References / links
- Tutorial (YouTube)
- TikTok / Reel reference
- Official docs
- ChatGPT prompt
- Tool link
- Repo link
- Folder link
- Screenshot
- Screen recording
- Essential keywords

### 14. ClickUp deliverable
```
[ ] Video
[ ] Transcript or summary
[ ] Links
[ ] Prompt used
[ ] Skill or file used
[ ] Step-by-step
[ ] Common errors
[ ] Final result
```

Task name format: `[Brand] - [Problem] - [Solution] - [Tool]`

Example: `Trellis - Google Ads manual metrics - Claude Skill + Google Ads API`

## Where skills live

Local compilation drive (Google Drive):
https://drive.google.com/drive/u/0/folders/13HIUfSxOMcGQ-swZMwtquaJXBRcL6jSb

Repository: Trellis Brain `00-Trellis-Core/Strategy-Models/` (Hormozi source maps)
