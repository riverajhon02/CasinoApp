from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserResponse
from app.db.database import get_db
from app.api.deps import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserResponse)
def get_me(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return current_user