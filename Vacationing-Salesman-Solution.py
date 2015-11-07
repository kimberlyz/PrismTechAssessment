import os.path
import googlemaps

def getDistance(itinerary):
    # Using Google Maps API
    gmaps = googlemaps.Client(key="AIzaSyANqVJ8vves5_QgdSev6-Hxv4_UQJQJJfI")

    # Will hold the distances in km between subsequent cities
    distances = []

    for i in range(0, len(itinerary)-1):
        mydistance = gmaps.distance_matrix(itinerary[i], itinerary[i+1])
        distances.append(int(mydistance['rows'][0]['elements'][0]['distance']['text'].rstrip(' km').replace(',', '')))

    return distances

if __name__ == "__main__":
    filename = input('Please enter the name of a text file: ')

    # If the file cannot be found, prompt the user for input again
    while os.path.isfile(filename) == False:
        filename = input('Could not find the text file. Please try again: ')

    # Will hold the "city, country" lines from the text file
    itinerary = []

    # Read from file line by line to extract "city, country" text
    with open(filename) as f:
        for line in f:
            itinerary.append(line.strip())

    # Holds distances in km between subsequent cities
    distances = getDistance(itinerary)

    print('Success! Your vacation itinerary is:\n')

    for i in range(0, len(itinerary)-1):
        print(itinerary[i], ' -> ', itinerary[i+1], ": ", distances[i], 'km')

    print('\nTotal distance covered in your trip: ', sum(distances), 'km')
