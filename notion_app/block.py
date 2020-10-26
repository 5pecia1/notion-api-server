
from notion.markdown import plaintext_to_notion, notion_to_plaintext
from notion.maps import property_map
from notion.block import TextBlock as TB

class TextBlock(TB):
    title_plaintext = property_map(
        "title",
        python_to_api=plaintext_to_notion,
        api_to_python=notion_to_plaintext,
        markdown=True,
    )