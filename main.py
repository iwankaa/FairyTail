class PetriNet:
    def __init__(self):
        self.places = {"Start": 1, "Home": 0, "Lake": 0, "Forest": 0, "End": 0}

    def add_tokens(self, place, tokens):
        self.places[place] += tokens

    def remove_tokens(self, place, tokens):
        if self.places[place] >= tokens:
            self.places[place] -= tokens
            return True
        return False

    def has_tokens(self, place, tokens):
        return self.places[place] >= tokens

    def execute_transition(self, transition):
        if transition == "Home":
            if self.has_tokens("Start", 1):
                if self.remove_tokens("Start", 1):
                    self.add_tokens("Home", 1)
                    return True
        elif transition == "Lake":
            if self.has_tokens("Home", 1):
                if self.remove_tokens("Home", 1):
                    self.add_tokens("Lake", 1)
                    return True
        elif transition == "Forest":
            if self.has_tokens("Lake", 1):
                if self.remove_tokens("Lake", 1):
                    self.add_tokens("Forest", 1)
                    return True
        return False

if __name__ == "__main__":
    petri_net = PetriNet()

    print("Вітаємо в симутялорі казки")

    while not petri_net.has_tokens("End", 1):
        choice = input("Розвиток казки: ")
        if choice in ["Залишитися вдома", "Дім"]:
            if petri_net.execute_transition("Home"):
                print(f"Сьогодні ми будемо сидіти вдома {choice}.")
            else:
                print("Invalid choice at this stage.")
        elif choice in ["Forest"]:
            if petri_net.execute_transition("Forest"):
                print(f"Сьогодні ми підемо в ліс {choice}.")
            else:
                print("Invalid choice at this stage.")
        elif choice in ["Lake"]:
            if petri_net.execute_transition("Lake"):
                print(f"Сьогодні ми підемо на озеро {choice}.")
            else:
                print("Invalid choice at this stage.")
