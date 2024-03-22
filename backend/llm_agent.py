import os
from langchain_community.llms import OpenAI
from langchain.agents import initialize_agent, AgentType, Tool
from langchain import SerpAPIWrapper


def get_llm_response(
    topic: str, description: str, wordcount, isLiveSearchEnabled
) -> str:
    res = ""
    llm = OpenAI()
    if isLiveSearchEnabled:
        res = search_google(topic)
    else:
        res = llm(topic)
    prompt = f"Please generate a {wordcount}-word paragraph of Little Red Book copy based on the {topic} {description} and {res}, include as many emoji as possible, and add a few hashtags at the end of the copy, something like: '#travel'."
    return llm(prompt)


def search_google(topic: str) -> str:
    llm = OpenAI()
    search = SerpAPIWrapper()
    tools = [
        Tool(
            name="Intermediate Answer",
            func=search.run,
            description="useful for when you need to ask with search",
        )
    ]

    self_ask_with_search = initialize_agent(
        tools,
        llm,
        agent=AgentType.SELF_ASK_WITH_SEARCH,
        verbose=True,
        handle_parsing_errors=True,
    )

    return self_ask_with_search(topic)


if __name__ == "__main__":
    llm = OpenAI()
    # print(get_llm_response("openai sora", "llm", 100, False))
    print(get_llm_response("openai sora", "llm", 100, True))
