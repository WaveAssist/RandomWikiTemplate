<h1 align="center">RandomWiki</h1>

<p align="center">
  <a href="https://waveassist.io/assistant/randomwiki-template">
    <img src="https://img.shields.io/badge/Deploy_with-WaveAssist-007F3B" alt="Deploy with WaveAssist" />
  </a>
  <img src="https://img.shields.io/badge/RandomWiki-Automated%20Wikipedia%20Summaries-blue" alt="RandomWiki Badge" />
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
</p>

---

## Overview

RandomWiki is an automation workflow for [WaveAssist](https://waveassist.io) that retrieves a random Wikipedia article summary and sends it by email. This process leverages the WaveAssist platform for node orchestration, scheduling, and variable management.

---

## One-Click Deploy on WaveAssist

<p>
  <a href="https://waveassist.io/assistant/randomwiki-template" target="_blank">
    <img src="https://waveassistapps.s3.us-east-1.amazonaws.com/public/Button.png" alt="Deploy on WaveAssist" width="230" />
  </a>
</p>

Deploy RandomWiki instantly on [WaveAssist](https://waveassist.io)—the zero-infrastructure automation platform that handles orchestration and scheduling for you.

> 🔐 You may need to log in or create a free WaveAssist account before continuing.


#### How to Use

1. Click the button above or visit [waveassist.io/assistant/randomwiki-template](https://waveassist.io/assistant/randomwiki-template)
2. No required variables to configure.
3. Run the starting node: **wikipedia_random_summary**  
   *(Collects a random summary from Wikipedia.)*
4. Click **Deploy** to schedule this workflow.

✅ You're now set up for automated Wikipedia summaries by email.

---

## Manual Deployment

You can also run RandomWiki as a set of standalone scripts with your own scheduler (like cron).

### Scripts:

- `wikipedia_random_summary.py`
- `daily_wikipedia_email.py`

### Requirements

No Python package requirements are specified in this template. If needed, install any additional dependencies found in the node scripts.

---

## Features

- **WikipediaRandomSummary**  
  Fetches a random article summary from Wikipedia using Wikimedia's REST API.
- **DailyWikipediaEmail**  
  Sends the collected summary by email in markdown format.
- **Processing Variables:**  
  Utilizes variables such as `wiki_summary`, and `email_sent` to manage and send email content.

---

Built with ❤️ by the WaveAssist team. Want help or integrations? [Say hello](https://waveassist.io).
