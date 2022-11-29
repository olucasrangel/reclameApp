import csv
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def mainMenu():
    clear()
    global escolha
    escolha = input(
        """
========== CRUD Menu ==========


[1] Nova Reclamação
[2] Historico de Reclamações
[3] Editar Reclamação
[4] Deletar Reclamação
[0] Fechar reclameApp\n """
    )
    cursor()


def cursor():
    if escolha == "1":
        return register()
    elif escolha == "2":
        return userinfo()
    elif escolha == "3":
        return editUser()
    elif escolha == "4":
        return deleteUser(), deleteinfo()
    elif escolha == "0":
        print("...")
    else:
        return mainMenu()


def register():
    clear()
    try:
        user = input("Usuário a ser registrado: ")
        company = input("Empresa: ")
        data = open("user.csv", "a")
        data.write(f"{user},{company}\n")
    finally:
        return mainMenu()


def userinfo():
    global user, userDetail
    clear()
    user = input("Qual historico gostaria de visualizar?\n").casefold()
    readUsers = open("report.csv", "r")
    linhas = csv.reader(readUsers, delimiter=",")
    userDetail = {}
    for log in linhas:
        userDetail[log[0]] = log[1:]
    showUserInfo()


def showUserInfo():
    try:
        clear()
        info = print(
            f"Usuário: {user} \nReclamação: {userDetail[user][0]} \nstatus: {userDetail[user][1]}"
        )
        backToMenu = input(f"[0] Para retornar ao menu inicial\n ")
        while not backToMenu == "0":
            showUserInfo()
        else:
            mainMenu()
    except KeyError:
        noUserError = input(
            f"User {user} nao encontrado ou sem informacoes registradas\npressione qualquer botao para voltar ao menu"
        )
        mainMenu()


def checkinfo():
    try:
        readUsers = open("report.csv", "r")
        linhas = csv.reader(readUsers, delimiter=",")
        info = {}
        for j in linhas:
            info[j[0]] = j[:1]
        if str(info[userlogin]) == str(f"['{userlogin}']"):
            editInfo()
    except KeyError:
        addinfo()


def editUser():
    clear()
    global userlogin
    print("Login é necessario para adicionar informacoes ao proprio user!")
    userlogin = input("Usuário: ")
    company = input("Empresa: ")
    userscsv = open("user.csv", "r")
    linhas = csv.reader(userscsv, delimiter=",")
    users = []
    for log in linhas:
        users.append(log)
    logou = False
    for i in users:
        if i[0] == userlogin and i[1] == company:
            logou = True
            if logou:
                checkinfo()
    if not logou:
        print("Usuario nao encontrado,")
        input("Pressione qualquer botão para voltar ao menu inicial.")
        mainMenu()


def editInfo():
    readUsers = open("report.csv", "r")
    linhas = csv.reader(readUsers, delimiter=",")
    userDetail = {}
    for log in linhas:
        userDetail[log[0]] = log[1:]
    clear()
    print(
        f"Usuário: {userlogin} \nReclamação: {userDetail[userlogin][0]} \nstatus: {userDetail[userlogin][1]}"
    )
    reportNew = input("Updated Report: ")
    statusNew = input("Updated Status: ")
    for data in userDetail:
        if data == userlogin:
            update = True
    if update:
        userDetail = f"{userlogin},{reportNew},{statusNew}"
        updatedinfo = []
    with open("report.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row[0] == userlogin:
                updatedinfo.append(row)
        updateinfo(updatedinfo)
    data2 = open("report.csv", "a")
    data2.write(f"{userDetail}\n")
    input("pressione qualquer botao para voltar ao menu")
    mainMenu()


def addinfo():
    lerlog = open("user.csv", "r")
    csvlog = csv.reader(lerlog, delimiter=",")
    users = []
    for log in csvlog:
        users.append(log)
    for i in users:
        if i[0] == userlogin:
            report = input("Qual reclamação gostaria de fazer?")
            status = input(
                "Qual status da reclamação (resolvida/em andamento)"
            )
            data = open("report.csv", "a")
            data.write(f"{i[0]},{report},{status}\n")
            backToMenu = input("[0] para voltar ao menu\n")
            if backToMenu == "0":
                mainMenu()
            else:
                mainMenu()


def deleteUser():
    global duser
    clear()
    updatedlist = []
    with open("user.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        duser = input("Nome do User a ser removido:\n")
        for row in reader:
            if not row[0] == duser:
                updatedlist.append(row)
        print("Usuário Removido com sucesso!")
        updatefile(updatedlist)


def updatefile(updatedlist):
    with open("user.csv", "w", newline="") as csvfile:
        Writer = csv.writer(csvfile)
        Writer.writerows(updatedlist)
    backToMenu = input("[0] para voltar ao menu\n")
    if backToMenu == "0":
        mainMenu()
    else:
        clear()
        updatefile(updatedlist)


def deleteinfo():
    clear()
    updatedinfo = []
    with open("report.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row[0] == duser:
                updatedinfo.append(row)
        updateinfo(updatedinfo)


def updateinfo(updatedinfo):
    with open("report.csv", "w", newline="") as csvinfo:
        Writer = csv.writer(csvinfo)
        Writer.writerows(updatedinfo)


mainMenu()
