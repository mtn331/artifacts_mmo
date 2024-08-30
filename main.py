## Max page is 4, with page size of 100

## First to do, get resources, use the database to check what the level required is, use the get all maps to get the resources, I am interested in:
## TODO: Handle the cooldowns, if it is not a 200, 25s cd per action, action is gathering, moving etc..

"""
    data[].content.code retrieves a list of all the codes

    I want to check the level required for the resource.
    If I know the level, I can look through the map and retrieve the resources that are available, if matches to level 1 resources for example, then go to that tile

.data[] | select(."level">=1) | select(.level <=5).code
"""

import requests
import json
import os
import time
from dotenv import load_dotenv

load_dotenv(override=True)
CHARACTER_NAME = "python"

header = {'Authorization': f"Bearer {os.getenv("TOKEN")}"}

character_url="https://api.artifactsmmo.com/my/characters"
map_url = "https://api.artifactsmmo.com/maps/?page=2&size=100"
url = "https://api.artifactsmmo.com/maps/?content_type=resource&page=1&size=100"


def get_current_stats():
    pass

def get_inventory():
    pass

## Should switch skill once reached a certain level
## Also count the amount of requests sent to the server, if it is too much, then stop the script

def move_to_tile(character_name, x, y):
    move_url = f"https://api.artifactsmmo.com/my/{character_name}/action/move"
    response = requests.post(move_url, headers=header, data={'x': x, 'y': y}, timeout=5)
    if response.status_code == 200:
        print('Moved to:', x, y)
    else:
        print('Failed to move to:', x, y)
        print('Response is not 200, status code:', response.status_code)
        print('Response:', response.text)


def gather_resource(character_name, resource_code):
    gather_url = f"https://api.artifactsmmo.com/my/{character_name}/action/gathering"
    response = requests.post(gather_url, headers=header, timeout=5)
    details = response.json()['data']['details']
    if response.status_code == 200:
        print('Gathered resource:', details['items'][0]['code'])
        print('XP gained:', details['xp'])
    else:
        print('Failed to gather resource')
        print('Response is not 200, status code:', response.status_code)
        print('Response:', response.text)

## Move to tile, perform action
def get_character_stats():
    pass

def process_resource_data_2(data):
    resources_by_code = {}

    for resource in data['data']:
        code = resource['code']
        skill = resource['skill']
        level = resource['level']
        if code not in resources_by_code:
            resources_by_code[code] = {}
        resources_by_code[code] = {'level': level, 'skill': skill}
    return resources_by_code


def save_response_to_json(response, file_name):
    json_response = response.json()
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(json_response, f, ensure_ascii=False, indent=4)



resources_file = os.path.join(os.path.dirname(__file__), 'resources.json')
payload = {}
headers = {
  'Accept': 'application/json'
}

with open(resources_file, 'r', encoding='utf-8') as f_in_res, \
  open('map.json', 'r', encoding='utf-8') as f_in_map:
    map = json.load(f_in_map)
    resources = json.load(f_in_res)
    pretty_resources = json.dumps(resources, indent=4) ## Is a string

dic = process_resource_data_2(resources)
## Heb een dict met de resources per level en dan de skill en dan de code (code is de naam van de resourcee zoals ash tree)
## Op de map moet ik onder .data[0].content.code , content kan null zijn, dan is er geen code

for resource in map['data']:
    if resource['content']:
      code= resource['content']['code']
      try:
          value = dic[code]
          print('Resource found:', value)
          x_coord = resource['x']
          y_coord = resource['y']
          # print('Moving to:', x_coord, y_coord)
          # move_to_tile(CHARACTER_NAME, x_coord, y_coord)
          # gather_resource(CHARACTER_NAME, code)
      except KeyError:
          print('Resource not found')
while True:
    gather_resource(CHARACTER_NAME, code)
    time.sleep(26)


# I should check my characters current level for the skills,
## then on the map I check if the resources are available for that level, equal or lesser
## I should get the code and then link the level and skill to it