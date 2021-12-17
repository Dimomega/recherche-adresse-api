import requests
import webbrowser

boucle = 0
while boucle == 0:
    while True:
        adresse = input('Quelle adresse recherchez-vous ? : ')
        try:
            int(adresse[0])
            break
        except:
            print("Remplir ce champ, en commençant par un numéro d'adresse")

    while True:
        while True:
            try:
                limite = int(input("Limite de recherche de ville ? : "))
                break
            except:
                print("Saisir un chiffre : ")
            
        if limite <= 0 or limite > 36000:
            print("Entrer une valeur entre 0 et 36 000 : ")
        else:
            break
    
    parametre = {'q' : adresse, 'limit': limite}
    r = requests.get("https://api-adresse.data.gouv.fr/search/", params = parametre)
    r = r.json()

    entier = len(r["features"])
    print("\n\nRecherche terminé, il y a %s résultats : \n" %(entier))

    encore = 1

    incrementation = 10
    debut = 0
    mettrefin = 0

    if debut + incrementation >= entier:
        fin = entier
        mettrefin = 1
    else:
        fin = incrementation
    
    while encore == 1:
        for x in range(debut, fin):
            print(r["features"][x]["properties"]["label"])

        print("----------------------")
        if mettrefin == 0:
            while True:
                plusRes = input("Voulez-vous plus de résultat (y/n) : ")
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

    print("-------------------------------------")

    while True:
        message1 = input('\n\nVoulez-vous ouvrir sur Google map ? (y/n) : ')
        if message1 == 'y' or message1 == 'n':
            break
        else:
            print('Entrer y ou n')
        
    if message1 == 'y':
        while True:
            while True:
                try:
                    print("\n\nLa légende est la suivante : "+"\n1 : "+ r["features"][0]["properties"]["label"] + " Si vous voulez voir l'adresse de " + r["features"][0]["properties"]["label"] + " taper 1 et ainsi de suite : ")
                    valeur = int(input("\nVoulez-vous ouvrir Google map avec l'adresse (taper le nombre que vous voulez ouvrir) : "))
                    break
                except:
                    print("Merci de saisir un chiffre")
            if valeur - 1 <= -1 or valeur - 1 > entier:
                print("Entrer un valeur entre 1 et %s" %(entier))
            else:
                break

        x = r["features"][valeur - 1]["geometry"]["coordinates"][0]
        y = r["features"][valeur - 1]["geometry"]["coordinates"][1]

        adresseMap = "www.google.com/maps/@"+str(y)+","+str(x)+",20z"
        adresseHTML = adresseMap

        webbrowser.open(adresseHTML)

    print("-------------------------------------")
    while True:
        message = input('\n\nVoulez-vous chercher une autre adresse ? (y/n) : ')
        if message == 'y' or message == 'n':
            break
        else:
            print('Entrer y ou n : ')

    if message == "n":
        print("\nMerci d'avoir utilisé notre programme")
        boucle = 1
