from sqlalchemy.orm import Session
from ..repositories.user import UserRepository
from ..orm import session_context

def extract_user_repository(
) -> UserRepository:
    with session_context() as session:
        return UserRepository(
            session=session
        )