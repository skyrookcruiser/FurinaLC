from pydantic import BaseModel, Field
from typing import List, Optional

from . import action_event
from . import personality_event
from . import theme
from . import ego


class Event(BaseModel):
    id: int = 0
    eventType: str = ""
    canSkip: bool = False
    actionEvent: Optional[action_event.ActionEvent] = None
    personalityEvent: Optional[personality_event.PersonalityEvent] = None


class EventList(BaseModel):
    list: List[Event] = []
