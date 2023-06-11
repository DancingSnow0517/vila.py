import asyncio
import logging
from abc import ABC
from typing import TYPE_CHECKING, Dict, Type, List, Callable, Coroutine, Any
import inspect

if TYPE_CHECKING:
    from ..bot import VilaBot

HANDLE_TYPE = Callable[['Event'], Coroutine[Any, Any, None]]
log = logging.getLogger(__name__)


class Event(ABC):
    pass


class EventManager:
    event_handles: Dict[Type[Event], List[HANDLE_TYPE]]

    def __init__(self, bot: 'VilaBot') -> None:
        self.bot = bot

        self.event_handles = {}

    async def post(self, event: Event):
        for handle in self.event_handles.get(event.__class__, []):
            await handle(event)

    def subscribe(self, name: str, handle: HANDLE_TYPE):

        sig = inspect.signature(handle)
        params = list(sig.parameters.values())
        if len(params) != 1:
            log.error('Event handle %s params lens not match.', name)
            return
        event_type = params[0].annotation
        if not issubclass(event_type, Event):
            log.error('Event handle %s type not match.', name)
            return

        if not asyncio.iscoroutinefunction(handle):
            log.error('Event handle %s is not coroutine function.', name)
            return

        if event_type not in self.event_handles:
            self.event_handles[event_type] = []
        self.event_handles[event_type].append(handle)
        log.info('Event handle %s registered.', name)

    def subscribe_all(self, module):
        for name, handle in inspect.getmembers(module):
            if name.startswith('_'):
                continue
            if inspect.isfunction(handle):
                self.subscribe(name, handle)

