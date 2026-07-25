import random

print("=======================================================")
print("====  Bienvenue dans mon jeu dans le terminal  ====")
print("=======================================================")

name = input("Entrez le nom de votre héros : ")
pv_hero = 100
attaque = 10
bouclier = 5
print(f"Bonjour héros {name} ! Vous avez {pv_hero} points de vie et {attaque} points d'attaque ! Tu as {bouclier} points de bouclier.")

inventaire = ["potion de soin"]

en_jeu = True

while en_jeu and pv_hero > 0:
    print("\n--- QUE VEUX-TU FAIRE ? ---")
    print("1. Explorer les environs")
    print("2. Ouvrir ton inventaire")
    print("3. Voir mes stats")
    print("4. Quitter le jeu")
    choix = input("\nTon choix (1-4) : ")

    if choix == "1":
        evenement = random.choice(["monstre", "tresor", "rien"])
        
        if evenement == "monstre":
            pv_monstre = 50
            attaque_ogre = 12
            print("\nUn ogre apparaît devant toi !...")
            
            while pv_hero > 0 and pv_monstre > 0:
                print("\n--- Que veux-tu faire ? ---") 
                print("1. Attaquer")
                print("2. Fuir")
                action = input("\nQuelle action (1-2) : ")

                if action == "1":
                    # --- TON TOUR ---
                    print("\nTu attaques l'ogre ......")
                    pv_monstre = pv_monstre - attaque 
                    print(f"L'ogre a {pv_monstre} PV")
                    
                    # --- LE TOUR DE L'OGRE ---
                    if pv_monstre > 0:
                        print("L'ogre t'attaque ....")
                        pv_hero = pv_hero + bouclier - attaque_ogre
                        print(f"Tu as {pv_hero} points de vie")
                    else:
                        print("Tu as vaincu l'ogre !")

                elif action == "2": 
                    print("\nTu as fui")
                    break

        elif evenement == "tresor":
            print("\nTu as trouvé une potion de soin !")
            inventaire.append("Potion de soin")
            
        elif evenement == "rien":
            print("\nTu continues à avancer...")

    elif choix == "2":
        print(f"\nTu as ouvert ton inventaire, tu as : {inventaire}")

    elif choix == "3":
        print("\nVoici tes stats....")

    elif choix == "4":
        print("\nTu quittes le jeu...")
        break
        
    else:
        print("\nErreur, tu dois choisir 1 , 2 , 3 ou 4")

# Ce message s'affiche si la boucle s'arrête car les PV tombent à 0
if pv_hero <= 0:
    print("\n☠️ Tes PV sont tombés à zéro... GAME OVER !")
