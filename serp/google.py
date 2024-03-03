from utils.utils import prepare_config
from serp.google_base import GoogleBase
from serp.serp import SerpClient, SerpClientAsync
from typing import Optional, Dict, Any

class Google(GoogleBase):
    def __init__(self, client):
        if not isinstance(client, SerpClient):
            raise TypeError("Google requires a SerpClient instance")
        self.client = client

    def scrape_google_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Google search results for a given query.

        Args:

            query (str): The search query.
            opts (GoogleSearchOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "None",
                    "callback_url": None,
                    "parse": False,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self.prepare_search_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_url(
        self, url: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Google search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (GoogleUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "geo_location": None,
                    "parse": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self.prepare_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_ads(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Google Ads search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleAdsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "None",
                    "callback_url": None,
                    "parse": None,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_ads_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_suggestions(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Google suggestions for a given query.

        Args:
            query (str): The search query.
            opts (GoogleSuggestionsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "locale": None,
                    "geo_location": None,
                    "user_agent_type": "desktop",
                    "render": "html",
                    "callback_url": None,
                    "parse": False,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self.prepare_suggestions_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_hotels(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Google Hotels search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleHotelsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "html",
                    "callback_url": None,
                    "parse": False,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_hotels_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_travel_hotels(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Google Travel Hotels search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleTravelHotelsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": None,
                    "start_page": None,
                    "locale": None,
                    "geo_location": None,
                    "user_agent_type": "desktop",
                    "render": "html",
                    "callback_url": None,
                    "parse": False,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_travel_hotels_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_images(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Google Images search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleImagesOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": None,
                    "callback_url": None,
                    "parse": False,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_images_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_trends_explore(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Google Trends Explore results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleTrendsExploreOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": "desktop",
                    "geo_location": None,
                    "callback_url": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_trends_explore_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

class GoogleAsync(GoogleBase):
    def __init__(self, client):
        if not isinstance(client, SerpClientAsync):
            raise TypeError("GoogleAsync requires a SerpClientAsync instance")
        self.client = client

    async def scrape_google_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Google search results for a given query.

        Args:

            query (str): The search query.
            opts (GoogleSearchOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "None",
                    "callback_url": None,
                    "parse": False,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self.prepare_search_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_url(
        self, url: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Google search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (GoogleUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "geo_location": None,
                    "parse": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self.prepare_url_payload(url, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_ads(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Google Ads search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleAdsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "None",
                    "callback_url": None,
                    "parse": None,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_ads_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_suggestions(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Google suggestions for a given query.

        Args:
            query (str): The search query.
            opts (GoogleSuggestionsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "locale": None,
                    "geo_location": None,
                    "user_agent_type": "desktop",
                    "render": "html",
                    "callback_url": None,
                    "parse": False,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self.prepare_suggestions_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_hotels(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Google Hotels search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleHotelsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "html",
                    "callback_url": None,
                    "parse": False,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_hotels_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_travel_hotels(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Google Travel Hotels search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleTravelHotelsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": None,
                    "start_page": None,
                    "locale": None,
                    "geo_location": None,
                    "user_agent_type": "desktop",
                    "render": "html",
                    "callback_url": None,
                    "parse": False,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_travel_hotels_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_images(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Google Images search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleImagesOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": None,
                    "callback_url": None,
                    "parse": False,
                    "context": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_images_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_trends_explore(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Google Trends Explore results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleTrendsExploreOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": "desktop",
                    "geo_location": None,
                    "callback_url": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_trends_explore_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response
