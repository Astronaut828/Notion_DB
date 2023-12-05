from langchain.document_loaders import NotionDirectoryLoader

# Specify the path to the Notion database dump directory
notion_db_directory = "Notion_DB/Notion_Dump"

# Create a NotionDirectoryLoader instance
loader = NotionDirectoryLoader(notion_db_directory)

# Load data from the Notion database dump
docs = loader.load()

# Process and work with the loaded data as needed
print(docs)