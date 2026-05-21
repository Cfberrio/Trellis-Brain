---
brand: Discipline-Rift
area: projects
subarea: drf
note_type: spec
status: active
canonical: true
used_for_ai: true
source_type: curated
source_reference: "ClickUp Doc 8cqnrff-11737 page 8cqnrff-13097 (10. Landing Page)"
owner: Luis Torres
last_updated: 2026-05-21
sensitivity: internal
hub_role: leaf
---

# DRF Landing Page — Spec

## Parent
- [[01-Brands/Discipline-Rift/04-Projects/DRF/Phase-1-Full-Playbook|DRF Phase 1 Playbook]]

## Related
- [[01-Brands/Discipline-Rift/04-Projects/DRF/Onboarding-Video-Script|Onboarding Video Script]]
- [[01-Brands/Discipline-Rift/04-Projects/DRF/DRF-Home|DRF Home]]

## Status — Tech / publishing

For now: standalone project with own temporary published link. **Do not buy new domain yet.**

Later options:
- Keep inside same DR ecosystem
- Move to subdomain (`franchise.disciplinerift.com`, `opportunities.disciplinerift.com`, `join.disciplinerift.com`, `build.disciplinerift.com`)
- Embed into main DR project

## Page flow

### 1. Required entry gate pop-up (hard gate)
Capture lead info **before** they consume the page.

**Fields:**
- First Name
- Email
- Phone Number
- Sport Experience (dropdown: Volleyball / Tennis / Pickleball / Flag Football)

**CTA:** Continue

### 2. Hero section

**Headline:** Own a Local Youth Sports Program With a Proven Playbook

**Subheadline:**
> For driven young individuals with sports experience who want to build something real, lead locally, and make an impact through youth sports, without starting from scratch.

**3 quick pointers:**
- Built on a proven system
- Lead locally in the sport you know and impact
- Gain real leadership and business experience

**Primary CTA:** Apply Now
**Secondary CTA:** Watch the 1-minute overview

### 3. Three value cards
1. **Proven Playbook** — You follow a system that has already been built and tested.
2. **Local Leadership** — You help run and grow youth sports in your area.
3. **Real Experience** — You gain leadership, operational experience, and real-world responsibility.

### 4. Pre-application video section

**Title:** Watch this first

Support text covers:
- Why this opportunity exists
- Who it is for
- Why it matters

Tone: emotional, outcome-focused, simple, low-pressure.

**CTA below video:** Apply Now (sends to Tinder/swipe application).

### 5. Info boxes below video

**Box 1 — Contact**
- Discipline Rift
- Email: info@disciplinerift.com
- Phone / GHL: [insert GHL number]

**Box 2 — What to Expect**
- Application received
- Team review
- Follow-up if qualified
- Next-step: call with us

**Box 3 — Still Have Questions?**
Review common questions about opportunity, commitment, support, next steps. Button: View FAQ.

### 6. Application page (separate, linked)

**Format:** Tinder-style swipe interface

**Structure:**
- Step 1 — Quick info (prefilled from popup OR confirmed silently)
- Step 2 — Swipe section / short answers (see [[01-Brands/Discipline-Rift/04-Projects/DRF/Phase-1-Full-Playbook|Phase 1 Playbook]] — 15 swipes)

### 7. Post-application flow

**Message:** Application Received! Video unlocked for the next steps.

**Video copy:**
> This video breaks down the opportunity more clearly — what the license really is, what you would do, the expectations, and the path forward.

- 3-minute video (see [[01-Brands/Discipline-Rift/04-Projects/DRF/Onboarding-Video-Script|Onboarding Video Script]])
- Embedded on page + popup modal

**Next-step message below video:**
> Our admin team will review your application and reach out by text or email with the next step if it seems like a good fit.
>
> **Timeline:** Follow-up within 1–3 business days.

## Post-application email

**Subject:** Your DR application is in: DR license could be next

**Body:**
> We received your application. Before we review it, watch this short video to better understand the opportunity, what the license could look like, and what happens next.

**Main CTA:** Required: Watch the 3-Minute Overview

**Lower support section:**
- Questions? Contact us at info@disciplinerift.com or [GHL number]
- Want more clarity first? View the FAQ

## Recommended content blocks

### A. Hero
- Headline
- Description
- 3 bullets
- Apply button

### B. Credibility strip
- Thousands of players coached
- 100+ coaches worked with
- Programs run in Central Florida

### C. What this opportunity leads to (outcome-first, not franchise-first)
- Meaningful leadership through sports
- Real-world organizational and operational experience
- A proven structure for building locally
- Lasting impact on players, families, and community
- A way to turn your sports background into something meaningful

### D. Who This Is For
- Individuals with extensive sports experience
- Driven to lead and make a real impact through sports
- Ready to use a proven structure instead of guessing
- Looking for real leadership and organizational experience, not random work

### E. Video
Embedded space for 1-minute pre-application video.

### F. Apply section
Button to start swipe application.

## FAQ (10 questions)

**1. What is this opportunity?**
This is an opportunity to become a DR license holder and help lead local youth sports programming using Discipline Rift's systems, structure, and playbook.

**2. Would I own something, or am I just helping run it?**
You would own a license and operate through a legal entity tied to the opportunity. This is designed to be more than just helping out. It is a real leadership and ownership-based path.

**3. Do I need to pay for the license or startup costs?**
No. DR covers 100% of the core costs tied to launching the opportunity.

**4. Would I receive compensation?**
Yes. You would receive a stipend, with structure based on factors like your location, expected expenses, and local realities.

**5. What kind of background are you looking for?**
The main requirement is **extensive experience as a player** in one of the supported sports. Coaching, volunteer, or leadership experience is helpful, but optional.

**6. Is coaching experience required?**
No. Coaching experience is not required. Strong player experience is the main requirement.

**7. Is this just a coaching role?**
No. Coaching may be part of it, but this is also about leadership, local execution, responsibility, and helping build something meaningful through sports.

**8. Do I need business experience?**
No. Prior business experience is not required. What matters more is your sports background, leadership potential, consistency, and willingness to learn.

**9. What happens after I apply?**
After applying, you'll be directed to a short follow-up video that explains the opportunity more clearly. From there, our team reviews applications and reaches out if it looks like a strong match.

**10. How soon will I hear back?**
You can expect a follow-up within 1–3 business days.

## Backend requirements (minimum)

- Capture popup lead data
- Store application responses
- View submissions in simple dashboard
- Tag status:
  - lead captured
  - application started
  - application completed
  - watched post-apply video

## Positioning note

**Do NOT lead with "franchise" too aggressively on the page.**

Internally = DR Franchise / licensed operator.
Externally = lead with:
- Run a local youth sports program
- Proven playbook
- Build something real
- Leadership + impact + experience

Then explain the structure later. Lowers skepticism + fits ad logic.

## Simplified user journey

```
Ad → page gate popup → one-page → 1-minute video → apply button → swipe application → thank-you page → 3-minute video → follow-up SMS/email
```
