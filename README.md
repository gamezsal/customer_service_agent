# README: Customer Service Agent

This project is a professional AI-powered technical support assistant built using the **Agent Development Kit (ADK)**. It is designed to handle customer inquiries systematically, maintain a consistent persona, and interact with external systems through custom tools.

## Project Overview
The agent, is a Senior Technical Support Specialist with 5 years of experience. It follows a strict methodology to ensure high-quality service:
1.  **Acknowledge:** Show empathy for the customer's situation.
2.  **Clarify:** Ask targeted questions to understand the issue.
3.  **Solve:** Provide clear, step-by-step solutions.
4.  **Verify:** Confirm the issue is fully resolved.

## Prerequisites
*   **Python 3.11 or higher**
*   **pip** (Python package installer)
*   An **API Key** from Google AI Studio (Gemini API)

## Installation & Setup

1.  **Create a Workspace Directory:**
    ```bash
    mkdir adk-projects
    cd adk-projects
    ```

2.  **Set Up a Virtual Environment:**
    *   **Mac/Linux:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    *   **Windows:**
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```

3.  **Install the ADK Framework:**
    ```bash
    pip install google-adk
    ```

4.  **Create the Project:**
    ```bash
    adk create customer_service_agent
    cd customer_service_agent
    ```

## Configuration

Open the `.env` file in your project directory and add your credentials. **Note: Do not share or commit this file.**

```text
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your-actual-api-key-here
```

To prevent your keys from being uploaded to GitHub, ensure your `.gitignore` file includes:
```text
.env
__pycache__/
.venv/
```

## Agent Features

### 1. Structured Instructions
The agent uses a professional instruction pattern including Identity, Mission, Methodology, and Boundaries. This ensures the agent never provides sensitive information (like passwords) and knows when to escalate issues to billing or engineering teams.

### 2. State Templating
The agent uses session state to personalize interactions. For example, it can greet users by name using the syntax:
`"Hello {user:name?Guest}, how can I help you today?"`

### 3. Integrated Tools
The agent is equipped with custom tools to perform actions such as:
*   `check_order_status`: Queries the database for real-time shipping info.
*   `process_refund`: Handles refund requests according to company policy.

### 4. Structured Output
To ensure the agent's data can be used by other systems, it uses **Pydantic schemas** to return guaranteed JSON structures for specific tasks like ticket creation.

## How to Run

To test the agent in a visual chat interface, run the following command from your project directory:

```bash
adk web
```

This will start a local server at `http://localhost:8000`. 

## Project Structure
*   `agent.py`: The main file where the `root_agent` and custom tools are defined.
*   `__init__.py`: Required for the ADK framework to discover your agent.
*   `.env`: Local environment variables and secrets.
