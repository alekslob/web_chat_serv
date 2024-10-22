
class WebChatError(Exception):
    '''Базовое исключение'''

class WebChatApiError(WebChatError):
    '''Базовое исключение для реквестов'''
    status_code = 400


class ValidationModelError(WebChatApiError):
    '''Ошибка валидации'''

class UserNotFoundException(WebChatApiError):
    '''Не найден пользователь'''
    
class UserAlreadyExists(WebChatApiError):
    '''Нельзя создать пользователя с такими же данными'''

class PasswordError(WebChatApiError):
    '''Неверный пароль'''