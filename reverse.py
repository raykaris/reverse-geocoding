import opencage
from opencage.geocoder import OpenCageGeocode
from pprint import pprint

key=""#paste api key from opencage.com
geocoder= OpenCageGeocode(key)
results = geocoder.reverse_geocode(#enter latitude and longitude coordinates separated with a comma)
print(results)