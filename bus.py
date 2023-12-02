# admin user
class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.from_des = from_des
        self.to = to
        self.departure = departure
        self.seat = ["Empty" for i in range(20)]


class Phitron:
    total_bus = 5
    total_bus_lst = []

    def add_bus(self):
        bus_no = int(input("Enter but no : "))

        flag = 1
        for w in self.total_bus_lst:
            if bus_no == w["coach"]:
                print("Bus alrady added")
                flag = 0
                break

        if flag:
            bus_driver = input("Enter bus driver name : ")
            bus_arrival = input("Enter bus arrival time : ")
            bus_departure = input("Enter bus deperture time : ")
            bus_from = input("Enter the start from : ")
            bus_to = input("Enter the bus destination : ")
            self.new_bus = Bus(
                bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_to
            )
            self.total_bus_lst.append(vars(self.new_bus))
            print("\n Bus Added Successfull Done")



class Counter(Phitron):
    user_lst = []

    def redervation(self):
        bus_no = int(input("Enter Bus No : "))
        for w in self.total_bus_lst:
            if bus_no == w["coach"]:
                passenger = input("Enter your name : ")
                seat_no = int(input("Enter your seat no : "))

                if seat_no > 20:
                    print("No Seats Available!!!")
                elif w["seat"][seat_no - 1] != "Empty":
                    print("Seat Already Booked")

                else:
                    w["seat"][seat_no - 1] = passenger
            else:
                print("No Bus Available")

        for bus in self.total_bus_lst:
            print(bus["seat"])

    def show_ticket(self):
        bus_no = int(input("Enter Bus Number"))
        for w in self.total_bus_lst:
            if bus_no == w["coach"]:
                print("*" * 50)
                print()
                print(f"{' '*10} {'#'*10} bus info {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t\t Driver :{w['driver']}")
                print(
                    f" arrival : {w['arrival']} \t\t\t Departure Time : {w['departure']} \n From : {w['from_des']} \t\t\t To : {w['to']}"
                )

                print()

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end="\t")
                        a += 1
                        for j in range(2):
                            print(f"{a}. {w['seat'][a-1]}", end="\t")
                            a += 1
                        print()
                    print("*" * 50)

    def get_users(self):
        return self.user_lst

    def crate_account(self):
        name = input("Enter your name : ")
        password = input("Ente your password : ")

        self.new_user = User(name, password)
        self.user_lst.append(vars(self.new_user))

    def available_buses(self):
        if len(self.total_bus_lst) == 0:
            print("No Buses Available")

        else:
            print("*" * 50)
            for bus in self.total_bus_lst:
                print()
                print(f"{' '*10}{'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(
                    f"Bus Number : {bus['coach']} \t Departure time : {bus['departure']} \n From: \t{bus['from_des']} \t\t To: \t{bus['to']}"
                )

                print("*" * 50)


while True:
    company = Phitron()
    b = Counter()
    print("1. Create an account \n2. Login to your account \n3. EXIT")

    user_input = int(input("Enter Your Choich : "))

    if user_input == 3:
        break
    elif user_input == 1:
        b.crate_account()
    elif user_input == 2:
        name = input("Enter your username : ")
        password = input("Enter your password : ")

        flag = 0
        isAdmin = False
        if name == "admin" and password == "123":
            isAdmin = True

        if isAdmin == False:
            for user in b.get_users():
                if user["username"] == name and user["password"] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{''*10} welcome to bus ticket booking system")
                    print("1. Available buses \n2. Show bus info \n3. Reservation \n4. EXIT")
                    a = int(input("Enter your choise : "))
                    if a == 4:
                        break
                    elif a == 1:
                        b.available_buses()
                    elif a == 2:
                        b.show_ticket()
                    elif a == 3:
                        b.redervation()

            else:
                print("No Username Found")
        else:
            while True:
                print(f"\n{''*10} Hello Admin Welcome to bus ticket booking system")
                print("1. Add bus \n2. Available buses \n3. Show bus info \n4. Exit ")
                a = int(input("Eter your chose : "))
                if a == 4:
                    break
                elif a == 1:
                    b.add_bus()
                elif a == 2:
                    b.available_buses()
                elif a == 3:
                    b.show_ticket()


