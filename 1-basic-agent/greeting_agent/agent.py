from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",  #must match folder name! (ADK requirement).
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting agent",  #used to give other agents information about what this agent does.
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """, #used to give the agent instructions on what to do.
)
