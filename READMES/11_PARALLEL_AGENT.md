Main Idea:
 - Agents work in parallel and combine their findings.  
 - We'll create a Parallel Agent to gather information concurrently.
 - We'll then create a Sequential Pipeline to gather information in two stages:
  - system_info_gatherer: a wrapper for a group of agents working in parallel
  - system_report_synthesizer: takes the output from system_info_gatherer and produces a result.

- Example: Parallel Research Agent.
- Example: Computer Health Checking Agent.
- "Please get the stats for my computer"
- A cpu, memory, disk info agent will work together (utilizing tools that leverage python libraries to check the system memory and capacity), and the results are synthesized by the synthesizer agent.

NOTE:
 - Use parallel agents whenever you want to complete a lot of related parallel work at the same time.