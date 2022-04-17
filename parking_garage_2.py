class ParkingGarage():
    def __init__(self):
        self.ticket = ['1', '2', '3', '4', '5', '6','7', '8','9','10']
        self.parking_spaces = ['1', '2', '3', '4', '5', '6','7', '8','9','10']
        self.current_tickets = {}
        self.paid = False

    def take_ticket(self, ticket):
        # for ticket in self.ticket:
        if self.ticket and self.parking_spaces == 0:
            print("sorry we are full")
        if len(self.ticket) and len(self.parking_spaces) > 0:
            show_ticket = self.ticket.pop(0)
            self.parking_spaces.pop(0)
            self.current_tickets.update({show_ticket:self.paid})  
            print(f"please take ticket number {show_ticket}" )
        print(self.current_tickets)
        
            
        


    def pay_for_parking(self, pay):
        
        if pay in self.current_tickets:
            print(f"please pay ticket number {pay}" )
            if pay in self.current_tickets:
                self.paid = True
                paid = self.current_tickets.pop(pay.lower(), self.paid)
                self.ticket.append(pay)
                # self.parking_spaces.append(pay)
                print(self.current_tickets)
                print(paid)
                print(f'tickets left: {self.ticket}')
                print(f"Thank you for paying ticket number {pay} you have 15 minutes to leave")
        else:
            print("please enter correct ticket number")

    def leave_garage(self,leave):
        
        if leave in self.ticket:
            self.parking_spaces.append(leave)
            print(f'spaces left: {self.parking_spaces}')
            print(f'tickets left: {self.ticket}')
            print(f'spaces dictionary: {self.current_tickets}')
            print("thank you have a nice day")
        else:
            print("please pay before exiting")
 

class UI():
    def __init__(self):
        self.parking_garage = ParkingGarage()


    def garage_parking(self):
        while True:
    #Press a button and take a tickets  
            ticket = input("What would you like to do: Park, Pay or Leave? ")
            if ticket.lower() == 'park':
                self.parking_garage.take_ticket(ticket)
                
        
            if ticket.lower() == 'pay':
                pay = input("Please enter your ticket number")
                self.parking_garage.pay_for_parking(pay)
                    
                

            elif ticket.lower() == "leave":
                leave = input("Please Enter your ticket number ").lower()
                self.parking_garage.leave_garage(leave)
                

            
        

def main():
    ui = UI()
    ui.garage_parking()

if __name__ =="__main__":
    main()
                    
                    