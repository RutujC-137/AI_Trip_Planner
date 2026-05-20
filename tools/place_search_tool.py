import os 
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List 
from langchain.tools import tool
from dotenv import load_dotenv 

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()
    
    def _setup_tools(self)-> List:
        """"Setup all tools for the place search tool"""
        @tool
        def search_attractions(place: str)-> dict:
            """Search attraction of a place"""
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by google: {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}"
            
        
        @tool
        def search_restaurants(place: str)-> dict:
            """Search restaurants of a place"""
            try:
                restaurants_result = self.google_places_search.google_search_restaurants(place)
                if restaurants_result:
                    return f"following are the restaurants of {place} as suggested by google:{restaurants_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}"

        @tool
        def search_activities(place:str)-> str:
            """Search acitivites of a place"""
            try:
                restaurants_results = self.google_places_search.google_search_activity(place)
                if restaurants_results:
                    return f"Following are the activities in and around {place} as suggested by google:{restaurants_results}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_acitivity(place)
                return f"Google cannot find the details due to {e}. \n following are the activities of {place} "
            
        @tool
        def search_transportation(place: str)-> str:
            """Search transportation of a place """
            try:
                restaurants_result = self.google_places_search.google_search_transportation(place)
                if restaurants_result:
                    return f"Following are the modes of transportation available in {place} as suggested by google:{restaurants_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the modes of transportation available in {place}"

        return [search_attractions, search_restaurants, search_activities, search_transportation ]

