# Billy Thomas - Driver
# Braydon Armstrong - 2
# Brennan LeBlanc - 1

from abc import ABC, abstractmethod

class TradingCard(ABC):
   @abstractmethod
   def cost(self):
       pass
   def __init__(self, ID, rarity, yearReleased):
       self.ID = ID
       if(rarity > 0 and rarity < 11):
        self.rarity = rarity
       self.yearReleased = yearReleased
   def getID(self):
       return self.ID
   def getRarity(self):
       return self.rarity
   def getYearReleased(self):
       return self.yearReleased
   def setRarity(self, rarity):
       if(rarity > 0 and rarity < 11):
        self.rarity = rarity
   def __str__(self):
       return "#" + str(self.ID) + "(" + str(self.yearReleased) + "): Rarity: " + str(self.rarity)
   
class PlayingCard(TradingCard):
    def __init__(self, ID, rarity, yearReleased, holographic, condition):
        super().__init__(ID, rarity, yearReleased)
        self.holographic = holographic
        if(condition in ["Mint", "Good", "Poor"]):
            self.condition = condition
    def getHolographic(self):
        return self.holographic
    def getCondition(self):
        return self.condition
    def setCondition(self, condition):
        if(condition in ["Mint", "Good", "Poor"]):
            self.condition = condition
    def cost(self):
        cost = 0
        if(self.condition == "Mint"):
            cost = 5.15 * (self.rarity/2)
        elif(self.condition == "Good"):
            cost = 2.15 * (self.rarity/2)
        elif(self.condition == "Poor"):
            cost = 0.5 * (self.rarity/2)
        
        if(self.holographic):
            cost *= 5

        return round(cost,2)
    
    def __str__(self):
        string = super().__str__()
        return string + "\tCost: $" + str(self.cost()) + "\n\tHolographic: " + str(self.holographic) + "\tCondition: " + str(self.condition)
cardList = []


class HockeyCard(TradingCard):
    def __init__(self, ID, rarity, yearReleased, playerName, jerseyNumber, numGamesWon):
        super().__init__(ID, rarity, yearReleased)
        self.playerName = playerName
        self.jerseyNumber = jerseyNumber
        self.numGamesWon = numGamesWon
    def getPlayerName(self):
        return self.playerName
    def getJerseyNumber(self):
        return self.jerseyNumber
    def getNumGamesWon(self):
        return self.numGamesWon
    def cost(self):
        return self.getNumGamesWon() * (2023 - super().getYearReleased())/10 * (0.15 + super().getRarity() / 5)
    def __str__(self):
        return str(super()) + f"\tCost: ${round(self.cost(), 2)}\n\t {self.playerName} (#{self.jerseyNumber}) - {self.numGamesWon} Games Won"

card = PlayingCard(1, 9, 2021, True, "Good")
card2 = PlayingCard(5, 2, 1788, True, "Poor")
card3 = PlayingCard(4, 6, 2004, True, "Good")
cardList.append(PlayingCard(6, 4, 2011, False, "Mint"))
cardList.append(PlayingCard(99, 4, 2013, False, "Poor"))
cardList.append(card)
cardList.append(card2)
cardList.append(card3)

hCard = HockeyCard(1,4,2021,"Joe Swanson",99,-21)
cardList.append(hCard)
cardList.append(HockeyCard(2,9,2024,"Jackie Chan",-1,1))
cardList.append(HockeyCard(4,1,2023,"Jackie Cha",3,1))
cardList.append(HockeyCard(2,9,2024,"Jack Chan",1,3))


def func(e):
    return e.cost()

cardList.sort(key=func)

cardList.reverse()

while(len(cardList) > 3):
    cardList.pop(3)

for x in cardList:
    print(x)