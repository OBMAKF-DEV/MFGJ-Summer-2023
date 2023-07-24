from source.items import Item


class Container:
    """Base class for objects that can store items.
    
    Attributes:
        items(list[item]): The items held in the container.
    """

    def __init__(self, items: list[Item] | None = None):
        self.items = [item for item in items] if isinstance(items, list) else []

    def interact(self):
        """Opens the container showing the items inside."""
        print("Items:")
        for item in self.items:
            print(f"\t- {item.name}")
            _ = input()

    def get_items(self, command: str):
        """called after interacting with the container, the player has the option
        to get the items from the container"""
        if command == "No":
            return None

        return self.items


