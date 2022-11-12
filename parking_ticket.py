
class ParkingGarage ():
    
    def __init__ (self, tickets, parkingSpaces, currentTicket, money):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.money = int

    def takeTicket(self):
        if self.tickets == 0:
            print("Sorry the parking garage if full")
        else: 
            self.tickets -= 1
            self.parkingSpaces -= 1
            print(f"parking spot left: {self.tickets}")
            print(f"parking spot left: {self.parkingSpaces}")
        
    def currentTickets(self):
        self.currentTicket["status"] = "not paid"
        print(self.currentTicket)
        

    def payForParking(self):
        if self.tickets == 20:
            print("The garage is empty, are you sure the car is in here? ")
        else: 
            self.money = int(input("The parking is gonna be 2$, (type '2' to prove your payment) "))
            if self.money == 2:
                self.currentTicket["status"] = "paid"
                print(self.currentTicket)
                print("The parking was successfully paid, you can leave the parking within the next 15 minutes ")
            if self.money != 2:
                self.currentTicket["status"] = "not paid"
                
    def leaveGarage(self):
        if self.currentTicket["status"] == "paid":
            print("Have a nice day! ")
            self.tickets += 1
            self.parkingSpaces += 1
            print(f"parking spot left: {self.tickets}")
            print(f"parking spot left: {self.parkingSpaces}")
        if self.currentTicket["status"] == "not paid":
            print("Sorry you need to pay the entire amount, try again")
        
        
    
cuneoParking = ParkingGarage(20, 20, {}, 2)
    
def run():
    while True:
        response = input("Do you want to enter or leave the garage? (enter/leave)")
        
        if response.lower() == "enter":
                cuneoParking.takeTicket()
                cuneoParking.currentTickets()
            
        elif response.lower() == "leave":
            cuneoParking.payForParking()
            cuneoParking.leaveGarage()
            
        else:
            ("Can you answer again? ")
            
        
run()