<img width="100%" src="./assets/hero-3d.svg" alt="Het Patel — Full-Stack Developer" />

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2800&pause=900&color=8B5CF6&center=true&vCenter=true&width=600&lines=Full-Stack+Developer+%C2%B7+MERN+%2B+Next.js;Building+FirstBookit+%E2%80%94+Live+Booking+SaaS;AI-Powered+Products+%C2%B7+Groq+%2B+Claude;Ship+it.+Iterate.+Ship+again." />
</p>

<p align="center">
  <a href="https://buildbyhet.me"><img src="https://img.shields.io/badge/Portfolio-buildbyhet.me-8B5CF6?style=for-the-badge&logo=firefox&logoColor=white" alt="Portfolio"></a>
  <a href="https://linkedin.com/in/Hetkumar-Sanjaykumar-Patel"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:het@buildbyhet.me"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://instagram.com/hetpatel0812"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a>
</p>

---

## 🚀 About Me

I'm a **Computer Engineering student** and **full-stack developer** working on **[FirstBookit](https://firstbookit.in)** — a live, multi-role sports-venue booking SaaS — where I own features end-to-end: from schema design and API architecture to frontend implementation and production deployment.

I care about shipping things that actually work — clean architecture, production deployments, and code that solves a real problem, not just a demo.

- 🔭 **Currently building:** FirstBookit — a live booking SaaS (Next.js · Express · Prisma · PostgreSQL) — scheduling, dynamic pricing, multi-role auth, Razorpay payments, revenue analytics
- 🤖 **Exploring:** AI-powered products using LLM APIs (Groq, Anthropic/Claude)
- 🏗️ **Shipped:** 25+ production features on a live SaaS + 19 demo & client sites across 16 industries
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

**What I've built & shipped:**
- 📅 **Schedule template system** — recurring weekly schedules with override support
- 💰 **Dynamic pricing engine** — peak/off-peak pricing rules with timezone-safe calculations
- 📊 **Revenue analytics dashboard** — venue-level earnings, booking trends, and customer insights
- 🧾 **Multi-slot booking flow** — cart-style booking with Razorpay payment integration & refunds
- 📱 **WhatsApp booking confirmations** — automated notifications via messaging API
- 🔔 **In-app notification system** — real-time alerts for bookings, cancellations & payments
- 🐛 **Critical production fixes** — N+1 query optimization, timezone bug resolution, PR-reviewed workflow

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

## 🤖 Featured Projects

### 🎯 [HireLoop](https://hireloop-tau.vercel.app/) — AI Mock Interview Platform

An AI interviewer that spans **21 tech roles** with adaptive, real-time questioning in **voice or text mode**. Each ~30-minute session ends with **per-question scored feedback** and a personalized improvement plan. Features a terminal-style UI with token-streamed responses. Open source (MIT).

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

### 🧠 CiteMind — AI Citation Memory Agent · 🏆 HackBaroda 2026 Finalist

A full-stack AI agent that monitors brand citations across AI search engines (ChatGPT, Perplexity, Claude) and diagnoses citation decay in real time, using persistent memory to learn which fixes recover citations over time.

`Next.js` · `Node.js/Express` · `MongoDB` · `Groq` · `Hindsight`

<details>
<summary><b>🧠 Architecture</b></summary>

```mermaid
flowchart TD
    subgraph PROBE["🔍 Probe layer"]
        P1["ChatGPT"]
        P2["Perplexity"]
        P3["Claude"]
    end
    subgraph CORE["⚙️ Agent core"]
        DET["Citation detector"]
        DIAG["Decay diagnosis"]
        MEM["Hindsight memory<br/>what fixed what"]
    end
    subgraph OUT["📈 Surface"]
        DASH["Live dashboard"]
        REC["Ranked fix recommendations"]
    end

    P1 --> DET
    P2 --> DET
    P3 --> DET
    DET --> DIAG
    DIAG --> MEM
    MEM -->|learned playbook| REC
    DIAG --> DASH
    REC --> DASH
    REC -.->|re-test| P1

    classDef c fill:#8b5cf6,stroke:#c4b5fd,color:#fff,stroke-width:1px
    classDef a fill:#0ea5e9,stroke:#7dd3fc,color:#fff,stroke-width:1px
    classDef o fill:#a855f7,stroke:#e9d5ff,color:#fff,stroke-width:1px
    class P1,P2,P3 c
    class DET,DIAG,MEM a
    class DASH,REC o
```

</details>

---

## 🌐 Demo & Client Projects

> 19+ websites designed and built across 16 industries — a mix of live client work and portfolio demos.

| Industry | Project | Link |
|----------|---------|------|
| ✈️ Travel | FindUrTrip *(live client)* | [Visit](https://findurtrip.org/) |
| 🏭 Industrial | SCE Boiler Spares *(live client)* | [Visit](https://sceboilerspares.vercel.app/) |
| 🏥 Healthcare | Sanjeevani Hospital *(demo)* | [Visit](https://sanjeevani-hospital-blush.vercel.app/) |
| 🦷 Dental | ARIA Dental Studio *(demo)* | [Visit](https://arhaclinic.netlify.app/) |
| 🏋️ Fitness | Forge Gym *(demo)* | [Visit](https://forgegymdemo.netlify.app/) |
| 💇 Salon & Beauty | Lumiere Salon *(demo)* | [Visit](https://lumieresalondemo.netlify.app/) |
| ⚖️ Legal | Mehta & Kapadia *(demo)* | [Visit](https://lawdemowebsite.netlify.app/) |
| 🏛️ Architecture | Angan Architecture *(demo)* | [Visit](https://anganarechitecture.netlify.app/) |
| 🏢 Real Estate | Aavas Realty *(demo)* | [Visit](https://aavas-realty.vercel.app/) |
| 🎓 Education | Aakash International School *(demo)* | [Visit](https://aakash-international-school.vercel.app/) |
| 🍽️ Restaurant | Angan Restaurant *(demo)* | [Visit](https://angan-restaurant.vercel.app/) |
| 🎉 Events | Mehr Events *(demo)* | [Visit](https://mehrevents.netlify.app/) |
| 🛒 E-commerce | Apna Bazar *(demo)* | [Visit](https://apna-bazar-rust.vercel.app/) |

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

<div align="center">
  <img height="165em" src="https://github-readme-stats.vercel.app/api?username=Het161&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true&hide_border=true" alt="Het's GitHub stats" />
  <img height="165em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Het161&layout=compact&langs_count=6&theme=tokyonight&hide_border=true" alt="Top languages" />
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=Het161&theme=tokyonight&hide_border=true&ring=8B5CF6&fire=F85D7F&currStreakLabel=8B5CF6" alt="GitHub Streak" />
</div>

<div align="center">
  <img width="98%" src="https://github-readme-activity-graph.vercel.app/graph?username=Het161&theme=tokyo-night&hide_border=true&area=true&custom_title=Contribution%20Activity&color=8B5CF6&line=22D3EE&point=F472B6" alt="Contribution activity graph" />
</div>

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=Het161&theme=algolia&no-frame=true&no-bg=true&margin-w=8&column=7" alt="GitHub trophies" />
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

They're reproducible: [`assets/generate-3d-assets.py`](./assets/generate-3d-assets.py) rebuilds all four files.

```bash
python3 assets/generate-3d-assets.py
```

| Asset | What it shows |
|-------|---------------|
| [`hero-3d.svg`](./assets/hero-3d.svg) | Isometric skyline where each tower bobs on its own easing curve |
| [`architecture-3d.svg`](./assets/architecture-3d.svg) | FirstBookit's four layers, with request packets travelling between them |
| [`stack-orbit-3d.svg`](./assets/stack-orbit-3d.svg) | The stack orbiting a core cube, fading as each node passes behind |
| [`ship-loop-3d.svg`](./assets/ship-loop-3d.svg) | plan → build → ship → measure → iterate, on a loop |

</details>

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=Het161&label=Profile%20Views&color=8B5CF6&style=flat" alt="Profile Views" />

  ### 💡 "Ship it. Iterate. Ship again."

  <b>Open to full-time & internship roles · Ahmedabad, India 🇮🇳</b>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,20&height=120&section=footer" />
