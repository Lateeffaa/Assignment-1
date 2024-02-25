class User:
    '''
    Class to represent a User
    '''
    def __init__(self, f_name, l_name, dob, booking_reference_num, passport):
        self._f_name = f_name #first name
        self._l_name = l_name #last name
        self._dob = dob #date of birth
        self._booking_reference_num = booking_reference_num
        self._passport = passport # passport number
#setter and getter methods for the attributes above
    def get_f_name(self):
        return self._f_name
    def set_f_name(self, f_name):
        self._f_name = f_name

    def get_l_name(self):
        return self._l_name
    def set_l_name(self, l_name):
        self._l_name = l_name

    def get_dob(self):
        return self._dob
    def set_dob(self, dob):
        self._dob = dob

    def get_booking_reference_num(self):
        return self._booking_reference_num
    def set_booking_reference_num(self, booking_reference_num):
        self._booking_reference_num = booking_reference_num

    def get_passport(self):
        return self._passport
    def set_passport(self, passport):
        self._passport = passport

#authenticate the user login with the provided username and password
    def login(self, username, password):
        if username == "example_username" and password == "example_password":
            return True
        else:
            return False
#book a flight for the user with the given information
    def bookFlight(self, departure, arrival, date):
        if departure == "Chicago" and arrival == "New York" and date == "06-12-2020":
            return True
        else:
            return False

    def retrieveBoardingPass(self, booking_reference):
        if booking_reference == self._booking_reference_num:
            return True
        else:
            return False






'''
Class to represent the National Airlines system
'''
from enum import Enum
class class_type(Enum):
    economy = "Economy class"
    business = "Business class"
    first = "First class"
class NAsystem:
    def __init__(self, departure_t, arrival_t, flight_num, from_location, to_location, gate, terminal, class_type):
        self.departure_t = departure_t
        self.arrival_t = arrival_t
        self.flight_num = flight_num
        self.from_location = from_location
        self.to_location = to_location
        self.gate = gate
        self.terminal = terminal
        self.class_type = class_type

#setter and getter methods for the attributes above
    def get_departure_t(self):
        return self.departure_t
    def set_departure_t(self, departure_t):
        self.departure_t = departure_t

    def get_arrival_t(self):
        return self.arrival_t
    def set_arrival_t(self, arrival_t):
        self.arrival_t = arrival_t

    def get_flight_num(self):
        return self.flight_num
    def set_flight_num(self,flight_num):
        self.flight_num = flight_num

    def get_from_location(self):
        return self.from_location
    def set_from_location(self,from_location):
        self.from_location = from_location

    def get_to_location(self):
        return self.to_location
    def set_to_location(self,to_location):
        self.to_location = to_location

    def get_gate(self):
        return self.gate
    def set_gate(self,gate):
        self.gate = gate

    def get_terminal(self):
        return self.terminal
    def set_terminal(self,terminal):
        self.terminal = terminal

    def get_class_type(self):
        return self.class_type
    def set_class_type(self,class_type):
        self.class_type = class_type

#generates a boarding pass for the user based on the booking information
    def generateBoardingPass(self, user):
        boarding_pass = BoardingPass(user.get_f_name() + " " + user.get_l_name(), self.from_location, self.to_location, "2024-03-01", self.departure_t, self.arrival_t,self.terminal, self.gate, "07:30", self.flight_num, "TCKT001", "09A")
        return boarding_pass

    def updatePassengerInformation(self, user, new_info):
        user.set_f_name(new_info.get_f_name())
        user.set_l_name(new_info.get_l_name())
        user.set_dob(new_info.get_dob())
        user.set_passport(new_info.get_passport())
        return "Personal information is updated successfully."


'''
Class to represent the National Airlines employee
'''
from enum import Enum
class class_t(Enum):
    Manager = "Manager"
    FlightAttendant = "Flight Attendant"
    Op_management = "Operation Management"
    PS_agent = "Passenger Service Agent"


class NAemployee:
    def __init__(self, e_f_name, e_l_name, emp_id, emp_email, department):
        self._e_f_name = e_f_name
        self._e_l_name = e_l_name
        self._emp_id = int(emp_id)
        self._emp_email = emp_email
        self._department = department

    # setter and getter methods for the attributes above
    def get_e_f_name(self):
        return self._e_f_name

    def set_e_f_name(self, e_f_name):
        self._e_f_name = e_f_name

    def get_e_l_name(self):
        return self._e_l_name

    def set_e_l_name(self, e_l_name):
        self._e_l_name = e_l_name

    def get_emp_id(self):
        return self._emp_id

    def set_emp_id(self, emp_id):
        self._emp_id = emp_id

    def get_emp_email(self):
        return self._emp_email

    def set_emp_email(self, emp_email):
        self._emp_email = emp_email

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    # verify identity of user
    def verifyIdentity(self, user):
        if user.get_booking_reference_num() == self._emp_id:
            return True
        else:
            return False

    # updates users personal information
    def updatePersonalInformation(self, user, new_info):
        user.set_f_name(new_info.get_f_name())
        user.set_l_name(new_info.get_l_name())
        user.set_dob(new_info.get_dob())
        user.set_passport(new_info.get_passport())
        return "Personal information is updated successfully."

    # resolve issues with the boarding pass
    def resolveBoardingPassIssue(self, boarding_pass):
        print("Issue with boarding pass resolved. New boarding pass issued.")
        return "New boarding pass issued."







'''
Class to represent the boarding pass
'''
class BoardingPass:
    def __init__(self, passenger_name, from_location, to_location, date, departure_t, arrival_t, terminal, gate, boarding_t, flight_num, ticket_num, seat_num):
        self.passenger_name = passenger_name
        self.from_location = from_location
        self.to_location = to_location
        self.date = date
        self.departure_t = departure_t
        self.arrival_t = arrival_t
        self.terminal = terminal
        self.gate = gate
        self.boarding_t = boarding_t
        self.flight_num = flight_num
        self.ticket_num = ticket_num
        self.seat_num = seat_num
#setter and getter methods for the attributes above
    def get_passenger_name(self):
        return self.passenger_name
    def set_passenger_name(self, passenger_name):
        self.passenger_name = passenger_name

    def get_from_location(self):
        return self.from_location
    def set_from_location(self, from_loc):
        self.from_location = from_loc

    def get_to_location(self):
        return self.to_location
    def set_to_location(self, from_loc):
        self.from_location = from_loc

    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date

    def get_departure_t(self):
        return self.departure_t
    def set_departure_t(self, departure_t):
        self.departure_t = departure_t

    def get_arrival_t(self):
        return self.arrival_t
    def set_arrival_t(self, arrival_t):
        self.arrival_t = arrival_t

    def get_terminal(self):
        return self.terminal
    def set_terminal(self, terminal):
        self.terminal = terminal

    def get_gate(self):
        return self.gate
    def set_gate (self, gate):
        self.gate = gate

    def get_flight_num(self):
        return self.flight_num
    def set_flight_num (self, flight_num):
        self.flight_num = flight_num

    def get_boarding_t(self):
        return self.boarding_t
    def set_boarding_t(self, boarding_t):
        self.boarding_t = boarding_t

    def get_flight_num(self):
        return self.flight_num
    def set_flight_num(self, flight_num):
        self.flight_num = flight_num

    def get_ticket_num(self):
        return self.ticket_num
    def set_ticket_num(self, ticket_num):
        self.ticket_num = ticket_num

    def get_seat_num(self):
        return self.seat_num
    def set_seat_num (self, seat_num):
        self.seat_num = seat_num

# displays boarding pass details
    def displayDetails(self):
        print("Passenger Name: ", self.passenger_name)
        print("Travelling From: ", self.from_location)
        print("Travelling To: ", self.to_location)
        print("Date: ", self.date)
        print("Departure Time: ", self.departure_t)
        print("Arrival Time: ", self.arrival_t)
        print("Terminal: ", self.terminal)
        print("Gate: ", self.gate)
        print("Boarding Time: ", self.boarding_t)
        print("Flight Number: ", self.flight_num)
        print("Ticket Number: ", self.ticket_num)
        print("Seat Number: ", self.seat_num)



#sample testing class 1 using objects:
user1 = User("James", "Smith", "20-3-1999", "12ABC34", "HZ244DP2")
print("Passenger name: ", user1._f_name, user1._l_name)
print("Date of Birth: ", user1._dob)
print("Booking reference number: ", user1._booking_reference_num)
print("Passport number: ", user1._passport)
print("Login username: ", user1.login("example_username", "example_password"))
print("Flight: ", user1.bookFlight("Chicago", "New York", "06-12-2020"))
print("Boarding pass number: ", user1.retrieveBoardingPass("12ABC34"))

#sample testing class 2 using objects:
system1 = NAsystem("06-12-2020 at 11:20AM", "06-12-2020 at 13:30PM", "NA4321", "Chicago", "New York", "Gate 3", "Terminal 2", class_type.first)
print("Departure Time: ", system1.get_departure_t())
print("Arrival Time: ", system1.get_arrival_t())
print("Flight Number: ", system1.get_flight_num())
print("Travelling From: ", system1.get_from_location())
print("Travelling To:", system1.get_to_location())
print("Gate: ", system1.get_gate())
print("Terminal: ", system1.get_terminal())
print("Class Type: ", system1.get_class_type())
boarding_pass = system1.generateBoardingPass(user1)
print("Generated Boarding Pass: ", boarding_pass)

#sample testing class 3 using objects:
employee1 = NAemployee("Lateefa", "Bani Malek", 202213598, "lateefa.A.BaniMalek@example.com", class_t.Manager)
print("First Name:", employee1.get_e_f_name())
print("Last Name:", employee1.get_e_l_name())
print("Employee ID:", employee1.get_emp_id())
print("Employee Email:", employee1.get_emp_email())
print("Department:", employee1.get_department())

user_verification = User("James", "Smith", "20-3-1999", "12345", "HZ244DP2")
print("Identity Verified:", employee1.verifyIdentity(user_verification))

#sample testing class 4 using objects:
# Creating an object of the BoardingPass class
boarding_pass = BoardingPass("Athbah Abdulla", "Chicago", "New York", "2024-03-01", "09:00", "11:30", "Terminal 1", "Gate 5", "08:30", "FL123", "TCKT001", "14A")

boarding_pass.set_passenger_name("Lily Smith")
boarding_pass.set_from_location("Los Angeles")
boarding_pass.set_to_location("London")
boarding_pass.set_date("2024-03-02")
boarding_pass.set_departure_t("10:30")
boarding_pass.set_arrival_t("15:00")
boarding_pass.set_terminal("Terminal 3")
boarding_pass.set_gate("Gate 8")
boarding_pass.set_boarding_t("09:45")
boarding_pass.set_flight_num("FL456")
boarding_pass.set_ticket_num("TCKT002")
boarding_pass.set_seat_num("20B")
boarding_pass.displayDetails()