Stateful Multi Agent:
 - High level: Customer Service Group Agent
 - Has sub agents: Policy Agent, Sales Agent, Course Support Agent, Order Agent
 - Sales Agent allows a customer to purchase a course, which updates the state. 
 - Order Agent allows a customer to be able to refund a course. 
 - We'll first check to see if that user owns the course, and then determine if they can do a refund.
 - This is why shared state will be super useful here, because the refund, sales, support agents, etc. can work together based on whether the user has purchased a course before or not.

In short, agents can be more intelligent when working together if they share state. It gives them shared context in a conversation and can better help assist the user on their needs. Hope that makes sense.

