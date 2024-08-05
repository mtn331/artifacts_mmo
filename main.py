## Max page is 4, with page size of 100

## First to do, get resources, use the database to check what the level required is, use the get all maps to get the resources, I am interested in:
"""
    data[].content.code retrieves a list of all the codes

    I want to check the level required for the resource.
    If I know the level, I can look through the map and retrieve the resources that are available, if matches to level 1 resources for example, then go to that tile

.data[] | select(."level">=1) | select(.level <=5).code
"""

import requests
import json
import os

level_1_resources = ["ash_tree", "gudgeon_fishing_spot", "copper_rocks"]


url = "https://api.artifactsmmo.com/maps/?content_type=resource&page=1&size=100"
resources_file = os.path.join(os.path.dirname(__file__), 'resources.json')
payload = {}
headers = {
  'Accept': 'application/json'
}

# response = requests.get(url, headers=headers, data=payload)
# print(response.text)

with open(resources_file, 'r', encoding='utf-8') as f_in:
    resources = json.load(f_in)
    pretty_resources = json.dumps(resources, indent=4)
print(pretty_resources)

