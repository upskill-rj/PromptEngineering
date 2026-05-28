# ollama commands
========================

OpenClaw - Personal AI with 100+ skills
ollama launch openclaw

Claude - Anthropic's coding tool with subagents
ollama launch claude

Codex - OpenAI's open-source coding agent
ollama launch codex

OpenCode - Anomaly's open-source coding agent
ollama launch opencode

Droid - Factory's coding agent across terminal and IDEs
ollama launch droid

Pi - Minimal AI agent toolkit with plugin support
ollama launch pi

ollama pull qwen2.5-coder:1.5b
ollama pull deepseek-r1:1.5b

name: Local Config
version: 1.0.0
schema: v1
models:
  - name: deepseek r1
    provider: ollama
    model: deepseek-r1:1.5b 
    roles:
      - chat
      - edit
      - apply
  - name: qwen 2.5 coder:1.5B
    provider: ollama
    model: qwen2.5-coder:1.5b
    roles:
      - autocomplete
  - name: Nomic Embed
    provider: ollama
    model: nomic-embed-text:latest
    roles:
      - embed



PS D:\Development> ollama ls
NAME                  ID              SIZE      MODIFIED
deepseek-r1:latest    6995872bfe4c    5.2 GB    9 minutes ago
deepseek-r1:1.5b      e0979632db5a    1.1 GB    5 hours ago
qwen2.5-coder:1.5b    d7372fd82851    986 MB    5 hours ago
PS D:\Development>

✓ OpenClaw is running

  Open the Web UI:
    http://localhost:18789/#token=c222d2420537a622d46dd2b96ae735f6289fca941151fdfd

  Quick start:
    /help             see all commands
    openclaw skills                         browse and install skills

  The OpenClaw gateway is running in the background.
  Stop it with: openclaw gateway stop
  
PS C:\WINDOWS\System32> ollama serve
Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.

PS C:\WINDOWS\System32> openclaw gateway stop 



🦞 OpenClaw 2026.4.9 (0512059) — Less clicking, more shipping, fewer "where did that file go" moments.

Stopped Windows login item: OpenClaw Gateway

PS C:\WINDOWS\System32> openclaw gateway autostart disable
error: too many arguments for 'gateway'. Expected 0 arguments but got 2.

PS C:\WINDOWS\System32> ollama serve
Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
PS C:\WINDOWS\System32> openclaw uninstall --all --yes

🦞 OpenClaw 2026.4.9 (0512059) — Alexa, but with taste.

Recommended first: openclaw backup create
Stopped Windows login item: OpenClaw Gateway
Removed Windows login item: C:\Users\Lenovo\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\OpenClaw Gateway.cmd
Removed task script: C:\Users\Lenovo\.openclaw\gateway.cmd
Removed ~\.openclaw
Removed ~\.openclaw\workspace
CLI still installed. Remove via npm/pnpm if desired.


PS C:\WINDOWS\system32> go install github.com/sammcj/gollama@latest
PS C:\WINDOWS\system32> gollama -L
Linking Ollama models to LM Studio (directory: C:\Users\Lenovo\.lmstudio\models)

Found 6 models to link:
1. phi4-mini:latest
2. qwen2.5-coder:7b
3. llama3.2:latest
4. deepseek-r1:latest
5. deepseek-r1:1.5b
6. qwen2.5-coder:1.5b

# Starting linking process...

Linking model: phi4-mini:latest... success!
Linking model: qwen2.5-coder:7b... success!
Linking model: llama3.2:latest... success!
Linking model: deepseek-r1:latest... success!
Linking model: deepseek-r1:1.5b... success!
Linking model: qwen2.5-coder:1.5b... success!


# Python Environments: Refresh All Environment Managers

ollama pull qwen2.5-coder:1.5b
ollama pull deepseek-r1:1.5b
ollama launch openclaw
ollama launch claude
ollama run qwen2.5-coder
ollama pull qwen2.5-coder:7b


# Best balance for coding on your spec
ollama pull qwen2.5-coder:7b
ollama pull qwen2.5-coder:3b     # Very fast, good enough for simple tasks
ollama pull qwen2.5-coder:14b(strong for coding)

# Or even lighter and faster
ollama pull phi4:mini
ollama pull gemma2:9b
ollama pull llama3.2



# Best one for your T14 (3B - 8B == fast + good quality on 16GB RAM)
ollama pull phi4-mini:latest
ollama pull qwen2.5-coder:3b     # Very fast, good enough for simple tasks
ollama pull gemma3:4b            # Newer and efficient
ollama pull qwen2.5-coder:7b
Qwen2.5 Coder 7B 
Deepseek R1 8B 



# Or the explicit 3.8B version
ollama pull phi4-mini:3.8b


Best LLM Models for YOUR Laptop (2026)
👉 Llama 3 (8B)
Best balance (chat + coding + reasoning)
Most stable + widely supported
ollama pull llama3

👉 Why:

Top all-rounder in 7–8B class
🥈 Best for Coding (VERY IMPORTANT for you 👨‍💻)
👉 DeepSeek Coder (6.7B)
ollama pull deepseek-coder

👉 Why:

Strong for:
Java
APIs
debugging
Better than general models for code tasks
🥉 Fast + Lightweight (Daily usage)
👉 Phi-3 Mini / Phi-4 Mini (~3–4B)
ollama pull phi3

👉 Why:

Runs fastest on CPU
Designed for low-resource laptops (~3.5GB RAM)
⚡ Best Speed Model
👉 Mistral (7B)
ollama pull mistral

👉 Why:

Faster generation vs Llama
Good for:
quick answers
iteration
🌍 Best Multilingual + Smart Reasoning
👉 Qwen 2.5 / Qwen 3 (7B)
ollama pull qwen2.5

👉 Why:

Strong in:
reasoning
structured output
coding


Install these 4 models:

ollama pull llama3
ollama pull mistral
ollama pull phi3
ollama pull deepseek-coder

👉 Covers everything:

Chat → llama3
Coding → deepseek
Fast → phi3
Balanced → mistral


D:\AI\OllamaModels

C:\Users\Lenovo\.ollama\models\blobs


mklink /J "C:\Users\<your-user>\.ollama\models" "D:\Ollama\models"


mklink /J "C:\Users\Lenovo\.ollama\models" "D:\AI\OllamaModels"


PS D:\AI\OllamaModels> ollama ls
NAME                  ID              SIZE      MODIFIED
llama3:latest         365c0bd3c000    4.7 GB    7 minutes ago
qwen2.5-coder:3b      f72c60cabf62    1.9 GB    14 minutes ago
qwen2.5-coder:1.5b    d7372fd82851    986 MB    3 hours ago
PS D:\AI\OllamaModels> ollama rm llama3:latest


# Install these 4 models:

ollama pull llama3
ollama pull mistral
ollama pull phi3
ollama pull deepseek-coder
ollama pull qwen2.5


PS C:\Users\Lenovo> ollama ls
NAME                     ID              SIZE      MODIFIED
qwen2.5-coder:3b         f72c60cabf62    1.9 GB    14 minutes ago === Working Fine
gemma4:latest            c6eb396dbd59    9.6 GB    30 minutes ago === Working Fine
deepseek-coder:latest    3ddd2d3fc8d2    776 MB    44 minutes ago === Working Fine
phi3:latest              4f2222927938    2.2 GB    46 minutes ago === Working Fine
mistral:latest           6577803aa9a0    4.4 GB    50 minutes ago === Working Fine
llama3:latest            365c0bd3c000    4.7 GB    53 minutes ago === Working Fine


PS C:\Users\Lenovo>

3.6

gemma4:latest 
mini-max 2.7
qwen2.5-coder:3b
opencode


# Build a classic Snake game in this repo.

Scope & constraints:
- Implement ONLY the classic Snake loop: grid movement, growing snake, food spawn, score, game-over, restart.
- Reuse existing project tooling/frameworks; do NOT add new dependencies unless truly required.
- Keep UI minimal and consistent with the repo’s existing styles (no new design systems, no extra animations).

# Implementation plan:

1) Inspect the repo to find the right place to add a small interactive game (existing pages/routes/components).
2) Implement game state (snake positions, direction, food, score, tick timer) with deterministic, testable logic.
3) Render: simple grid + snake + food; support keyboard controls (arrow keys/WASD) and on-screen controls if mobile is present in the repo.
4) Add basic tests for the core game logic (movement, collisions, growth, food placement) if the repo has a test runner.

# Deliverables:

- A small set of files/changes with clear names.
- Short run instructions (how to start dev server + where to navigate).
- A brief checklist of what to manually verify (controls, pause/restart, boundaries).

# 7 Types of AI Explained

* Reactive Machines: These are the most basic types of AI, designed to act only on current data and scenarios. They do not store memories or e past experiences to inform future actions. Example: IBM’s Deep Blue.

* Limited Memory AI: These systems can store past data for a short period to make decisions. Most modern AI, such as chatbots and self-driving rs, falls into this category.

Theory of Mind AI: A future, theoretical type of AI that aims to understand human emotions, beliefs, and thoughts to interact socially.
Self-Aware AI: A hypothetical stage where AI possesses its own consciousness, self-awareness, and emotions.
* Artificial Narrow Intelligence (ANI): Also known as "Weak AI," this type is designed and trained for a specific task, such as voice cognition, face recognition, or web searches.

* Artificial General Intelligence (AGI): Also known as "Strong AI," this is a theoretical AI that can understand, learn, and apply knowledge in manner similar to human intelligence across diverse tasks.

* Artificial Superintelligence (ASI): A hypothetical future AI that surpasses human intelligence in every field, including scientific eativity, general wisdom, and social skills.


* Vercel(Hosting)	-- 	Zero-config deployment with global edge network. Automatic HTTPS, preview deployments for staging, and serverless API utes eliminate the need for a separate backend server. steps to host simple html to Vercel

* Vercel AI -- Vercel AI is a comprehensive platform and open-source TypeScript SDK designed for developers to build, deploy, and manage AI-powered applications, particularly frontend chat and streaming interfaces. Key features include the AI SDK (for UI and model integration),  Gateway (managing API keys/rate limits across models), and Fluid Compute for specialized AI workloads. 

github - Repository

webhook -- A webhook is an HTTP-based, event-driven mechanism used to automatically send real-time data between applications

* Supabase -- Supabase is an open-source "Backend-as-a-Service" (BaaS) platform built on PostgreSQL that provides developers with a full backend stack, including a database, authentication, real-time APIs, file storage, and serverless edge functions. It acts as an open-source ternative to Firebase, designed to speed up development by eliminating the need to manage infrastructure.

* Edge functions - Edge functions are lightweight, server-side code snippets that execute on global Content Delivery Networks (CDNs) nearest to the user, rather than a centralized server. They enable low-latency, personalized web experiences by processing requests closer to the source. mmon use cases include authentication, A/B testing, and real-time data modification.

* N8N -- n8n is a powerful, low-code workflow automation tool used to connect applications, manipulate data, and automate repetitive tasks. It allows users to build complex, multi-step workflows using a visual node-based interface, supporting over 400 integrations (e.g., Slack, Google eets, Jira) and offering both self-hosted and cloud-based options.

* Amazon Bedrock -- Amazon Bedrock is a fully managed AWS service that provides a single API to access high-performing foundation models (FMs) from AI companies like Anthropic, Meta, Mistral, and Amazon. It is a serverless platform designed for building generative AI applications with curity, privacy, and customization capabilities (like fine-tuning and RAG), allowing developers to build without managing infrastructure.

* Hugging Face -- Hugging Face is a leading open-source AI community and platform often called the "GitHub of Machine Learning," designed for collaborating on AI models, datasets, and applications. It enables users to easily share, discover, and deploy state-of-the-art models for NLP, mputer vision, and audio, largely through its popular transformers library.

* Claude Cowork -- Claude Cowork is an agentic AI assistant from Anthropic designed to function as a digital coworker by operating directly on user’s desktop to automate multi-step tasks, such as managing files, organizing data, and interacting with applications.

* Claude Code -- Claude Code is an agentic AI coding tool developed by Anthropic that operates directly in the terminal to read, write, test, and debug code across projects. Unlike chatbot assistants, it acts as an autonomous agent, making Git commits and executing multi-step development tasks from simple English prompts. It is optimized for speed, autonomy, and deep codebase understanding, often referred to as a oding agent" or "AI pair programmer".

* Claude Cowork -- Claude Cowork is an agentic AI feature within the Anthropic Claude Desktop app designed to act as a digital teammate rather than just a chat interface. It works directly on a user’s local computer, reading, writing, and organizing files, managing projects, and nning multi-step tasks across apps, allowing users to delegate complex workflows entirely.

* Pomelli -- Pomelli by Google Labs is an experimental AI marketing tool designed to help businesses, particularly small ones, generate -brand content and marketing campaigns.

* Miro -- Miro AI is an AI-powered innovation workspace that integrates generative artificial intelligence directly into Miro's visual collaboration platform to accelerate workflows. It helps teams brainstorm, visualize complex ideas, summarize content, and automate tasks thin an infinite whiteboard.

* Roo Code -- Roo Code (formerly Roo Cline) is an open-source, autonomous AI coding agent designed as a VS Code extension. It acts as a digital partner that can read, write, refactor, and debug code across multiple files, running terminals and browser tasks to complete software development work. Key features include high customizability, permission-based actions, and support for various LLMs. 








		