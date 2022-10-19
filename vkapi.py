from lib2to3.pgen2 import token
from os import system
from pickle import TRUE
from tokenize import Token
system("pip install vk_api")
import vk_api
import requests
import subprocess
from vk_api.longpoll import VkEventType, VkLongPoll
import vk_api, threading, time


#███████████████████████████████████████████████████████████████████████████████████████████████████
#████████████████████████████████████████╔═════════════════╗████████████████████████████████████████
#████████████████████████████████████████║by BS_NIK_Channel║████████████████████████████████████████
#████████████████████████████████████████╚═════════════════╝████████████████████████████████████████
#███████████████████████████████████████████████████████████████████████████████████████████████████
autor = "by Бот-Мейкеры"




def logo():
    try:
        subprocess.call("clear")  # linux/mac
    except:
        subprocess.call("cls", shell=True)
    print("██╗░░░░░░░██░██░░██░░░░░░░░░███╗░░░░████████░░██░\n░██╗░░░░░██░░██░██░░░░░░░░░██░██╗░░░██╔═══██░░░░░\n░░██╗░░░██░░░████░░░░░░░░░██░█░██╗░░██████░░░░██╗\n░░░██░░██░░░░██░██╗░░░░░░███░░░███░░██░░░░░░░░██║\n░░░░████░░░░░██░░██░░░░░░█░░░░░░░█░░██░░░░░░░░██║\n░░░░╚═════════╝░░░░██████░░░░░░░░╚═══╝░░░░░░░░╚═╝\n░░░░░░░░░░░░░░░░░░░╚════╝░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░by Бот-Мейкеры░░░\n[ VK_API client  ~  v.1.0  ~  The MIT License ]\n[ Dev: BS_NIK_Channel ~ prod. by Бот-Мейкеры® ]")
    


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    logo()
    key = input("Введите код авторизации: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device
  
def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


session = requests.Session()
login, password = '+79###', '###'
vk_session = vk_api.VkApi(
        login,  #login (+79... или ....@gmail.com)
        password,# passwd
        auth_handler=auth_handler, # функция для обработки двухфакторной аутентификации
        captcha_handler=captcha_handler)
       

vk_session.auth(token_only=True)
api = vk_session.get_api()
res = api.users.get()

def authorization():
    vk_session.auth(token_only=True)



def send_message(user_id, message, **kwargs):
    api.messages.send(
        user_id=user_id,
        message=message,
        random_id=0,
        **kwargs
    )


# for event in VkLongPoll(vk_session).listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         text = event.text.lower()
#         user_id = event.user_id
#         print('Текст: ', event.text)

#         if text == "hello":
#             send_message(user_id, "Hello!")
vk_session.auth(token_only=True)


def checkver():

    ver = '90'
    version = requests.post("https://fsystem88.ru/spymer/version.php").json()["version"]
    if int(ver) < int(version):
        new_wer="\nВерсия устарела и нуждается в обновлении!"


def set_user_status():
    i = str(input("Введите новый статус, иначе Exit >>> "))
    if i == "Exit":
     menu()
    else:
     api.status.set(text=i)
    



def wall_get():
    try:
        subprocess.call("clear")  # linux/mac
    except:
        subprocess.call("cls", shell=True)
    logo()
    response = api.wall.get(count=5)
    print("Найдено ",response['count'],"постов\n")
    if response['items'][0]['text'] == "":
          print("\nТекст: Без текста")
    else:
          print("\nТекст:", response['items'][0]['text'],"\n")



    def list(i_stena = 0): 
      try:
        try:
          subprocess.call("clear")  # linux/mac
        except:
          subprocess.call("cls", shell=True)
        logo()
        
        if response['items'][i_stena]['text'] == "":
          print("\nТекст: Без текста")
        else:
          print("\nТекст:", response['items'][i_stena]['text'],"\n")
        
        try:
         print("Файлы: ",response['items'][i_stena]['attachments'][0]['photo']['sizes'][9]['url'],"\n")
        except:
          pass
      except IndexError:
          print("\nОшибка: такого поста нету!")
      i_stena = int(input("\n1) Exit - ДЛЯ ВЫХОДА\nВведите пост >>> "))
      if i_stena == "Exit":
        menu()
      list(i_stena)
        
  
    try:

       ch = input("\n Exit - ДЛЯ ВЫХОДА\nВведите выход/пост >>> ")
       try:
        if ch  == "Exit":
         print(ch,"nax")
         menu()
       
        else:
           print(ch)
           list(int(ch))
       except:
         exit()
    except Exception as err:
        print("Error syka: ",err)
        pass
        
def send_message(user_id, message, **kwargs):
    api.messages.send(
        user_id=user_id,
        message=message,
        random_id=0,
        **kwargs
    )



# def af():
#     chood = "ok"
#    # while chood != "Exit":
#     while TRUE:
#         for event in VkLongPoll(api).listen():
#             if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#                 text = event.text.lower()
#                 print("Новое сообщение:",text)
#                 if text == "hello":
#                     send_message(event.user_id, "Hello!")
# # while chood != "Exit":
        
    





def information():
   logo()
   res = api.users.get()
   print("\nID:",res[0]['id'],"\nИмя:",res[0]['first_name'],"\nФамилия:",res[0]['last_name'])
   try:
       ch = int(input("\n1) Выход >>> "))
       if ch  == 1:
         exit()
   except:
        information()

def message_and_pict_on_the_wall():
   try:
        subprocess.call("clear")  # linux/mac
   except:
        subprocess.call("cls", shell=True)
   logo()     
   upl = vk_api.VkUpload(vk_session)
#  загрузить картинку и разместить ее на стене
   photo = upl.photo_wall([input("(Файл должен находиться в директории этой программы)\nВведите имя изображения и расширением >>>")])
   vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
   api.wall.post(message="Загрузка картинки", attachments=[vk_photo_id])
   try:
       ch = int(input("1) Выход >>> "))
       if ch  == 1:
         exit()
   except:
        pass



def on_reg_menu():
    logo()
    print("██████░░░░░░░░░                ░░░░░░░░░██████\n         Происходит авторизация в VK         \n██████░░░░░░░░░                ░░░░░░░░░██████\n")
    
def menu():
    try:
        subprocess.call("clear")  # linux/mac
    except:
        subprocess.call("cls", shell=True)
    
    logo()
    print("██████░░░░░░░░░                ░░░░░░░░░██████\n    Вы авторизовались как",res[0]['first_name'],res[0]['last_name'],"\n██████░░░░░░░░░                ░░░░░░░░░██████\n")
    print("1) Последняя запись со стены.\n2) Информация.\n3) Создать пост\n4) Изменить статус страницы")
    ch = int(input("Введите номер пункта >>> "))
    if ch  == 1:
     wall_get()
    elif ch  == 2:
     information()
    elif ch  == 3:
     map_or_m_exit()
    #elif ch  == 4:
    #  menu()
    #  pass
    # elif ch  == 5:
    #   af()
    elif ch == 4:
      set_user_status()
     




def map_or_m_exit():
    logo()
    i = int(input("\n1) Создать простой пост с текстом\n2) Создать ост с текстом + картинка\n3) Выход\nВведите номер пункта >>> "))
    if i == 1:
        message_on_the_wall()
    if i == 2:
        message_and_pict_on_the_wall()
    elif i == 3:
        menu()

def message_on_the_wall():
    logo()
    print("Ebat")
    i = input("Введите текст, иначе пропишите Exit для выхода >>> ")
    if i == "Exit":# or i == 1:
        menu()
    else:
        try:
           api.wall.post(message= i )
           cp0 = str(input("Успешно отправлено! Отправить ещё?"))
           if cp0 == "Да":
            message_on_the_wall()
           else:
            menu()
        except:
            pass


        

on_reg_menu()










try:
    try:
        subprocess.call("clear")  # linux/mac
    except:
        subprocess.call("cls", shell=True)
    
    vk_session.auth(token_only=True)
    api = vk_session.get_api()
    res = api.users.get()

    menu()
   # print("Вы авторизовались как",res[0]['first_name'],res[0]['last_name'])
except vk_api.AuthError as error_msg:
    print("Errror: ",error_msg)




# code = '18dczc1337a63427fa'
# redirect_url = 'http://example.com'
# app = 000000
# secret = 'dGbpoJdqNuMlGDECgO9I'

# vk_session = vk_api.VkApi(app_id=app, client_secret=secret)

# try:
#         vk_session.code_auth(code, redirect_url)
# except vk_api.AuthError as error_msg:
#         print(error_msg)
        

# print(vk_session.token['user_id'])
# print(vk_session.token['access_token'])
