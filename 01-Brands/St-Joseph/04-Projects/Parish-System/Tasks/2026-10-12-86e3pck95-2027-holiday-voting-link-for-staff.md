---
brand: St-Joseph
area: projects
subarea: parish-system
note_type: project
status: active
canonical: false
used_for_ai: true
source_type: imported
source_reference: "https://app.clickup.com/t/86e3pck95"
owner: Cristian
last_updated: 2026-11-17
sensitivity: internal
related_systems:
  - clickup
  - st-joseph-connect
related_notes:
  - "[[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home]]"
hub_role: leaf
tags:
  - st-joseph
  - clickup-task
  - week-oct-19
---

# Build interactive 2027 holiday voting link for St Joseph staff

## Parent
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Semana ClickUp: OCT 19 🪪

## Ficha
| Campo | Valor |
|---|---|
| ClickUp | [86e3pck95](https://app.clickup.com/t/86e3pck95) |
| Estado | aprobado |
| Prioridad | — |
| Creada por | Luis Torres |
| Asignados | Cristian Berrío |
| Creada | 2026-10-12 15:47 |
| Actualizada | 2026-10-21 12:20 |
| Cerrada | 2026-10-21 12:19 |
| Fecha límite | — |
| Tiempo registrado | — |

## Resumen
Luis pidió un enlace único para que los 15 miembros del staff de St Joseph voten sus 4 feriados flexibles de 2027, con comentarios, reacciones y ranking en vivo, construido como primer módulo de un Staff space reutilizable (sin login, con registros de staff reales) y siguiendo la lógica del Excel St_Joseph_Holiday_Poll_2027.xlsx. Cristian lo publicó el 13 de octubre en formation-foundations.lovable.app/vote, con página de administración en /admin/staff (exportar Excel con el mismo formato, cerrar votación, resetear votos, editar la lista de staff) y pruebas de concurrencia. El 21 de octubre Luis pidió que las fechas Chancery pick no se votaran y quitar el 31 de diciembre, pero luego pidió abortar y revertir esos cambios; Cristian confirmó que los revirtió. No quedan pendientes abiertos en los comentarios.

## Descripción
## Objective
Ship one shareable link where every St Joseph staff member can vote on their 4 flexible holidays for 2027, comment on each date, and watch the standings update live. It should feel fun, not like a form.
## Context
We're loading St Joseph staff into the portal. The full software isn't approved yet, so they asked for a taste first: this holiday voting tool. It's small, but it's our demo, so it needs to look polished and work flawlessly on phones.

The attached PDF (**Staff holiday voting poll.pdf**) is the first draft mockup. Use it as the base for layout and copy. Original request: [https://app.clickup.com/t/86e3p6vdw?comment=90170261611242](https://app.clickup.com/t/86e3p6vdw?comment=90170261611242)

**How it works (from the mockup)**
*   Header: "ST JOSEPH · 2027 HOLIDAYS" / **Pick Your Four**
*   Each person gets **4 votes**. Tap a day to spend a vote, tap again to take it back. Top 4 dates become the flexible holidays.
*   "Voting as \_\_\_. Not you?" identity switch
*   **Standings** section (live ranking) and **Who picked what** (who voted for each date + who still hasn't voted)
*   **Add a day**: any weekday in 2027 not already on the ballot or off. Shows the name of who added it.
*   **Already off, no vote needed** section

**Staff (15):** Carly, Fr Benjamin, Fr Joseph, Ariel, Mary, Kori, Danette, Luis, Steven, Oriana, Rita, Chris, Nivaldo, Julia, Wendy

**Ballot from the mockup**

| Date | Day | Tag |
| ---| ---| --- |
| Mon Jan 18 | Dr. Martin Luther King Day | Chancery pick |
| Mon Feb 15 | Presidents' Day | Starter idea |
| Thu Mar 25 | Holy Thursday | Starter idea |
| Fri Mar 26 | Good Friday | Chancery pick |
| Mon Mar 29 | Easter Monday | Starter idea |
| Fri Apr 30 | St. Joseph the Worker (observed) | Starter idea |
| Mon May 3 | St. Joseph the Worker (observed) | Starter idea |
| Mon Nov 1 | All Saints' Day | Starter idea |
| Wed Nov 24 | Day before Thanksgiving | Starter idea |
| Fri Nov 26 | Thanksgiving Holiday | Chancery pick |
| Wed Dec 8 | Immaculate Conception | Starter idea |
| Thu Dec 23 | Christmas Holiday | Chancery pick |

**Add these to the ballot (Starter idea)**

| Date | Day | Why |
| ---| ---| --- |
| Fri Mar 19 | Solemnity of St. Joseph | Their patron's actual feast, lands on a Friday. Long weekend. Biggest miss in the draft. |
| Wed Feb 10 | Ash Wednesday | Start of Lent |
| Thu May 6 | Ascension Thursday | Holy day; pairs with Fri May 7 for a 4-day weekend |
| Mon Aug 16 | Assumption (observed) | Aug 15 is a Sunday |
| Mon Oct 11 | Columbus / Indigenous Peoples' Day | Long weekend |
| Fri Nov 12 | Veterans Day (observed bridge) | Nov 11 is a Thursday |
| Mon Dec 13 | Our Lady of Guadalupe (observed) | Dec 12 is a Sunday |
| Fri Dec 31 | New Year's Eve | Jan 1, 2028 is a Saturday |

**Already off (show, not votable):** Fri Jan 1 New Year's Day · Mon May 31 Memorial Day · Fri Jun 18 Juneteenth (obs.) · Mon Jul 5 Independence Day (obs.) · Mon Sep 6 Labor Day · Thu Nov 25 Thanksgiving Day · Fri Dec 24 Christmas Day (obs.)

**Make it fun**
*   Confetti / star burst when someone spends their 4th vote, plus a "Ballot locked in 🎉" moment
*   Comment thread on every date card (name + timestamp) and quick emoji reactions (🙏 🏖️ 🔥 ⛪)
*   Standings as a live race bar chart; the current top 4 get a highlighted "Winning" badge
*   Little personality per card (e.g. "Long weekend" badge with a 🏖️, saint days with ⛪)
*   Progress meter: "9 of 15 have voted"
## To Keep in Mind
*   **Votes and comments must be shared and persistent** (real backend, e.g. Supabase). Everyone must see the same live data, not local-only state like the mockup.
*   **Remove Sat May 1** from the ballot. It's a weekend and breaks the "weekdays only" rule. The Apr 30 / May 3 observed options cover it.
*   Identity: pick your name from the 15 staff on first visit (stored on device), with a simple way to switch. No passwords; keep friction near zero. Block one person from casting more than 4 votes.
*   Add a day: reject weekends, dates outside 2027, duplicates, and dates already off. Show a friendly message suggesting the Friday/Monday next to a weekend date.
*   Admin view for Luis: reset votes, remove a date, edit the staff list, close voting, export results.
*   Tie handling for the 4th spot: show the tie clearly so the Chancery can decide.
*   Mobile-first. Most staff will open this from a text or email on their phone.
*   Branding is St Joseph's, not Discipline Rift. Clean and simple, no DR marketing copy.
*   Test: 15 users voting at the same time, toggling votes on/off, adding a date then voting it into the top 4, comments with long text.
*   Deliver one short URL Luis can send to the whole staff.

* * *

## Update (Oct 12): Excel source of truth + Staff area vision
### Excel: St\_Joseph\_Holiday\_Poll\_2027.xlsx (attached)
The app should mirror the spreadsheet's logic:
*   **Ballot sheet**: date, weekday, name, Chancery pick (Yes/blank), votes, rank, result, plus a **cut line check** that flags when the 4th spot is tied.
*   **Votes sheet**: staff × date grid ("who picked what"), max 4 per person, per-person Picks count and a "Not voted" status.
*   **Schedule sheet**: 7 fixed holidays + 4 flexible slots (top 4 by votes) = **11 total days off**.
*   Chancery picks and fixed holidays come from the **Chancery Holiday Schedule memo (Regina-Marie Aldrin, Sept 24, 2026)**. Show that source line under "Already off".
*   **Excel vs. this task:** the Excel still lists Sat May 1 and doesn't have the 8 Starter idea additions. This task wins: drop May 1, add the 8 dates.
*   **Ties:** provisional rank breaks ties by date order (same as the Excel), but the UI must label it "Tied, Chancery decides" instead of silently picking one.
*   **Export must match the Excel layout** (Ballot / Votes / Schedule) so results drop straight into the existing file.
### Bigger picture: first module of the Staff area, not a one-off
This is foreshadowing: every staff member who joins the platform will need a place to manage their **profile, votes, and posts**. We are NOT building a standalone holiday feature. Build it as the first module inside a **Staff space** they can open, see, and play with.
*   **No staff login yet.** This is a sandbox so St Joseph staff can vote and see how good the software feels.
*   **Login-ready data model:** each person is a real **staff record** (name, school, initials/avatar). Votes, comments, reactions, and added days all point to that record, not a loose name string. Later, login just claims the existing record, no rewrite.
*   **Poll = generic, reusable module** (title, options, votes per person, rules, open/closed). "Holidays 2027" is just the first instance.
*   **Leave room in the UI** (staff home / nav) for future modules: profile, posts/announcements, more polls. Don't build them now, just don't paint us into a corner.

## Subtareas
_Sin subtareas._

## Adjuntos
| Archivo | Tipo | Fecha | Subido por |
|---|---|---|---|
| Staff holiday voting poll.pdf | pdf | 2026-10-12 15:47 | Luis Torres |
| St_Joseph_Holiday_Poll_2027.xlsx | xlsx | 2026-10-12 16:24 | Luis Torres |
| image.png | png | 2026-10-21 12:04 | Luis Torres |

## Comentarios
### 2026-10-12 16:25 · Luis Torres
St_Joseph_Holiday_Poll_2027.xlsx@Brain Excel that has more information about staff and how this feature should be implemented correctly

 this is also a foreshadowing of the fact that we need to figure out a way for every staff member who wants to have access to our platform to be able to manage their profile, votes, and posts like this and that kind of stuff. We don't want to create a whole feature just to pick holidays, but rather we want to have a place where staff can go in and see it. As of right now, we won't have staff login, but the idea is that this can be a sandbox testing feature for them to vote and see how cool our software is

(Adjunto en el comentario: St_Joseph_Holiday_Poll_2027.xlsx)

#### ↳ Respuesta 2026-10-12 16:26 · Brain
I added the Excel rules and your Staff area plan to the end of the 86e3pck95 description. Cristian now has it framed as the first module of a reusable Staff space, not a one-off holiday feature.

What I added
From the Excel: The app should copy the spreadsheet's three sheets (Ballot, Votes, Schedule) and its total: 7 fixed holidays + 4 flexible days = 11 days off. The fixed holidays and Chancery picks are credited to Regina-Marie's Sept 24 memo. Results export in the same layout as the Excel, so they drop straight into your file.

Where the Excel and the task disagree, the task wins: the Excel still lists Sat May 1 and is missing the 8 extra dates.

Ties: the Excel quietly breaks ties by date order. The app can rank them that way for now, but it has to show "Tied, Chancery decides" so nobody gets bumped without anyone noticing.

Staff area plan:
No login for now. It's a sandbox so staff can try the software.
Each person gets a real staff record, and their votes, comments and added days are saved to it. When login comes later, staff sign in and keep everything they already did, with no rebuild.
Polls are built so they can be reused. Holidays 2027 is just the first one.
The staff home has room for profile, posts and more polls later, but those don't get built now.

### 2026-10-13 14:54 · Cristian Berrío
 the holiday voting is live. Here is how it works, step by step.

The link to send the staff

https://formation-foundations.lovable.app/vote

That's the only link staff need. It opens the 2027 holidays ballot directly. It works on any phone or computer, with no app, no account and no password. Right now it has 0 votes: nobody has used it yet.

What a staff member does (step by step)

They open the link. A window asks "Who are you?" and shows the 15 names (Carly, Fr Benjamin, Fr Joseph, Ariel, Mary, Kori, Danette, Luis, Steven, Oriana, Rita, Chris, Nivaldo, Julia, Wendy).
They tap their name. The phone remembers it, so they only do this once. The page then says "Voting as Chris. Not you?". Tapping Not you? lets them switch to another name.
If they just want to look around first, they tap "Just looking for now". As soon as they try to vote, the app asks who they are.
They tap a day to vote. The star on that day fills in gold and the card turns green. Tapping the same day again takes the vote back.
Everyone has 4 votes. The bar at the top shows ☆☆☆☆ and how many votes they have left.
When they spend the 4th vote, confetti goes off and the page says "Ballot locked in 🎉". They can still change their mind: take one vote back, then give it to another day.
If they try a 5th vote, the card shakes and the app tells them to take a vote back first. The database enforces this too, so nobody can end up with more than 4, even by tapping very fast.
Optionally, they can comment on any day, react with 🙏 🏖️ 🔥 ⛪, or add a day that isn't on the ballot (see below).

Everything is shared and live: when one person votes, everyone else's screen updates within about a second.

What each part of the page means

Top of the page
☆☆☆☆ "You have 4 votes": your own votes. It changes to "2 votes left", then "Ballot locked in 🎉".
"9 of 15 have voted": how many staff have cast at least one vote, with their initials.

The ballot: one card per day, in date order (20 days). On each card:
Date box: month, day and weekday.
Chancery pick (gold label): one of the 4 days the Chancery suggested in Regina-Marie's Sept 24 memo (MLK Day, Good Friday, Thanksgiving Holiday, Christmas Holiday).
Starter idea: a day we suggested as an alternative.
Added by [name]: a day a staff member added themselves.
🏖️ Long weekend: the day connects to a weekend (a Monday, a Friday, or a day next to a day already off).
⛪ Church day: a feast or holy day.
"Next to Thanksgiving Day" and similar: the day sits right next to a day already off.
Small italic note: context, e.g. "Aug 15 falls on a Sunday".
"4 votes" + initials: how many votes the day has and who gave them.
🏆 Winning: the day is in the top 4 right now.
Tied, Chancery decides: the day is tied for the last spot (explained below).
🙏 🏖️ 🔥 ⛪: quick reactions with a count. Tap once to add yours, again to remove it.
Comment: opens the conversation for that day. Each comment shows the name and when it was written. People can delete their own comments.

Standings: a live ranking. Each day with votes gets a bar, and the bars move up and down as people vote. A dashed CUT LINE sits under 4th place: everything above it would be a flexible holiday today.

Our 2027 days off: the final result in one place: 7 fixed days + 4 flexible days = 11 days off. The 4 flexible slots fill in with the current leaders.

Who picked what
"Still to vote": names of people who haven't voted yet.
Below that, each person who voted and the days they picked (e.g. "Chris 4/4").

Add a day: anyone can put a new day on the ballot, for example their patron saint's feast. It appears on the ballot for everyone with "Added by [name]", and people can vote for it like any other day. The app only accepts weekdays in 2027 that aren't already on the ballot or already off. If someone picks a Saturday or Sunday, the app says so and offers the Friday or Monday next to it with one tap.

Already off, no vote needed: the 7 fixed holidays, which nobody votes on (New Year's Day, Memorial Day, Juneteenth, Independence Day, Labor Day, Thanksgiving Day, Christmas Day). Below them it credits the source: Chancery Holiday Schedule memo from Regina-Marie Aldrin, Sept 24, 2026.

How the winners are decided

The 4 days with the most votes become the flexible holidays.
Ties: if two or more days are tied for the last spot (for example two days with 5 votes each for one remaining spot), the app does not pick one quietly. It shows "Tied, Chancery decides" on those days and explains the tie under the standings. The ranking still lists the earlier date first, the same way your Excel did, but it is labelled clearly as a tie.

Your admin page (results and controls)

https://formation-foundations.lovable.app/admin/staff. Sign in with an administrator account; it's also in the left menu as "Staff space".

You'll see:
Voted 9 / 15, Votes cast, Voting Open/Closed, Cut line (Waiting / Clear / Tie)
A table that mirrors the Excel's Ballot sheet: date, day, Chancery pick, votes, rank, result (In / Out / Tied) and who voted.

Buttons:
Copy staff link: copies the /vote link to send.
Open ballot: opens the page staff see.
Export Excel: downloads the results in the same layout as St_Joseph_Holiday_Poll_2027.xlsx (Ballot, Votes and Schedule sheets, same rows and columns), so the numbers drop straight into your file.
Close voting: staff can still see everything, but nobody can vote or add days. Reopen voting undoes it.
Reset votes: deletes every vote, for everyone. It asks for confirmation first and cannot be undone. Comments and added days stay.
🗑 on a row: removes that day from the ballot. Anyone who voted for it gets their vote back.
Staff list tab: rename someone, add a new person (e.g. a new hire), or switch someone off. People switched off disappear from the name list and their votes stop counting; switching them back on restores both.

Differences from the Excel (on purpose, as the task asked)

Sat May 1 was removed. It's a weekend, and the Fri Apr 30 / Mon May 3 options cover it.
8 days were added: Solemnity of St. Joseph (Fri Mar 19), Ash Wednesday, Ascension Thursday, Assumption (obs.), Columbus / Indigenous Peoples' Day, Veterans Day bridge, Our Lady of Guadalupe (obs.), New Year's Eve.

This is the first piece of the "Staff space"

At the top of the page staff see Home · Holidays 2027 · Profile (Soon) · Posts (Soon). The Home page greets them by name and shows open polls. Each person is saved as a real staff record, and their votes and comments belong to that record. When we add staff login later, each person claims their record and keeps everything they did. Polls can be reused: a future poll is a new entry, not a new feature.

What we tested before publishing

15 people voting at the same time: nobody ended with more than 4 votes, and all extra taps were refused.
One person tapping 8 days at the same instant: exactly 4 votes were kept.
Turning votes on and off quickly: the last tap always wins.
A day added in the middle of voting climbed into the top 4.
Very long comments: they wrap correctly on phones.
Live updates: another phone's vote showed up in under a second.
Rejections: weekends, 2028 dates, duplicates and days already off are all refused with a friendly message.

All tests ran on a separate demo copy, so the real ballot is clean.

Good to know

No passwords, on purpose. That keeps it zero-friction, but it means someone could tap a coworker's name. Every vote shows the voter's initials, so it would be visible. If that matters, staff login is the next step.
There is no automatic deadline. Voting stays open until you press Close voting.

Next step: send formation-foundations.lovable.app/vote to the staff.
@Luis Torres

### 2026-10-21 12:05 · Luis Torres
image.png
chancery pick dates are not supossed to be voted on @Cristian Berrío

(Adjunto en el comentario: image.png)

### 2026-10-21 12:11 · Luis Torres
@Cristian Berrío tambien quita el dia de dec 31 porfa

### 2026-10-21 12:18 · Luis Torres
aborta cambios @Cristian Berrío olvidalte de eso

### 2026-10-21 12:18 · Luis Torres
reviertelos si puedes

### 2026-10-21 12:20 · Cristian Berrío
ya los reverti hermano

## Related
- [[01-Brands/St-Joseph/04-Projects/Parish-System/Parish-System-Home|Parish System Home]]
- Solicitud original en la semana OCT 19 🪪: [86e3p6vdw](https://app.clickup.com/t/86e3p6vdw?comment=90170261611242)
