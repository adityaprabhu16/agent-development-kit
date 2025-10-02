- Agents work in the order we have them come in.
- You can't summarize any webpage without get_page_contents.
- Quick example: 
  - input -> sub_agents_1 -> sub_agents_2 -> output
- Then you need to write that to state. Walk through it step by step. 

- Example: lead qualification pipeline
- We give some information to agent (lead information).
- This lead information will then be scored (how urgent the problem is, budget, etc.).
- Then we'll generate next steps.
- In summary, we're building a sequential workflow here.

Example: 
 - Lead Information: Name: John Doe Email: john@gmail.com Interest: Something with AI maybe Notes: Met at conference, seemed interested but was vague about needs.

 1. valid 
 2. 2: Vague interest and unclear needs suggest low qualification.
 3. Reccomendation: John Doe's vague interest and low qualification score (2) suggest a nurturing approach. I recommend sending John some introductory educational content about AI applications to spark his interest and better understand his needs.

 This strategy is common with Crew AI agents, where the agents work together on the task.