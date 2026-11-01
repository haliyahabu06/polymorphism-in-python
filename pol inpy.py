class Cricket:
    def __init__(self, player, score):
        
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")


class Football:
    def __init__(self, player, score):
        
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")



cricket = Cricket('Rohit', 85)
football = Football('Arjun', 2)

sports_list = [cricket, football]

print("--- Displaying Sports Info and Play Action ---")
for sport in sports_list:
    sport.info()
    sport.play()
    print()


print("--- Testing Encapsulation (Direct Modification Attempt) ---")
cricket.__score = 999 
print(f"Attempted direct change. Current score via getter: {cricket.get_score()}") 
print("(The score remains 85 because __score is private and protected!)")
print()

print("--- Updating Scores Safely via Setter ---")
cricket.set_score(95)
football.set_score(3)

print("\n--- Verified Final Scores ---")
print(f"Cricket final score: {cricket.get_score()}")
print(f"Football final score: {football.get_score()}")
