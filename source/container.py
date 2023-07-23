from source.items import Item


class Container:
    """Base class for objects that can store items.
    
    Attributes:
        items(list[item]): The items held in the container.
    """
    _state: int = 0
    
    def __init__(self, items: list[Item] | None = None):
        self.items = [item for item in items] if isinstance(items, list) else []
    
    def interact(self):
        """Opens the container showing the items inside."""
        self._state = 1
        self.open()
        # Todo. add functionality for picking up / storing items.
    
    def open(self):
        print("Items:")
        for item in self.items:
            print(f"\t- {item.name}")
            _ = input()
        # Temp