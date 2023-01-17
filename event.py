from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Event:
    event_object: str
    event_object_id: str
    earliest_year: int
    earliest_month: int
    earliest_day: int
    earliest_location: List[float]
    event_id: int
    event_type: str
    latest_year: Optional[int] = None
    latest_month: Optional[int] = None
    latest_day: Optional[int] = None
    latest_location: Optional[List[float]] = None



