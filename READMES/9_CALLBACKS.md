Callbacks:
 - before_agent_callback: before any logic happens inside the AI solution. That is, right when things kicked off.
 - after_agent_callback: after the logic processing happens, what we want to do with the agent after. 
 - before_model_callback: preprocessing before sending a request to an AI model. 
 - after_model_callback: postprocessing after receiving a response from the AI model. 
 - before_tool_callback: some validation before a tool is being called.
 - after_tool_callback: some post-processing after a tool is called by the agent.

Most commonly used:
 - before_agent_callback: Good for setting up resources or state needed only for this specific agent's run, performing validation checks on the session state.
 - after_agent_callback: Good for logging and documenting the request. Called immediately after the agent's _run_async_impl (or _run_live_impl) implementation successfully completes. It does not run if the agent was skipped due to before_agent_callback returning content or if end_invocation was set during the agent's run.
 - before_model_callback: Allows inspection and modification of the request going into the LLM (ensuring a specific model is fit, and so on.). Examples for use cases include adding gaurd rails. 
 - after_model_callback: Called just after a response is received from the LLM, before it's processed further by the invoking agent. 
 - before_tool_callback: to perform authorization or inspect / format the tool request. 
 - after_tool_callback: to log the tool results and/or save information state.

NOTE: You can run adk web at the top level of an application and you can then choose the agent you want to run within the appropriate sub folder.