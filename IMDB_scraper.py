from bs4 import BeautifulSoup as _bs
from requests import get
from IPython import embed
import pprint
from create_file import create_actor_file 

pp = pprint.PrettyPrinter(indent=1)

# change this input to the IMDB url for the actor you want data in

input = 'https://www.imdb.com/name/nm3836977/?ref_=tt_cl_t1'

url = get(input)
content = url.content
parsed = _bs(content, 'lxml')
projects = parsed.find_all(class_="filmo-row")
header = parsed.find(class_="header")

# the initial actor data dictionary which gets updated as you run the file


actor_data = {
  "name": header.find(class_="itemprop").getText(strip=True),
  "age": 0,
  "image": parsed.find(id="name-poster")['src'] if parsed.find(id="name-poster") else '',
  "projects": {},
  "project_references": []
}

# this function will acquire the data for a given project (movie, show, ect...)

def get_project_data(project_input):
  project_url = get(project_input)
  content = project_url.content
  parsed_content = _bs(content, 'lxml')
  cast_list = parsed_content.find(class_="cast_list").find_all(class_=['odd','even']) if parsed_content.select('[class="cast_list"]') else False
  poster = parsed_content.find(class_="poster").find('img') if parsed_content.select('[class="poster"]') else False
  actors = []
  if( poster and cast_list ):
    for actor in cast_list:
      actors.append({
        "name": actor.find('a').getText(strip=True) if actor.select('a') else 'not found',
        "character": actor.find(class_="character").getText(strip=True) if actor.select('[class="character"]') else 'not found',
        "image": actor.find('img')['src'],
        "actor_url": 'https://www.imdb.com/' + actor.find('a')['href'] if actor.select('a[href]') else 'not found'
      }) 
    return { 
      'image': poster['src'],
      'actors': actors,
      'storyline': parsed_content.find(class_="summary_text").getText(strip=True),
    }
  else:
    return {
      'image': 'not found',
      'actors': 'not found',
      'storyline': 'not found'
    }

for project in projects:
  project_name = project.find('a').get_text(strip=True)
  project_url = 'https://www.imdb.com/' + project.find('a')['href']
  project_data = get_project_data(project_url)
  actor_data["projects"][project_name] = {
    "title": project_name,
    "year_released": project.find(class_='year_column').get_text(strip=True),
    "project_url": project_url,
    "character": list( project.children )[-1].replace('\n',''),
    "image": project_data["image"],
    "actors": project_data["actors"],
    "storyline": project_data["storyline"]
  }
  actor_data["project_references"] = [ *(actor_data["project_references"]), project_name ]

# this embed() is just a debugger. It will turn your command line into an interactive playground to work with actor_data
create_actor_file(actor_data)
# here you could figure out how to store to a database, or process the data in some other way
# create_actor_file(actor_data)
