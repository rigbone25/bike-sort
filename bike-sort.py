#gave these some fake values just for test purposes... except wheel_sizes those are real
sub_600 = [1, 2,]
over_600 = [5, 6,]
wheel_sizes = [20, 24, 26, 27.5, 29]
road_bikes = []
mtb_bikes = []

class Inventory_Check:

#this sets up the parameters for an inputted bike and stores them in self (i think?? lol)
    def __init__(self, wheel_size, size, discipline, price):
        self.wheel_size = wheel_size
        self.size = size
        self.discipline = discipline
        self.price = price

#this will sort the given bike into 1 of 2 bins based on price
    def price_sort(self):
        if self.price <= 600:
            sub_600.append(self)
        else:
            over_600.append(self)

#this will group the bike into 1 of 2 bins again, but based on the terrain it is made for
    def bike_terrain(self):
        if self.discipline.lower() == "road":
            road_bikes.append(self)
        elif self.discipline.lower() == "mtb" or "mountain":
            mtb_bikes.append(self)
        else:
            print("Discipline parameter not entered correctly in database; please reformat")


#this is a test bike being put thru my 3 functions, only indices 2 and 3 should be in use right now
bike_1 = Inventory_Check(wheel_sizes[3], "M", "MTB", 1000)

#this calls the bike_terrain functn (which will fill array mtb_bikes) and then prints it as a string
bike_1.bike_terrain()
print(str(mtb_bikes))
