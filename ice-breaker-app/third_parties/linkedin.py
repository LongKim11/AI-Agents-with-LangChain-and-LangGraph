import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = "https://api.scrapin.io/v1/enrichment/profile"
        params = {"apikey": os.environ["SCRAPIN_API_KEY"],
                  "linkedInUrl": linkedin_profile_url}
        response = requests.get(api_endpoint, params=params, timeout=10)

    data = response.json().get("person")
    return data

if __name__ == "__main__":
    print(scrape_linkedin_profile("https://www.linkedin.com/in/eden-marco/", mock=True))