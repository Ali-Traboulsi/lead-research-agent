import os
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import BaseChatPromptTemplate
from langchain_huggingface.llms import HuggingFaceEndpoint
from langchain_core.runnables import RunnableSequence

load_dotenv()

hf_api_key = os.getenv("HUGGINGFACE_API_KEY")

question_1 =\
    """
    Explain {terminology} in {style} way so that {user} can understand
    """

prompt_template_1 =  ChatPromptTemplate(question_1)

question_2 = """What is cricket provide brief details."""
prompt_template_2 = ChatPromptTemplate.from_template(question_2)


output_parser = StrOutputParser()

falcon_llm = HuggingFaceEndpoint(
huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    temperature = 0.5,
    max_tokens = 100,
    top_p = 0.9,
    frequency_penalty = 0.0,
    timeout=3000,
    do_sample=True,
    repo_id="tiiuae/falcon-7b"
)


chain_1_way = prompt_template_1 | falcon_llm | output_parser

chain_2_way = prompt_template_2 | falcon_llm | output_parser

def run_chain_1_way(terminology: str, style: str, user: str):
    user_input = {
        "terminology": terminology,
        "style": style,
        "user": user
    }
    return chain_1_way.run(user_input)

def run_chain_2_way(terminology: str, style: str, user: str
):
    user_input = {
        "terminology": terminology,
        "style": style,
        "user": user
    }
    return chain_2_way.run(user_input
    )


def main():
    print(run_chain_1_way("cricket", "simple", "a 10 year old"))
    # print(run_chain_2_way("cricket", "simple", "a 10 year old"))


if __name__ == "__main__":
    main()