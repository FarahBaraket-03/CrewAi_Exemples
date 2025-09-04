# CrewAI Examples Repository

A collection of practical examples, tutorials, and starter projects demonstrating the power and flexibility of CrewAI for building multi-agent AI systems.

## 🚀 What is CrewAI?

CrewAI is a cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI enables these agents to work in tandem, tackling complex tasks that would be difficult for a single agent to handle. 
This repository serves as a practical guide to getting started.



## 🚀 Featured AI Agent Frameworks

- [<img src="https://cdn.simpleicons.org/langchain" alt="LangChain logo" width="25" height="25"> LangChain ](https://python.langchain.com/)
- [<img src="https://cdn.prod.website-files.com/66cf2bfc3ed15b02da0ca770/66d07240057721394308addd_Logo%20(1).svg" alt="CrewAI logo" width="35" height="25"> CrewAI](https://www.crewai.com/)


## 📁 Projects Overview

### 🤖 [AI Research & Report Crew](/research_ai_developments/)
**Agents that research and synthesize the latest AI advancements**
- **Researcher Agent:** Searches for cutting-edge AI developments using web search tools
- **reporting_analyst Agent:** Evaluates and compares the significance of findings then Compiles research into comprehensive, well-structured reports
- **Perfect for:** Staying updated with AI breakthroughs, market research, technical analysis

### 📰 [News Scraper Crew](/news_scraper/)
**Intelligent agents that extract and process news content**
- **Scout Agent:** Identifies relevant news sources and URLs
- **Extractor Agent:** Uses browser automation to scrape article content
- **Summarizer Agent:** Creates concise summaries of news articles
- **Ideal for:** Media monitoring, content aggregation, trend analysis

### ✈️ [Travel Planning Crew](/travel_planning/)
**Personalized travel itinerary creators**
- **Destination Expert:** Researches optimal locations based on preferences
- **Itinerary Planner:** Creates detailed day-by-day schedules
- **Budget Analyst:** Calculates costs and suggests budget-friendly options
- **Great for:** Trip planning, vacation organization, travel recommendations

### 🎮 [Game Builder Crew](/gamebuilder/)
**AI-powered game development team with quality assurance**
- **Senior Software Engineer:** Creates software as needed with Python expertise
- **Quality Control Engineer:** Analyzes code for errors, security vulnerabilities, and logic issues
- **Chief QA Engineer:** Ensures code fulfills requirements and maintains high quality standards
- **Includes examples:** 🐍 Snake, 👻 Pac-Man, and other classic game implementations
- **Perfect for:** Rapid prototyping, educational projects, code quality assuranc

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.10+**
- **uv** (Python package manager)
- An API key from **OpenAI**, **Anthropic**, or another supported LLM provider.
- **Serper API Key** (for search functionality):
    - Get it from: [https://serper.dev/api-key](https://serper.dev/api-key)

- **Browserless API Key** (for web scraping and browser automation):
    - Get it from: [https://www.browserless.io/](https://www.browserless.io/)




## ⚡ Quick Start

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/FarahBaraket-03/CrewAi_Exemples.git
    cd CrewAi_Exemples
    ```

2.  **Create a virtual environment and install dependencies:**
    `uv` makes this incredibly fast. From the project root, run:
    ```bash
    uv sync
    ```
    This will read the `pyproject.toml` file and create a virtual environment (in `.venv`) with all necessary dependencies installed.


3.  **Fill in your `.env` file:**
    ```env
    # LLM Provider (Choose one)
    OPENAI_API_KEY=your-openai-api-key-here
    # ANTHROPIC_API_KEY=your-anthropic-api-key-here

    # Search & Browser Tools
    SERPER_API_KEY=your-serper-api-key-here
    BROWSERLESS_API_KEY=your-browserless-api-key-here
    ```





    ## 🤖 How to Create Your Own Crew

The general pattern for building with CrewAI is:

1.  **Define Agents:** Create your AI workforce. Assign each agent a `role`, a `goal`, and a `backstory`.
2.  **Create Tasks:** Break down your objective into smaller tasks. Assign each task to an agent and define the expected output.
3.  **Form the Crew:** Assemble your agents into a crew. Choose a process (e.g., `sequential` or `hierarchical`) that dictates how they collaborate.
4.  **Kick it off:** Run `crew.kickoff()` and let your AI team do the work!
