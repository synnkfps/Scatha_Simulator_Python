import random
import time

ANSI_RESET  = '\33[0m'
ANSI_RED    = '\33[31m'
ANSI_YELLOW = '\33[33m'
ANSI_BLUE   = '\33[34m'
ANSI_PURPLE = '\33[35m'
ANSI_CYAN   = '\033[36m'
ANSI_WHITE  = '\33[37m'

def main():
    magic_find = 0
    pet_luck = 0
    looting = 0
    number_pets = 0
    delay_kills = 0

    formatterDecimal = lambda x: f'{int(x):.5f}'

    print("Hellow ! Welcome to the hell of Scatha farming !")
    print("Here, you can just try your luck to see if you are lucky today to obtain your Scatha !")

    # todo: system args acceptance
    try:
        magic_find = int(input("Please enter your actual magic find (take in account the magic find gain with bestiary): "))
        pet_luck = int(input("Now, enter your actual pet luck: "))
        looting = int(input("Enter your level of looting of your weapon (0-5): "))
        number_pets = int(input("Enter the number of pets drops you want to simulate: "))
        delay_kills = float(input("Finally, Enter the delay between worm kills [in milliseconds] (0 = Instant results | 100 = Recommended)): "))
    except:
        print(f'Error occurred, please enter only integers. (and float on kills delay)')

    scathaRareBaseDrop = 0.24
    scathaEpicBaseDrop = 0.12
    scathaLegBaseDrop = 0.04

    luckCalc = (magic_find+pet_luck)/100


    newBaseDropRareWithoutLooting = scathaRareBaseDrop*(1+(luckCalc))
    newBaseDropEpicWithoutLooting = scathaEpicBaseDrop*(1+(luckCalc))
    newBaseDropLegWithoutLooting = scathaLegBaseDrop*(1+(luckCalc))

    lootingPercentage = looting/100

    newBaseDropRare = newBaseDropRareWithoutLooting+(lootingPercentage*newBaseDropRareWithoutLooting)
    newBaseDropEpic = newBaseDropEpicWithoutLooting+(lootingPercentage*newBaseDropEpicWithoutLooting)
    newBaseDropLeg = newBaseDropLegWithoutLooting+(lootingPercentage*newBaseDropLegWithoutLooting)

    luckyNumberRare = (100/newBaseDropRare)
    luckyNumberEpic = (100/newBaseDropEpic)
    luckyNumberLeg = (100/newBaseDropLeg)

    print("\nYou have 1/" + str(luckyNumberRare) + " for dropping a Rare Scatha. (" + formatterDecimal(newBaseDropRare) + "%)")
    print("You have 1/" + str(luckyNumberEpic) + " for dropping a Epic Scatha. (" + formatterDecimal(newBaseDropEpic) + "%)")
    print("You have 1/" + str(luckyNumberLeg) + " for dropping a Legendary Scatha. (" + formatterDecimal(newBaseDropLeg) + "%)\n")

    time.sleep(0.5)

    nbOfScathaKills = 0
    nbOfWormsKills = 0
    nbOfScathaKillsTotal = 0
    nbOfWormsKillsTotal = 0

    randInt = 0
    randWorms = 0
    nbPetRare = 0
    nbPetEpic = 0
    nbPetLeg = 0

    nbOfPetAchieved = False 

    while not nbOfPetAchieved:
        while (randInt%luckyNumberLeg != 0 and randInt%luckyNumberEpic != 0 and randInt%luckyNumberRare != 0) and nbOfScathaKills == 0:
            randWorms = random.randrange(5)+1
            time.sleep(delay_kills/1000)

            if randWorms >= 1 and randWorms <= 4:
                nbOfWormsKills += 1
                print("You killed " + ANSI_WHITE + nbOfWormsKills + ANSI_RESET + f" Worm{'s' if nbOfWormsKills==1 else''} !")
            
            elif randWorms == 5:
                randInt = random.randrange((luckyNumberLeg*luckyNumberEpic*luckyNumberRare)+1)
                nbOfScathaKills += 1
                print("You killed " + ANSI_WHITE + nbOfScathaKills + ANSI_RESET + f" Worm{'s' if nbOfScathaKills==1 else''} !")
        
        if delay_kills > 0:
            time.sleep(500/1000)

        if randInt%luckyNumberLeg == 0:
            nbPetLeg += 1
            magic_find = str(magic_find)
            print("\n" + ANSI_YELLOW + "PET DROP! " + ANSI_YELLOW + "Scatha " + ANSI_CYAN + "(" + magic_find + "% ★ Magic Find)\n" + ANSI_RESET)
            magic_find = int(magic_find)
        elif randInt%luckyNumberEpic == 0:
            nbPetEpic += 1
            magic_find = str(magic_find)
            print("\n" + ANSI_YELLOW + "PET DROP! " + ANSI_PURPLE + "Scatha " + ANSI_CYAN + "(" + magic_find + "% ★ Magic Find)\n" + ANSI_RESET)
            magic_find = int(magic_find)
        elif randInt%luckyNumberRare == 0:
            nbPetRare += 1
            magic_find = str(magic_find)
            print("\n" + ANSI_YELLOW + "PET DROP! " + ANSI_BLUE + "Scatha " + ANSI_CYAN + "(" + magic_find + "% ★ Magic Find)\n" + ANSI_RESET)
            magic_find = int(magic_find)
        
        percentageScatha = nbOfScathaKills/(nbOfScathaKills+nbOfWormsKills)

        print("Number of Worms killed: " + nbOfWormsKills)
        print("Number of Scathas killed: " + nbOfScathaKills)
        print("Percentage of Scathas: " + "{:.2f}".format(percentageScatha*100))

        randInt = 0

        nbOfScathaKillsTotal += nbOfScathaKills
        nbOfWormsKillsTotal += nbOfWormsKills
			
		# The number of pets drops you want to simulate.
        nbOfPetAchieved = (nbPetRare+nbPetEpic+nbPetLeg) >= number_pets

        nbOfScathaKills = 0
        nbOfWormsKills = 0
    
    if (nbPetRare+nbPetEpic+nbPetLeg) > 1:
        percentageScathaTotal = nbOfScathaKillsTotal/(nbOfScathaKillsTotal+nbOfWormsKillsTotal)

        print("\nNumber of Worms total killed: " + nbOfWormsKillsTotal)
        print("Number of Scathas total killed: " + nbOfScathaKillsTotal)
        print("Percentage of Scathas total: " + "{:.2f}".format(percentageScathaTotal*100) + "%")
        print("\nNumber of Legendary Scatha Pet: " + nbPetLeg);
        print("Number of Epic Scatha Pet: " + nbPetEpic);
        print("Number of Rare Scatha Pet: " + nbPetRare);
        print("Number of total Scatha Pet: " + (nbPetRare+nbPetEpic+nbPetLeg))

main()
input('Type anything then press enter to close.') # prevent closing
