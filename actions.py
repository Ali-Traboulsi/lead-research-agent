import os
from langchain_cohere.llms import Cohere
from langchain.chains import LLMChain
from prompts import create_prompt


# Make sure you have set the API key as an environment variable
# (You can use python-dotenv to manage .env files if needed)

# Define the Cohere model and chain
def setup_lead_gen_chain(parameters):
    # Initialize Cohere LLM - Note: api_key not passed directly
    cohere_llm = Cohere()  # Will automatically look for COHERE_API_KEY in environment

    # Create prompt using the custom prompt function
    prompt = create_prompt(parameters)

    # Set up chain using LLM and prompt
    llm_chain = LLMChain(prompt=prompt, llm=cohere_llm)
    return llm_chain

