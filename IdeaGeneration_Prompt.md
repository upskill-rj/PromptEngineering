# Idea Generation Prompt Framework

**Document Version**: 2.0  
**Last Updated**: 2026-05-09  
**Maintainer**: upskill-rj  
**License**: Open Source  

---

## 📋 Executive Overview

This document provides a **systematic framework** for generating high-quality ideas across multiple domains using AI-assisted prompting. It follows enterprise-grade principles:
- **Modularity**: Reusable components and templates
- **Consistency**: Standardized structure for all prompts
- **Scalability**: Framework supports custom extensions
- **Measurability**: Success metrics for idea validation
- **Documentation**: Complete rationale and best practices

---

## 🎯 Core Framework

### Prompt Architecture Pattern

Each prompt in this framework follows this structure:

```
[ROLE] + [CONTEXT] + [SPECIFIC REQUEST] + [CONSTRAINTS] + [OUTPUT FORMAT] + [EVALUATION CRITERIA]
```

**Why this matters:**
- **Role**: Positions AI with appropriate expertise level
- **Context**: Establishes constraints and domain knowledge
- **Request**: Clear, measurable objective
- **Constraints**: Defines scope and limitations
- **Output Format**: Ensures actionable responses
- **Evaluation**: Provides quality benchmarks

---

## 📚 Prompt Catalog by Domain

### Category 1: Creative & Innovation
**Purpose**: Generate original ideas with market/audience consideration  
**Success Metric**: Ideas are actionable, novel, and audience-aligned

#### 1.1 Creative Project Ideation
```
You are a creative strategist with expertise in [DOMAIN: art, design, writing, etc.].

CONTEXT:
- My passion/interest: [specific interest or hobby]
- Current skill level: [beginner/intermediate/advanced]
- Available resources: [budget, time, materials]
- Target outcome: A project that showcases my capabilities

REQUEST:
Generate 5-7 unique project ideas that:
1. Align with my passion and skills
2. Are feasible within my constraints
3. Have clear differentiation from existing work
4. Include revenue/portfolio potential

For each idea, provide:
- Project name and 1-line description
- Required skills and resources
- Estimated timeline
- Success indicators
- Difficulty assessment

CONSTRAINTS:
- Ideas must be original (not direct copies)
- Must be completable within 3-6 months
- Should leverage emerging trends in the field
```

**Validation Checklist:**
- [ ] Ideas are specific and actionable
- [ ] Resource requirements are realistic
- [ ] Market viability is apparent
- [ ] Each idea has distinct positioning

---

#### 1.2 Business Concept Development (Niche Market)
```
You are a business strategist specializing in niche market validation and go-to-market strategy.

CONTEXT:
- Target niche market: [description of specific market segment]
- Problem being solved: [define the core pain point]
- Differentiation factor: [what makes this unique]
- Business model preference: [B2B, B2C, B2B2C, hybrid]
- Startup stage: [idea/pre-seed/seed/validation]

REQUEST:
Develop a comprehensive business concept including:

1. **Market Analysis**
   - Market size estimation and growth trajectory
   - Competitive landscape (3-5 key competitors)
   - Customer persona (demographics, psychographics, behaviors)
   - Market entry barriers and opportunities

2. **Value Proposition**
   - Unique value proposition (one sentence)
   - Key differentiators (vs. alternatives)
   - Pricing strategy rationale

3. **Revenue Model**
   - Primary revenue stream
   - Secondary revenue streams (if applicable)
   - Unit economics (gross margin expectations)

4. **Go-to-Market Strategy**
   - Initial customer acquisition channels
   - Customer lifecycle strategy
   - Key performance indicators (KPIs)

5. **Risk Assessment**
   - Top 3 business risks and mitigation
   - Technical/operational risks
   - Market timing risks

6. **Validation Roadmap**
   - Minimum viable product (MVP) definition
   - Validation hypotheses
   - Success metrics for next phase

OUTPUT FORMAT:
Use a structured markdown format with sections, bullet points, and clear hierarchy.
Include 1-2 sentence justifications for key decisions.

EVALUATION CRITERIA:
- Concept viability: 1-10
- Market opportunity: 1-10
- Execution feasibility: 1-10
- Competitive positioning: 1-10
```

**When to Use:** Before investing time/capital in a business idea  
**Expected Output Quality**: Executive summary level, ready for investor pitch

---

### Category 2: Digital Marketing & Content Strategy
**Purpose**: Build systematic, data-informed content and marketing strategies  
**Success Metric**: Content strategy is implementable and measurable

#### 2.1 Social Media Content Calendar
```
You are a content strategist with expertise in multi-platform social media management.

CONTEXT:
- Brand/Business: [name and 2-3 sentence description]
- Primary platforms: [Instagram, LinkedIn, TikTok, Twitter, YouTube, etc.]
- Content pillars: [main content themes, e.g., Education, Entertainment, Community]
- Posting frequency: [daily, 3x weekly, weekly per platform]
- Current audience size: [estimate or actual]
- Campaign goals: [awareness, engagement, conversion, community building]
- Content calendar duration: [30-day, 90-day, quarterly]

REQUEST:
Generate a detailed content calendar that includes:

1. **Content Pillar Distribution** (% allocation per pillar per platform)
2. **Posting Schedule** (optimal times, frequency, format mix)
3. **Content Ideas** (20+ specific post ideas with descriptions)
4. **Content Formats** (video, carousel, Reel, long-form, Stories, etc.)
5. **Engagement Strategy** (how to respond, community management guidelines)
6. **Analytics Framework** (key metrics to track per platform)
7. **Hashtag Strategy** (20-30 relevant hashtags with usage guidelines)
8. **Collaboration Opportunities** (guest posts, cross-promotions)

FORMAT REQUIREMENT:
- Create a week-by-week breakdown in table format
- Include post copy suggestions (80-120 characters max)
- Specify visual/content type for each post
- Identify "pillar post" (main content) vs. "filler" content

MEASURABILITY:
Define success for this calendar:
- Engagement rate target: X%
- Follower growth target: X/month
- Conversion metric: [specific KPI]
- Content resonance: Track which topics get 50%+ engagement above baseline

CONSTRAINTS:
- Posts must align with brand voice and values
- Content must be original or properly attributed
- Should include 15-20% educational content minimum
```

**Expected Outcome**: Ready-to-execute calendar with clear execution framework

---

#### 2.2 Blog Content Strategy & SEO Framework
```
You are an SEO strategist and content marketer specializing in organic traffic growth.

CONTEXT:
- Blog topic/niche: [e.g., "SaaS product management," "sustainable living"]
- Target audience: [specific professional or consumer segment]
- Current traffic: [if existing blog: monthly unique visitors]
- SEO maturity: [new domain/established/growing]
- Content production capacity: [posts per week you can realistically produce]
- Business goal: [lead generation, brand authority, product adoption, etc.]
- Monetization model: [ads, affiliate, product sales, subscriptions, etc.]

REQUEST:
Develop a comprehensive blog content strategy:

1. **Keyword Research & Clustering**
   - Target keyword (primary, 50-100 monthly searches minimum)
   - Long-tail keywords (7-15 keywords, 10-30 monthly searches)
   - Content pillars (3-5 main themes with 4-6 subtopics each)
   - Keyword difficulty assessment

2. **Content Roadmap** (First 6 months)
   - Phase 1 (Weeks 1-8): Foundation content (SEO basics, authority building)
   - Phase 2 (Weeks 9-16): Monetization content (conversion-focused)
   - Phase 3 (Weeks 17-26): Scale content (deep dives, advanced topics)

3. **Article Templates**
   - Blog post template (structure, word count, format)
   - Required sections (intro, body, CTA, internal links)
   - Keyword integration guidelines

4. **Link Building Strategy**
   - Internal linking map (how to link posts together)
   - External link opportunities (30+ potential sources)
   - Guest post pitches (5 sample pitch templates)

5. **Measurement Framework**
   - Primary metrics: Organic traffic, lead volume, conversion rate
   - Secondary metrics: Engagement, avg. time on page, bounce rate
   - Success benchmarks for 3-month, 6-month, 12-month milestones

6. **Traffic Growth Projections**
   - Month 1-3: X organic sessions (realistic baseline)
   - Month 4-6: X organic sessions (growth phase)
   - Month 12: X organic sessions (maturation)

OUTPUT STRUCTURE:
- Priority-ranked keyword list (with search volume, difficulty, priority)
- Content calendar (12-month view with post sequence)
- Competitive analysis (top 3 ranking pages for primary keyword)
- Content brief template (ready to hand to writers)

CONSTRAINTS:
- Avoid keyword stuffing; prioritize readability
- All claims must be sourced or properly qualified
- Posts should be 1,500-3,000 words minimum for SEO optimization
- Include freshness updates schedule (quarterly reviews)
```

**Deliverable Readiness**: Strategy document ready for content team execution

---

### Category 3: Education & Professional Development
**Purpose**: Create structured learning and skill development frameworks  
**Success Metric**: Roadmap is time-bound, measurable, and outcome-focused

#### 3.1 Personalized Study/Learning Plan
```
You are an educational strategist and learning design expert.

CONTEXT:
- Learning objective: [specific exam, certification, skill, or subject]
- Current knowledge level: [completely new/some experience/intermediate]
- Time available per week: [X hours/week for learning]
- Target completion date: [specific date or timeframe]
- Learning style preference: [visual, kinesthetic, reading/writing, auditory, or mixed]
- Prior relevant experience: [describe relevant background]
- Constraints: [budget, language, technology access, etc.]

REQUEST:
Design a comprehensive learning plan including:

1. **Goal Definition & Decomposition**
   - Primary learning outcome (measurable, specific)
   - Sub-goals (3-5 intermediate milestones)
   - Prerequisite knowledge assessment
   - Expected time investment (hours total)

2. **Curriculum Structure**
   - Week-by-week learning modules (12-week minimum structure)
   - Topics/units per week with estimated hours
   - Key concepts and competencies
   - Practical application opportunities per module

3. **Resource Selection**
   - Primary learning resources (courses, books, videos)
   - Supplementary resources (communities, mentors, forums)
   - Practice materials and assessment tools
   - Real-world project/application ideas

4. **Assessment & Progress Tracking**
   - Weekly self-assessment questions
   - Mid-point checkpoint (week 6): proficiency test
   - Final assessment: What does "completion" look like?
   - Scoring rubric or success criteria

5. **Habit & Accountability System**
   - Optimal study schedule (specific days/times)
   - Accountability mechanisms (study group, mentor, tracking tool)
   - Motivation maintenance strategies
   - Common obstacles and mitigation strategies

6. **Retention & Application Strategy**
   - Spaced repetition schedule (review intervals)
   - Active recall exercises (not passive re-reading)
   - Real-world application projects
   - Teaching others as retention mechanism

OUTPUT FORMAT:
- Detailed week-by-week calendar (in table format)
- Resource matrix (what, where, cost, time commitment)
- Daily/weekly schedule template with time blocking
- Progress tracking checklist

SUCCESS DEFINITION:
- Completion metrics: X certification/exam score, or demonstrable skill
- Proficiency benchmark: [specific rubric]
- Timeline: Target completion date with milestones every 2-3 weeks

CONSTRAINTS:
- Plan must be realistic for stated time commitment
- Include buffer weeks for difficult concepts
- Resources must be verifiable and accessible
- Should include at least one practical project
```

**Use Case**: Career development, certification prep, skill acquisition  
**Expected Outcome**: Day-one actionable learning schedule

---

#### 3.2 Workshop/Course Curriculum Design
```
You are an instructional design expert and subject matter specialist.

CONTEXT:
- Topic: [specific domain/skill to teach]
- Audience: [skill level, background, learning goals]
- Format: [in-person, hybrid, online, self-paced]
- Duration: [total hours, session length, number of sessions]
- Expected participants: [number, diversity of experience]
- Learning outcomes priority: [knowledge, skills, certification, or mixed]

REQUEST:
Design a complete workshop curriculum:

1. **Learning Objectives** (SMART format)
   - By end of workshop, participants will be able to: [3-5 measurable outcomes]
   - Knowledge level: [Bloom's taxonomy level: remember, understand, apply, analyze, evaluate, create]

2. **Curriculum Map**
   - Module breakdown (# of modules, duration each)
   - Topic sequence and dependencies
   - Key concepts per module
   - Real-world application for each module

3. **Session-by-Session Breakdown**
   - Session number, duration, and topic
   - Learning objectives for each session
   - Content outline (15-20 minute segments)
   - Interactive activities/exercises
   - Assessment method (quiz, project, group discussion)

4. **Materials & Resources**
   - Presentation slides outline
   - Handout/reference materials needed
   - Tool requirements (software, equipment)
   - Pre-work for participants (if applicable)

5. **Engagement & Interactivity**
   - Mix of lecture, discussion, hands-on, and group work
   - Questions to facilitate thinking
   - Case studies or real-world examples (minimum 3)
   - Guest expert input (if relevant)

6. **Assessment Strategy**
   - Pre-assessment (gauge starting knowledge)
   - Formative assessments (during workshop)
   - Summative assessment (demonstrate learning)
   - Post-workshop evaluation and feedback mechanism

7. **Instructor Guide**
   - Common questions and answers
   - Timing guidelines per section
   - Facilitation tips (especially for interactive sections)
   - Troubleshooting guide

OUTPUT DELIVERABLES:
- Curriculum outline (with time allocations)
- Module templates (ready for expansion)
- Sample session plan (one detailed example)
- Assessment rubric
- Participant workbook outline

CONSTRAINTS:
- Must fit within stated duration
- Include breaks (especially for sessions >2 hours)
- Content must be verifiable and current
- Activities must be feasible with stated participant count
- Accessibility considerations for diverse learners
```

**Validation**: Can a trained facilitator teach this curriculum independently?

---

### Category 4: Personal & Professional Growth
**Purpose**: Create systematic personal development and brand-building strategies  
**Success Metric**: Strategy is implementable with clear KPIs

#### 4.1 Personal Branding Strategy
```
You are a personal branding strategist and professional development consultant.

CONTEXT:
- Current role/title: [your professional position]
- Career goal: [5-year vision]
- Unique strengths/differentiators: [3-5 key strengths]
- Current online presence: [LinkedIn, blog, social media, GitHub, portfolio, etc.]
- Target audience: [who should know about you? employers, clients, community, etc.]
- Current visibility/network size: [estimate or actual]
- Industry/field: [specific industry]

REQUEST:
Develop a comprehensive personal branding strategy:

1. **Brand Positioning**
   - Your personal brand statement (1-2 sentences)
   - Key positioning: [specialist vs. generalist, technical vs. business, etc.]
   - Unique value proposition (what you offer that others don't)
   - Competitive differentiation (vs. peers in your field)

2. **Brand Messaging Framework**
   - Core message (what you want known for)
   - Supporting messages (3-5 secondary themes)
   - Elevator pitch (30 seconds, authentic)
   - Extended biography (100 words)
   - Social media bio templates (per platform)

3. **Online Presence Audit & Strategy**
   - Current platform assessment (LinkedIn, Twitter, GitHub, blog, portfolio)
   - Platform prioritization (which matter most for your goals?)
   - Content themes and pillars
   - Posting strategy per platform
   - Profile optimization recommendations

4. **Content & Visibility Plan**
   - What to publish/share (thought leadership, tutorials, insights)
   - Content calendar (3-month plan, 1-2 posts per week minimum)
   - Speaking/conference opportunities
   - Professional community engagement
   - Networking and relationship building strategy

5. **Portfolio/Showcase Development**
   - Portfolio platform recommendation (website, GitHub, Medium, etc.)
   - Case studies to develop (3-5 key projects)
   - Skills demonstration strategy
   - Social proof collection (testimonials, recommendations)

6. **Measurement Framework**
   - Visibility metrics: LinkedIn profile views, social reach, website traffic
   - Engagement metrics: Interaction rate, comment quality, message inbound
   - Opportunity metrics: Interview requests, partnership offers, speaking invitations
   - 6-month and 12-month benchmarks

7. **90-Day Action Plan**
   - Weeks 1-2: Profile optimization and messaging finalization
   - Weeks 3-6: Content launch and network engagement
   - Weeks 7-12: Performance tracking and strategy adjustment
   - Monthly review checklist

OUTPUT:
- Personal brand statement and value proposition
- Messaging guide (for different contexts)
- Platform-specific optimization checklist
- 90-day action plan (week-by-week tasks)
- KPI dashboard template

CONSTRAINTS:
- Authenticity is non-negotiable (all claims must be truthful)
- Must be sustainable (realistic for time commitment)
- Should differentiate you from others in your field
- All online presence should be professionally appropriate
- Strategy should align with long-term career goals
```

**Success Factor**: Internal consistency across all platforms

---

#### 4.2 Skill-Building Roadmap
```
You are a career development strategist and technical skill assessment expert.

CONTEXT:
- Current skill level: [beginner/intermediate/advanced]
- Target skill/role: [specific skill or role to develop toward]
- Time horizon: [6 months / 1 year / 18 months]
- Weekly time investment: [X hours available per week]
- Learning preference: [hands-on projects, courses, mentorship, etc.]
- Constraints: [budget, access, language, etc.]
- Career goal this supports: [why this skill matters to you]

REQUEST:
Create a comprehensive skill-building roadmap:

1. **Skill Gap Analysis**
   - Current competency level (1-10 per sub-skill)
   - Target competency level per sub-skill
   - Prerequisite skills (must learn first)
   - Related skills (good to learn alongside)
   - Time to competency estimate (per sub-skill)

2. **Learning Path (Phased Approach)**
   - Foundation phase: [weeks X-Y: core concepts and prerequisites]
   - Building phase: [weeks X-Y: deeper skill development]
   - Application phase: [weeks X-Y: real-world projects]
   - Mastery phase: [weeks X-Y: refinement and specialization]

3. **Resource Recommendations**
   - Structured courses (with cost, duration, instructor)
   - Books/documentation (with reading time estimates)
   - Practice platforms (Leetcode, Kaggle, GitHub, etc.)
   - Communities (forums, Discord, study groups)
   - Mentorship/coaching opportunities
   - Project ideas for hands-on learning

4. **Practice & Application Strategy**
   - Deliberate practice exercises (with difficulty progression)
   - Project ideas (3-5 capstone projects, increasing complexity)
   - Real-world application opportunities
   - Public demonstration of skills (GitHub, portfolio, etc.)

5. **Accountability & Progress Tracking**
   - Monthly milestones (what should be completed each month?)
   - Assessment checkpoints (week 4, 8, 12, etc.)
   - Proficiency benchmarks (how to know you're progressing?)
   - Red flags/trouble spots to watch for

6. **Continuous Improvement Loop**
   - Quarterly skill reassessment
   - Plan adjustments based on progress
   - Feedback mechanisms (code reviews, mentors, etc.)
   - Long-term maintenance plan (skill keeps evolving)

OUTPUT STRUCTURE:
- Skill breakdown (sub-skills with current/target proficiency)
- Phase-by-phase timeline (with duration and focus)
- Resource matrix (organized by phase with links)
- Project progression (easy → medium → difficult)
- Monthly checklist template

SUCCESS METRICS:
- Technical assessment: [specific benchmark to pass]
- Project completion: [capstone project demonstrates skill]
- Time to competency: [realistic timeline based on inputs]
- Sustainability: [plan should last 6-18 months, not burn you out]

CONSTRAINTS:
- Must respect stated time commitment (no 60-hour weeks)
- Balance theory with hands-on projects (50/50 minimum)
- Include regular breaks to avoid burnout
- Resources should be free or low-cost (unless indicated)
```

**Validation Check**: Can someone follow this plan without a mentor and still succeed?

---

### Category 5: Wellness & Productivity
**Purpose**: Design sustainable personal systems for health and productivity  
**Success Metric**: Routine is sustainable, measurable, and personalized

#### 5.1 Wellness Routine for Productivity Optimization
```
You are a wellness coach, productivity expert, and behavioral change specialist.

CONTEXT:
- Current lifestyle: [sedentary, moderately active, etc.]
- Pain points: [lack of energy, poor sleep, distraction, stress, etc.]
- Wellness goals: [physical health, mental clarity, energy, stress reduction]
- Work schedule: [9-5, flexible, shift work, etc.]
- Family/life commitments: [dependent care, family obligations, etc.]
- Health constraints: [injuries, disabilities, health conditions]
- Resources available: [budget, gym access, space, etc.]
- Preferred activity types: [examples of things you enjoy]

REQUEST:
Design a personalized wellness routine addressing:

1. **Sleep Optimization** (foundation)
   - Sleep schedule recommendation (bedtime, wake time)
   - Sleep hygiene practices (environment, habits, wind-down)
   - Estimated sleep quality improvement timeline
   - Troubleshooting strategies (for known sleep issues)

2. **Physical Activity Strategy**
   - Recommended activities (based on preferences and constraints)
   - Weekly schedule (duration, frequency, type)
   - Progression plan (weeks 1-12)
   - Home-based alternatives (if needed)
   - Performance metrics to track

3. **Nutrition & Hydration Plan**
   - Daily water intake target and reminders
   - Meal timing strategy (especially around work)
   - Pre/post-workout nutrition (if applicable)
   - Quick healthy snack ideas
   - Energy management through food

4. **Stress Management & Mental Health**
   - Daily stress reduction practices (5-10 min minimum)
   - Weekly deeper wellness practices (meditation, journaling, etc.)
   - Breathing techniques for acute stress
   - Environmental changes for mental clarity
   - Resources for ongoing support

5. **Daily Routine Structure**
   - Morning routine (30-60 min, energy-building)
   - Work blocks with movement breaks
   - Midday reset practice (10-15 min)
   - Evening wind-down routine (30 min)
   - Weekend recovery practices

6. **Productivity Integration**
   - Energy management across day (peak hours for important work)
   - Breaks schedule (frequency and type)
   - Focus time protection strategies
   - Recovery time built in (avoid burnout)
   - Energy tracking method

7. **Habit Formation & Accountability**
   - Habit stacking (attach new habits to existing ones)
   - Weekly check-in process
   - Difficulty levels (start easy, progress gradually)
   - Relapse protocol (what to do when routine breaks)
   - Support system (accountability partner, app, etc.)

OUTPUT DELIVERABLES:
- Daily routine template (with time blocks)
- Weekly activity schedule
- Habit tracker template
- 12-week progression plan
- Emergency/travel adjustment guidelines

SUCCESS DEFINITION:
- Measurable outcomes: [sleep quality improvement, energy level, productivity metrics]
- Sustainability: Plan must last 12+ months
- Baseline vs. 12-week targets: [specific improvements expected]

CONSTRAINTS:
- Routine must fit within stated time/resource constraints
- Should be sustainable indefinitely (not a "quick fix")
- Start small; add gradually (avoid overwhelm)
- Account for weekends and flexibility (not rigid)
- Should improve rather than decrease social/family time
```

**Realistic Expectation**: 2-3 week adjustment period, real benefits by week 6-8

---

#### 5.2 Self-Care Routine for Stress Management
```
You are a mental health wellness specialist and stress management expert.

CONTEXT:
- Primary stress sources: [work, relationships, finances, health, etc.]
- Current stress level: [1-10 scale]
- Available time per day: [X minutes for self-care]
- Physical space available: [bedroom, office, outdoor, etc.]
- Budget: [free, $X/month]
- Previous self-care: [what has worked/not worked before]
- Preferred self-care modalities: [physical, creative, social, solitude, nature, etc.]
- Barriers to self-care: [time, guilt, perfectionism, energy, etc.]

REQUEST:
Develop a personalized, sustainable self-care routine:

1. **Self-Care Assessment & Needs Analysis**
   - Stress triggers (specific situations, people, times)
   - Physical symptoms of stress (tension, sleep, digestion, etc.)
   - Emotional/mental stress signals (irritability, anxiety, numbness, etc.)
   - Current coping mechanisms (healthy and unhealthy)
   - Self-care gaps (what's missing from current approach)

2. **Multi-Pillar Self-Care Plan**
   - **Physical self-care**: Movement, rest, nutrition, medical care
   - **Emotional self-care**: Expression, processing, connection, creativity
   - **Mental self-care**: Learning, mindfulness, boundaries, perspective
   - **Social self-care**: Connection, community, intimacy, support
   - **Spiritual self-care**: Meaning, purpose, values, practices

3. **Tiered Self-Care Routine** (based on time available)
   - **Daily minimum** (10-15 min): Non-negotiable stress relief
   - **Standard routine** (30-45 min): Regular wellness practice
   - **Deep self-care** (60-90+ min): Weekly restoration
   - **Emergency protocol** (5-10 min): Crisis stress relief

4. **Specific Practices & Techniques**
   - Guided options for each self-care pillar
   - Instructions/resources for each practice
   - Substitutions if one approach isn't working
   - Progression (start simple, add complexity)

5. **Boundary & Recovery Strategy**
   - Time blocking (protect self-care time)
   - Boundary scripts (saying no, protecting time)
   - Energy management (rest days, activity balance)
   - Preventing self-care collapse

6. **Progress Tracking & Adjustment**
   - Stress level tracking method
   - What to measure (sleep, mood, productivity, etc.)
   - Monthly review questions
   - When/how to adjust routine
   - Seasonal variations (adjust as needed)

7. **Support & Professional Resources**
   - When to seek professional help (therapist, counselor, doctor)
   - Crisis resources (hotlines, emergency contacts)
   - Supportive communities
   - Books, apps, or resources for deeper work

OUTPUT:
- Daily self-care checklist (realistic options)
- Weekly routine template (with timing)
- Stress response toolkit (what to do when stressed)
- Boundary protection strategies
- Progress tracking template
- Resource list (apps, books, communities)

BASELINE METRICS:
- Current stress level: [1-10]
- Target stress level: [1-10] at 30 days
- Sleep quality, mood, energy tracking
- Success definition (what does "better" look like?)

CONSTRAINTS:
- Must be sustainable long-term
- Should not add more stress/guilt
- Practices must be genuinely enjoyable (not punishment)
- Should enhance life quality, not feel like an obligation
- Account for bad days/setbacks
```

**Key Principle**: Self-care is not selfish; it's essential maintenance

---

### Category 6: Planning & Strategy
**Purpose**: Create structured plans for events, timelines, and executions  
**Success Metric**: Plan is detailed, realistic, and executable

#### 6.1 Project Planning Framework
```
You are a project management expert and strategic planner.

CONTEXT:
- Project type: [business, personal, creative, etc.]
- Scope: [description of what's being done]
- Timeline: [target completion date]
- Resources: [budget, team size, skills available]
- Constraints: [technical, regulatory, resource, timeline, etc.]
- Success definition: [what does "done" look like?]
- Stakeholders: [who needs to be involved/informed]

REQUEST:
Develop a comprehensive project plan:

1. **Project Charter**
   - Project statement (1-2 sentences, clear purpose)
   - SMART objectives (specific, measurable, achievable, relevant, time-bound)
   - Success criteria (how to know project succeeded)
   - Key constraints (time, budget, technical, scope)
   - Risk tolerance (what's acceptable?)

2. **Scope Definition**
   - What's included (clear boundaries)
   - What's NOT included (scope exclusions)
   - Deliverables (tangible outputs)
   - Key milestones

3. **Work Breakdown Structure (WBS)**
   - Major phases
   - Work packages per phase
   - Dependencies (what must happen before X?)
   - Estimated effort per work package

4. **Timeline & Schedule**
   - Critical path (sequence of dependent tasks)
   - Gantt chart or timeline (with dependencies)
   - Key milestones and gates
   - Buffer/contingency time built in
   - Resource allocation over time

5. **Resource Planning**
   - Team/roles needed
   - Skill requirements
   - Tool/technology needs
   - Budget breakdown
   - External dependencies

6. **Risk Management**
   - Top 5-10 identified risks
   - Impact and probability assessment
   - Mitigation strategies
   - Contingency plans
   - Risk owner assignments

7. **Communication Plan**
   - Stakeholder communication schedule
   - Status reporting mechanism
   - Escalation path (if issues arise)
   - Documentation/knowledge management

8. **Quality Assurance**
   - Quality standards for deliverables
   - Testing/validation approach
   - Review/approval process
   - Acceptance criteria per deliverable

9. **Lessons Learned Process**
   - Post-project retrospective
   - What worked, what didn't
   - Improvements for future projects

OUTPUT:
- Executive summary (1-page overview)
- Detailed project plan (20-30 pages or equivalent)
- Timeline/Gantt chart
- Risk register
- RACI matrix (responsible, accountable, consulted, informed)

MEASURABLE OUTCOMES:
- On-time delivery: [date]
- On-budget delivery: [budget]
- Quality metrics: [specific standards]
- Team satisfaction/learning: [how to measure]

CONSTRAINTS:
- Plan must respect stated constraints
- Must include realistic contingency (15-25% buffer)
- Should be reviewable and approachable by non-specialists
- Must identify all critical dependencies
- Regular updates/adjustments required
```

---

#### 6.2 Event Planning & Execution Strategy
```
You are an event strategist and project coordinator.

CONTEXT:
- Event type: [conference, workshop, celebration, launch, etc.]
- Date: [specific date]
- Location: [physical, virtual, hybrid]
- Expected attendance: [number of attendees]
- Budget: [$X total]
- Purpose: [what should attendees experience/learn/feel?]
- Key outcomes: [measurable goals for the event]

REQUEST:
Develop a complete event plan:

1. **Event Vision & Objectives**
   - Event statement (what is this event?)
   - Key outcomes for attendees
   - Success metrics (how to measure success)
   - Brand/tone (the experience you want to create)

2. **Attendee & Stakeholder Analysis**
   - Primary attendee personas
   - Decision-makers to influence
   - VIP/important attendees
   - Communication timeline per segment

3. **Event Program Structure**
   - Overall timeline (start-finish)
   - Session breakdown (if multi-session)
   - Key moments/highlights
   - Speaker/presenter sequence
   - Break points and logistics

4. **Logistics & Operations**
   - Venue requirements and setup
   - Technology/equipment needed
   - Catering/refreshments plan
   - Registration process
   - Signage and wayfinding
   - Parking/transportation (if applicable)

5. **Marketing & Promotion Strategy**
   - Pre-event promotion timeline (8-12 weeks before)
   - Promotional channels (email, social, PR, partnerships)
   - Messaging and positioning
   - Registration incentives/mechanisms
   - Target reach/attendance rate

6. **Experience Design** (what makes it memorable?)
   - Arrival experience
   - Key moments throughout event
   - Networking opportunities
   - Interactive elements
   - Closing/takeaway

7. **Risk & Contingency Planning**
   - Top risks (weather, no-shows, technical, etc.)
   - Backup plans (weather, for key elements)
   - Communication plan if issues arise

8. **Post-Event Strategy**
   - Attendee follow-up (timeline and messaging)
   - Feedback collection method
   - Content repurposing (recordings, articles, etc.)
   - Relationship maintenance next steps

9. **Detailed Execution Checklist**
   - 12 weeks before: Strategy, budget approval, save-the-date
   - 8 weeks before: Marketing launch, speaker confirmation
   - 4 weeks before: Registration tracking, logistics finalization
   - 2 weeks before: Final confirmations, contingency prep
   - 1 week before: Setup planning, final communications
   - Event week: Daily checklist, day-of checklist
   - Post-event: Thank you, feedback, analysis

OUTPUT:
- Event plan document (10-15 pages)
- Timeline/Gantt chart
- Budget breakdown
- Risk register with contingencies
- Day-of execution checklist
- Template for attendee communications

MEASURABLE SUCCESS:
- Attendance rate: [X% of registrations attend]
- Attendee satisfaction: [X/5 stars]
- Engagement metrics: [specific participation targets]
- Post-event conversion: [if applicable]

CONSTRAINTS:
- Must stay within budget
- Realistic timeline for team size
- Contingencies for likely problems
- Builds in setup/breakdown time
- Post-event follow-up planned
```

---

## 🔧 Advanced Features & Customization

### Extending the Framework

To add new prompt templates:

1. **Identify the domain** (where does this fit in the framework?)
2. **Follow the architecture pattern** (Role → Context → Request → Constraints → Output → Evaluation)
3. **Include measurable success criteria**
4. **Add sample outputs or examples**
5. **Document prerequisites and dependencies**

### Combining Prompts

Many use cases require **prompt chaining**:

```
Example: Starting a startup
├─ Prompt 2.1 (Business Concept Development)
├─ Prompt 2.2 (Blog Content Strategy - for marketing)
├─ Prompt 4.1 (Personal Branding - for founder visibility)
├─ Prompt 6.1 (Project Planning - for execution)
└─ Prompt 5.1 (Wellness Routine - for sustainable work)
```

---

## 📊 Evaluation Framework: How to Assess Response Quality

After using any prompt, evaluate the AI response on these criteria:

| Criterion | Excellent (4) | Good (3) | Fair (2) | Poor (1) |
|-----------|---|---|---|---|
| **Specificity** | Highly customized to your inputs | Generally relevant | Generic, some relevance | Ignores your context |
| **Actionability** | Can execute immediately | Mostly executable | Needs significant work | Not actionable |
| **Completeness** | All requested elements included | Most elements present | Partial information | Missing key components |
| **Feasibility** | Realistic for stated constraints | Mostly feasible | Some unrealistic aspects | Ignores constraints |
| **Structure** | Clear, organized, well-formatted | Good organization | Somewhat disorganized | Poorly structured |
| **Depth** | Thorough, detailed analysis | Adequate depth | Surface-level | Superficial |

**Scoring**: 20-24 = Excellent | 16-19 = Good | 12-15 = Fair | <12 = Revise and retry

---

## 🎓 Best Practices for Prompt Engineering

### Before Using a Prompt:

1. **Prepare your context**: Have specific, accurate information ready
2. **Be honest about constraints**: Budget, time, skills, resources
3. **Define success**: What does "good" output look like for you?
4. **Research frameworks**: Understand the domain (don't just rely on AI)

### While Using a Prompt:

1. **Fill in ALL variables**: Partial information = partial results
2. **Use exact numbers** (not "small amount," use "$500" or "3 hours")
3. **Specify format**: Do you want tables, lists, paragraphs, diagrams?
4. **Ask for reasoning**: Request explanations for key recommendations

### After Receiving Output:

1. **Evaluate against criteria**: Use the evaluation framework above
2. **Iterate**: Ask follow-up questions to refine results
3. **Validate assumptions**: Check recommendations against your research
4. **Adapt, don't adopt**: Customize the output to your specific situation
5. **Document changes**: Track why you modified recommendations

### Common Pitfalls to Avoid:

❌ **Vague context**: "I want to start a business" (too generic)  
✅ **Specific context**: "I want to start a B2B SaaS for expense management targeting finance teams at mid-size startups"

❌ **Ignoring constraints**: Not mentioning you have $1,000 budget  
✅ **Clear constraints**: "Budget: $1,000, Timeline: 3 months, Solo founder"

❌ **Passive consumption**: Taking AI output as gospel  
✅ **Active evaluation**: Fact-checking claims, validating recommendations

❌ **One-shot prompts**: Ask once, never follow up  
✅ **Iterative refinement**: Ask 3-5 follow-up questions to deepen output

---

## 📖 Resources & References

### AI Model Considerations:

- **GPT-4**: Best for complex reasoning, nuanced strategy
- **Claude**: Excellent for detailed analysis and synthesis
- **Specialized models**: Domain-specific models may outperform general ones

### Complementary Tools:

- **Roadmaps**: [Roadmap.sh](https://roadmap.sh), [Product Hunt](https://producthunt.com)
- **Project Management**: Asana, Monday.com, Notion
- **Learning**: Coursera, Udemy, LinkedIn Learning
- **Analytics**: Google Analytics, Mixpanel, Amplitude

---

## 📝 Document Changelog

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2024-Q1 | Initial prompt collection | upskill-rj |
| 2.0 | 2026-05-09 | Framework redesign, enterprise standards, evaluation criteria | upskill-rj |

---

## 📄 License & Usage

This prompt framework is **open source and freely available** for personal and professional use. 

**Attribution requested but not required**: If you share this, a link to this repository is appreciated.

**Contributing**: Issues, improvements, and new prompts are welcome. Submit via GitHub issues or pull requests.

---

## 🤝 Getting Help

- **Questions about framework**: Create a GitHub issue
- **Prompt improvements**: Submit pull requests or discussions
- **Domain-specific additions**: Describe the need; collaborate on solution

---

**Last Updated**: 2026-05-09 | **Framework Version**: 2.0 | **Status**: Production Ready
