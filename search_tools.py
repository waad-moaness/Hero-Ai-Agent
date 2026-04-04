from typing import List, Any

class SearchTool:
    def __init__(self, index):
        self.index = index

    def search(self, query: str) -> List[Any]:
        """
        You are an expert Hugging Face MLOps assistant.
        Perform a semantic search on the Hugging Face Hub documentation index to find guides, tutorials, and deployment steps.

        Args:
            query (str): The search query string.

        Returns:
            List[Any]: A list of up to 5 relevant documentation chunks from the Hugging Face Hub.

        - Use this tool whenever the user asks about Hugging Face, Spaces, deploying models, managing datasets, or the Hub API.
        - ALWAYS pass a single string argument: `query`
        - Optimize your query by extracting the core technical keywords.
        - NEVER pass multiple fields
        - NEVER invent parameters

        Example:
        User: How do I securely add my API key to a Hugging Face Space?
        Tool call: search(query="add secrets environment variables Spaces")
        """
        return self.index.search(query, num_results=3)