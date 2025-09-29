from datetime import datetime
from google.adk.agents import Agent 
from google.adk.tools import google_search

#Below is a doctstring so the agent knows what the tool does.
#format is an optional parameter that the agent can use.
def get_current_time(format: str = "%Y-%m-%d %H:%M:%S") -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    #Make sure to return a dictionary so the agent know what you're returning (e.g. it will look at the key)
    #Be as helpful as possible!
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

#Note: you can't use both built-in tools and custom function tools in the same agent!
root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    """,
    #tools=[google_search],  #tools is a list of tools that the agent can use. Only one built-in tool is supported for each agent.
    tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)
