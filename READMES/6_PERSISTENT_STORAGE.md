Persistent State Storage:
 - We want to save sessions to our database. 
 - utils.py: includes all of the specific methods that will be used in main.py
 
Running the agent:
 - Delete our database so we're running with a clean slate. 
 - Run Scenario 1: Blank database (doesn't exist) - ADK will create it for us.
 - python main.py #spins everything up, creates my_agent_data.db
 - Run Scenario 2: Close out of the application and try retrieving your reminder (CRUD)
 - You can see the state before and after the request.

You can install SQLite Viewer in order to see what's happening inside the db:
 - app_states
 - events
 - sessions
 - user_states

