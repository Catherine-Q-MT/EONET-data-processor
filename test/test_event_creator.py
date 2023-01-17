from typing import Any

import pytest

from event import Event
from event_creator import parse_data_into_events


class TestEventCreator:

    @pytest.fixture
    def mock_data(self) -> dict[Any, Any]:
        return {
            "title": "EONET Events",
            "description": "Natural events from EONET.",
            "link": "https://eonet.gsfc.nasa.gov/api/v2.1/events",
            "events": [
                {
                    "id": "EONET_2734",
                    "title": "Iceberg A23A",
                    "description": "",
                    "link": "https://eonet.gsfc.nasa.gov/api/v2.1/events/EONET_2734",
                    "categories": [
                        {
                            "id": 15,
                            "title": "Sea and Lake Ice"
                        }
                    ],
                    "sources": [
                        {
                            "id": "BYU_ICE",
                            "url": "http://www.scp.byu.edu/data/iceberg/ascat/a23a.ascat"
                        },
                        {
                            "id": "NATICE",
                            "url": "https://usicecenter.gov/pub/Iceberg_Tabular.csv"
                        }

                    ],
                    "geometries": [
                        {
                            "date": "2011-08-30T00:00:00Z",
                            "type": "Point",
                            "coordinates": [-41.4727, -75.8853]
                        },
                        {
                            "date": "2023-01-13T00:00:00Z",
                            "type": "Point",
                            "coordinates": [-46.97, -72.15]
                        }

                    ]
                }
            ]
        }

    @pytest.fixture
    def mock_data_single_event(self) -> dict[Any, Any]:
        return {
            "title": "EONET Events",
            "description": "Natural events from EONET.",
            "link": "https://eonet.gsfc.nasa.gov/api/v2.1/events",
            "events": [
                {
                    "id": "EONET_2734",
                    "title": "Iceberg A23A",
                    "description": "",
                    "link": "https://eonet.gsfc.nasa.gov/api/v2.1/events/EONET_2734",
                    "categories": [
                        {
                            "id": 15,
                            "title": "Sea and Lake Ice"
                        }
                    ],
                    "sources": [
                        {
                            "id": "BYU_ICE",
                            "url": "http://www.scp.byu.edu/data/iceberg/ascat/a23a.ascat"
                        },
                        {
                            "id": "NATICE",
                            "url": "https://usicecenter.gov/pub/Iceberg_Tabular.csv"
                        }

                    ],
                    "geometries": [
                        {
                            "date": "2011-08-30T00:00:00Z",
                            "type": "Point",
                            "coordinates": [-41.4727, -75.8853]
                        }
                    ]
                }
            ]
        }

    def test_event_object_created(self, mock_data: dict) -> None:
        expected_result = [Event(event_object='Iceberg A23A',
                                 event_object_id='EONET_2734',
                                 earliest_year=2011,
                                 earliest_month=8,
                                 earliest_day=30,
                                 earliest_location=[-41.4727, -75.8853],
                                 event_id=15,
                                 event_type='Sea and Lake Ice',
                                 latest_year=2023,
                                 latest_month=1,
                                 latest_day=13,
                                 latest_location=[-46.97, -72.15]
                                 )
                           ]

        result = parse_data_into_events(mock_data)
        assert expected_result == result

    def test_event_object_created_with_single_geometry(self, mock_data_single_event: dict) -> None:
        expected_result = [Event(event_object='Iceberg A23A',
                                 event_object_id='EONET_2734',
                                 earliest_year=2011,
                                 earliest_month=8,
                                 earliest_day=30,
                                 earliest_location=[-41.4727, -75.8853],
                                 event_id=15,
                                 event_type='Sea and Lake Ice',
                                 latest_year=None,
                                 latest_month=None,
                                 latest_day=None,
                                 latest_location=None
                                 )
                           ]

        result = parse_data_into_events(mock_data_single_event)
        assert expected_result == result
