# Agent Development Kit (ADK) Crash Course

This repository contains examples for learning Google's Agent Development Kit (ADK), a powerful framework for building LLM-powered agents.

## Getting Started

### Setup Environment

You only need to create one virtual environment for all examples in this course. Follow these steps to set it up:

```bash
# Create virtual environment in the root directory
python -m venv .venv

# Activate (each new terminal)
# macOS/Linux:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate.bat
# Windows PowerShell:
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Once set up, this single environment will work for all examples in the repository.

### Setting Up API Keys

#### Step 1: Get Your Google API Key

1. **Create a Google Cloud Account**: Go to https://cloud.google.com/?hl=en and create an account if you don't have one
2. **Create a New Project**: 
   - In the Google Cloud Console, create a new project or select an existing one
   - Note your project ID for later use
3. **Get Your API Key**:
   - Go to https://aistudio.google.com/apikey
   - Click "Create API Key"
   - Select your Google Cloud project from the dropdown
   - Copy the generated API key (keep it secure!)
4. **Enable Billing**: 
   - Go to the Google Cloud Console billing section
   - Connect your project to a billing account (required for API usage)
   - Note: Google provides free credits for new users

#### Step 2: Set Up Environment Variables

For each example project you want to run:

1. **Navigate to the example folder** (e.g., `1-basic-agent/greeting_agent/`)
2. **Create a `.env` file** in that folder with the following content:
   ```
   # Google API Key for Gemini models
   # Get your API key from: https://aistudio.google.com/apikey
   GOOGLE_API_KEY=your_actual_api_key_here
   ```
3. **Replace `your_actual_api_key_here`** with the API key you copied from step 1

**Important Notes:**
- Never commit your `.env` file to version control (it contains sensitive information)
- Each example folder needs its own `.env` file
- If a folder doesn't have a `.env.example` file, create the `.env` file manually using the format above

#### Step 3: Verify Your Setup

Test your API key by running any example:
```bash
cd 1-basic-agent
adk web
```

If you see authentication errors, double-check:
- Your API key is correct and properly formatted
- Your Google Cloud project has billing enabled
- The `.env` file is in the correct directory

## Examples Overview

Here's what you can learn from each example folder:

### 1. Basic Agent
Introduction to the simplest form of ADK agents. Learn how to create a basic agent that can respond to user queries.

### 2. Tool Agent
Learn how to enhance agents with tools that allow them to perform actions beyond just generating text.

### 3. LiteLLM Agent
Example of using LiteLLM to abstract away LLM provider details and easily switch between different models.

### 4. Structured Outputs
Learn how to use Pydantic models with `output_schema` to ensure consistent, structured responses from your agents.

### 5. Sessions and State
Understand how to maintain state and memory across multiple interactions using sessions.

### 6. Persistent Storage
Learn techniques for storing agent data persistently across sessions and application restarts.

### 7. Multi-Agent
See how to orchestrate multiple specialized agents working together to solve complex tasks.

### 8. Stateful Multi-Agent
Build agents that maintain and update state throughout complex multi-turn conversations.

### 9. Callbacks
Implement event callbacks to monitor and respond to agent behaviors in real-time.

### 10. Sequential Agent
Create pipeline workflows where agents operate in a defined sequence to process information.

### 11. Parallel Agent
Leverage concurrent operations with parallel agents for improved efficiency and performance.

### 12. Loop Agent
Build sophisticated agents that can iteratively refine their outputs through feedback loops.

## Official Documentation

For more detailed information, check out the official ADK documentation:
- https://google.github.io/adk-docs/get-started/quickstart

## Support

Need help or run into issues? Join our free AI Developer Accelerator community on Skool:
- [AI Developer Accelerator Community](https://www.skool.com/ai-developer-accelerator/about)

In the community you'll find:
- Weekly coaching and support calls
- Early access to code from YouTube projects
- A network of AI developers of all skill levels ready to help
- Behind-the-scenes looks at how these apps are built


Setup README and environment.


Setup Instructions:
 - Core components:
   - Inside ADK, make a root_agent. The root agent is the entry point to all of the requests.

- Running an agent:
   - adk  (tells you everything you can do with adk)
   - adk api_server (creates a FastAPI server for agents)
   - adk run 
   - adk web (starts a FastAPI server with Web UI for agents)