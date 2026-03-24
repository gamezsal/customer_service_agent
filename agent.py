"""
Real-world applications
Application: Personalized customer service agent
Combines state templating and namespaces for customer support:

""" 
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

# Setup
session_service = InMemorySessionService()
session = session_service.create_session(app_name="support", user_id="customer1")

# Initialize state
session.state["user:name"] = "Alex Johnson"
session.state["user:tier"] = "premium"
session.state["user:language"] = "English"
session.state["app:business_hours"] = "24/7"
session.state["app:escalation_threshold"] = 3

# Agent with templating
root_agent = LlmAgent(
    model='gemini-2.5-flash',
    instruction="""
You are a {user:tier} customer support agent.

Customer info:
- Name: {user:name?Guest}
- Support tier: {user:tier?standard}
- Language: {user:language?English}

Session info:
- Message #{messages_in_conversation?1}
- Issue: {issue_category?general support}
- Business hours: {app:business_hours}

{needs_escalation?!! ESCALATION THRESHOLD REACHED. Route to human agent if unresolved.}

Respond in {user:language} with personalized support.
""",
    output_key="response"
)

runner = Runner(agent=root_agent, app_name="support", session_service=session_service)