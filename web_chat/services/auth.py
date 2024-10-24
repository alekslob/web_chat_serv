from ..exceptions import UserAlreadyExists, PasswordError, UserNotFoundException
from ..dto.auth import AuthSchema, AuthResponse
from ..orm.users import UserModel

from ..repositories.user import UserRepository

from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

class AuthServices:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def _create_access_token(self, identity: str) -> str:
        return create_access_token(identity=identity, fresh=True)

    def _create_refresh_token(self, identity: str) -> str:
        return create_refresh_token(identity=identity)

    def _build_auth_response(self, access_token_identity: str, refresh_token_identity: str ) -> AuthResponse:
        return AuthResponse(
            token = self._create_access_token(identity=access_token_identity),
            refresh_token=create_refresh_token(identity=refresh_token_identity)
        )

    def auth(self, authschema: AuthSchema) -> AuthResponse:
        if self.user_repository.get_user_by_name(authschema.username):
            raise UserAlreadyExists('Пользователь с таким именем уже существует!')
        user = self.user_repository.add_user(
            UserModel(
                username=authschema.username,
                hash_password=generate_password_hash(authschema.password)
            )
        )
        return self._build_auth_response(access_token_identity=user.id, refresh_token_identity=user.id)
    
    def login(self, authschema: AuthSchema) -> AuthResponse:
        user = self.user_repository.get_user_by_name(authschema.username)
        if not user:
            raise UserNotFoundException(f'Пользовтель {authschema.username} не найден!')
        if not check_password_hash(user.hash_password, authschema.password):
            raise PasswordError('Неверный пароль!')
        return self._build_auth_response(access_token_identity=user.id, refresh_token_identity=user.id)

    def check_token(self, user_id: int) -> AuthResponse:
        #
        return self._build_auth_response(access_token_identity=user_id, refresh_token_identity=user_id)