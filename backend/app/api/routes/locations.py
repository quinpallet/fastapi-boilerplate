from typing import List
from fastapi import APIRouter, HTTPException

router = APIRouter()

locations = [
    {"id": 1, "name": "本宮3G", "plant_code": "1", "location_code": 1001},
    {"id": 2, "name": "本宮4G", "plant_code": "8", "location_code": 1004}
]


@router.get("/")
async def get_all_locations() -> List[dict]:

    return locations


@router.get("/name/{name}")
async def get_location_by_name(name: str) -> int:
    location = next((x for x in locations if x["name"] == name), None)
    if location is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return location["location_code"]


@router.get("/plant_code/{code}")
async def get_location_by_plant_code(code: str) -> int:
    location = next((x for x in locations if x["plant_code"] == code), None)
    if location is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return location["location_code"]
