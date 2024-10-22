from ..repositories.user import UserRepository
from ..dto.user import UserResponce

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_info_by_id(self, id: int) -> UserResponce:
        user = self.user_repository.get_user_by_id(id)
        return UserResponce.model_validate(user)