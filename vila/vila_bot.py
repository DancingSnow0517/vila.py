from .event.event_manager import EventManager
from .utils.vila_config import VilaConfig


class VilaBot:

    def __init__(self) -> None:
        # self.config = VilaConfig.load()
        self.event_manager = EventManager(self)

    ...