from bs4 import BeautifulSoup
import requests
from openai import OpenAI
import os
from dotenv import load_dotenv
from IPython.display import Markdown, display



class WebsiteScrapper:

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

        load_dotenv(override=True)
        api_key = os.getenv('OPENAI_API_KEY')

        if not api_key:
            print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
        elif not api_key.startswith("sk-proj-"):
            print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
        elif api_key.strip() != api_key:
            print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")

        self.openai = OpenAI()

        self.system_prompt = "You are an assistant that analyzes the contents of a website " \
                             "and provides a short summary, ignoring text that might be navigation related. " \
                             "Respond in markdown."

        self.user_prompt = f"You are looking at a website titled {self.title}"
        self.user_prompt += "\nThe contents of this website is as follows;" \
                       "please provide a short summary of this website in markdown." \
                       "If it includes news or announcements, then summarize these too.\n\n"
        self.user_prompt += self.text

        self.messages=[
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt}
        ]
    
    def summarize(self):
        response = self.openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages = self.messages
        )
        return response.choices[0].message.content
   
         