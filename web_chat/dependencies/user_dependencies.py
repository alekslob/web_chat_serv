from ..services.user import UserService
from ..repositories.user import UserRepository
from .user_repository_dependencies import extract_user_repository


def extract_user_services(
        user_repository: UserRepository = extract_user_repository()
)-> UserService:
    return UserService(
        user_repository=user_repository
    )