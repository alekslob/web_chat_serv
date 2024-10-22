from ..exceptions import UserAlreadyExists, PasswordError, UserNotFoundException
from ..dto.auth import AuthSchema, AuthResponse
from ..orm.users import UserModel

from ..repositories.user import UserRepository

from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

class AuthServices:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def auth(self, authschema: AuthSchema) -> AuthResponse:
        if self.user_repository.get_user_by_name(authschema.username):
            raise UserAlreadyExists('Пользователь с таким именем уже существует!')
        user = self.user_repository.add_user(
            UserModel(
                username=authschema.username,
                hash_password=generate_password_hash(authschema.password)
            )
        )
        return AuthResponse(
            token=create_access_token(identity=user.id, fresh=True),
            refresh_token=create_refresh_token(identity=user.id)
            )
    
    def login(self, authschema: AuthSchema) -> AuthResponse:
        user = self.user_repository.get_user_by_name(authschema.username)
        if not user:
            raise UserNotFoundException(f'Пользовтель {authschema.username} не найден!')
        if not check_password_hash(user.hash_password, authschema.password):
            raise PasswordError('Неверный пароль!')
        return AuthResponse(
            token=create_access_token(identity=user.id, fresh=True),
            refresh_token=create_refresh_token(identity=user.id)
            )

    def check_token(self, user_id) -> AuthResponse:
        ...