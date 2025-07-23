from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter import scrape_user_tweets
from output_parsers import summary_parser, Summary

def ice_break_with(name:str) -> tuple[Summary, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_url, mock=True)

    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(twitter_username, mock=True)

    summary_template = """
        given the information about a person from Linkedin {linkedin_data} and Twitter {twitter_data} I want you to create:
        1. a short summary
        2. two interesting facts about them

        Use both information from Linkedin and Twitter.

        {format_instructions}
    """
    summary_prompt_template = PromptTemplate(input_variables=["linkedin_data", "twitter_data"], template=summary_template, partial_variables={"format_instructions": summary_parser.get_format_instructions()})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    chain = summary_prompt_template | llm | summary_parser

    res:Summary = chain.invoke({"linkedin_data": linkedin_data, "twitter_data": tweets})

    return res, linkedin_data.get("photoUrl")

if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")

    ice_break_with("Eden Marco Udemy")

    


