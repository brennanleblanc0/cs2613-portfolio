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
        if (rarity <= 10 and rarity >= 1):
            self.rarity = rarity
    def __str__(self):
        return f"#{self.ID} ({self.yearReleased}): Rarity: {self.rarity}"
    @abstractmethod
    def cost(self):
        pass

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
