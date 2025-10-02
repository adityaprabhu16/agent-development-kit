Loop Agents:
 - Agents iterate on a problem over and over again until it solves it. "Sequential Agents on Steroids"
 - E.g. Linkedin Post Generator that uses a Sequential and Loop Agent pattern in the Agent Development Kit (ADK) to generate and refine a LinkedIn post.
   - We have an agent that generates the LinkedIn post and stores its result to a specific output key (e.g. "current_post" as a state).
   - The quality refinement agent will attempt to access "current_post" and make the contents better or reject it.
   - A reviewer agent will then attempt to access the "current_post" updated from the quality refinement agent's output and confirm it meets standards.
 - NOTE: having a good exit condition here is a MUST because we need to make sure it's clear when it's time to give up or when we've successfully completed the goal.

 Overview:
  - 1. Generate a LinkedIn Post
  - 2. Iteratively refine the post until quality requirements are met.
