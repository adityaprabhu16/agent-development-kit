Root agents:
 - Delegates tasks to other agents.

Inside ADK:
 - The ADK root agent will get the query passed in from the user. 
 - The ADK agent will look at the DESCRIPTION of all of the sub agents.
 - Once it knows who to pass the work to, the root agent is out of the picture.
 - The sub agent then takes control, and determines what tool calls to make to answer the question
 - Once the answer is received, it will generate the result and return the final response.
 - ADK is all about delegation and immediately answering the question.
 - If you don't like this workflow where we delegate the task to another agent and can't use built-in tool calls, check out some of these other options
  - Sequential Agents
  - Parallel Agents
  - Loop Agents

Other ADK Consideration: Agent-as-a-Tool:
 - Agent-as-a-Tool: When Agent A calls Agent B as a tool (using Agent-as-a-Tool). Agent B's answer is passed back to Agent A, which then retains control and continues to handle future user input. Agent A RETAINS CONTROL and continues to handle future user input.

 - Sub-agent: When Agent A calls Agent B as a sub-agent, the responsibility of answering the user is COMPLETELY TRANSFERED to Agent B. Agent A is effectively out of the loop. All subsequent user input will be answered by Agent B.

Usage:
 - To use an agent as a tool, wrap the agent with the AgentTool class. That way, we can also take advantage of built-in tools like Google Search (see news_analyst agent).
 - tools=[AgentTool(agent=agent_b)]


Core Limitations working with ADK:
 - Built-in tools cannot be used within a sub-agent. 
 - Recall from lesson 2: builtin tools include Google Search, Code Execution, Retrieval Augmented Generation (RAG)

Inside CrewAI (an ADK alternative):
 - You have one task, and you have multiple agents try to work on it
 - E.g. you have Get Weather, and you have multiple agents working on it 
 - E.g. a weather agent, a research agent, and together these agents will work together to answer the question and collaborate.