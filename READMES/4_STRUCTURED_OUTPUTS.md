Structured outputs are very important when we start doing things with multi-agent because we'll need to make sure the output of agent A is formatted properly before we go to agent B.

Ways to structure data:
 - input_schema: Define a Pydantic BaseModel represent an expected input structure. (Not reccomended often in the event a previous agent's output is messed up, and it needs to be used as input in the next agent, you break the pipeline!)
 - output_schema: Define a Pydantic BaseModel that represents a Pydantic BaseModel representing an expected output structure.
 - output_key: Provde a string key. If set, the text content of the agent's final response will be automatically saved to the session's state dictionary under this key (e.g., session.state[output_key] = agent_response_text). This is useful for passing results between agents or steps in a workflow. 
   - E.g. allows a shared "pool" or state where agents can use the result of a previous agent's work (e.g. one agent finds the capital saves it under an output_key, and another agent can use that result to look up information on the capital).


