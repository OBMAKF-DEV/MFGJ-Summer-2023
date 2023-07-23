class NPC:
    """Base class for all NPC entities."""
    def __init__(self, name: str, tag: str) -> None:
        """Initialize a new NPC.
        
        Args:
            name (str): The NPC's Name.
            tag (str): NPC Category.
        """
        self.name = name
        self.tag = tag.title()
    
    def __str__(self) -> str:
        return f"{self.tag}.{self.name}"


class QuestNPC(NPC):
    """Essential `QuestNPC` entity.
    
    Provides additional functionality and support that allows the user to interact with
    the NPC, engaging in dialog and starting / completing quests."""
    def __init__(self, name: str, tag: str) -> None:
        super(QuestNPC, self).__init__(name, tag)
        self.dialogue = f'../resources/dialogues/{self}.txt'
    
    def talk(self,):
        ...
