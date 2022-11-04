import requests
from bs4 import BeautifulSoup
import json

url = "https://api-front.ecoregistry.io/api/project/public"

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br,ç",
    "Accept-Language": "es;q=0.9",
    "Authorization": "Bearer null",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "api-front.ecoregistry.io",
    "If-None-Match": 'W/"ef23-gqFcJEpxY0GgCeVo3tcVNdg/Av0"',
    "lng": "es",
    "Origin": "https://www.ecoregistry.io",
    "platform": "ecoregistry",
    "Referer": "https://www.ecoregistry.io/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
}

print(f"Reading {url}...")

res = requests.get(url, headers=headers)

res_json = json.loads(json.dumps(res.json()))

projects = []
for project in res_json["projects"]:
    projects.append(project)

with open("projects_ecoregistry.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(projects))
    file.close()

print("Done!")