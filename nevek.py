
import random
import time

"""nevek=["Hegedűs Sándor","Dávid Márton","Bojtos Márk","Harangi Márton Balázs","Orlai Zsombor Botond","Oláh Gergő Csongor","Környei Márk István","Czirják Noel","Balogh Kevin","Vitális Viktor","Li Yuanhao","Karsai Zétény","Hecks Márton","Balázs Dávid","Nagy Trisztán","Markus Ádám","Várkonyi Dorisz","Kárász Zsombor","Németh Arion László","Karlovics Tamás","Dömötör Marcell","Nagy Ádám","Tóvizi Réka" ,"Molnár Gergő Boldizsár","Kölcze Szabolcs","Szűcs Roland Balázs","Szabó Zétény","Nagy Boglárka","Lerch Levente","Takács Luca","Molnar Vimce Béla","Mező Gábor"]
nevek.sort()

nevekSz=[]
lepes=0

for i in range(len(nevek)):
    nevekSz.append(nevek[lepes])
    lepes += 1
    for j in range(5):
        nevekSz.append(random.randint(1,5))
print(nevekSz)"""


nevek1 = []
exit = False

runn = int(input("\033[1;32mHow many names will be there max? "))
print("\033[1;32mThen, you can write maximum", "\033[1;4m\033[1;31m" + str(runn) + "\033[1;0m\033[1;37m", "\033[1;32mnames.\033[1;37m")
runn = int(runn)-1

x = input("\033[1;34mName: \033[1;37m")
nevek1.append(x.title())

while exit != True and int(runn) >= len(nevek1):
    x = input("\033[1;34mNext name or exit: \033[1;37m")
    nevek1.append(x.title())
    if 'Exit' in nevek1:
        nevek1.remove("Exit")
        answer = input("\033[1;31mNo other names wanted(true/false): \033[1;37m")
        if answer.lower() == "true":
            exit = True
        elif answer.lower() == "false":
            runn += 1
            print("\033[1;31m\033[1;4mEXIT\033[0m isn't compatible with this list.")
        else:
            runn += 1
            print("\033[1;31mYou typed something wrong.\033[1;37m")

passing = False

while passing == False:
    check = input("\033[1;35mDo you want to check your list(yes/no)? \033[1;37m")
    if check.lower() == "yes":
        print("\033[1;33mYour list:\033[1;37m", nevek1)
        check2 = input("\033[1;34mEverything's all right(yes/no)? \033[1;37m")
        if check2.lower() == "yes":
            passing = True
            print("\033[1;33mThat's good.\033[1;37m")
        elif check2.lower() == "no":
            passing = True
            command = ""
            while command.lower() != 'done':
                command = input("\033[1;35mWhat kind of changes do you want?(type HELP for the commands.) \033[1;37m")
                if command.lower() == 'help':
                    time.sleep(1)
                    print("\033[1;34mremove - remove an element from the list.\ninsert - place a new element in the list\nsort - sort the line alphabetically\ndone - done with changes\ncheck - check the current list\033[1;37m")
                elif command.lower() == 'check':
                    print(nevek1)
                    time.sleep(1)
                elif command.lower() == 'remove':
                    quantity = input("\033[1;34mHow many parts you want to remove? \033[1;37m")
                    for x in range(int(quantity)):
                        what = input("\033[1;33mWhat do you want to remove? \033[1;37m")
                        nevek1.remove(what.title())
                        time.sleep(1)
                        print("\033[1;33m"+what.title(), "is removed.\033[1;37m")
                        time.sleep(1)
                elif command.lower() == 'insert':
                    quantity = input("\033[1;34mHow many things you want to insert? \033[1;37m")
                    for x in range(int(quantity)):
                        where = int(input("\033[1;33mWhere do you want to insert? \033[1;37m"))
                        what = input("\033[1;33mWhat do you want to insert? \033[1;37m")
                        where -= 1
                        time.sleep(1)
                        nevek1.insert(int(where), what.title())
                        print("\033[1;33m"+what.title(), "is added.\033[1;37m")
                        time.sleep(1)
                elif command.lower() == 'sort':
                    nevek1.sort()
                    time.sleep(1)
                    print("\033[1;34mList is sorted.\033[1;37m")
                elif command.lower() == 'done':
                    print("\033[1;34mNo other changes will be made.\033[1;37m")
                else:
                    print("\033[1;31mYou mistyped something.\033[1;37m")
        else:
            print("\033[1;31mYou mistyped something.\033[1;37m")
    elif check.lower() == "no":
        passing = True
        print("\033[1;33mPassing without checking...\033[1;37m")
    else:
        print("\033[1;31mYou typed something wrong.\033[1;37m")

print("\033[1;31mCounting in progress...\033[1;37m")

aa = 0

while int(aa) != 3:
    aa +=1
    print(str(aa) + '...')
    time.sleep(1)


nevek2=[]
lepes=0

for i in range(len(nevek1)):
    nevek2.append(nevek1[lepes])
    lepes += 1
    for j in range(5):
        nevek2.append(random.randint(1, 5))
print(nevek2)













