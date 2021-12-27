import requests
import webbrowser

boucle = 0
while boucle == 0:
    while True:
        print("\n")
        adresse = input('Veuillez saisir le numéro et le nom de la rue recherchés : ')
        try:
            int(adresse[0])
            break
        except:
            print(" /!\ Remplir ce champ, en commençant par un numéro d'adresse /!\ ")

    while True:
        while True:
            try:
                print("\n")
                limite = int(input("Saisir le nombre de villes maximum recherchées : "))
                break
            except:
                print(" /!\ Saisir un nombre ou un chiffre : /!\ ")
            
        if limite <= 0 or limite > 36000:
            print(" /!\ Entrer une valeur entre 0 et 36 000 : /!\ ")
        else:
            break
    
    parametre = {'q' : adresse, 'limit': limite}
    r = requests.get("https://api-adresse.data.gouv.fr/search/", params = parametre)
    r = r.json()

    entier = len(r["features"])
    print("\n----------------------------------------")
    print("Recherche terminé, il y a %s résultats : " %(entier))
    print("----------------------------------------\n")

    encore = 1

    incrementation = 10
    debut = 0
    mettrefin = 0
    liste = []

    if debut + incrementation >= entier:
        fin = entier
        mettrefin = 1
    else:
        fin = incrementation
    
    while encore == 1:
        for x in range(debut, fin):
            print(r["features"][x]["properties"]["label"])
            liste.append(r["features"][x]["properties"]["label"])

        if mettrefin == 0:
            while True:
                print("\n--------------------------------------")
                plusRes = input("Voulez-vous plus de résultat (y/n) : ")
                print("--------------------------------------")
                if plusRes == 'y' or plusRes == 'n':
                    break
                else:
                    print('Entrer y ou n')
        else:
            encore = 0
            break

        if plusRes == "n":
            encore = 0
        else:
            debut = debut + incrementation
            fin = debut + incrementation

            if fin >= entier:
                fin = entier
                mettrefin = 1

    while True:
        if entier != 0: 
            print("\n---------------------------------------------")
            message1 = input('Voulez-vous ouvrir sur Google map ? (y/n) : ')
            print("---------------------------------------------\n")
            if message1 == 'y' or message1 == 'n':
                break
            else:
                print('Entrer y ou n')
        else : 
            break
        
    if message1 == 'y':
        
        while True:
            while True:
                try:
                    print("Adresse(s) visualisable sur Google Maps : \n")
                    index = 1
                    for y in liste:
                        print("[" + str(index) + "] - " + y + ".")
                        index += 1
                    valeur = int(input("\nSélectionnez l'index de l'adresse que vous désirez visualiser via Google Maps : "))
                    break
                except:
                    print(" /!\ Merci de saisir un chiffre /!\ ")
                    print("\n")
            if valeur - 1 <= -1 or valeur - 1 > entier:
                print(" /!\ Entrer un valeur entre 1 et %s /!\ " %(entier))
                print("\n")
            else:
                break

        x = r["features"][valeur - 1]["geometry"]["coordinates"][0]
        y = r["features"][valeur - 1]["geometry"]["coordinates"][1]

        adresseMap = "www.google.com/maps/@"+str(y)+","+str(x)+",20z"
        adresseHTML = adresseMap

        webbrowser.open(adresseHTML)

    while True:
        print("\n--------------------------------------------------")
        message = input('Voulez-vous chercher une autre adresse ? (y/n) : ')
        print("--------------------------------------------------\n")
        if message == 'y' or message == 'n':
            break
        else:
            print('Entrer y ou n : ')

    if message == "n":
        print("--------------------------------------")
        print("Merci d'avoir utilisé notre programme.")
        print("--------------------------------------\n")
        boucle = 1
