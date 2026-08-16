<img width="100%" src="./assets/hero-3d.svg" alt="Het Patel — Full-Stack Developer" />

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2800&pause=900&color=8B5CF6&center=true&vCenter=true&width=600&lines=Full-Stack+Developer+%C2%B7+MERN+%2B+Next.js;Building+FirstBookit+%E2%80%94+Live+Booking+SaaS;AI-Powered+Products+%C2%B7+Groq+%2B+Claude;Ship+it.+Iterate.+Ship+again." />
</p>

<p align="center">
  <a href="https://buildbyhet.me"><img src="https://img.shields.io/badge/Portfolio-buildbyhet.me-8B5CF6?style=for-the-badge&logo=firefox&logoColor=white" alt="Portfolio"></a>
  <a href="https://linkedin.com/in/Hetkumar-Sanjaykumar-Patel"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:het@buildbyhet.me"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://instagram.com/hetpatel0812"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a>
  <!-- Drop resume.pdf into this repo, then uncomment the line below to publish it:
  <a href="./resume.pdf"><img src="https://img.shields.io/badge/Résumé-PDF-22C55E?style=for-the-badge&logo=readdotcv&logoColor=white" alt="Résumé"></a>
  -->
</p>

---

## 🎯 Open to Work

| | |
|---|---|
| **Looking for** | Full-stack / backend internships now · new-grad SWE roles from **mid-2028** |
| **Available** | Immediately for internships & contract work · part-time alongside coursework |
| **Location** | Ahmedabad, India 🇮🇳 · open to remote and relocation |
| **Strongest in** | Next.js · TypeScript · Node/Express · PostgreSQL + Prisma · production LLM APIs |
| **Reach me** | [het@buildbyhet.me](mailto:het@buildbyhet.me) · [LinkedIn](https://linkedin.com/in/Hetkumar-Sanjaykumar-Patel) · usually reply within a day |

---

## 🚀 About Me

I'm a **Computer Engineering student** and **full-stack developer** working on **[FirstBookit](https://firstbookit.in)** — a live, multi-role sports-venue booking SaaS — where I own features end-to-end: from schema design and API architecture to frontend implementation and production deployment.

I care about shipping things that actually work — clean architecture, production deployments, and code that solves a real problem, not just a demo.

- 🔭 **Currently building:** FirstBookit — a live booking SaaS (Next.js · Express · Prisma · PostgreSQL) — scheduling, dynamic pricing, multi-role auth, Razorpay payments, revenue analytics
- 🤖 **Exploring:** AI-powered products using LLM APIs (Groq, Anthropic/Claude)
- 🏗️ **Shipped:** 25+ production features on a live SaaS · **6 live client websites** · 19+ builds across 16 industries
- 🌱 **Deepening:** Data Structures & Algorithms (Java) and system-design fundamentals
- 📫 **Reach me:** het@buildbyhet.me · [buildbyhet.me](https://buildbyhet.me)

---

## 💼 What I Do

- 🔧 **Full-Stack Development** — MERN stack (MongoDB, Express, React, Node.js), Next.js, REST APIs, end-to-end feature ownership
- 🎨 **Frontend Engineering** — responsive, modern UIs with React, Next.js & Tailwind CSS; performance-focused and mobile-first
- 🏗️ **Backend & Architecture** — multi-role JWT auth, SaaS products, scheduled jobs, payment integrations, serverless & database design
- 🤖 **AI Integration** — building products on top of LLM APIs (Groq, Claude) with streaming, RAG, and real-time interaction
- 🚀 **SaaS Product Development** — working on a live production platform with real users, real payments, and real deadlines

<img width="100%" src="./assets/ship-loop-3d.svg" alt="Ship it. Iterate. Ship again." />

---

## 🛠️ Tech Stack

<img width="100%" src="./assets/stack-orbit-3d.svg" alt="Tech stack in orbit" />

<p align="center">
  <img src="https://skillicons.dev/icons?i=ts,js,react,nextjs,nodejs,express,mongodb,postgres,prisma,tailwind,python,git,github,vercel,postman&perline=8" alt="Tech Stack" />
</p>

**Languages:** TypeScript · JavaScript · Python · SQL · Java (learning DSA)
**Frontend:** React · Next.js · Tailwind CSS · React Query (TanStack)
**Backend:** Node.js · Express · REST APIs · JWT Auth · node-cron
**Databases:** PostgreSQL · MongoDB · Prisma ORM · MongoDB Atlas
**AI & Tools:** Groq · Anthropic (Claude) API · Razorpay · Git · Vercel · Render · Postman

---

## 💼 Professional Work

### 🏟️ [FirstBookit](https://firstbookit.in) — Sports Venue Booking SaaS · Developer

A live, production SaaS platform for sports venue management serving real venues and players. I work as a developer on the team, owning features end-to-end.

<img width="100%" src="./assets/architecture-3d.svg" alt="FirstBookit production architecture — layered isometric diagram" />

**What I've built & shipped — 25+ features across 3 user roles (venue owner · admin · player):**
- 📅 **Schedule template system** — recurring weekly schedules with per-date overrides, so a venue configures a season once instead of editing every day
- 💰 **Dynamic pricing engine** — peak/off-peak rules evaluated timezone-safe, removing a class of bugs that had been mispricing slots across IST day boundaries
- 📊 **Revenue analytics dashboard** — venue-level earnings, booking trends and customer insights, replacing manual register-keeping
- 🧾 **Multi-slot booking flow** — cart-style checkout across multiple slots in one transaction, with Razorpay payments, webhook-confirmed bookings and refunds
- 📱 **WhatsApp booking confirmations** — automated confirmations at the moment payment captures, cutting no-shows from missed SMS
- 🔔 **In-app notification system** — real-time alerts for bookings, cancellations and payments
- 🐛 **Critical production fixes** — eliminated N+1 queries on the booking list, resolved a timezone bug affecting slot boundaries, all through a PR-reviewed workflow

<!-- Numbers to add once you can share them: venues live · monthly bookings · GMV processed ·
     dashboard load time before/after the N+1 fix · uptime. One real figure beats three adjectives. -->



`Next.js 15` · `React 19` · `Express` · `Prisma` · `PostgreSQL` · `Razorpay` · `TanStack Query`

<details>
<summary><b>🧾 How a multi-slot booking actually flows through the system</b></summary>

```mermaid
sequenceDiagram
    autonumber
    participant P as 🧑 Player
    participant W as Next.js App
    participant A as Express API
    participant D as PostgreSQL
    participant R as Razorpay
    participant N as Notifications

    P->>W: Pick venue + multiple slots
    W->>A: POST /bookings/checkout
    A->>D: Validate schedule + price rules
    A->>D: Reserve slots in a transaction
    A->>R: Create payment order
    R-->>P: Payment sheet
    P->>R: Pay
    R-->>A: Webhook payment.captured
    A->>D: Confirm booking + write ledger
    A->>N: Fan out confirmations
    N-->>P: WhatsApp + in-app alert
    A-->>W: Booking confirmed
```

</details>

---

## 🛡️ [DhanRakshak](https://dhanrakshakai.netlify.app/) — On-Device Scam Guardian for Rural India

<p>
  <a href="https://dhanrakshakai.netlify.app/"><img src="https://img.shields.io/badge/Live%20Demo-dhanrakshakai-F5B32A?style=for-the-badge&logo=netlify&logoColor=1a1a1a" alt="Live demo"></a>
  <a href="https://github.com/Het161/DHANRAKSHAK"><img src="https://img.shields.io/badge/Source-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="Source"></a>
  <img src="https://img.shields.io/badge/Maverick%20Effect%20AI%20Challenge-2026-34D399?style=for-the-badge" alt="Maverick Effect AI Challenge 2026">
</p>

A scam guardian for the people UPI brought online and nobody built for. It flags a fraud **before the money moves**, explains **which trick** was used in plain Gujarati, and keeps working with **no internet at all** — because the detector itself ships to the phone.

The part I care about most: **the AI never decides what is a scam.** Rules plus a LightGBM model score every known tactic and set the verdict; the local model only translates that verdict into her words, with the actual RBI/NPCI advisory attached. That's why a small offline model can be trusted here.

<img width="100%" src="./assets/dhanrakshak-3d.svg" alt="DhanRakshak on-device detection pipeline — isometric diagram" />

- 📴 **Offline-first** — real engine exported to the device; verdict in ~150 ms, nothing uploaded
- 🗣️ **Gujarati-first** — language is the first screen, every verdict can be spoken, elder mode throughout
- 🎧 **Practice a scam call, safely** — the app plays the fraudster in a real Gujarati voice and coaches her through spotting each trick
- 📸 **Four inputs, one engine** — SMS/WhatsApp text, links, screenshots (the fake "collect request" trap) and voice notes
- ☎️ **One tap to act** — ask a family member, or report to the 1930 cybercrime helpline

`Next.js PWA` · `FastAPI` · `Rules + LightGBM` · `Qwen (local) + Groq` · `Chroma` · `Whisper + edge-tts` · `Docker`

---

## 🔬 DriftLock — Sub-Pixel Die-Site Recovery for Wafer Inspection

<p>
  <a href="https://www.youtube.com/watch?v=UR5ryk2oOdo"><img src="https://img.shields.io/badge/Demo%20Video-YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Demo video"></a>
  <a href="https://github.com/Het161/driftlock"><img src="https://img.shields.io/badge/Source-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="Source"></a>
  <img src="https://img.shields.io/badge/SEMICON%20India-Applied%20Materials%20PS-3B82F6?style=for-the-badge" alt="SEMICON India · Applied Materials problem statement">
</p>

Built for the **Drift-Sense** problem statement (Applied Materials): a wafer inspection tool must return to the *same* die site thousands of times a day, but the stage drifts — and the layout repeats everywhere, so template matching hands back hundreds of near-identical matches.

Our answer is deliberately **classical CV, grounded in SEM physics** — no deep learning, nothing in the judges' as-is run that can break. We generate DRAM-style data with real SEM noise (Poisson + Gaussian, edge brightening), then localize with a multi-scale ZNCC sweep, the official centre rule, and a sub-pixel fit. Output is `(x, y)` **plus a PSR confidence** — when a field is genuinely ambiguous, we say so instead of guessing.

<img width="100%" src="./assets/driftlock-3d.svg" alt="DriftLock matching pipeline — isometric diagram" />

- 📐 **Incommensurate mat pitches** were the breakthrough — pure lattice data ranked the truth **~762nd** under noise; landmarks that never line up inside the frame took it to **rank 0, 0.43 px error**
- ⚡ **CPU only** — no GPU, no model weights, under a second per pair
- 🧾 **Every generator constant is citation-tagged** in code `[S1]–[S12]`, traced to SEM physics or DRAM 6F² literature
- 🎯 **Honest failure** — the PSR flag exists for the deliberately ambiguous periodic region in the official test set

`Python 3.10` · `NumPy` · `OpenCV` · `SciPy` · `ZNCC multi-scale matching` · `Matplotlib`

*Team DriftLock — Het Patel (lead) · Eklavya Jha, Gandhinagar University*

---

## 🤖 Featured Projects

### 🎯 [HireLoop](https://hireloop-tau.vercel.app/) — AI Mock Interview Platform

An AI interviewer that spans **21 tech roles** with adaptive, real-time questioning in **voice or text mode**. Each ~30-minute session ends with **per-question scored feedback** and a personalized improvement plan. Features a terminal-style UI with token-streamed responses.

`Next.js` · `TypeScript` · `Groq (Llama 3.3 70B)` · `Web Speech API`

<details>
<summary><b>🧠 Architecture</b></summary>

```mermaid
flowchart LR
    U["🎙️ Candidate"] -->|voice or text| UI["Terminal UI<br/>Next.js + TypeScript"]
    UI -->|Web Speech API| STT["Speech to text"]
    STT --> API["Interview route<br/>edge runtime"]
    UI --> API
    API --> CTX["Session context<br/>role + difficulty + history"]
    CTX --> LLM["Groq · Llama 3.3 70B"]
    LLM -->|token stream| API
    API -->|SSE| UI
    CTX --> ADAPT["Adaptive engine<br/>21 role tracks"]
    ADAPT --> SCORE["Per-question scoring"]
    SCORE --> PLAN["📊 Improvement plan"]

    classDef c fill:#8b5cf6,stroke:#c4b5fd,color:#fff,stroke-width:1px
    classDef a fill:#0ea5e9,stroke:#7dd3fc,color:#fff,stroke-width:1px
    classDef o fill:#a855f7,stroke:#e9d5ff,color:#fff,stroke-width:1px
    class U,UI,STT c
    class API,CTX,LLM,ADAPT a
    class SCORE,PLAN o
```

</details>

### 📖 [GitStory](https://git-story-gold.vercel.app/) — AI GitHub Storyteller

Transforms any GitHub user's commits, repositories, and languages into an **AI-generated, magazine-style developer narrative** in seconds, with shareable editorial output.

`Next.js 15` · `MongoDB` · `Anthropic (Claude) API`

<details>
<summary><b>🧠 Architecture</b></summary>

```mermaid
flowchart LR
    IN["👤 GitHub username"] --> GH["GitHub REST + GraphQL<br/>commits · repos · languages"]
    GH --> AGG["Aggregation layer<br/>signals + timeline"]
    AGG --> CACHE[("MongoDB<br/>story cache")]
    AGG --> CLAUDE["Anthropic Claude<br/>narrative generation"]
    CLAUDE --> STORY["📰 Magazine-style story"]
    CACHE --> STORY
    STORY --> SHARE["Shareable page"]

    classDef c fill:#8b5cf6,stroke:#c4b5fd,color:#fff,stroke-width:1px
    classDef a fill:#0ea5e9,stroke:#7dd3fc,color:#fff,stroke-width:1px
    classDef o fill:#a855f7,stroke:#e9d5ff,color:#fff,stroke-width:1px
    class IN,GH c
    class AGG,CACHE,CLAUDE a
    class STORY,SHARE o
```

</details>

---

## 🤝 Client Work — Live in Production

> Six real businesses running on sites I designed, built and deployed. Each one is a paying client's public front door, not a portfolio piece.

<img width="100%" src="./assets/clients-3d.svg" alt="Live client work — six production websites" />

| Business | What they do | Site |
|----------|--------------|------|
| **FindUrTrip** | Travel & tour packages | [findurtrip.org](https://www.findurtrip.org/) |
| **SCE Boiler Spares** | Industrial boiler spares & supply | [sceboilerspares.com](https://www.sceboilerspares.com/) |
| **KBC Global** | Private-label manufacturing & brand building (D2C) | [kbcglobal.in](https://www.kbcglobal.in/) |
| **BLS Packaging** | Bottles, caps, closures & perfume packaging | [blspackaging.in](http://blspackaging.in/) |
| **Shree Har Packaging** | Bag-closing machines & packaging equipment | [shreeharpackaging.in](https://www.shreeharpackaging.in/) |
| **TT Marketing** | Industrial weighing systems & digital scales | [ttmarketing.co.in](https://ttmarketing.co.in/) |

---

## 🎨 Demo Sites — Built to Show Clients

> One complete build per industry, made so a prospective client can see their own business before committing. Layout, copy, responsive pass and deploy — all of it real.

<img width="100%" src="./assets/demos-3d.svg" alt="Demo sites — eleven industries" />

| Industry | Project | Link |
|----------|---------|------|
| 🏥 Healthcare | Sanjeevani Hospital | [Visit](https://sanjeevani-hospital-blush.vercel.app/) |
| 🦷 Dental | ARIA Dental Studio | [Visit](https://arhaclinic.netlify.app/) |
| 🏋️ Fitness | Forge Gym | [Visit](https://forgegymdemo.netlify.app/) |
| 💇 Salon & Beauty | Lumiere Salon | [Visit](https://lumieresalondemo.netlify.app/) |
| ⚖️ Legal | Mehta & Kapadia | [Visit](https://lawdemowebsite.netlify.app/) |
| 🏛️ Architecture | Angan Architecture | [Visit](https://anganarechitecture.netlify.app/) |
| 🏢 Real Estate | Aavas Realty | [Visit](https://aavas-realty.vercel.app/) |
| 🎓 Education | Aakash International School | [Visit](https://aakash-international-school.vercel.app/) |
| 🍽️ Restaurant | Angan Restaurant | [Visit](https://angan-restaurant.vercel.app/) |
| 🎉 Events | Mehr Events | [Visit](https://mehrevents.netlify.app/) |
| 🛒 E-commerce | Apna Bazar | [Visit](https://apna-bazar-rust.vercel.app/) |

<p align="center"><b>→ See all 19+ projects at <a href="https://buildbyhet.me">buildbyhet.me</a></b></p>

---

## 🧊 3D Contribution Graph

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./profile-3d-contrib/profile-night-rainbow.svg">
    <source media="(prefers-color-scheme: light)" srcset="./profile-3d-contrib/profile-season-animate.svg">
    <img src="./profile-3d-contrib/profile-night-rainbow.svg" alt="3D Contribution Graph" />
  </picture>
</div>

---

## 📊 GitHub Stats

<img width="100%" src="./assets/github-stats-3d.svg" alt="GitHub stats — repos, stars, followers and top languages" />

<div align="center">
  <img src="https://streak-stats.demolab.com?user=Het161&theme=tokyonight&hide_border=true&ring=8B5CF6&fire=F85D7F&currStreakLabel=8B5CF6" alt="GitHub Streak" />
</div>

<div align="center">
  <img width="98%" src="https://github-readme-activity-graph.vercel.app/graph?username=Het161&theme=tokyo-night&hide_border=true&area=true&custom_title=Contribution%20Activity&color=8B5CF6&line=22D3EE&point=F472B6" alt="Contribution activity graph" />
</div>

---

## 🐍 Contribution Snake

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Het161/Het161/output/github-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Het161/Het161/output/github-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/Het161/Het161/output/github-snake.svg">
  </picture>
</div>

---

<details>
<summary><b>🎨 About the 3D artwork in this README</b></summary>

<br/>

The isometric scenes above (`hero`, `architecture`, `stack orbit`, `ship loop`) are **hand-generated animated SVGs** — no images, no JavaScript, no external libraries. Every cube is projected with real isometric math and animated with native SVG `<animate>` / `<animateMotion>`, so they run anywhere GitHub renders an image.

They're reproducible: [`assets/generate-3d-assets.py`](./assets/generate-3d-assets.py) rebuilds the scenes, and [`assets/generate-stats-card.py`](./assets/generate-stats-card.py) rebuilds the stats card from the GitHub API — no third-party image host that can go down.

```bash
python3 assets/generate-3d-assets.py
python3 assets/generate-stats-card.py Het161
```

| Asset | What it shows |
|-------|---------------|
| [`hero-3d.svg`](./assets/hero-3d.svg) | Isometric skyline where each tower bobs on its own easing curve |
| [`architecture-3d.svg`](./assets/architecture-3d.svg) | FirstBookit's four layers, with request packets travelling between them |
| [`stack-orbit-3d.svg`](./assets/stack-orbit-3d.svg) | The stack orbiting a core cube, fading as each node passes behind |
| [`ship-loop-3d.svg`](./assets/ship-loop-3d.svg) | plan → build → ship → measure → iterate, on a loop |
| [`dhanrakshak-3d.svg`](./assets/dhanrakshak-3d.svg) | Four inputs into one on-device engine, inside a "nothing leaves the phone" boundary |
| [`driftlock-3d.svg`](./assets/driftlock-3d.svg) | A repeating die field being swept, decoy matches fading, the true site locked at 0.43 px |
| [`clients-3d.svg`](./assets/clients-3d.svg) | Six client sites as isometric browser windows, each with a live pulse and a shine sweep |
| [`demos-3d.svg`](./assets/demos-3d.svg) | The demo wall — eleven industries, lit one at a time on a rolling cycle |
| [`github-stats-3d.svg`](./assets/github-stats-3d.svg) | Live repo/star/follower counts and a 3D language chart, regenerated daily by [`stats.yml`](./.github/workflows/stats.yml) |

</details>

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=Het161&label=Profile%20Views&color=8B5CF6&style=flat" alt="Profile Views" />

  ### 💡 "Ship it. Iterate. Ship again."

  <b>Open to full-time & internship roles · Ahmedabad, India 🇮🇳</b>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,20&height=120&section=footer" />
