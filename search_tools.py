from typing import List, Any

class SearchTool:
    def __init__(self, index):
        self.index = index

    def search(self, query: str) -> List[Any]:
        """
        You are a codebase assistant.
        Perform a text-based search on the FAQ index.

        Args:
            query (str): The search query string.

        Returns:
            List[Any]: A list of up to 5 search results returned by the FAQ index.

        - Use the search tool when the user asks about the repository
        - ALWAYS pass a single string argument: `query`
        - NEVER pass multiple fields
        - NEVER invent parameters

        Example:
        User: What are the prerequisites?
        Tool call: search(query="course prerequisites")
        """
        return self.index.search(query, num_results=5)
