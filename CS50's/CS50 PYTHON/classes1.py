class Flight():
    def __init___(self, capacity):
        self.capacity = capacity
        self.passenger= []

    def add_passenger(self, name):
        if not self.oper_seats():
            return False
        self.passengers.append(name)
        return  True

    def open_seats(self):
        return self.capacity - len(self.passenger)


flight = Flight(3)

people = ["labanya","toma","robi"]
for person in people:
    #success = flight.add_passenger(person)
    if flight.add_passenger(person):

    if success:
        print(f"Added {person} to flight succcessfully")

    else:
        print(f"No available seats for {person}")