# author: Jan Tschada
# SPDX-License-Identifier: Apache-2.0

from georapid.client import GeoRapidClient
import requests
from typing import List
from .types import OutputType


def enrich(client: GeoRapidClient, latitudes: List[float], longitudes: List[float], out: OutputType = OutputType.LOCAL) -> List[str]:
    """
    Enriches locations using date and time values of the corresponding standard time zones. 
    The local date and time value for each location are determined at the time of execution.

    :param client: The client instance to use for this query.
    :param latitudes: The latitudes representing the locations.
    :param longitudes: The longitudes representing the locations.
    :param out: The output for the timestamps e.g. "local" means local time or "dtc" means date-time-classification.

    :return: A list of date and time values for each location.
    """
    # Validate input parameters
    for latitude in latitudes:
        if latitude < -90.0 or 90.0 < latitude:
            raise ValueError(f'Invalid latitude value! {latitude} is not in the range of [-90.0, 90.0].')

    for longitude in longitudes:
        if longitude < -180.0 or 180.0 < longitude:
            raise ValueError(f'Invalid longitude value! {longitude} is not in the range of [-180.0, 180.0].')

    # Prepare the request payload
    payload = {
        'lat': latitudes,
        'lon': longitudes,
        'out': out.value
    }

    # Make the request to the service
    endpoint = '{0}/enrich'.format(client.url)
    response = requests.post(endpoint, headers=client.auth_headers, json=payload)
    response.raise_for_status()  # Raise an error for bad responses

    # Return the enriched locations
    return response.json()

def convert(client: GeoRapidClient, latitudes: List[float], longitudes: List[float], times: List[str], out: OutputType = OutputType.LOCAL) -> List[str]:
    """
    Converts date and time values from UTC to local time or time of day for the specified locations.

    :param client: The client instance to use for this query.
    :param latitudes: The latitudes representing the locations.
    :param longitudes: The longitudes representing the locations.
    :param times: The UTC times for each location in ISO 8601 format.
    :param out: The output for the timestamps e.g. "local" means local time or "dtc" means date-time-classification.

    :return: A list of date and time values for each location.
    """
    # TODO: Implement the convert function
    raise NotImplementedError("The convert function is not yet implemented.")

def time_of_day(client: GeoRapidClient, latitudes: List[float], longitudes: List[float], times: List[str]) -> List[str]:
    """
    Classifies local time values to time of day values like „last night“, „morning“, „noon“, „afternoon“, „evening“ and „night“.
    The classifier uses seasonal locations of the sun and moon providing realistic classifications.

    :param client: The client instance to use for this query.
    :param latitudes: The latitudes representing the locations.
    :param longitudes: The longitudes representing the locations.
    :param times: The UTC times for each location in ISO 8601 format.

    :return: A list of time of day values for each location.
    """
    # TODO: Implement the time_of_day function
    raise NotImplementedError("The time_of_day function is not yet implemented.")
