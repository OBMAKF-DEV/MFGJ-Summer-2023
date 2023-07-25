class Item:
    """Base class for in game items that can be pickup by the player."""

    def __init__(self, name: str, item_description: str, heal_amount: int):
        self.name = name
        self.item_description = item_description
        self.heal_amount = heal_amount  # heal items have a non-zero heal_amount value

    def read_description(self):
        return self.item_description

    def heal_player(self):
        return self.heal_amount
