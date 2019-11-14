import pprint
result = {'info': {'copyright': {'imageAltText': '© 2019 MapQuest, Inc.',
                        'imageUrl': 'http://api.mqcdn.com/res/mqlogo.gif',
                        'text': '© 2019 MapQuest, Inc.'},
          'messages': [],
          'statuscode': 0},
 'options': {'ignoreLatLngInput': False, 'maxResults': -1, 'thumbMaps': True},
 'results': [{'locations': [{'adminArea1': 'US',
                             'adminArea1Type': 'Country',
                             'adminArea3': 'MA',
                             'adminArea3Type': 'State',
                             'adminArea4': '',
                             'adminArea4Type': 'County',
                             'adminArea5': 'Wellesley, Wellesley Hills',
                             'adminArea5Type': 'City',
                             'adminArea6': '',
                             'adminArea6Type': 'Neighborhood',
                             'displayLatLng': {'lat': 42.29761,
                                               'lng': -71.26176},
                             'dragPoint': False,
                             'geocodeQuality': 'STREET',
                             'geocodeQualityCode': 'B3CCA',
                             'latLng': {'lat': 42.29761, 'lng': -71.26176},
                             'linkId': 'US/STR/p0/10907727',
                             'mapUrl': 'http://www.mapquestapi.com/staticmap/v5/map?key=1GJGgIOEKx3NdB0OyKuyc1DeZQNquhO2&type=map&size=225,160&locations=42.29761,-71.26176|marker-sm-50318A-1&scalebar=true&zoom=15&rand=267397972',
                             'postalCode': '02481',
                             'sideOfStreet': 'N',
                             'street': 'Babson College Drive',
                             'type': 's',
                             'unknownInput': ''},
                            {'adminArea1': 'US',
                             'adminArea1Type': 'Country',
                             'adminArea3': 'FL',
                             'adminArea3Type': 'State',
                             'adminArea4': '',
                             'adminArea4Type': 'County',
                             'adminArea5': 'Babson Park',
                             'adminArea5Type': 'City',
                             'adminArea6': '',
                             'adminArea6Type': 'Neighborhood',
                             'displayLatLng': {'lat': 27.84321,
                                               'lng': -81.53535},
                             'dragPoint': False,
                             'geocodeQuality': 'STREET',
                             'geocodeQualityCode': 'B3CCA',
                             'latLng': {'lat': 27.84321, 'lng': -81.53535},
                             'linkId': 'US/STR/p0/7375897',
                             'mapUrl': 'http://www.mapquestapi.com/staticmap/v5/map?key=1GJGgIOEKx3NdB0OyKuyc1DeZQNquhO2&type=map&size=225,160&locations=27.84321,-81.53535|marker-sm-50318A-2&scalebar=true&zoom=15&rand=-2014937441',
                             'postalCode': '33827',
                             'sideOfStreet': 'N',
                             'street': 'College Drive',
                             'type': 's',
                             'unknownInput': ''},
                            {'adminArea1': 'US',
                             'adminArea1Type': 'Country',
                             'adminArea3': 'FL',
                             'adminArea3Type': 'State',
                             'adminArea4': '',
                             'adminArea4Type': 'County',
                             'adminArea5': 'Babson Park, Crooked Lake Park, '
                                           'Lake Wales',
                             'adminArea5Type': 'City',
                             'adminArea6': '',
                             'adminArea6Type': 'Neighborhood',
                             'displayLatLng': {'lat': 27.8342,
                                               'lng': -81.58886},
                             'dragPoint': False,
                             'geocodeQuality': 'STREET',
                             'geocodeQualityCode': 'B3CCA',
                             'latLng': {'lat': 27.8342, 'lng': -81.58886},
                             'linkId': 'US/STR/p0/7376429',
                             'mapUrl': 'http://www.mapquestapi.com/staticmap/v5/map?key=1GJGgIOEKx3NdB0OyKuyc1DeZQNquhO2&type=map&size=225,160&locations=27.8342,-81.58886|marker-sm-50318A-3&scalebar=true&zoom=15&rand=-1274182043',
                             'postalCode': '33827,33859',
                             'sideOfStreet': 'N',
                             'street': 'College Boulevard',
                             'type': 's',
                             'unknownInput': ''},
                            {'adminArea1': 'US',
                             'adminArea1Type': 'Country',
                             'adminArea3': 'IN',
                             'adminArea3Type': 'State',
                             'adminArea4': '',
                             'adminArea4Type': 'County',
                             'adminArea5': 'Indianapolis',
                             'adminArea5Type': 'City',
                             'adminArea6': '',
                             'adminArea6Type': 'Neighborhood',
                             'displayLatLng': {'lat': 39.91978,
                                               'lng': -86.2158},
                             'dragPoint': False,
                             'geocodeQuality': 'STREET',
                             'geocodeQualityCode': 'B3CCA',
                             'latLng': {'lat': 39.91978, 'lng': -86.2158},
                             'linkId': 'US/STR/p0/11161004',
                             'mapUrl': 'http://www.mapquestapi.com/staticmap/v5/map?key=1GJGgIOEKx3NdB0OyKuyc1DeZQNquhO2&type=map&size=225,160&locations=39.91978,-86.2158|marker-sm-50318A-4&scalebar=true&zoom=15&rand=-492879037',
                             'postalCode': '46268',
                             'sideOfStreet': 'N',
                             'street': 'Babson Court',
                             'type': 's',
                             'unknownInput': ''},
                            {'adminArea1': 'US',
                             'adminArea1Type': 'Country',
                             'adminArea3': 'MA',
                             'adminArea3Type': 'State',
                             'adminArea4': '',
                             'adminArea4Type': 'County',
                             'adminArea5': 'Wellesley, Wellesley Hills',
                             'adminArea5Type': 'City',
                             'adminArea6': '',
                             'adminArea6Type': 'Neighborhood',
                             'displayLatLng': {'lat': 42.29767,
                                               'lng': -71.26461},
                             'dragPoint': False,
                             'geocodeQuality': 'INTERSECTION',
                             'geocodeQualityCode': 'I1CCA',
                             'latLng': {'lat': 42.29767, 'lng': -71.26461},
                             'linkId': 'US/XSTR/p0/4099298',
                             'mapUrl': 'http://www.mapquestapi.com/staticmap/v5/map?key=1GJGgIOEKx3NdB0OyKuyc1DeZQNquhO2&type=map&size=225,160&locations=42.29767,-71.26461|marker-sm-50318A-5&scalebar=true&zoom=15&rand=1670496158',
                             'postalCode': '02481',
                             'sideOfStreet': 'N',
                             'street': 'Babson College Drive',
                             'type': 's',
                             'unknownInput': ''}],
              'providedLocation': {'location': 'Babson College'}}]}


pprint.pprint(result["results"])

print(type(result['results']), len(result['results']))