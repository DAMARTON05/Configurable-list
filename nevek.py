
import random

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

runn = int(input("\033[1;32mHow many names will be there max?  "))
print("Then, you can write maximum", runn, "names.\033[1;37m")

x = input("\033[1;34mName: \033[1;37m")
nevek1.append(x.title())

while exit != True and runn >= len(nevek1):
    x = input("\033[1;34mNext name or exit: \033[1;37m")
    nevek1.append(x.title())
    if 'Exit' in nevek1:
        nevek1.remove("Exit")
        answer = input("\033[1;31mNo other names wanted(true/false): \033[1;37m")
        if answer.lower() == "true":
            exit = True
        elif answer.lower() == "false":
            print("\033[1;31m\033[1;4mEXIT\033[0m isn't compatible with this list.")
        else:
            print("\033[1;31mYou typed something wrong.\033[1;37m")

passing = False

while passing == False:
    check = input("\033[1;35mDo you want to check your list(yes/no)? \033[1;37m")
    if check.lower() == "yes":
        print("\033[1;33mYour list:\033[1;37m", nevek1)
        check2 = input("Everything's all right(yes/no)? ")
        if check2.lower() == "yes":
            passing = True
            print("That's good.")
        elif check2.lower() == "no":
            passing = True
            command = ""
            while command.lower() != 'done':
                command = input("What kind of changes do you want?(type HELP for the commands.) ")
                if command.lower() == 'help':
                    print("remove - remove an element from the list.\ninsert - place a new element in the list\nsort - sort the line alphabetically\ndone - done with changes")
                elif command.lower() == 'remove':
                    quantity = input("How many parts you want to remove? ")
                    for x in range(int(quantity)):
                        what = input("What do you want to remove? ")
                        nevek1.remove(what.title())
                elif command.lower() == 'insert':
                    quantity = input("How many things you want to insert? ")
                    for x in range(int(quantity)):
                        where = input("Where do you want to insert? ")
                        what = input("What do you want to insert? ")
                        where -= 1
                        nevek1.insert(int(where), what)
                elif command.lower() == 'sort':
                    nevek1.sort()
                elif command.lower() == 'done':
                    print("No other changes will be made.")
                else:
                    print("You mistyped something.")
        else:
            print("You mistyped something.")
    elif check.lower() == "no":
        passing = True
        print("Passing without checking...")
    else:
        print("You typed something wrong.")


