from datetime import datetime
from typing import List

from event import Event


def time_parser(datetime_str: str):
    return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')


def parse_data_into_events(event_json: dict) -> List[Event]:
    pass
    event_list = []
    for event_data in event_json.get('events'):
        first_geometry = event_data.get('geometries')[0]
        last_geometry = None if len(event_data.get('geometries')) <= 1 else event_data.get('geometries')[-1]

        earliest_event_date = time_parser(first_geometry.get('date'))
        if last_geometry is not None:
            latest_event_date = time_parser(last_geometry.get('date'))
            event_data = Event(event_object=event_data.get('title'),
                               event_object_id=event_data.get('id'),
                               earliest_year=earliest_event_date.year,
                               earliest_month=earliest_event_date.month,
                               earliest_day=earliest_event_date.day,
                               earliest_location=first_geometry.get('coordinates'),
                               event_id=int(event_data.get('categories')[0].get('id')),
                               event_type=event_data.get('categories')[0].get('title'),
                               latest_year=latest_event_date.year,
                               latest_month=latest_event_date.month,
                               latest_day=latest_event_date.day,
                               latest_location=last_geometry.get('coordinates')
                               )
        else:
            event_data = Event(event_object=event_data.get('title'),
                               event_object_id=event_data.get('id'),
                               earliest_year=earliest_event_date.year,
                               earliest_month=earliest_event_date.month,
                               earliest_day=earliest_event_date.day,
                               earliest_location=first_geometry.get('coordinates'),
                               event_id=int(event_data.get('categories')[0].get('id')),
                               event_type=event_data.get('categories')[0].get('title')
                               )

        event_list.append(event_data)
    return event_list
