from typing import Any

from fastapi import APIRouter

from api.deps import CurrentUser
from model.user import UserPublic

router = APIRouter()

@router.post("/login/access-token")
async def login_access_token():
    return {"message": "Login Access Token"}

@router.post("/login/test-token", response_model=UserPublic)
def test_token(current_user: CurrentUser) -> Any:
    """
    Test access token
    """
    return current_user
