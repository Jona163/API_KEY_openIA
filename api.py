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
    