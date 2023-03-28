
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

runn = int(input("Approximately how many names will be written? "))
runn *= 1.5
x = input("\033[1;32mName: \033[1;37m")
nevek1.append(x.title())

for i in range(runn):
    x = input("\033[1;32mNext name or exit: \033[1;37m")
    nevek1.append(x.title())
    if 'Exit' in nevek1:
        nevek1.remove("Exit")
        answer = input("\033[1;31mNo other names wanted(true/false): \033[1;37m")
        if answer.lower() == "true":
            break
        elif answer.lower() == "false":
            print("\033[1;31m\033[1;4mEXIT\033[0m isn't compatible with this list.")
        else:
            print("\033[1;31mYou typed something wrong.\033[1;37m")

check = input("\033[1;35mDo you want to check your list(yes/no)? \033[1;37m")
if check.lower() == "yes":
    print("Your list:", nevek1)
    check2 = input("Everything's all right(yes/no)? ")
    if check2.lower() == "yes":
        pass
    elif check2.lower() == "no":
        pass
elif check.lower() == "no":
    print("Passing without checking...")
else:
    print("You typed something wrong.")


