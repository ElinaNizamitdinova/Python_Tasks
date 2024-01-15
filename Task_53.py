def find_name():
    print("ввдедите фио")
    print(contact[input()])


def delete():
    print("введите ФИО удаляемого контакта")
    del contact[input()]


def change_name():
    print("введите фио изменяемого контакта и новое имя")
    name1,name2=input().split()
    contact[name2] = contact.pop(name1)


def append_name():
    print("введите фио")
    name=input()
    s=[]
    print("введите телефон")
    s.append(input())
    print("введите коментарий")
    s.append(input())
    contact[name]=s


def print_Menu():
    print("menu:")
    print("Нажмите 1 для получения контакта")
    print("Нажмите 2 для удаления контакта")
    print("Нажмите 3 для изменения контакта")
    print("Нажмите 4 для добавления контакта")
    print("Нажмите 5 для вывода всех контактов")
    print("Нажмите 0 для завершения программы")
   
    





contact =dict()
with open("contacts.txt", 'r+') as contacts:
    A=contacts.readline().split()
    while A:
        contact[A[0]]=A[1:]
        A=contacts.readline().split()
print_Menu()
Menu=[1,2,3,4,5,0]
a=int(input())
#print(contact)
while not (a in Menu):
    print_Menu()
    a=int(input())
while a:
    if a==1:
        find_name()
    elif a==2:
        delete()
    elif a==3:
        change_name()
    elif a==4:
        append_name()
    elif a==5:
        print(contact)      
    
    print_Menu()
    a=int(input())
    
contacts.close()
contacts=open('input.txt','w')
    
for key,value in contact.items():
    print(key,value)
    contacts.write(str(key)+' ')
    contacts.write(str(value[0])+' ')
    contacts.write(str(value[1])+' ')
    contacts.write('\n')