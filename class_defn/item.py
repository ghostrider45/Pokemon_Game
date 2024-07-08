class Item:
    def __init__(self, name, type, effect, description):
        self.name = name
        self.type = type
        self.effect = effect
        self.description = description

    def use(self, target):
        print(f"Using {self.name} on {target.name}!")
        self.effect(target)
