from lat_lng1 import *

import requests
import json
import time
from random import randint
import csv


# lat_lng = open_with_csv('lat_lng.csv')

# Create and write in csv file.
with open( "my_address_components.csv", "w") as f:
	output = csv.writer(f)
	i = 1

# Google Reverse Geocoding.
	for ll in lat_lng:
		# sleeps
		time.sleep(.01)

		def get_address():
			try:
				raw_address = requests.get('http://maps.googleapis.com/maps/api/geocode/json?latlng=' + ll )
				full_address = raw_address.json()
				my_full_address = (full_address['results'][0]['formatted_address'])
				output.writerow([i, my_full_address])
				print("Success!! {}".format(i))
			except:
				print("N/A {}".format(i))
				output.writerow([i, "N/A"])
				pass

		get_address()		
		i += 1










