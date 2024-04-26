from pydantic import BaseModel
from typing import Optional, List
from .user import UserViewSchema
from .hike import HikeViewSchema

class FavoriteSchema(BaseModel):
    """ Define how a new favorite to be inserted should be represented """
    user_id: int = 1
    hike_id: int = 1


class FavoriteViewSchema(BaseModel):
    """ Define how a favorite will be returned: user_id + hike_id + hike details. """
    user_id: int = 1
    # hike_id: int = 1

class FavoriteListSchema(BaseModel):
    """ Define how a list of favorites will be returned. """
    favorites: List[FavoriteViewSchema]

class FavoriteDelSchema(BaseModel):
    """ Define how the data returned after a delete request should be structured. """
    message: str
    user_id: int
    hike_id: int