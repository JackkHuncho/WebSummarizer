# imports
import subprocess
import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display

# constants
OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS     = {"Content-Type": "application/json"}
MODEL       = "llama3.2"

# Pull the Ollama model (replaces the Jupyter “!ollama” magic)
try:
    subprocess.run(["ollama", "pull", MODEL], check=True)
except FileNotFoundError:
    print("Warning: 'ollama' CLI not found—make sure it's installed and on your PATH.")
except subprocess.CalledProcessError:
    print(f"Warning: failed to pull model {MODEL}. You may need to run it manually.")

# constant system prompt for what we are doing
systemPrompt = (
    "You are an assistant that analyzes the contents of a website "
    "and provides a short summary, ignoring text that might be navigation related. "
    #"Respond in markdown"
)

# headers to take care of the special case websites
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    )
}

# website class to use BeautifulSoup to webscrape html
class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

def mkMessages(wsite):
    usrPrompt  = f"You are looking at a website with the title {wsite.title}\n"
    usrPrompt += "The content of the website is as follows; please summarize it:\n\n"
    usrPrompt += wsite.text
    return usrPrompt

def WebSummary(website):
    # make the website object from the provided url
    wsite = Website(website)

    # create the messages list, from the prompts
    messages = [
        {"role": "system", "content": systemPrompt},
        {"role": "user",   "content": mkMessages(wsite)}
    ]
    payload = {
        "model":    MODEL,
        "messages": messages,
        "stream":   False
    }

    response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
    response.raise_for_status()
    summary = response.json()["message"]["content"]
    #display(Markdown(summary)) for jupyter
    print(summary)

# main code
while True:
    print('Type the website URL to be summarized, or "q" to quit:')
    website = input().strip()
    if website.lower() == 'q':
        break
    try:
        WebSummary(website)
    except Exception as e:
        print("Error:", e)
    print()

print('Thank you for using the web summarizer tool!')

