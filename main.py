from fastapi import FastAPI
from actions import setup_lead_gen_chain
from prompts import create_prompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    cohere_api_key = os.getenv("COHERE_API_KEY")

    # Define your parameters, either hard-coded or dynamically received
    parameters = {
        "role": "Lead Generation Assistant",
        "objective": "Assist the user in finding leads based on LinkedIn Sales Navigator criteria.",
        "context": "This agent helps users find relevant leads to improve outreach and sales.",
        "sop": "1. Take user input for criteria. 2. Search for leads based on criteria. 3. Refine results.",
        "instructions": "Ensure criteria match; avoid irrelevant results; confirm accuracy.",
        "tools": "Access to LinkedIn Sales Navigator data, Q&A database for FAQs.",
        "examples": [
            {"Q": "Find leads in tech industry", "A": "Targeting tech industry leads with relevant roles."},
            {"Q": "Identify decision-makers in healthcare", "A": "Focusing on healthcare decision-makers."}
        ]
    }

    # Initialize chain
    llm_chain = setup_lead_gen_chain(parameters)

    # Example user input
    user_input = {"criteria": "technology companies, mid-size, CTOs in New York"}
    output = llm_chain.run(user_input)
    print(output)

if __name__ == "__main__":
    main()
