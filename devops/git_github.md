### 🔹 What is Git?

**Git** is a **version control system**—a tool that helps developers track changes in code over time.

Think of it like a **time machine + collaboration tool** for your code.

#### Key features:

* Tracks every change (who changed what & when)
* Lets you go back to previous versions
* Supports branching (work on features without breaking main code)
* Works locally on your machine (offline)

#### Example:

You write code today → tomorrow you break something → Git lets you **restore yesterday’s working version** easily.

---

### 🔹 What is GitHub?

GitHub is a **cloud-based platform** that hosts Git repositories online.

It uses Git but adds collaboration features.

#### Key features:

* Store your code online (remote repository)
* Collaborate with teams
* Code review (Pull Requests)
* Issue tracking
* CI/CD integrations

---

### 🔹 Git vs GitHub (Simple Difference)

| Feature         | Git             | GitHub                       |
| --------------- | --------------- | ---------------------------- |
| Type            | Tool (software) | Platform (service)           |
| Runs on         | Local machine   | Cloud / Web                  |
| Purpose         | Version control | Code hosting & collaboration |
| Internet needed | ❌ No            | ✅ Yes                        |

---

### 🔹 Real-life Analogy

* **Git** = Microsoft Word’s “Track Changes” (but much more powerful)
* **GitHub** = Google Drive where you store & share documents with others

---

### 🔹 How they work together

1. You write code on your laptop
2. Use **Git** to track changes
3. Push code to **GitHub**
4. Team members pull and collaborate

---

### 🔹 Basic Workflow

```bash
git init              # Initialize repo
git add .             # Stage changes
git commit -m "msg"   # Save version
git push              # Upload to GitHub
```

---

Here’s a **clear, practical step-by-step guide** to configure Git with **Visual Studio Code** on your system 👇

---

# 🔧 Step 1: Install Git

Download and install Git from
👉 Git official website

During installation:

* Keep default settings (recommended)
* Ensure **“Git from command line”** is selected

---

# 🔧 Step 2: Verify Git Installation

Open terminal in VS Code (`Ctrl + ~`) or Command Prompt:

```bash
git --version
```

If installed correctly, you’ll see something like:

```
git version 2.x.x
```

---

# 🔧 Step 3: Configure Username & Email (IMPORTANT ⚠️)

This fixes the error you saw earlier.

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Example:

```bash
git config --global user.name "Rahul Jha"
git config --global user.email "rahul@email.com"
```

Check config:

```bash
git config --list
```

---

# 🔧 Step 4: Open Project in VS Code

1. Open VS Code
2. Click **File → Open Folder**
3. Select your project folder

---

# 🔧 Step 5: Initialize Git Repository

In VS Code terminal:

```bash
git init
```

Or:

* Click **Source Control (left sidebar)**
* Click **"Initialize Repository"**

---

# 🔧 Step 6: Connect VS Code with GitHub

Sign in to GitHub:

1. Press `Ctrl + Shift + P`
2. Type: `GitHub: Sign in`
3. Follow browser authentication

---

# 🔧 Step 7: Install Recommended Extensions (Optional but Useful)

* GitHub Pull Requests
* GitLens (very helpful for history)

Search in Extensions tab:

* **GitLens**

---

# 🔧 Step 8: First Commit from VS Code

1. Go to **Source Control panel**
2. Click `+` to stage files
3. Enter commit message
4. Click ✔️ to commit

Or via terminal:

```bash
git add .
git commit -m "Initial commit"
```

---

# 🔧 Step 9: Create Repository on GitHub

1. Go to GitHub website
2. Click **New Repository**
3. Copy repo URL

---

# 🔧 Step 10: Link Local Repo to GitHub

```bash
git remote add origin https://github.com/username/repo.git
git branch -M main
git push -u origin main
```

---

# 🔥 Common Errors & Fixes

### ❌ Error: user.name / user.email not set

✔ Fix: Run Step 3

---

### ❌ Authentication failed

✔ Fix:

* Use **Personal Access Token (PAT)** instead of password
* Or login via VS Code GitHub sign-in

---

### ❌ Git not recognized

✔ Fix:

* Restart system
* Reinstall Git with PATH enabled

---


