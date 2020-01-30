import json

class Planet:

    #Constructor method to initialize attributes.
    def __init__(self, name, mass, planetType, radius, density, lengthOfYear, lengthOfDay, numberOfMoons, equatorialIncilination, meanOrbitVelocity, averageOrbitDistance, volume, escapeVelocity, surfaceGravity):
        self.name = name
        self.mass = mass
        self.planetType = planetType
        self.radius = radius
        self.density = density
        self.lengthOfYear = lengthOfYear
        self.lengthOfDay = lengthOfDay
        self.numberOfMoons = numberOfMoons
        self.equatorialIncilination = equatorialIncilination
        self.meanOrbitVelocity = meanOrbitVelocity
        self.averageOrbitDistance = averageOrbitDistance
        self.volume = volume
        self.escapeVelocity = escapeVelocity
        self.surfaceGravity = surfaceGravity

#Open and parse json data into a python object.
with open ('SpaceDex/Planets.json') as file:
    read = json.load(file)
    planet_data = read['planets']

#Empty dictionary to hold planet information being parsed from json file.
#Will be utilized later to initialize to Planet objects using Planets class.
planets = {}

#Iterate through the json object to populate the empty dictionary with planetary information.
for i in range(0,8):
    planets[planet_data[i]['name']] = [planet_data[i]['mass'], planet_data[i]['planet Type'], planet_data[i]['radius'],
                                       planet_data[i]['density'], planet_data[i]['lengthOfYear'], planet_data[i]['lengthOfDay'],
                                       planet_data[i]['numberOfMoons'], planet_data[i]['equatorialIncilination'],
                                       planet_data[i]['meanOrbitVelocity'], planet_data[i]['averageOrbitDistance'],
                                       planet_data[i]['volume'], planet_data[i]['escapeVelocity'], planet_data[i]['surfaceGravity']]

#Create planets of class object from dictionary values imported from json file.
Mercury = Planet("Mercury", planets['Mercury'][0], planets['Mercury'][1], planets['Mercury'][2], planets['Mercury'][3], planets['Mercury'][4],
               planets['Mercury'][5], planets['Mercury'][6], planets['Mercury'][7], planets['Mercury'][8], planets['Mercury'][9],
               planets['Mercury'][10], planets['Mercury'][11], planets['Mercury'][12])

Venus = Planet("Venus", planets['Venus'][0], planets['Venus'][1], planets['Venus'][2], planets['Venus'][3], planets['Venus'][4],
               planets['Venus'][5], planets['Venus'][6], planets['Venus'][7], planets['Venus'][8], planets['Venus'][9],
               planets['Venus'][10], planets['Venus'][11], planets['Venus'][12])

Earth = Planet("Earth", planets['Earth'][0], planets['Earth'][1], planets['Earth'][2], planets['Earth'][3], planets['Earth'][4],
               planets['Earth'][5], planets['Earth'][6], planets['Earth'][7], planets['Earth'][8], planets['Earth'][9],
               planets['Earth'][10], planets['Earth'][11], planets['Earth'][12])

Mars = Planet("Mars", planets['Mars'][0], planets['Mars'][1], planets['Mars'][2], planets['Mars'][3], planets['Mars'][4],
               planets['Mars'][5], planets['Mars'][6], planets['Mars'][7], planets['Mars'][8], planets['Mars'][9],
               planets['Mars'][10], planets['Mars'][11], planets['Mars'][12])

Jupiter = Planet("Jupiter", planets['Jupiter'][0], planets['Jupiter'][1], planets['Jupiter'][2], planets['Jupiter'][3], planets['Jupiter'][4],
               planets['Mars'][5], planets['Mars'][6], planets['Mars'][7], planets['Mars'][8], planets['Mars'][9],
               planets['Jupiter'][10], planets['Jupiter'][11], planets['Jupiter'][12])

Saturn = Planet("Saturn", planets['Saturn'][0], planets['Saturn'][1], planets['Saturn'][2], planets['Saturn'][3], planets['Saturn'][4],
               planets['Saturn'][5], planets['Saturn'][6], planets['Saturn'][7], planets['Saturn'][8], planets['Saturn'][9],
               planets['Saturn'][10], planets['Saturn'][11], planets['Saturn'][12])

Uranus = Planet("Uranus", planets['Uranus'][0], planets['Uranus'][1], planets['Uranus'][2], planets['Uranus'][3], planets['Uranus'][4],
               planets['Uranus'][5], planets['Uranus'][6], planets['Uranus'][7], planets['Uranus'][8], planets['Uranus'][9],
               planets['Uranus'][10], planets['Uranus'][11], planets['Uranus'][12])

Neptune = Planet("Neptune", planets['Neptune'][0], planets['Neptune'][1], planets['Neptune'][2], planets['Neptune'][3], planets['Neptune'][4],
               planets['Neptune'][5], planets['Neptune'][6], planets['Neptune'][7], planets['Neptune'][8], planets['Neptune'][9],
               planets['Neptune'][10], planets['Neptune'][11], planets['Neptune'][12])





















