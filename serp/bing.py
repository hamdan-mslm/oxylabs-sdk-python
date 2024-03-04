from serp.bing_base import BingBase
from typing import Optional, Dict, Any
from serp.serp import Serp, SerpAsync
from utils.utils import prepare_config

class Bing(BingBase):
    def __init__(self, client):
        if not isinstance(client, Serp):
            raise TypeError("Bing requires a Serp instance")
        self.client = client

    def scrape_bing_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, 
        timeout: Optional[int] = None
    ) -> Dict[str, Any]:
        
        """
        Scrapes Bing search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": DEFAULT_DOMAIN,
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "locale": None,
                    "geo_location": None,
                    "render": None,
                    "parse": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_search_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response
    
    def scrape_bing_url(
        self, url: str, opts: Optional[Dict[str, Any]] = None, timeout: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Scrapes Bing search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BingUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "callback_url": None,
                    "render": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self.prepare_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response
    
class BingAsync(BingBase):
    def __init__(self, client):
        if not isinstance(client, SerpAsync):
            raise TypeError("BingAsync requires a SerpAsync instance")
        self.client = client

    async def scrape_bing_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: Optional[int] = None, 
        poll_interval: Optional[int] = None
    ) -> Dict[str, Any]:
        
        """
        Asynchronously scrapes Bing search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "locale": None,
                    "geo_location": None,
                    "render": None,
                    "parse": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds between status checks for the asynchronous job. Defaults to 2.

        Returns:
            The response from the server after the job is completed.
        """
        
        config = prepare_config(poll_interval=poll_interval, timeout=timeout)
        payload = self.prepare_search_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response
    
    async def scrape_bing_url(
        self, url: str, opts: Optional[Dict[str, Any]] = None, 
        timeout: Optional[int] = None, poll_interval: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Bing search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BingUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "callback_url": None,
                    "render": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds between status checks for the asynchronous job. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(poll_interval=poll_interval, timeout=timeout)
        payload = self.prepare_url_payload(url, opts)
        response = await self.client.get_resp(payload, config)
        return response
    