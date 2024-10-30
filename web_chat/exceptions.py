
class WebChatException(Exception):
    '''Базовое исключение'''

class ConfigurationException(WebChatException):
    '''Не заполнен или отстутствует файл конфигурации'''

class WebChatApiException(WebChatException):
    '''Базовое исключение для реквестов'''
    status_code = 400


class ValidationException(WebChatApiException):
    '''Ошибка валидации'''

class UserNotFound(WebChatApiException):
    '''Не найден пользователь'''
    
class UserAlreadyExists(WebChatApiException):
    '''Нельзя создать пользователя с такими же данными'''

class PasswordError(WebChatApiException):
    '''Неверный пароль'''

class TokenException(WebChatApiException):
    '''Ошибка с токеном'''