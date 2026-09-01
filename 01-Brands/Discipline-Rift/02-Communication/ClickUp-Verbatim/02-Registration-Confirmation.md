---
brand: Discipline-Rift
area: communication
subarea: clickup-mirror
note_type: source-transcript
status: active
canonical: false
used_for_ai: true
source_type: verbatim-transcription
clickup_doc_id: 8cqnrff-21297
clickup_page_id: 8cqnrff-6577
clickup_page_name: "02. Registration Confirmation"
clickup_last_edited: 2026-06-18
verbatim: false
content_status: rewritten-2026-08-31-not-implemented-in-code
last_synced: 2026-08-27
sensitivity: internal
hub_role: leaf
---

# 02. Registration Confirmation

## Parent
- [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/NOTIFICATIONS]]

> [!warning] No longer a verbatim ClickUp mirror
> Rewritten 2026-08-31 per Luis's feedback: schedule (coach + times) now renders first, then team, then payment, then student/emergency contact last. Headline names the season. Invoice redesigned with the registered legal identity (DBA, FEI/EIN, principal address). **This is a proposed spec, not yet implemented** — the live email still comes from `registrationConfirmationHtml()` in `~/Documents/DISCIPLINERIFT/disciplinerift/supabase/functions/_shared/email-templates.ts`, unchanged. The ClickUp page below is also stale (older, pre-fix design, was never the live source anyway). See [[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library#2. Registration Confirmation|Operational Email Library §2]] for the full rationale and section-by-section breakdown.

---

DISCIPLINE RIFT
Registration Successful! ${STUDENT_FIRST_NAME} is now registered for: ${SEASON_NAME}

PRACTICE SCHEDULE
${PRACTICE_OCCURRENCES}
Coach: ${COACH_NAME}
Location: ${LOCATION}
Schedule shown in Miami timezone (EST/EDT)

TEAM INFORMATION
Team: ${TEAM_NAME}
School: ${SCHOOL_NAME}
Location: ${SCHOOL_LOCATION}
Description: ${TEAM_DESCRIPTION}

PAYMENT RECEIPT
Registration: ${SUBTOTAL}
Processing Fee (3.25% + $0.25): ${FEE}
Total Paid: ${TOTAL}
Paid on: ${DATE}

STUDENT
Full Name: ${STUDENT_FIRST_NAME} ${STUDENT_LAST_NAME}
Grade: ${GRADE}
Emergency Contact: ${EMERGENCY_CONTACT_NAME}
Emergency Phone: ${EMERGENCY_PHONE}

* * *

Discipline Rift · Torres Rivero LLC
713 W. Yale Street, Orlando, FL 32804
Support: [info@disciplinerift.com](mailto:info@disciplinerift.com)
Phone: (407) 614-7454
Web: [www.disciplinerift.com](http://www.disciplinerift.com/)
This is an automated email. If you have any questions, please don't hesitate to contact us.

Invoice PDF attached (redesigned):
Discipline Rift DBA / Torres Rivero LLC
FEI/EIN: 86-3157842
926 Spring Palms Loop, Orlando, FL 32828

![](https://t9017418223.p.clickup-attachments.com/t9017418223/cae32f26-59f4-4697-a769-32bbfa09d530/image.png)

---

## Related
- **Curated + annotated version:** [[01-Brands/Discipline-Rift/02-Communication/Templates/Operational-Email-Library#2. Registration Confirmation|Operational Email Library §2]]
- **Index:** [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/NOTIFICATIONS|ClickUp NOTIFICATIONS (verbatim)]]
- **Previous page:** [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/01-OTP-Email|01.  OTP Email]]
- **Next page:** [[01-Brands/Discipline-Rift/02-Communication/ClickUp-Verbatim/03-30-Day-Reminder-N8N|03. 30 day reminder (N8N)]]
- **Open in ClickUp (still has the OLD, pre-fix copy):** https://app.clickup.com/9017418223/v/dc/8cqnrff-21297/8cqnrff-6577
