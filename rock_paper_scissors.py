class Game:
    def __init__(self, message):
        self.score1 = 0
        self.score2 = 0
        self.round = 0
        print(f"{message}")
        pass

    def score(self, player):
        match player:
            case "player1":
                self.round += 1
                self.score1 += 1
                print(f"player1 score: {self.score1}")
            case "player2":
                self.round += 1
                self.score2 += 1
                print(f"player2 score: {self.score2}")
            case _:
                print("Invalid player")

    def is_game_over(self) -> bool:
        if self.round == 2 and abs(self.score1 - self.score2):
            return True
        elif self.round == 3:
            return True
        else:
            return False


welcome_message = "Hello, let's play!"
game = Game(welcome_message)


game.score("player1")
