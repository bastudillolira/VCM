import pandas as pd
from urllib.request import Request, urlopen
import json

url = 'https://www.cityforestcredits.org/wp-content/uploads/2022/08/CFC-Registry-Project-List-20220810.csv'

print("Reading URL...")
req = Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
content = urlopen(req)

df = pd.read_csv(content)

print("URL done!")

json_string = df.to_json()

result_dict = json.loads(json_string)

with open('CFC.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_dict, json_file, ensure_ascii=False, indent=4)
