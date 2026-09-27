import httpx

class UrlChecker:
    def __init__(self) -> None:
        self.client = httpx.AsyncClient()

    async def checker(self, url):
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return [response.status_code, url]
        except httpx.HTTPStatusError as err:
            print(f"Error: {err}")
        except httpx.RequestError as err:
            print(f"Error: {err}")
            return None
        
    async def close(self):    
        await self.client.aclose()