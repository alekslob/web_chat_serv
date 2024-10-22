from ..services.auth_services import AuthServices
from ..repositories.user import UserRepository
from .user_repository_dependencies import extract_user_repository

def extract_auth_services(
        user_repository: UserRepository = extract_user_repository()
)-> AuthServices:
    return AuthServices(
        user_repository=user_repository
    )