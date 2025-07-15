import httpx

BASE_URL = "https://swapi.dev/api/people/"

async def get_all_people_names():
    names = []
    url = BASE_URL

    async with httpx.AsyncClient(verify=False) as client:
        while url:
            try:
                response = await client.get(url, timeout=10.0)
                response.raise_for_status()
                data = response.json()
            except httpx.HTTPError as exc:
                raise Exception(f"Erreur lors de l'appel à SWAPI: {exc}")

            page_names = [person["name"] for person in data.get("results", [])]
            names.extend(page_names)

            url = data.get("next")

    return {"names": names}
