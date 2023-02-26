import pgeocode
import math

def distance_by_postal_code(postal_code1, postal_code2):
    # Get the latitude and longitude coordinates for both postal codes
    lat1, lon1 = pgeocode.GeoDistance("IN").query_postal_code(postal_code1)
    lat2, lon2 = pgeocode.GeoDistance("IN").query_postal_code(postal_code2)
    
    # Calculate the great circle distance between the two coordinates using the haversine formula
    radius = 6371  # Earth's radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c
    
    return distance

postal_code1 = "400028"
postal_code2 = "110055"

distance = distance_by_postal_code(postal_code1, postal_code2)
print("The distance between {} and {} is {:.2f} km".format(postal_code1, postal_code2, distance))
