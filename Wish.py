import time
import random


item = {"5star": 0, "4star" : 0, "3star" : 0}
item2 = {"Venti" : 0,"Hu Tao" : 0,"Xiao" : 0,"Ganyu" : 0,"Albedo" : 0,"Zhongli" : 0, "Diluc" : 0, "Jean" : 0, "Keqing" : 0, "Mona" : 0, "Qiqi" : 0, "Tartaglia" : 0,                          "Yanfei" : 0, "Rosaria" : 0, "Beidou" : 0,"Diona" : 0,"Fischl" : 0,"Xingqiu" : 0,"Ningguang" : 0,"Xinyan" : 0, "Bennett" : 0, "Chongyun" : 0, "Noelle" : 0, "Barbara" : 0, "Sucrose" : 0, "Razor" : 0, "Xiangling" : 0, "Amber" : 0}
featured = {"title" : "", "5star" : "Venti",                                   "4star1" : "Sucrose", "4star2" : "Razor", "4star3" : "Noelle"}
data = {"pity5" : 0, "pity4" : 0, "guarantee5" : False, "guarantee4" : False, "primos" : 0, "money": 0, "spent" : 0}
result = {"item" : 0, "star" : 0, "droptype" : 0, "1" : "-", "2" : "-", "3" : "-", "4" : "-", "5" : "-", "6" : "-", "7" : "-", "8" : "-", "9" : "-", "10" : "-"}

def menu_main():
    print("\n" * 200)
    print("==========\nWish! BY NAVEE\nVersion 1.6\n==========\n")
    print("1. View Banner")
    print("2. View Items")
    print("3. Shop")
    print("4. Dev Notes")
    print("\n5. Quit")
    a=input("\n >")

    if a == "1":
        menu_bannerpick()
    elif a == "2":
        menu_items()
    elif a == "3":
        menu_shop()
    elif a == "4":
        menu_notes()
    elif a == "5":
        menu_exit()
    else:
        menu_main()



def menu_banner():
    global data
    print("\n" * 200)
    print("==========\n" + str(featured["title"]) + "\n==========\nFeatured: " + str(featured["5star"]) + "     " + str(featured["4star1"]) + " " + str(featured["4star2"]) + " " + str(featured["4star3"]) + "\n==========\n")
    print("Primos: " + str(data["primos"]))
    print("1. Wish x1  (Primos x160)")
    print("2. Wish x10 (Primos x1600)")
    print("3. Back")
    
    a=input("\n >")
    required = 0
    pull = 0

    
    if a == "1":
        required = 160
        if data["primos"] >= required:
            data["primos"] -= required
            pull = 1
        else:
            print("\n" * 200)
            print("Not enough Primogems!")
            time.sleep(1)
            menu_banner()
    elif a == "2":
        required = 1600
        if data["primos"] >= required:
            data["primos"] -= required
            pull = 10
        else:
            print("\n" * 200)
            print("Not enough Primogems!")
            time.sleep(1)
            menu_banner()
    elif a == "3":
        menu_main()
    else:
        menu_banner()

    while pull > 0:
        print("\n" * 200)
        switch4p = 0
        switch5p = 0
        switch4 = 0
        switch5 = 0
        gacha = random.randint(1,1000)
        result["droptype"] = 0
        data["pity5"] += 1
        data["pity4"] += 1
        data["spent"] += 1

        if data["pity5"] >= 90:
            result["star"] = 5
            gacha = 0
        elif data["pity5"] > 75:
            gacha2 = random.randint(1,10)
            if gacha2 == 1:
                result["star"] = 5
                gacha = 0
        elif data["pity4"] >= 10:
            result["star"] = 4
            gacha = 0

        if gacha != 0:
            if gacha <= 6:
                result["star"] = 5
                result["droptype"] = "Pure Luck Drop"
            elif gacha <= 51:
                result["star"] = 4
                result["droptype"] = "Pure Luck Drop"
            else:
                result["star"] = 3
                result["droptype"] = "Standard Drop"
        else:
            result["droptype"] = "Pity Drop"

        gacha = 0
        gacha = random.randint(1,1000)

        if result["star"] == 5:
            switch5p = True
            item["5star"] += 1
            
            if gacha <= 500 or data["guarantee5"] == True:
                result["item"] = featured["5star"]
                switch5 = False
                
            elif gacha <= 600:
                result["item"] = "Diluc"
                switch5 = True
            elif gacha <= 700:
                result["item"] = "Jean"
                switch5 = True
            elif gacha <= 800:
                result["item"] = "Mona"
                switch5 = True
            elif gacha <= 900:
                result["item"] = "Keqing"
                switch5 = True
            elif gacha <= 1000:
                result["item"] = "Qiqi"
                switch5 = True
                
        elif result["star"] == 4:
            switch4p = True
            item["4star"] += 1
            
            if gacha <= 500 or data["guarantee4"] == True:
                gacha = random.randint(1,3)
                if gacha == 1:
                    result["item"] = featured["4star1"]
                elif gacha == 2:
                    result["item"] = featured["4star2"]
                elif gacha == 3:
                    result["item"] = featured["4star3"]
                switch4 = False
                
            elif gacha <= 517:
                result["item"] = "Chongyun"
                switch4 = True
            elif gacha <= 534:
                result["item"] = "Noelle"
                switch4 = True
            elif gacha <= 551:
                result["item"] = "Barbara"
                switch4 = True
            elif gacha <= 568:
                result["item"] = "Sucrose"
                switch4 = True
            elif gacha <= 585:
                result["item"] = "Razor"
                switch4 = True
            elif gacha <= 602:
                result["item"] = "Xiangling"
                switch4 = True
            elif gacha <= 619:
                result["item"] = "Ningguang"
                switch4 = True
            elif gacha <= 636:
                result["item"] = "Xingqiu"
                switch4 = True
            elif gacha <= 653:
                result["item"] = "Fischl"
                switch4 = True
            elif gacha <= 670:
                result["item"] = "Diona"
                switch4 = True
            elif gacha <= 687:
                result["item"] = "Beidou"
                switch4 = True
            elif gacha <= 704:
                result["item"] = "Yanfei"
                switch4 = True
            elif gacha <= 721:
                result["item"] = "Rosaria"
                switch4 = True
            elif gacha <= 750:
                result["item"] = "Bennett"
                switch4 = True
            elif gacha > 750:
                result["item"] = "Semi-Garbage Weapon"
                switch4 = True

        elif result["star"] == 3:
            result["item"] = "Garbage Weapon"
            item["3star"] += 1


        if result["star"] == 5:
            flash = 15
            message = (str(result["item"]) + "\n" + str(result["star"]) + " Star!\n")
            while flash > 0:
                print("\n" * 200)
                print(str(result["droptype"]))
                print("Pulls left: " + str(pull-1) + "\n")
                if (flash%2) == 1:
                    print(str(message))
                else:
                    print("\n")
                print("5StarPity: " + str(data["pity5"]) + "  4StarPity: " + str(data["pity4"]))
                print("5StarGuar: " + str(data["guarantee5"]) + "  4StarGuar: " + str(data["guarantee4"]) + "\n")
                time.sleep(0.25)
                flash -= 1
            flash = 0
            message = 0
        else:
            print(str(result["droptype"]))
            print("Pulls left: " + str(pull-1) + "\n")
            print(str(result["item"]) + "\n" + str(result["star"]) + " Star!\n")
            print("5StarPity: " + str(data["pity5"]) + "  4StarPity: " + str(data["pity4"]))
            print("5StarGuar: " + str(data["guarantee5"]) + "  4StarGuar: " + str(data["guarantee4"]) + "\n")


        if result["star"] == 4:
            if switch4 == True:
                data["guarantee4"] = True
            elif switch4 == False:
                data["guarantee4"] = False

        elif result["star"] == 5:
            if switch5 == True:
                data["guarantee5"] = True
            elif switch5 == False:
                data["guarantee5"] = False


        if switch4p == True:
            data["pity4"] = 0

        if switch5p == True:
            data["pity5"] = 0




        if result["star"] == 4:
            time.sleep(3)

        if result["item"] != "Garbage Weapon" and result["item"] != "Semi-Garbage Weapon":
            item2[result["item"]] += 1

            
        
        result[str(pull)] = result["item"]
        switch4p = 0
        switch5p = 0
        switch4 = 0
        switch5 = 0
        result["item"] = 0
        result["star"] = 0
        pull -= 1
        input("\nContinue>")

        

    print("\n" * 200)
    print("==========\nResult:\n==========\n")
    print(str(result["10"]) + "\n" + str(result["9"]) + "\n" + str(result["8"]) + "\n" + str(result["7"]) + "\n" + str(result["6"]) + "\n" + str(result["5"]) + "\n" + str(result["4"]) + "\n" + str(result["3"]) + "\n" + str(result["2"]) + "\n" + str(result["1"]))
    input("\nEnd>")
    result["1"] = "-"
    result["2"] = "-"
    result["3"] = "-"
    result["4"] = "-"
    result["5"] = "-"
    result["6"] = "-"
    result["7"] = "-"
    result["8"] = "-"
    result["9"] = "-"
    result["10"] = "-"
    menu_banner()
                
            
            
            
        
def menu_bannerpick():
    global featured
    print("\n" * 200)
    print("==========\nPick your Banner! (More Coming Soon!)\n==========\n")
    print("1. Tartaglia")
    print("2. Venti")
    print("3. Hu Tao")
    print("4. Keqing")
    print("5. Xiao")
    print("6. Ganyu")
    print("7. Albedo")
    print("8. Zhongli (UPDATE!)")
    print("\n9. Back")
    a=input("\n >")
    if a == "1":
        featured["title"] = "Farewell of Snezhnaya"
        featured["5star"] = "Tartaglia"
        featured["4star1"] = "Rosaria"
        featured["4star2"] = "Fischl"
        featured["4star3"] = "Barbara"
        menu_banner()
    if a == "2":
        featured["title"] = "Ballad in Goblets"
        featured["5star"] = "Venti"
        featured["4star1"] = "Sucrose"
        featured["4star2"] = "Razor"
        featured["4star3"] = "Noelle"
        menu_banner()
    elif a == "3":
        egg = random.randint(1,20)
        if egg == 1:
            featured["title"] = "Navee did not get Hu Tao :("
        else:
            featured["title"] = "Moment of Bloom"
        featured["5star"] = "Hu Tao"
        featured["4star1"] = "Xingqiu"
        featured["4star2"] = "Chongyun"
        featured["4star3"] = "Xiangling"
        menu_banner()
    elif a == "4":
        featured["title"] = "Dance of Lanterns"
        featured["5star"] = "Keqing"
        featured["4star1"] = "Barbara"
        featured["4star2"] = "Ningguang"
        featured["4star3"] = "Bennett"
        menu_banner()
    elif a == "5":
        featured["title"] = "Invitation to Mundane Life"
        featured["5star"] = "Xiao"
        featured["4star1"] = "Diona"
        featured["4star2"] = "Beidou"
        featured["4star3"] = "Xinyan"
        menu_banner()
    elif a == "6":
        featured["title"] = "Adrift in the Harbour"
        featured["5star"] = "Ganyu"
        featured["4star1"] = "Noelle"
        featured["4star2"] = "Xingqiu"
        featured["4star3"] = "Xiangling"
        menu_banner()
    elif a == "7":
        featured["title"] = "Secretum Secretorum "
        featured["5star"] = "Albedo"
        featured["4star1"] = "Fischl"
        featured["4star2"] = "Sucrose"
        featured["4star3"] = "Bennett"
        menu_banner()
    elif a == "8":
        featured["title"] = "Gentry of Hermitage (UPDATE!)"
        featured["5star"] = "Zhongli"
        featured["4star1"] = "Yanfei"
        featured["4star2"] = "Noelle"
        featured["4star3"] = "Diona"
        menu_banner()
    elif a == "9":
        menu_main()
    else:
        menu_bannerpick()
    
            
        
def menu_shop():
    global data
    print("\n" * 200)
    print("==========\nBuy Primogems!\nPrimos: " + str(data["primos"]) + "\nSpent: £" + str(data["money"]) + "\n==========\n")
    print("1. Buy x60   (£1) ")
    print("2. Buy x300  (£5 )")
    print("3. Buy x980  (£14)")
    print("4. Buy x1980 (£29)")
    print("5. Buy x3280 (£49)")
    print("6. Buy x6480 (£99)")
    print("\n7. Back")
    a=input("\n >")

    if a == "1":
        data["primos"] += 60
        data["money"] += 1
        menu_shop()
    elif a == "2":
        data["primos"] += 300
        data["money"] += 5
        menu_shop()
    elif a == "3":
        data["primos"] += 980
        data["money"] += 14
        menu_shop()
    elif a == "4":
        data["primos"] += 1980
        data["money"] += 29
        menu_shop()
    elif a == "5":
        data["primos"] += 3280
        data["money"] += 49
        menu_shop()
    elif a == "6":
        data["primos"] += 6480
        data["money"] += 99
        menu_shop()
    elif a == "7":
        menu_main()
    else:
        menu_shop()

def menu_items():
    print("\n" * 200)
    print("==========\nItem Drops\n==========\nWishes Spent: " + str(data["spent"]))

    if data["spent"] != 0:
        print("==========")
        print("Item Drop Ratio:")
        print("*****Star: ~" + str(int((item["5star"]/data["spent"]) * 100)) + "%")
        print("**** Star: ~" + str(int((item["4star"]/data["spent"]) * 100)) + "%")
        print("***  Star: ~" + str(int((item["3star"]/data["spent"]) * 100)) + "%")
        print("==========\n")
    else:
        print("==========\n")

    print("*****Star Items: " + str(item["5star"]))
    print("**** Star Items: " + str(item["4star"]))
    print("***  Star Items: " + str(item["3star"]))

    print("\n1. Check 5Stars")
    print("2. Check 4Stars")
    print("3. Back")
    a=input("\n >")

    if a == "1":
        print("\n" * 200)
        print("==========\n5 Star Characters (" + str(item["5star"]) +")\n==========\n")
        print("Tartaglia: " + str(item2["Tartaglia"]) + " Venti: " + str(item2["Venti"]) + " Hu Tao: " + str(item2["Hu Tao"]) + " Xiao: " + str(item2["Xiao"]) + " Ganyu: " + str(item2["Ganyu"]) + " Albedo: " + str(item2["Albedo"]) + " Zhongli: " + str(item2["Zhongli"]))
        print("Diluc: " + str(item2["Diluc"]) + ", Jean: " + str(item2["Jean"]) + ", Keqing: " + str(item2["Keqing"]) + ", Mona: " + str(item2["Mona"]) + ", Qiqi: " + str(item2["Qiqi"]))
        input("\nBack>")
        menu_items()
    elif a == "2":
        print("\n" * 200)
        print("==========\n4 Star Characters (" + str(item["4star"]) +")\n==========\n")
        print("Noelle: " + str(item2["Noelle"]) + " Rosaria: " + str(item2["Rosaria"]) + " Fischl: " + str(item2["Fischl"]) + " Barbara: " + str(item2["Barbara"]) + " Sucrose: " + str(item2["Sucrose"]) + " Razor: " + str(item2["Razor"]) + " Bennett: " + str(item2["Bennett"]) + " Diona: " + str(item2["Diona"]) + " Amber: " + str(item2["Amber"]))
        print("Xinyan: " + str(item2["Xinyan"]) + ", Yanfei: " + str(item2["Yanfei"]) + ", Beidou: " + str(item2["Beidou"]) + ", Chongyun: " + str(item2["Chongyun"]) + ", Ningguang: " + str(item2["Ningguang"]) + ", Xingqiu: " + str(item2["Xingqiu"]) + ", Xiangling: " + str(item2["Xiangling"]))
        input("\nBack>")
        menu_items()
    elif a == "3":
        menu_main()
    else:
        menu_items()



def menu_exit():
    print("\n" * 200)
    print("==========\nLeave?\n==========\n")
    print("1. Yes")
    print("2. No")
    a=input("\n >")

    if a == "1":
        exit()
    elif a == "2":
        menu_main()
    else:
        menu_exit()

def menu_notes():
    print("\n" * 200)
    print("==========\nNAVEE notes :)\n==========\n'DM for ideas'\n==========\n")

    time.sleep(0.2)
    print("-Zhongli banner updated!")
    time.sleep(0.2)
    print("-Character Yanfei added")
    time.sleep(0.2)
    print("-Drop rates adjusted")
    time.sleep(3)

    input("\nBack>")
    menu_main()


menu_main()


















































    
