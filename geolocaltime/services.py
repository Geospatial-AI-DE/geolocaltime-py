# author: Jan Tschada
# SPDX-License-Identifier: Apache-2.0

from georapid.client import GeoRapidClient
import requests
from typing import List


def enrich(client: GeoRapidClient, latitudes: List[float], longitudes: List[float], out: str) -> List[str]:
    """
    Enriches locations using date and time values of the corresponding standard time zones. 
    The local date and time value for each location are determined at the time of execution.

    :param client: The client instance to use for this query.
    :param latitudes: The latitudes representing the locations.
    :param longitudes: The longitudes representing the locations.
    :param out: The defined category.

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
        "latitudes": latitudes,
        "longitudes": longitudes,
        "out": out
    }

    # Make the request to the service
    endpoint = '{0}/enrich'.format(client.url)
    response = requests.post(endpoint, headers=client.auth_headers, json=payload)
    response.raise_for_status()  # Raise an error for bad responses

    # Return the enriched locations
    return response.json()