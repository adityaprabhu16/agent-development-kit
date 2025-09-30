import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
#Now we're using the DatabaseSessionService instead of the InMemorySessionService.
from google.adk.sessions import DatabaseSessionService
#Under the memory_agent directory, we have the agent.py file that defines the agent.
from memory_agent.agent import memory_agent
from utils import call_agent_async

load_dotenv()

# ===== PART 1: Initialize Persistent Session Service =====
# Using SQLite database for persistent storage
# Once we run this code, it will create a new database file in the root directory called my_agent_data.db.
db_url = "sqlite:///./my_agent_data.db"
session_service = DatabaseSessionService(db_url=db_url)


# ===== PART 2: Define Initial State =====
# This will only be used when creating a new session
#This will be a reminders agent. We'll now begin the process of working with our agent and database.
initial_state = {
    "user_name": "Brandon Hancock",
    "reminders": [],
}


async def main_async():
    # Setup constants
    APP_NAME = "Memory Agent"
    USER_ID = "aiwithbrandon"

    # ===== PART 3: Session Management - Find or Create =====
    # Check for existing sessions for this user
    #DatabaseSessionService has a method called list_sessions that will look for sessions for a given user.
    existing_sessions = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    # If there's an existing session, use it, otherwise create a new one
    if existing_sessions and len(existing_sessions.sessions) > 0:
        # Use the most recent session
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Continuing existing session: {SESSION_ID}")
    else:
        # Create a new session with initial state
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")

    # ===== PART 4: Agent Runner Setup =====
    # Create a runner with the memory agent
    #Core ingredients
    # 1. The agent with its tools
    # 2. The session service with our database
    runner = Runner(
        agent=memory_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    # ===== PART 5: Interactive Conversation Loop =====
    #We'll now begin the interactive conversation loop.
    print("\nWelcome to Memory Agent Chat!")
    print("Your reminders will be remembered across conversations.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Your data has been saved to the database.")
            break

        # Process the user query through the agent
        #defined in utils.py
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)


if __name__ == "__main__":
    asyncio.run(main_async())
