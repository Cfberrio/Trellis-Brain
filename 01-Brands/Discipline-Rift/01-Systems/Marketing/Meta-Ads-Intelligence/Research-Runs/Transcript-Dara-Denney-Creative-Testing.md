---
brand: Discipline-Rift
area: systems
subarea: marketing
note_type: evidence
status: active
canonical: true
used_for_ai: true
source_type: derived
source_reference: "Repo TrellisClaudeCode — domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/dara-denney-test-creatives-every-budget-transcript.md"
repo_path: domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/dara-denney-test-creatives-every-budget-transcript.md
owner: Cristian
last_updated: 2026-08-20
sensitivity: internal
hub_role: leaf
tags:
  - meta-ads
  - meta-ads/research-run
  - discipline-rift
aliases:
  - "Dara Denney creative testing transcript"
---

# Raw source — Dara Denney — "How to Test Facebook Ads Creatives at Every Budget (2026)"

## Parent
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Research-Runs-Index|Research runs — índice]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Meta-Ads-Intelligence-Home|Meta Ads Intelligence — Home]]

## Relacionado
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Experts/Expert-Dara-Denney|Dara Denney]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Research-Runs/Evidence-Dara-Denney-Creative-Testing|Mapa de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Evidence-Model|Modelo de evidencia]]
- [[01-Brands/Discipline-Rift/01-Systems/Marketing/Meta-Ads-Intelligence/Method/Meta-Ads-Research-Questions|Preguntas de investigación (A1–S2)]]

> [!info] Fuente y sincronización
> Copia fiel de `domains/ads/meta/intelligence/knowledge/research-runs/2026-08-14_youtube-apify/dara-denney-test-creatives-every-budget-transcript.md` (repo **TrellisClaudeCode**), sincronizada el 2026-08-20.
> El repo sigue siendo donde corre el pipeline. Esta bóveda es la capa de lectura y extracción: si el archivo del repo cambia, hay que volver a sincronizar esta nota.

---

**Status:** RAW SOURCE ARTIFACT. Not ingested. Not a DR claim. Not an operating rule.
**Level:** EXTERNAL PRACTITIONER CLAIM (source material only — see the paired `-evidence.md`).

---

## 1. Source identity

| Field | Value |
|---|---|
| Video title | How to Test Facebook Ads Creatives at Every Budget (2026) |
| URL | `https://www.youtube.com/watch?v=7knQyPYLmfo` |
| Video ID | `7knQyPYLmfo` |
| Channel | Dara Denney (`@daradenney`) |
| Channel ID | `UCFF55suuW0LjzXEnzDTNCnA` |
| Creator / expert | Dara Denney |
| `published_at` | **2025-03-28T12:30:07Z** |
| Duration | 1026 s (17:06) |
| Subscriber count at capture | 141,000 |
| View count at capture | 52,984 |
| Like count at capture | 1,630 |
| Comment count at capture | 195 |
| Geo restriction | none (`geo_restrict: null`) |

### ⚠ Title/date discrepancy — recorded, not resolved

The YouTube title says **"(2026)"** but `published_at` is **2025-03-28**, and the spoken transcript
says *"how to test ad creative in **2025**"* (0:00) and *"meta's algorithm is so advanced in **2025**"*
(1:22) and *"the easiest way to run meta ads creative right now in **2025**"* (4:01).

Conclusion: the video was **published 2025-03-28**; the on-platform title appears to have been
edited later for search. **Treat this source as ~17 months old and PRE-ANDROMEDA.** Do not treat
the "(2026)" in the title as a recency signal.

### Description (verbatim, as returned)

```
Sign-up for a 14 day Free Trial of Particl: https://bit.ly/3XPBapB

00:00:00 - 00:00:31 Why am I showing 3 different ways to test creatives?
00:00:32 - 00:03:00 How to Test Creatives w/ Small Budgets
00:03:01 - 00:04:41 Why I Use ASC for testing small budgets
00:04:42 - 00:06:39 My Expert Tip for Testing at Any Budget (Particl)
00:06:40 - 00:11:28 How to Test Creatives at $50K+ per month (Growth)
00:11:29 - 00:15:43 Big Budget Testing
00:15:44 - 00:17:04 Why I made this video

Meet Miguel: https://www.youtube.com/watch?v=nkJY6j_hFKg
```

---

## 2. Extraction metadata

| Field | Value |
|---|---|
| Retrieved | 2026-08-14 |
| Tool | Apify MCP |
| Discovery Actor | `logiover/youtube-search-scraper` — run `iIeFcdM517OHoaIxY`, dataset `LE2nS5MzgKh7f8ZY2` |
| Extraction Actor | `starvibe/youtube-video-transcript` — run `ikyrKAGH2aM7NlwrK`, dataset `xT5aaEkGr7n0a3yA7` |
| Caption track | `English (auto-generated)` — `is_auto_generated: true`, `language: en` |
| Transcript status | **COMPLETE** — 0.12 s → 1027.28 s of a 1026 s video. No gap. |
| Timestamps | Preserved. Blocks below are labelled with the segment start time. |
| Editing | Consecutive caption segments joined into readable blocks. **Wording unchanged.** Auto-caption errors preserved verbatim (`creat learnings`, `add toart`, `Barry hot`, `in even a little mad`, dropped words where the ASR lost audio). Nothing summarised, removed, or rewritten. |
| Raw JSON | Not committed. Re-retrievable from Apify dataset `xT5aaEkGr7n0a3yA7` (see §Extraction metadata). |

### Known ASR defects (verbatim, flagged — meaning NOT reconstructed)

At **8:16** and **12:28** the auto-captions **drop the word naming the budget mode**:

> *"the question of whether or not you should use ␣␣ or CBO is really a media buyer decision I personally generally use ␣␣ so that I can get a quick read"*
> *"I often find at this stage nearly all brands are using ␣␣ if you're actually working for one of these Brands and you're not using ␣␣ let me know"*

Context (contrast with CBO, "throttling that spend", per-ad-set budget) makes **ABO** the
overwhelmingly likely missing term, **but the captions do not contain it.** Recorded as a gap.
Do not quote these lines as if the word were present.

---

## 3. Complete transcript

**[0:00]** how to test ad creative in 2025 I am going to do something that has never been done on YouTube before I'm not going to show you just one way to test your meta ads creative I'm going to show you three because I believe this next statement to my core the way that you test ad creative when you're spending $3 million per month is vastly different than when you're just starting off or you have a much lower budget so let's jump into the ad account I'm going to show you exactly how I test creative at these different level levels for e-commerce

**[0:32]** so let's start with the lower budgets and how I would structure a creative testing for brands that are going to be spending anywhere from 5 grand to 15 grand per month or even a little bit lower in spoiler alert at this stage we are only using one campaign So in theory it's all creative testing especially if you're just getting started now I've actually set up a few first campaigns for some new brands recently and this is exactly how I do it because you're able to get those first few initial creat learnings without over complicating the setup

**[1:04]** so Dar here from the editing Bay really quick we are going to be going right for a sales campaign here that's going to be optimizing for purchases there is no way even if you are just starting off as a brand new brand if you want to go after those purchases we are not starting with traffic campaigns we are not starting with engagement campaigns or add toart campaigns meta's algorithm is so advanced in 2025 that you just have to tell what you want to go after which in this case is going to be those purchases

**[1:36]** now for Brands and businesses that are on the lower end of this budget Spectrum I really like to limit the ad creative to 10 in generally I really like to lean on primarily Statics to get back those first few pieces of creative learnings but often times I'll include a ugc style ad or even a ugc style Founders ad especially if it's already in the vault and they already have this ad creative available however like I mentioned I would really start focusing on Statics just because they're a lot easier to make and you can get more those messaging learnings that you can then roll into videos

**[2:12]** but the type of Statics I'd make sure that you are testing include benefit call out ads Us Versus Them headline ads ugly ad Statics testimonial Statics and again if you already have video creative that performed really well on Tik Tok or reals that's also something that I would include in your initial rounds of testing however wouldn't start testing a ton of new video until you start learning what type of messaging is actually converting your customers

**[2:39]** again start with 10 ad creatives at those lower budgets and then you can start to add another ad creative or two every single week and I wouldn't worry too much about turning ads off unless they really aren't meeting your CPA goal and for some reason the algorithm is spending a lot on them otherwise I would just let them run

**[2:58]** also I know if you've seen some of my past testing videos you might be surprised in even a little mad to hear that I'm using Advantage Plus shopping campaigns for testing at this level but hear me out I want to explain why so number one you can actually test more ad creatives more efficiently using an ASC campaign now compared to the growth testing stage where you're likely going to be spreading out that budget across different adsets and even a little bit across different campaigns if you're just using one ASC this is truly the most Consolidated type of setup that you can have

**[3:34]** essentially you want to make sure that your budget allows you to get out of the learning phase and this setup will help you do that at that lower budget and also because you're allowed to test more creatives more creatives means more opportunities to convert your customers so we are essentially able to hey have a more Consolidated campaign but have more ad creatives in that campaign underneath the setup

**[3:54]** and number two it's a way easier setup to manage so if you're a solopreneur doing it all yourself this is honestly the easiest way to run meta ads creative right now in 2025 is using one ASC campaign this way you don't have to worry about adding adsets tinkering with audiences trying to figure out retargeting or prospecting it just keeps it all in one campaign

**[4:21]** and I especially think if you are a brand new brand this is really powerful it also puts you in a much better position to again get those initial creative learnings and then be able to test other types of setups and account structures when you already have an idea about what works on the creative end which is a really good thing to do because your creative is going to be your biggest lever on the platform

**[4:44] — [SPONSOR SEGMENT — Particl, retained verbatim: it contains substantive merchandising claims]**
before we dive into the second creative testing method I want to share with you one of my new favorite tools particle which has genuinely changed the way that I approach creative testing especially at the growth and scale levels particle gives you real-time sales pricing andc data on some of the world's top brands and honestly one of the biggest gaps that I see right now in Creative testing is actually coming from the product and Merchandising perspective AKA figuring out what types of products and bundles to test bundles is especially a huge one which is why I really like looking inside of particle to see what types of products are actually selling for Brands

**[5:26]** they have two new features that I want to share with you number one is the marketing asset Library where you can get a full snapshot of a Brand's marketing from emails and website assets to social media creatives and yes even ad creatives and probably one of my most favorite features is events here you can see everything from sitewide discounts to product launches and even variant restocks all in one place

**[5:48]** so lately one of my big focuses as a creative strategist has been using meta ads and creative testing to explore better merchandising strategies for the brands that I work with even things like naming products differently or bundling different products together not too many people talk about this online yet but this is honestly where a number of my recent wins have been knowing how to look at a product suite and which products to position or bundles to create to then showcase on meta ads is candidly expert tier creative strategy

**[6:20]** and particle helps me zero in on what's actually selling and how they're being marketed which helps put me in a way better position to figure out how to implement those for my own Brands so if you work at a brand or you're doing research agency side this is truly a no-brainer please let me know in the comments if you have any questions at all about particle I am genuinely so passionate about this product and I would be super happy to help you out

**[6:42]** all right so if you are past that lean testing phase and you consistently starting to spend $1,000 per day or $30,000 per month or even up to $50,000 per month you have entered into what I call the growth testing phase so let's hop into the ad account and I can show you exactly what this looks like

**[7:00]** now what you'll notice is that many ad Accounts at this stage actually just have two core campaigns in fact you can and should just keep the ASC campaign that you had from the previous level as long as there is performance of course now I'll say this out ofcurrent structure is widely accepted as a best practice now Barry hot even broke it down in his recent course which was really awesome to see

**[7:22]** but you'll see here that we've added a creative testing campaign now this is a manual campaign not an ASC and when we top inside you'll actually see that every single test gets its own ad set so instead of tossing one to two new ads into an ASC every time you want to test a creative I actually create a new ads set here for each testing concept

**[7:46]** and typically I am going to be putting three to six ad creatives inside of each if you are on the lower end of that budget go ahead and just put in three but if you're working with a little bit more budget then sometimes that's where I see people test ing six to seven creatives

**[8:00]** now I typically recommend $100 to $200 per adset per day and I'll say too the question of whether or not you should use ␣␣ or CBO is really a media buyer decision I personally generally use ␣␣ so that I can get a quick read on ad creatives by throttling that spend so within a few short days I know hey is this ad creative going to work or not I don't have that looming question

**[8:30]** but I know many brands that use CBO here really successfully and I actually know of several six to seven figure Brands who actually use the one campaign method using this exact campaign in fact my business partner Miguel actually has a great YouTube video where he breaks down exactly how he does this for brands in that growth stage it's a super effective setup and it's absolutely another option that you have to test if you find that those ASC campaigns aren't working as well

**[9:02]** for either way CBO or ␣␣ your creative testing at the ad level is going to look exactly the same and at this stage yes you're going to have some tests that are more focused on images but I do find a lot of brands in this stage are concentrating a lot more on video and again each ad set is going to be it's each individual creative test and inside of that creative test you're going to have anywhere from four to six creatives or variations of those creative

**[9:27]** and at this stage I would have those variations take much bigger swings in your messaging I actually mentioned this last year in the video and it's something that I absolutely still do today so for instance you should do a creative test that's a little bit more like this as opposed to doing something like this and for videos that's going to be a really similar thing except you're going to be testing out different hooks again take those bigger swings and I also see a number of Brands testing out different lengths of video time here which is something that I really like to play with as well

**[9:55]** now ultimately the structure as a whole is going to do a few things for you number one it's going to isolate your creative testing from your scaling budget so that ASC campaign is essentially going to become your scaling campaign and what I like to do is when I find Winners in the creative testing campaign I'm going to then duplicate those into the ASC campaigns so it starts to become a campaign of winners

**[10:21]** and having your testing in a different campaign from your scaling helps keep the data quite a bit cleaner and it also stops from muddying performance with unproven tests which ultimately is going to give you more stability across campaigns I can't tell you how many times I've added a creative test to an otherwise performing campaign and I saw performance tank ultimately this is going to give you a lot more stability across your campaigns

**[10:44]** this structure also introduce variation testing which is going to allow us to really zero in on what type of messaging and formats are really converting and allow us to get quite granular with what is actually going to make them convert

**[10:59]** and the final reason it's a great foundation for scaling you have two campaigns one that is an ASC that is starting to be compounded with a lot more winners and you also have the creative testing campaign and as you are building them up side by side as long as they're getting performance having those two campaigns is ultimately another way to scale I used to call this horizontal scaling where you are essentially adding in more adets or more campaigns as opposed to Vertical scaling which is just increasing the budget ultimately brands that grow need a little bit of both

**[11:30]** all right let's talk about creative testing for big budget Brands AKA brands that are spending more than a million dollars per month on meta ads so how exactly is this different from the growth States well I'm going to be really honest functionally as it relates to the creative testing campaign it's not going to be wildly different typically you're still going to see only one creative testing campaign inside of these accounts

**[11:55]** now I've worked at Brand spending $5 million per month and they still just have one creative test Tes in campaign it's actually the things that are outside of that creative testing campaign that start to become a lot more complex

**[12:05]** now I will say that a few creative agencies do require their own creative testing campaign I'm not going to name any names but they're only doing this for reporting reasons it doesn't actually help things performance-wise

**[12:22]** another thing to note too is I often find at this stage nearly all brands are using ␣␣ if you're actually working for one of these Brands and you're not using ␣␣ let me know I'm just a little bit curious about that now I would still consider this a media bu choice because I've seen a select few ad accounts recently that were successfully using CBO at scale like this it's just not something that I see that often and I imagine that's because the creative teams want to get a really quick read on their ad creative so that they can start iterating and ingesting learnings for their road map a lot more quickly

**[12:54]** another thing to note to is I often see brands at this stage testing using cost caps not all the time by any means but really when you're starting to spend at these levels you have a good idea of what your target CPA should be on meta ads and if you already have a ton of great creative that's already performing well for you you really want to make your additional creative tests really perform well and only get the best of the best which is why you're going to likely add in that cost cap for those testing campaigns

**[13:23]** now I'm not going to leave you hanging once we get inside of ads manager to be honest the testing campaign is pretty much going to be looking exactly the same as I showed you in the gross stage and in theory too when you're at this stage you're going to already have a really good idea about what's working which is going to help guide your overall strategy

**[13:39]** I see most brands here launching creative tests at 200 per day and then they'll let it run for 7 days or so or maybe until it gets to a th000 and of course if you get an early read on a creative you see that it's working really well or you see that it's you know totally tanking they'll turn it off but if they see it's working well they'll start to scale it up you know as soon as possible really

**[14:01]** so what truly is the difference right it's primarily going to be volume you're going to be testing anywhere from 10 to 20 sometimes even more creative tests per week and it's not just more volume it's also a little bit more refined because at this stage you already have a pretty good idea about what's working so when you are doing more of that variation testing you're actually going to be testing a lot more slight differences here I'd say you're going to be doing more things like this instead of those bigger swings that we were doing in the growth testing phase

**[14:31]** and I'd also say here too that the creatives that you're going to be testing are just going to become a lot bigger swing so likely you're going to start testing into celebrities into bigger influencers you're going to be testing out some more higher production maybe you're going to do a high production Founders ad if a low five Founders ad is something that you saw worked really well when you are getting at the stage it's really about diversifying the type of creative that you have and doing that at a higher volume

**[15:01]** it's not an easy thing to do and I will will be so blunt I've seen the backend and how many brands are working and I'd say that we're all still learning the best methods to really make this work so while the testing structure itself doesn't change a ton from the growth to scale stage the complexity absolutely does you're going to have a lot more volume a lot more creative diversity which is why you know your team is going to look a lot lot different at this stage

**[15:27]** I actually think that's candidly the big thing that is going to change from that growth to scale stage is really the makeup of your team and if that's something that interests you please let me know in the comments I can definitely make more content about that

**[15:40]** now I find that most gurus online like to tell people that there's only one right way to do things on meta ads and I'm hoping that this video showed you that it's just not true my goal with this video ultimately was to show you that there are multiple ways to succeed on this platform which is really important to know when things don't seem to be working as well

**[16:07]** now I'll be blunt nine times out of 10 you likely have a creative problem on your hands especially if you're at those earlier stages so don't throw in the towel immediately on the format if you're not getting a winner just yet but I will say yeah you know if you're plugging Along on meta ads and it just doesn't seem to be working try a different testing strategy

**[16:25]** because ultimately I found that one of the most important things to success on meta ads is actually your mindset you absolutely have to have a testing mindset and really truly be curious about what is going to make your customers convert and I hope that this video gave you a little bit more insight into how I think about these things which is absolutely different when I'm working with a brand that is completely new and launching their first meta ads campaign to the brands that are scaling into the millions of AD ad sets that are scaling into the millions of ad spend per month it is a completely different ball game anyways love you so much see you next week bye

**[17:07] — END OF TRANSCRIPT**
