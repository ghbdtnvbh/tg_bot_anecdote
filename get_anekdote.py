import requests
from bs4 import BeautifulSoup

url = "https://baneks.site/random"
headers = {
    "accept":"*/*",
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}
def get_anekdot():
    resp = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(resp, "lxml")
    anekdot = str(soup.find(itemprop="description")).replace("<br/>", "\n")
    return BeautifulSoup(anekdot, "lxml").text

def update_url():
    anekdot = get_anekdot()
    while len(anekdot) > 130:
        anekdot = get_anekdot()
    else:
        return anekdot