import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url):
    visited = set()
    forms = []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    for form in soup.find_all("form"):
        action = form.get("action")
        method = form.get("method", "get").lower()
        inputs = []

        for input_tag in form.find_all("input"):
            name = input_tag.get("name")
            input_type = input_tag.get("type", "text")
            inputs.append({"name": name, "type": input_type})

        forms.append({
            "action": urljoin(url, action),
            "method": method,
            "inputs": inputs
        })

    return forms
