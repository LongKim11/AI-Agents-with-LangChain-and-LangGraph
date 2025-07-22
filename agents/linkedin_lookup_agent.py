import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from tools.tools import get_profile_url_tavily

load_dotenv()

def lookup(name: str) -> str:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    template = """given the full name {name_of_person} I want you to get a link to their Linkedin profile page. Your answer should contain only a URL"""

    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    tools_for_agent = [Tool(name="Crawl Google for Linked profile page", func=get_profile_url_tavily, description="useful for when you need to get the Linkedin page URL")]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format(name_of_person=name)})

    linkedin_profile_url = result["output"]

    return linkedin_profile_url

if __name__ == "__main__":
    print(lookup("Eden Marco"))