import math
# Need to modify this to return point from distance instead.
'''
This code was taken from the following source. It is slightly modified but is mostly intact:
Availability: https://www.geeksforgeeks.org/haversine-formula-to-find-distance-between-two-points-on-a-sphere/
Site: Geeks For Geeks
Author: N/A
Refactored slightly to return 
Go to the Python3 section, and this formula is in there.
'''
def haversine(lat1, lon1, lat2, lon2):
     
    # distance between latitudes and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0
 
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
 
    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2))
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c

if __name__ == "__main__":
    lat1 = 52.002144
    lon1 = -9.729547
    lat2 = 51.999445
    lon2 = -9.742693
    print(haversine(lat1, lon1,lat2, lon2), "K.M.")

    # lowest 52.002144  -9.729547
    # highest 51.999445  -9.742693