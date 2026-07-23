import random


print("=======================================================")
print("====  Bienvenue mon jeu dans le terminal  ====")
print("=======================================================")

name = input("Entrez le nom de votre héros : ")
pv_hero = 100
attaque = 10
bouclier = 5
print(f"Bonjour héro {name} ! Vous avez {pv_hero} points de vie et {attaque} points d'attaque ! Tu as {bouclier} points de bouclier.")


inventaire = ["potion de soin"]

en_jeu = True

while en_jeu and pv_hero > 0:
    print("\n--- QUE VEUX-TU FAIRE ? ---")
    print("1. Explorer les environs")
    print("2. Ouvrir ton inventaire ")
    print("3. Voir mes stats")
    print("4. Quitter le jeu")
    choix = input("\nTon choix (1-4) : ")


    if choix == "1":
        evenement = random.choice(["monstre", "tresor", "rien"])
        if evenement == "monstre":
               pv_monstre = 50
               attaque_orgre = 12
               print("Un orgre apparait devant toi !...")
               while pv_hero > 0 and pv_monstre > 0:
                      print("\n--- Que veux tu faire ? ---") 
                      print("1. Attaquer")
                      print("2.Fuir")
                      action = input("\nQuel action (1-2) : ")
                      if action == "1":
                             print("Tu attaque l'orgre ......")
                             pv_monstre = pv_monstre - attaque
                             print(f"\n L'orgre as {pv_monstre}")
                      if action == "2":
                             print("L'orgre t'attaque ....")
                             pv_hero = pv_hero + bouclier - attaque_orgre
                             print(f" Tu as {pv_hero} point de vie")


                      if action == "2":
                             print("Tu as fuir")
                             break

        elif evenement == "tresor":
               print("Tu as trouver une potion de soin")
               inventaire.append("Potion de soin")
        elif evenement == "rien":
               print("Tu continu à avancé...")

    elif choix == "2":
            print(f"Tu as ouvert ton inventaire tu as {inventaire}.")

    elif choix == "3":
            print("Vois-ci tes stats....")

    elif choix == "4":
            print("Tu quitte le jeu...")
            break
    else:
            print("Erreur, tu dois choisir 1 , 2 , 3 ou 4")
    
