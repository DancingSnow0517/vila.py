from .event.event_manager import EventManager


class VilaBot:

    def __init__(self) -> None:
        self.event_manager = EventManager(self)

    ...