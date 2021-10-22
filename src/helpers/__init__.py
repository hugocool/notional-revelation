import os
from notion_client import Client
from pydantic import BaseModel, HttpUrl, computed_field
from typing import List
from notional.records import Page

def search_notion(NOTION_TOKEN, query=None):
  base_query = dict(
      filter={
    'property':'object',
    'value':'page'
    },
    sort = {
      "direction":"descending",
      "timestamp":"last_edited_time"
    })
  

  if query:
    full_query = {**base_query,**dict(query=query)}
  else:
    full_query = base_query

  notion = Client(auth=NOTION_TOKEN)
  pages_result = notion.search(**full_query).get("results")

  return pages_result

  

# How to import a notion database model?
# How to make migrations if the notion model changes?


class NotionPage(Page,BaseModel):
  # title_text: str = ComputedField(lambda self: self.properties.get('title').title[0].plain_text)
  
  @computed_field
  @property 
  def title_text(self)->str:
    try: return self.properties.get('title').title[0].plain_text
    except: pass
     
  
def notion_pages_tuple(NOTION_TOKEN):
  notion_pages = search_notion(NOTION_TOKEN)
  pages = [NotionPage.parse_obj(page) for page in notion_pages]
#   pages_result = [page.dict(include={'id','url','title_text'}) for page in pages]

  return [(str(page.id),page.title_text) for page in pages if page.title_text]

