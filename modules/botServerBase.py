'''Упрощение API'''

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.upload import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from modules.user import User

class BotServerBase():
    ''' Базовый класс Бота '''
    def __init__(self, ptoken, group_id):
        self.vk_session = vk_api.VkApi(token = ptoken)
        self.vk_api = self.vk_session.get_api()
        self.vk_upload = VkUpload(self.vk_session)
        self.longpoll = VkBotLongPoll(self.vk_session, group_id)
    
    def run(self):
        '''Основной цикл'''

        print("Сервер запущен")
        for event in self.longpoll.listen():
            try:
                self.all(event)
                if event.type == VkBotEventType.MESSAGE_NEW:
                    self.newMessage(event)
                elif event.type == VkBotEventType.MESSAGE_REPLY:
                    self.replyMessage(event)
                elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
                    self.typingMessage(event)
                elif event.type == VkBotEventType.GROUP_JOIN:
                    self.groupJoin(event)
                elif event.type == VkBotEventType.GROUP_LEAVE:
                    self.groupLeave(event)
            except Exception  as e:
                print(e)

    ######################
    # Обработка сообщений
    ######################

    def newMessage(self,event):
        '''Входящее сообщение (override)'''

        print('\n----------------')
        print('Новое сообщение:')
        print('Для бота от: {0}'.format(event.obj.from_id))

    def replyMessage(self,event):
        '''Отправленное сообщение (override)'''

        print('\n----------------')
        print('Новое сообщение:')
        print('От меня для: {0}'.format(event.obj.peer_id))

    def typingMessage(self,event):
        '''Кто-то пишет (override)'''

        print('\n----------------')
        print('Печатает ', end='')
        print(event.obj.from_id, end=' ')
        print('для ', end='')
        print(event.obj.to_id)

    def groupJoin(self,event):
        '''Кто-то вступил в группу (override)'''

        print('\n----------------')
        print(event.obj.user_id, end=' ')
        print('Вступил в группу!')

    def groupLeave(self,event):
        '''Кто-то вышел из группу (override)'''

        print('\n----------------')
        print(event.obj.user_id, end=' ')
        print('Покинул группу!')

    def all(self,event):
        '''Проявлена любая активность (override)'''
        pass

    ######################
    # Работа с VK
    ######################

    def send_message(self, event, pmessage, pattachment = None):
        '''Отправить сообщение пользователю'''

        self.vk_api.messages.send(user_id=event.obj.from_id, random_id=get_random_id(), message=pmessage, attachment = pattachment)

    def send_message_keyboard(self, event, pmessage, pkeyboard, pattachment=None):
        '''Отправить сообщение пользователю'''
        self.vk_api.messages.send(user_id=event.obj.from_id, random_id=get_random_id(), message=pmessage,
                                  keyboard=pkeyboard, attachment=pattachment)

    def upload_document(self, event, file, title="document", tags=None):
        '''Загрузить документ'''

        doc = self.vk_upload.document_message(file, title, tags, event.obj.peer_id)
        self.send_message(event, title, self.build_attachment(doc))

    def build_attachment(self, uploadObject):
        "Построить выражение вложенного"
        typeObj = uploadObject["type"]
        return "{}{}_{}".format(typeObj, uploadObject[typeObj]["owner_id"], uploadObject[typeObj]["id"])

    def get_user_info(self, event):
        """ Получить информацию о пользователе в данной сессии """
        return User(self.vk_api.users.get(user_ids=event.obj.from_id, fields='sex, bdate, city, country, home_town')[0])

    def keyboardDays(self):
        """ Клавиатура "Дни недели" """
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Понедельник', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Вторник', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Среда', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Четверг', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Пятница', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Суббота', color=VkKeyboardColor.PRIMARY)
        return keyboard

    def keyboardWeek(self):
        """ Клавиатура "Номер недели" """
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Первая', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Вторая', color=VkKeyboardColor.PRIMARY)
        return keyboard
    


