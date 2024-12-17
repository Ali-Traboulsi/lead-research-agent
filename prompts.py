from data.knowledge import load_config
from langchain.prompts import PromptTemplate

knowledge_qa = load_config('data/knowledge.json')

def create_prompt(parameters):
    # load the config file
    config = load_config('data/config.json')

    # get the parameters
    prompt_template = """
    Role: {role}
    Objective: {objective}
    Context: {context}
    Step-by-Step Process (SOP): {sop}
    Instructions: {instructions}
    Tools & Subagents: {tools}
    Examples:
    {examples}
    """

    # Generate examples from the parameters
    example_text = "\n".join(
        [f"Q: {example['Q']} A: {example['A']}" for example in parameters.get("examples", [])]
    )

    prompt = PromptTemplate(
        input_variables=["role", "objective", "context", "sop", "instructions", "tools", "examples"],
        template=prompt_template
    )

    return prompt.format(
        role=parameters.get("role", "Lead Generation Assistant"),
        objective=parameters.get("objective", "Assist the user in finding leads based on LinkedIn Sales Navigator criteria."),
        context=parameters.get("context", "This agent helps users find relevant leads to improve outreach and sales."),
        sop=parameters.get("sop", "1. Take user input for criteria. 2. Search for leads based on criteria. 3. Refine results."),
        instructions=parameters.get("instructions", "Ensure criteria match; avoid irrelevant results; confirm accuracy."),
        tools=parameters.get("tools", "Access to LinkedIn Sales Navigator data, Q&A database for FAQs."),
        examples=example_text
    )
