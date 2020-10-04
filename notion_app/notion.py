import os

from dotenv import load_dotenv
from notion.client import NotionClient

load_dotenv()

client = NotionClient(token_v2=os.getenv("NOTION_TOKEN"))

def slugify(field: str) -> str:
    f = field.replace(" ", "_")
    return f.lower()