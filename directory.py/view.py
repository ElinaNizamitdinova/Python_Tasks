import text
import model


def main_menu()->int:
    for n,item in enumerate(text.main_menu):
        if n==0:
            print(item)
        else:
            print(f"\t{n}.{item}")
    while True:
        choice=input(text.main_menu_choice)
        if choice.isdigit() and 0< int(choice)< len(text.main_menu):
            return int(choice)
        else:
            print(f"Введите пункт меню от 1 до {len(text.main_menu-1)}")


def show_contact(p_book: model.PhoneBook ,error_messege:str):
    max_size=p_book.max_len()

    if p_book:
        print("\n"+"="*(sum(max_size)+7))
        for n, contact in p_book.items():
            print(f"{n:>3}.{contact[0]:< {max_size[0]+1}} {contact[1]:< {max_size[1]+1}} {contact[2]:< {max_size[2]+1}}")
        print((sum(max_size)+7)+"\n")
    else:
        print_messege(error_messege)

def print_messege(messege: str):
    print("\n"+"="*len(messege))
    print(messege)
    print("="*len(messege)+"\n")


def add_contact(messege:list[str],contact:list[str]= None):
    contact = contact if contact else ["","",""]
    for n,mes in enumerate(messege):
        field=input(mes)
        contact[n] = field if field else contact[n]
    return contact


def input_data(messege: str) -> str:
    return input(messege)




