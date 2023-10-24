import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# Замените этими значениями свой токен и ID группы (или страницы)
token = 'ВАШ_ТОКЕН'
group_id = 'ВАШ_ИД_ГРУППЫ'

# Авторизация бота
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

# Инициализация Long Poll
longpoll = VkLongPoll(vk_session)

# Функция для пересылки сообщения
def forward_message(peer_id, message_id):
    try:
        vk.messages.send(
            peer_id=peer_id,
            forward_messages=message_id
        )
        print(f"Сообщение {message_id} переслано в беседу {peer_id}")
    except Exception as e:
        print(f"Ошибка при пересылке сообщения: {str(e)}")

# Основной цикл бота
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.from_user:
        # Обработка входящего сообщения
        if event.peer_id == group_id:
            continue  # Пропустить сообщения из беседы, в которую бот отправляет сообщения
        forward_message(group_id, event.message_id)  # Пересылка сообщения в беседу
