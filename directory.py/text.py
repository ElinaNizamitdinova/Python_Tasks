main_menu=["Главное меню","Открыть файл",
           "Изменить файл","Показать контакт",
           "Создать контакт","Найти контакт",
           "Изменить контакт","Удалить кнтакт",
           "Выход"]



main_menu_choice="Выберите пункт меню"



load_successful="Телефонная книга успешно загружена!"



save_successful="Телефонная книга успешно сохранена!"



empty_phone_book="Телефонная книга пуста или не открыта"



new_contact=["Введите имя:","Введите номер:","Введите комментарий:"]



def new_contact_added_successful(name: str) -> str:
    return f"Контакст{name} успешно добавлен"



input_seash_word="Введите слово для поиска"
def contact_not_found(word:str)->str:
    return f"Контакты содержащие {word} не найдены!"


change_contact = ["Введите новое имя или ENTER для того, чтобы оставить без изменений",
                "Введите новый номер или ENTER для того, чтобы оставить без изменений",
                "Введите новый комментарий"]



input_id_change_contact = "Введите ID контакта, который нужно изменить"


def contact_changed_successful(name:str) -> str:
    return f"Контакт {name}успешно изменен"


input_id_delete_contact = "Введите ID контакта, который нужно удалить"

def contact_delete_successful(name:str) -> str:
    return f"Контакт {name} успешно удален"


good_bye="До новых встреч!"