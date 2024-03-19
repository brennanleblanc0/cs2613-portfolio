from abc import ABC, abstractmethod

class TradingCard(ABC):
    def __init__(self, ID, rarity, yearReleased):
        self.ID = ID
        self.rarity = rarity
        self.yearReleased = yearReleased
    def getID(self):
        return self.ID
    def getRarity(self):
        return self.rarity
    def getYearReleased(self):
        return self.yearReleased
    def setRarity(self, rarity):
        self.rarity = rarity
    def __str__(self):
        return "#" + self.ID + "(" + self.yearReleased + "): Rarity: " + self.rarity