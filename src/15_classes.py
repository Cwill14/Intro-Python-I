# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.latitude = lat
        self.longitude = lon
    def _str_(self):
        return 'latitude: {self.latitude}, longitude: {self.longitude}'.format(self = self)

test1 = LatLon(1, 2)
# print(f'latitude: {test1.latitude}, longitude: {test1.longitude}')
print(test1)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return 'name: {self.name}, latitude: {self.latitude}, longitude: {self.longitude}'.format(self = self)

test2 = Waypoint('alpha', 3, 4)
# print(f'name: {test2.name}, latitude: {test2.latitude}, longitude: {test2.longitude}')
print(test2)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def _str_(self):
        return 'name: {self.name}, difficulty: {self.difficulty}, size: {self.size}, latitude: {self.latitude}, longitude: {self.longitude}'.format(self = self)
test3 = Geocache('bravo', 'hard', 'big', 5, 6)
# print(f'name: {test3.name}, difficulty: {test3.difficulty}, size: {test3.size}, latitude: {test3.latitude}, longitude: {test3.longitude}')
print(test3)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
catacombs = Waypoint("Catacombs", 41.70505, -121.51521)
# print(f'name: {catacombs.name}, latitude: {catacombs.latitude}, longitude: {catacombs.longitude}')
print(catacombs)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
newberry = Geocache('charlie', 'medium', 'small', 7, 8)
print(newberry)
# Print it--also make this print more nicely
# print(geocache)
