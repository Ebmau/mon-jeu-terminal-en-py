import random


print("=======================================================")
print("====  Bienvenue mon jeu dans le terminal  ====")
print("=======================================================")

name = input("Entrez le nom de votre héros : ")
pv = 100
attaque = 10
bouclier = 5
print(f"Bonjour héro {name} ! Vous avez {pv} points de vie et {attaque} points d'attaque ! Tu as {bouclier} points de bouclier.")


inventaire = ["potion de soin"]

en_jeu = True

while en_jeu and pv > 0:
    print("\n--- QUE VEUX-TU FAIRE ? ---")
    print("1. Explorer les environs")
    print("2. Ouvrir ton inventaire ")
    print("3. Voir mes stats")
    print("4. Quitter le jeu")
    choix = input("\nTon choix (1-4) : ")


    if choix == "1":
        evenement = random.choice(["monstre", "tresor", "rien"])
        if evenement == "monstre":
               print("Un goblin apparait devant toi !...")
    elif choix == "2":
            print("Tu as ouvert ton inventaire")
    elif choix == "3":
            print("Vois-ci tes stats....")
    elif choix == "4":
            print("Tu quitte le jeu...")
    else:
            print("Erreur, tu dois choisir 1 , 2 , 3 ou 4")
    

