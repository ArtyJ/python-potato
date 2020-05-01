import time

class Treasure:
    name = ""
    xp = 0
    chance = 0
    abbr = ""
    
    def __init__(self, n, x, c, a):
        self.name = n
        self.xp = x
        self.chance = c
        self.abbr = a
    def __str__(self):
        if self.xp < 1: return "-"
        return f"{self.abbr}/{self.xp}/{self.chance}%"
        # print(f"name={self.name}, xp={self.xp}, chance={self.chance}%")
        
        
def initTreasures():
    treasures = {Treasure("None", 0, 0, "-"),
        Treasure("CoinPurse", 10, 5, "C"),                   
    Treasure("GoldRing", 25, 10, "GR"),
    Treasure("Priest'sChalice", 50, 20, "P"),
    Treasure("King'sCrown", 100, 25, "K"),
    Treasure("Genie'sLamp", 250, 30, "GL"),
    Treasure("SacretTreasure", 500, 50, "S")
    }
    #newlist = sorted(ut, key=lambda x: x.count, reverse=True)
    return sorted(treasures, key=lambda t: t.chance, reverse=True)


# calculate how many xp needed to level 100
def getXpTo(level, exp):
    # validate input
    if exp >= level:
        exp = 0
    if level >= 100:
        return 0
    return (level + 101) * (100 - level) / 2 - exp

def goldCost(level, treasureAmount):
    return (level * 200 + 600) * treasureAmount

def findChance100():
    # dad implemented
    n = 0
    list1 = initTreasures()
    for t1 in list1:
        for t2 in list1:
            if t2.chance > t1.chance: continue
            for t3 in list1:
                if t3.chance > t2.chance: continue
                for t4 in list1:
                    if t4.chance > t3.chance: continue
                    for t5 in list1:
                        if t5.chance > t4.chance: continue
                        comb = [t1,t2,t3,t4,t5]
                        if sum(t.chance for t in comb) == 100:
                            n += 1
                            print(f"No. {'%02d'%(n)}: {t1}, {t2}, {t3}, {t4}, {t5} => chance=100%, exp = {sum(t.xp for t in comb)}")

    print(f"Found {n} combinations at 100% chance of quality upgrade.")


def planUpgrade(name, level, exp, quality):
    # the goal is to spend the least gold to upgrade to level 100 and quality 10
    needXp = getXpTo(level, exp)
    needChance = (10 - quality) * 100
    if needChance < 0:
        needChance = 0
    # print(f"Upgrading {name} needs \t{needXp} XP and \t{needChance}%")
    print(f"{name}--{needXp}--{needChance}%")
    
    # every upgrade we can use 1-5 treasure
    # the 
    

if __name__ == '__main__': 
    start = time.time()
    treasures = initTreasures()
    print(treasures)
    # for t in treasures:
    #     t.prt()
 
    findChance100()
    
    print(f"Faction--Need XP--Need Chance")   
    planUpgrade("All-Seeing Eye", 100, 20, 10)
    planUpgrade("Amanithrax", 87, 72, 10)
    planUpgrade("City of Thieves", 43, 4, 2)
    planUpgrade("Crypt Keepers", 1, 0, 1)
    planUpgrade("Dark Pits", 13, 4, 2)
    planUpgrade("Fang Moor",32, 22, 3)
    planUpgrade("Frostfire Keep", 10, 10, 1)
    planUpgrade("Hall of Guardians", 110, 45, 10)
    planUpgrade("Lyrasza's Lair", 24, 0, 2)
    planUpgrade("Mirroed Halls", 77, 27, 10)
    planUpgrade("Primal Rift", 45, 10, 2)
    planUpgrade("Sea of Sorrow", 20, 5, 3)
    planUpgrade("Silver Necropolis", 35, 20, 2)
    planUpgrade("Stonesong Eyrie", 36, 34, 2)
    planUpgrade("Sunken Fleet", 36, 34, 2)
    planUpgrade("The Warrens", 25, 25, 2)
    planUpgrade("The Deep Hive", 33, 19, 3)
    planUpgrade("Werewoods", 18, 4, 1)
    planUpgrade("Wild Court", 1, 0, 1)
    
    # print("Funciton took {}ms".format((end-start)*1000.0)) 


