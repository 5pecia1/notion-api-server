import os

from dotenv import load_dotenv
from notion.client import NotionClient

load_dotenv()

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2=os.getenv("NOTION_TOKEN"))

# Replace this URL with the URL of the page you want to edit
page = client.get_block(os.getenv("NOTION_DEFAULT_BLOCK"))

print("The old title is:", page)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
page.title = "The title has now changed, and has *live-updated* in the browser!"