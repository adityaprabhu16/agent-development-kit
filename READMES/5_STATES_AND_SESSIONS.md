Sessions, Runners, and Events: 

A session inside ADK: (see visual within README section)
 - "Stateful chat history"
 - Has a state (a dictionary with keys and values).
 - Has events (message history, tool calls, etc. - everything that happens between us and the agent)
 - Additional information included in a session:
  - id
  - app_name
  - user_id
  - last_update_time

Types of sessions:
 - In-memory session: Our current session, lost when gone
 - Database session: Every conversation is stored to the DB, pulled from DB when we come back.
 - Vertex AI session: Every conversation stored in the cloud via Vertex AI

A runner inside ADK: 
 - A collection of two pieces of information: your agents and your session:
  - E.g. "what type of agents do we have available to handle a request?"
  - E.g. "look at our session and pass it over to the agent we decided that's responsible to handle the request"
  - Then that selected agent passes the information to to the LLM, delegates tool calling, returns a response.
  - Runner will then spit back the response.

  
Run:
 - python basic_stateful_session.py (which shows the question and answering pipeline in detail with logs).
 - You'll see:
 CREATED NEW SESSION:
        Session ID: 1fbfa204-7e14-4c73-aa5d-5052d8a96271
Final Response: Brandon's favorite TV show is Game of Thrones.

==== Session Event Exploration ====
=== Final Session State ===
user_name: Brandon Hancock
user_preferences: 
        I like to play Pickleball, Disc Golf, and Tennis.
        My favorite food is Mexican.
        My favorite TV show is Game of Thrones.
        Loves it when people like and subscribe to his YouTube channel.