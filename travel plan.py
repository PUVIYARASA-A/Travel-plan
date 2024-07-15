class Destination:
    def __init__(self):#constructor
        self.place=""

    def display(self):
        print(self.place)
        
class Trip:
     def __init__(self,place, departure_date, return_date):
        self.place = place
        self.departure_date = departure_date
        self.return_date = return_date
     def __str__(self):
        return f"Trip for {self.place}({self.departure_date} to {self.return_date})"
    
class Itinerary:
    def __init__(self, date):
        self.date = date
        
    def __str__(self):
        return f"Itinerary for {self.date} "
# Example usage:
kerala=Destination()
kerala.place=("Munnar", "Kochi")
kerala.display
karnataka=Destination()
karnataka.place=("Chikmagalur", "Coorg")
karnataka.display
choice = input("Choose your destination (Kerala/Karnataka): ").lower()
print("Departure on 2024-08-15(5pm)")
if choice == "kerala":
    iv_trip = Trip("kerala on", "2024-08-15", "2024-08-17")
    day1_itinerary = Itinerary("2024-08-16")
    print(iv_trip)
    print(day1_itinerary)
    print("day1: Reach Kochi and visit Wonderla")
    day2_itinerary = Itinerary("2024-08-17")
    print(day2_itinerary)
    print("day2: Reach and visit Munnar + Nightstay")
    
elif choice == "karnataka":
    iv_trip = Trip("karnataka on","2024-08-15", "2024-08-17")
    day1_itinerary = Itinerary("2024-08-16")
    print(iv_trip)
    print(day1_itinerary)
    print("day1: Reach Coorg and visit Bamboo Forest")
    day2_itinerary = Itinerary("2024-08-17")
    print(day2_itinerary)
    print("day2: Reach and visit Chikmagalur")
print("Will reach home on 2024-08-18")

