from langchain_tavily import TavilySearch
from langchain_google_community import (
    GooglePlacesTool,
    GooglePlacesAPIWrapper
)


class GooglePlaceSearchTool:
    def __init__(self, api_key: str):
        self.api_key = api_key

        if api_key and api_key.strip():
            self.places_wrapper = GooglePlacesAPIWrapper(
                gplaces_api_key=api_key
            )
            self.places_tool = GooglePlacesTool(
                api_wrapper=self.places_wrapper
            )
        else:
            self.places_wrapper = None
            self.places_tool = None

    def google_search_attractions(self, place: str):

        if not self.places_tool:
            raise Exception("Google Places API Key not found")

        return self.places_tool.run(
            f"top attractive places in and around {place}"
        )

    def google_search_restaurants(self, place: str):

        if not self.places_tool:
            raise Exception("Google Places API Key not found")

        return self.places_tool.run(
            f"top restaurants in and around {place}"
        )

    def google_search_activity(self, place: str):

        if not self.places_tool:
            raise Exception("Google Places API Key not found")

        return self.places_tool.run(
            f"activities in and around {place}"
        )

    def google_search_transportation(self, place: str):

        if not self.places_tool:
            raise Exception("Google Places API Key not found")

        return self.places_tool.run(
            f"transportation available in {place}"
        )


class TavilyPlaceSearchTool:

    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str):

        tavily_tool = TavilySearch(
            topic="general",
            include_answer=True
        )

        result = tavily_tool.invoke({
            "query": f"top attractions in {place}"
        })

        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]

        return result

    def tavily_search_restaurants(self, place: str):

        tavily_tool = TavilySearch(
            topic="general",
            include_answer=True
        )

        result = tavily_tool.invoke({
            "query": f"best restaurants in {place}"
        })

        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]

        return result

    def tavily_search_activity(self, place: str):

        tavily_tool = TavilySearch(
            topic="general",
            include_answer=True
        )

        result = tavily_tool.invoke({
            "query": f"activities in {place}"
        })

        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]

        return result

    def tavily_search_transportation(self, place: str):

        tavily_tool = TavilySearch(
            topic="general",
            include_answer=True
        )

        result = tavily_tool.invoke({
            "query": f"transportation in {place}"
        })

        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]

        return result