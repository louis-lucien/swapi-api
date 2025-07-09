import pytest
from app.services import get_all_people_names

@pytest.mark.asyncio
async def test_get_all_people_names():
    result = await get_all_people_names()
    assert result == {"names": ["Luke Skywalker", "Leia Organa", "Han Solo"]}
