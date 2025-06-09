# author: Jan Tschada
# SPDX-License-Identifier: Apache-2.0

from georapid.client import GeoRapidClient
from georapid.factory import EnvironmentClientFactory
from geolocaltime.services import enrich
from geolocaltime.types import OutputType

import unittest


class TestGeoLocalTimeService(unittest.TestCase):

    def setUp(self):
        host = 'geolocaltime.p.rapidapi.com'
        self.client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        self.latitudes = [50.0088, 39.437, 66.0557, 71.0201, 39.6466, 37.0969, 70.4]
        self.longitudes = [8.2756, -31.542, -23.7033, 26.1334, 44.8109, 13.9381, -47.1]
        self.utc_times = len(self.latitudes) * ['2024-10-19T09:18:42.542819']

    def test_enrich(self):
        result = enrich(self.client, self.latitudes, self.longitudes, OutputType.LOCAL)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(self.latitudes))