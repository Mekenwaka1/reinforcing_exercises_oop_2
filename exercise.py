class Location:
    def __init__(self, name):
        self.name = name

class Trip:
    def __init__(self):
        self.destinations = []

    def add_destination(self, location):
        self.destinations.append(location)

    def trip_iteration(self):
        numberOfdestinations = len(self.destinations)
        retval = 'Began trip.\n'
        if numberOfdestinations > 1:
            for i in range(1, numberOfdestinations):
                retval += f"Travelled from {self.destinations[i - 1].name} to {self.destinations[i].name}.\n"
        elif numberOfdestinations == 1:
            retval += f"Travelled to {self.destinations[0].name}\n"
        retval += 'Ended trip.'
        return retval

Trips = Trip()
Trips.add_destination(Location('Toronto'))
Trips.add_destination(Location('Ottawa'))
Trips.add_destination(Location('Montreal'))
Trips.add_destination(Location('Quebec City'))
Trips.add_destination(Location('Halifax'))
Trips.add_destination(Location('St. John\'s'))

print(Trips.trip_iteration())





