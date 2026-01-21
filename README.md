# Multi-Agent YouTube Content Summarization Pipeline using CrewAI

## Overview

This project automates the process of converting YouTube video content into well-structured blog pages using a multi-agent AI system built with **CrewAI**. Instead of relying on multiple human roles such as researchers and copywriters, the system orchestrates specialized AI agents to research video content and generate accurate, readable blog posts.

The goal is to demonstrate practical understanding of **AI agents, task decomposition, and agent orchestration** while solving a real-world content production problem.

---

## Problem Statement & Motivation

Manually converting YouTube videos into blog content is time-consuming and error-prone. A typical workflow involves:

* A **researcher** watching videos, extracting key ideas, and validating facts
* A **copywriter** transforming those notes into a blog post
* Multiple handoffs, increasing the risk of miscommunication and inconsistency

This project removes those inefficiencies by:

* Automating research and summarization
* Clearly separating responsibilities across AI agents
* Ensuring a repeatable, scalable workflow

---

## Solution Approach

The solution uses **CrewAI** to orchestrate multiple agents, each with a focused responsibility, working together to transform YouTube video content into a blog-ready format.

Key ideas:

* Each agent has a **single, well-defined role**
* Agents operate through **explicit tasks**
* Tools are used to give agents controlled access to external data

---

## Agent Architecture

### 1. Researcher (Domain Expert)

**Role:** Acts as a subject-matter researcher focused on understanding video content.

**Responsibilities:**

* Identify relevant videos based on a search query
* Extract detailed and accurate information from a specific YouTube channel

**Task Definition:**

* Identify the video `{search_query}` in the channel `{youtube_channel_handle}`
* Retrieve detailed information about the video from the same channel

---

### 2. Writer (Content Generator)

**Role:** Transforms researched information into a clear, readable blog post.

**Responsibilities:**

* Consume structured output from the Researcher agent
* Write a concise and informative blog summary
* Output content in markdown format

**Task Definition:**

* Use information from `{youtube_channel_handle}` related to `{search_query}` to write a blog post
* Save the final output to `new-blog-post.md`

---

## Tools Used

### YouTubeChannelSearchTool

This tool enables agents to interact with YouTube channel data in a controlled manner.

**Purpose:**

* Search for videos within a specific YouTube channel
* Retrieve video-level details required for summarization

The tool is only accessible to agents that require it, reinforcing clean separation between reasoning and data access.

---

## Workflow

1. **Researcher Agent Execution**

   * Uses `YouTubeChannelSearchTool`
   * Identifies the relevant video based on the search query
   * Extracts detailed content and context

2. **Handoff Between Agents**

   * The structured output from the Researcher is passed directly to the Writer agent
   * This eliminates ambiguity and communication gaps

3. **Writer Agent Execution**

   * Uses the research output as input
   * Generates a blog-style summary
   * Writes the content to `new-blog-post.md`

---

## CrewAI Orchestration

This project demonstrates effective use of CrewAI by:

* Defining agents with **clear boundaries and expertise**
* Assigning **explicit tasks** instead of vague goals
* Using tools as controlled interfaces rather than general-purpose browsing
* Creating a deterministic, explainable agent workflow

---

## Output

* A markdown blog post summarizing the selected YouTube video
* Clear traceability from video source → research → final content

---

## Key Learnings

* How to decompose a real-world workflow into agent-specific responsibilities
* Designing agent tasks that reduce overlap and confusion
* Using tools to ground agent outputs in external data
* Building scalable, repeatable AI content pipelines with CrewAI

---

## Future Improvements

* Support for multiple videos per blog post
* SEO optimization agent
* Publishing integration with CMS platforms
* Feedback loop for content quality evaluation

---

## Tech Stack

* Python
* CrewAI
* YouTubeChannelSearchTool
* Markdown for content output
