import json

class Planets:

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

