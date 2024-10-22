from sqlalchemy.ext.asyncio import AsyncSession
from ..orm.users import UserModel
class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    # def 