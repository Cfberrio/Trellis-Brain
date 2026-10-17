---
brain_note_id: "note:3b3e24da-520b-4c26-a1aa-0442e57ed8a3"
canonical_key: "ai-customer-service-instructions-02-parent-communication-evidencia"
brand_id: "discipline_rift"
---
# 02 parent communication — Evidencia

## Canonical Statement

- **rule**: When sending End of Season (EOS) communications, the {PARENT_NAME} and {SPORT} fields must not be modified as they auto-populate from the system.
- **process**: The only field requiring manual update in EOS templates is the (DATE) field, which must reflect the correct start week/date for the specific site.
- **rule**: EOS communications must confirm that no practice is held the week after a season ends and provide a direct registration link for the upcoming season.

## Evidence Log

- 2026-10-13T23:47:49.200Z — `clickup_doc_page:8cqnrff-11657/8cqnrff-10997`
  - `e1` (source_body): {PARENT_NAME} and {SPORT} are special fields. Do NOT modify or rewrite them. The only field that must be manually updated before sending is: (DATE) -> Replace with the correct start week/date for that site. ... Our previous {SPORT} season officially ended last week, so there is no practice today.

- 2026-10-13T23:49:01.773Z — `clickup_doc_page:8cqnrff-11657/8cqnrff-11157` (validation `bf6fa7fc-0891-4c24-b6c6-c128d62d9d62`)
  - `e1` (source_body): Our previous {SPORT} season officially ended last week, so there is no practice today. Registration for the upcoming season is now open... Spots in the team are limited and filled on a registration priority.
  - `e2` (source_body): Hi Parent, Our volleyball season ended last week, there is no practice today. New season registration is now open and begins the week of March 24. Spots are limited. Register here: https://disciplinerift.com/register
- **decision**: The End of Season (EOS) communication to parents must clarify that practice has ended and provide a direct link for registration for the upcoming season.
- **preference**: EOS email templates should use a direct, neutral tone, emphasizing limited spots and registration priority to encourage re-enrollment.
- **preference**: EOS text messages should be concise, stating the season has ended, the start date for the new season, and providing the registration URL.

- 2026-10-17T15:57:26.811Z — `clickup_doc_page:8cqnrff-21297/8cqnrff-6597` (validation `66b494d5-8f5c-4b1f-a7e3-aee496fe0788`)
  - `e1` (source_body): 1-Day Reminder for {{ $[json.name] }}
Hi {{ $json.firstname }},
There is one day left until the start of {{ $[json.name] }}.
Make sure to remind your child about the practices! Here’s the complete schedule:
SCHEDULE
{{ $json.scheduleHtml }}
See your child on the court!
- **decision**: Discipline Rift uses a standardized 1-day reminder email for parents before a season starts, including the child's name, the program name, and the complete schedule.
- **fact**: The 1-day reminder template includes contact information (info@disciplinerift.com, (407) 614-7454) and emphasizes volleyball, tennis, and pickleball as the core sports.

- 2026-10-17T15:59:51.487Z — `clickup_doc_page:8cqnrff-21297/8cqnrff-8077` (validation `81d66c69-ad8d-4e8c-afb5-3a3e1ce97649`)
  - `e1` (source_body): Week 1 Focus: Passing & Setting. This week, players will learn the foundations of ball control and teamwork. We will focus on passing to a target and setting up the next play... What to bring: Water bottle, Athletic shoes, Comfortable clothes, Knee pads optional.
- **fact**: Week 1 of the Discipline Rift Volleyball season focuses on the foundations of ball control and teamwork, specifically passing to a target and setting up the next play.
- **rule**: The Week 1 parent reminder email must include the practice focus, required gear (water, shoes, clothes, optional knee pads), and specific logistics (date, time, location).
- **preference**: Parent communication should emphasize the goal of helping players learn the game, grow in confidence, and enjoy being part of a team, while directing questions to the Parent Dashboard.

## Provenance

- Source: `clickup_doc_page` `8cqnrff-11657/8cqnrff-10997`
- Source hash: `41d9d23f4b46bbc3ff89034f63f2e4887ab706fc851a518bddbd02700186cdff`
- Observed at: 2026-10-13T23:47:49.200Z
- Decision: `649ca5f8-0e3a-4230-a5f9-ac3039023d1b`
- Upstream agent run: `5cb17616-fbf9-4465-b307-4489ae20f729`
- Validation run: `7b7ff43e-bf43-44c5-a9d1-fed8c3de77f4`
