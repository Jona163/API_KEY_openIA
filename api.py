import enum
from typing import Annotated 
from livekit.agents import llm
import logging

logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)

class Zone(enum.Enum):
    LIVING_ROOM="living-room"
    BEDROOM = "bedroom"
    kITCHEN = "kitchen"
    OFFICE = "office"
    
class AssistanFnc(llm.FunctionContext):
   def __init__(self)->None:
      super().__init__()

        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 23,
            Zone.OFFICE: 21,
        }
