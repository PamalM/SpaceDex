import json
from texttable import Texttable

#Class for planets and their attributes/information.
class Planet:

    #Constructor method to initialize attributes.
    def __init__(self, name, mass, planetType, radius, density, lengthOfYear,
                 lengthOfDay, numberOfMoons, equatorialIncilination, meanOrbitVelocity, averageOrbitDistance, volume, escapeVelocity, surfaceGravity):
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

    def comparePlanets(self, planet2):
        #Print table displaying both planets attributes side by side.
        t = Texttable(max_width=140)
        t.add_row(["Planet:", "", self.name, planet2.name])
        t.add_row(["Mass:", "", self.mass, planet2.mass])
        t.add_row(["Radius:", "", self.radius, planet2.radius])
        t.add_row(["Density:", "", self.density, planet2.density])
        t.add_row(["Length of Year:", "", self.lengthOfYear, planet2.lengthOfYear])
        t.add_row(["Length of Day:", "", self.lengthOfDay, planet2.lengthOfDay])
        t.add_row(["# Moons:", "", self.numberOfMoons, planet2.numberOfMoons])
        t.add_row(["Equatorial Incinination:", "", self.equatorialIncilination, planet2.equatorialIncilination])
        t.add_row(["Mean Orbit Velocity:", "", self.meanOrbitVelocity, planet2.meanOrbitVelocity])
        t.add_row(["Average Orbit Distance:", "", self.averageOrbitDistance, planet2.averageOrbitDistance])
        t.add_row(["Volume:", "", self.volume, planet2.volume])
        t.add_row(["Escape Velocity:", "", self.escapeVelocity, planet2.escapeVelocity])
        t.add_row(["Surface Gravity:", "", self.surfaceGravity, planet2.surfaceGravity])
        print(t.draw())

        # Compare the two planets on some select attributes.
        print("____________________________________________________")
        print(f"[{self.name}]: Larger mass" if (self.mass > planet2.mass) else f"[{planet2.name}]: Larger mass")
        print(f"[{self.name}]: Larger radius" if (self.radius > planet2.radius) else f"[{planet2.name}]: Larger mass")
        print(f"[{self.name}]: Larger density" if (self.density > planet2.density) else f"[{planet2.name}]: Larger mass")
        print(f"[{self.name}]: Larger mean orbit velocity" if (self.meanOrbitVelocity > planet2.meanOrbitVelocity) else f"[{planet2.name}]: Larger mean orbit velocity")
        print(f"[{self.name}]: Larger average orbit distance" if (self.averageOrbitDistance > planet2.averageOrbitDistance) else f"[{planet2.name}]: Larger average orbit distance")
        print(f"[{self.name}]: Larger volume" if (self.volume > planet2.volume) else f"[{planet2.name}]: Larger volume")
        print(f"[{self.name}]: Larger escape velocity" if (self.escapeVelocity > planet2.escapeVelocity) else f"[{planet2.name}]: Larger escape velocity")
        print(f"[{self.name}]: Larger surface gravity" if (self.surfaceGravity > planet2.surfaceGravity) else f"[{planet2.name}]: Larger surface gravity")
        print("____________________________________________________")

    def displayPlanet(self):
        #Method utilized to display the attributes/stats for one specific planet selected by the user.
        t = Texttable(max_width=140)
        t.add_row(["Planet:", "", self.name])
        t.add_row(["Mass:", "", self.mass])
        t.add_row(["Radius:", "", self.radius])
        t.add_row(["Density:", "", self.density])
        t.add_row(["Length of Year:", "", self.lengthOfYear])
        t.add_row(["Length of Day:", "", self.lengthOfDay])
        t.add_row(["# Moons:", "", self.numberOfMoons])
        t.add_row(["Equatorial Incinination:", "", self.equatorialIncilination])
        t.add_row(["Mean Orbit Velocity:", "", self.meanOrbitVelocity])
        t.add_row(["Average Orbit Distance:", "", self.averageOrbitDistance])
        t.add_row(["Volume:", "", self.volume])
        t.add_row(["Escape Velocity:", "", self.escapeVelocity])
        t.add_row(["Surface Gravity:", "", self.surfaceGravity])
        print(t.draw())


#Class for terminal commands/prompts for user, etc.
class Terminal :

    def initialGreeting(self):
        # Method called to initially prompt user upon first entry to application.
        print("|---------------------------------------------------------------------------|")
        print("|                                [SPACEDEX]                                 |")
        print("|---------------------------------------------------------------------------|")
        print("|     Welcome to SpaceDex, this is an application created by Pamal Mangat.  |")
        print("|     This Python script allows you to view information and even compare    |")
        print("|     planets within our solar system.                                      |")
        print("|                                                                           |")
        print("|     The application itself was created using JSON parsing, and a little   |")
        print("|     bit of magic from python itself and a strong passion for space.       |")
        print("|                                                                           |")
        print("|___________________________________________________________________________|\n")

    def menuSelect(self):
        #Prompt user with menu options and allow them to make a selection.
        print("|---------------------------------------------------------------------------|")
        print("|                                 [MENU]                                    |")
        print("|---------------------------------------------------------------------------|")
        print("|     Press [1] for specific information about one planet                   |")
        print("|     Press [2] to compare two planets                                      |")
        print("|     Press [3] to Exit                                                     |")
        print("|___________________________________________________________________________|\n")

        #Keep prompting user until they enter a valid (1 or 2) input for menu selection.
        #Return the menuSelection and redirect them according to their selection.
        while True:
            try:
                menuSelection = int(input('Please make Selection: '))

                #Valid menu selection, proceed and exit the loop.
                if (menuSelection == 1 or menuSelection == 2 or menuSelection == 3):
                    break

                #The input was a valid number, but not one of the specified menu options.
                else:
                    print("[Invalid selection]")
                    continue

            #Invalid selection. (Non-Numerical etc.)
            except:
                print("[Invalid selection]")

        #Return user's menu selection back to main.
        return menuSelection

    def singlePlanetMenu(self):
        #Present user with single planet submenu.
        print("|---------------------------------------------------------------------------|")
        print("|                             [Planet Index]                                |")
        print("|---------------------------------------------------------------------------|")
        print("|     Press [1] - Mercury                                                   |")
        print("|     Press [2] - Venus                                                     |")
        print("|     Press [3] - Earth                                                     |")
        print("|     Press [4] - Mars                                                      |")
        print("|     Press [5] - Jupiter                                                   |")
        print("|     Press [6] - Saturn                                                    |")
        print("|     Press [7] - Uranus                                                    |")
        print("|     Press [8] - Neptune                                                   |")
        print("|___________________________________________________________________________|\n")

        #Get user input; Determine to make sure it is valid.
        while True:
            try:
                planetSelection = int(input('Enter Planet: '))

                #Valid menu selection, proceed and exit the loop.
                if (planetSelection >= 1 and planetSelection <= 8):
                    break

                #The input was a valid number, but not one of the specified menu options.
                else:
                    print("[Invalid selection]")
                    continue

            #Invalid selection. (Non-Numerical etc.)
            except:
                print("[Invalid selection]")

        #Return planet slection back to the main to determine which planet was selection.
        return planetSelection

    def doublePlanetMenu(self):
        #Present user with double planet menu
        print("|---------------------------------------------------------------------------|")
        print("|                             [Planet Index]                                |")
        print("|---------------------------------------------------------------------------|")
        print("|     Press [1] - Mercury                                                   |")
        print("|     Press [2] - Venus                                                     |")
        print("|     Press [3] - Earth                                                     |")
        print("|     Press [4] - Mars                                                      |")
        print("|     Press [5] - Jupiter                                                   |")
        print("|     Press [6] - Saturn                                                    |")
        print("|     Press [7] - Uranus                                                    |")
        print("|     Press [8] - Neptune                                                   |")
        print("|___________________________________________________________________________|\n")

        #Get user input; Determine to make sure it is valid.
        while True:
            try:
                planetSelection = int(input('Select Planet 1: '))

                #Valid menu selection, proceed and exit the loop.
                if (planetSelection >= 1 and planetSelection <= 8):
                    break

                #The input was a valid number, but not one of the specified menu options.
                else:
                    print("[Invalid selection]")
                    continue

            #Invalid selection. (Non-Numerical etc.)
            except:
                print("[Invalid selection]")

        while True:
            try:
                planetSelection2 = int(input('Select planet 2:'))

                if (planetSelection2 >= 1 and planetSelection2 <= 8 and planetSelection2 != planetSelection):
                    break;

                elif (planetSelection2 == planetSelection):
                    print("[Can't compare the same planets]")
                    continue

                else:
                    print("[Invalid selection]")
                    continue

            except:
                print("[Invalid selection]")


        #Return planet slection back to the main to determine which planet was selection.
        return planetSelection, planetSelection2

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


#Initialize object to start running application.
command = Terminal()
command.initialGreeting()

while True:
    #Recieve menu selection from class and determine which submenu to redirect user to.
    menuSelection = command.menuSelect()

    #Dictionary to have a numerical key associated with a specific planet. To eliminate multiple if/else statements.
    planetIndex = {1:Mercury, 2:Venus, 3:Earth, 4:Mars, 5:Jupiter, 6:Saturn, 7:Uranus, 8:Neptune}

    #User picked to view information/attributes for a specific planet.
    if (menuSelection == 1):

        #Find the selected planet from the dictionary above and print it's attributes.
        selectedPlanet = planetIndex.get(command.singlePlanetMenu())

        #Display it's attributes/statistics.
        selectedPlanet.displayPlanet()

    #User wishes to compare 2 planets from the list.
    elif (menuSelection ==2):

        #Method returns 2 values, = 2 planets (Planet1, Planet2)
        planet = command.doublePlanetMenu()

        #Match the return values with a planet within the list.
        planet1 = planetIndex.get(planet[0])
        planet2 = planetIndex.get(planet[1])

        #Display and compare the planets attributes.
        planet1.comparePlanets(planet2)

    #User wishes to exit the program; Quit the loop.
    else:
        print("[Exiting! - Thank You.]")
        break




















