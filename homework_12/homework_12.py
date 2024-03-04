class Train:

    def __init__(self, number, length):
        self.number = number
        self.length = length
        self.train_carts = [Traincart(self, i) for i in range(1, self.length)]

    def train_route(self):
        routes = {
            0: "DEPO",
            1: "London - Hogwarts",
            2: "Hogwarts - London",
            3: "Kyiv - Mariupol",
            4: "Mariupol - Kyiv",
            5: "Kherson - Sevastopol",
            6: "Sevastopol - Kherson"
        }
        print(f"Train {self.number} is heading to {routes.get(self.number, 'an unknown station')}")

    def magnification(self, amount):
        if amount > 0:
            self.length += amount
            self.train_carts = [Traincart(self, i) for i in range(1, self.length)]

    def reduction(self, amount):
        if amount > 0:
            self.length -= amount
            self.train_carts = [Traincart(self, i) for i in range(1, self.length)]

    def lan(self):
        print(f"Train length: {self.length}")

    def traincarts(self):
        if not self.train_carts:
            print("The train has only a locomotive")
        else:
            for cart in self.train_carts:
                result = cart.get_passengers()
                if result["passengers"] == "absent":
                    print(f"Traincart {result['traincart']}: No passengers")
                else:
                    print(f"Traincart {result['traincart']}:")
                    for passenger in result["passengers"]:
                        print(f"\t{passenger}")

class Traincart:

    def __init__(self, train, number):
        self.train = train
        self.number = number
        self.passengers = []

    """def add_passenger(self, passenger_name, destination, place):
        if len(self.passengers) < 10 and 1 <= place <= 10:
            passenger_data = {
                "passenger_name": passenger_name,
                "destination": destination,
                "place": place
            }
            self.passengers.append(passenger_data)
            print(f"Passenger {passenger_name} added to Traincart {self.number}")
        else:
            print(f"Cannot add passenger to Cart {self.number}. Invalid place or cart is full.")"""

    def add_passenger(self, passenger_name, destination, place):
        if len(self.passengers) < 10 and place <= 10 * self.number :
            passenger_data = {
                "passenger_name": passenger_name,
                "destination": destination,
                "place": place
            }
            self.passengers.append(passenger_data)
            print(f"Passenger {passenger_name} added to Traincart {self.number}")
        else:
            print(f"Cannot add passenger to Cart {self.number}. Invalid place or cart is full.")

    def get_passengers(self):
        if not self.passengers:
            return {"traincart": self.number, "passengers": "absent"}
        else:
            result = []
            for passenger in self.passengers:
                result.append(passenger)
            return {"traincart": self.number, "passengers": result}


hogwarts_express = Train(1,4)
hogwarts_express.lan()
hogwarts_express.magnification(3)
hogwarts_express.lan()
hogwarts_express.reduction(2)
hogwarts_express.lan()
hogwarts_express.traincarts()
hogwarts_express.train_route()
hogwarts_express.train_carts[0].add_passenger("Harry Potter", "Hogwarts", 1)
hogwarts_express.train_carts[0].add_passenger("Hermione Granger", "Hogwarts", 2)
hogwarts_express.train_carts[0].add_passenger("Ron Weasley", "Hogwarts", 3)
hogwarts_express.lan()
hogwarts_express.traincarts()

freedom_train = Train(3,5)
freedom_train.train_carts[0].add_passenger("Taras Shevchenko", "Mariupol", 1),
freedom_train.train_carts[0].add_passenger("Lesya Ukrainka", "Mariupol", 2),
freedom_train.train_carts[0].add_passenger("Ivan Franko", "Mariupol", 3),
freedom_train.train_carts[0].add_passenger("Volodymyr Vernadsky", "Melitopol", 4),
freedom_train.train_carts[0].add_passenger("Hryhoriy Skovoroda", "Kharkiv", 5)
freedom_train.train_carts[0].add_passenger("Ivan Mazepa", "Berdyansk", 6),
freedom_train.train_carts[0].add_passenger("Bohdan Khmelnytsky", "Berdyansk", 7),
freedom_train.train_carts[0].add_passenger("Symon Petliura", "Zaporizhzhia", 8),
freedom_train.train_carts[0].add_passenger("Stepan Bandera", "Mariupol", 9),
freedom_train.train_carts[0].add_passenger("Dmytro Dontsov", "Kharkiv", 10),
freedom_train.train_carts[1].add_passenger("Pavlo Skoropadskyi", "Berdyansk", 11),
freedom_train.train_carts[1].add_passenger("Olena Teliha", "Melitopol", 12),
freedom_train.train_carts[1].add_passenger("Mykhailo Hrushevskyi", "Mariupol", 13),
freedom_train.train_carts[1].add_passenger("Ivan Nechuy-Levytsky", "Berdyansk", 14),
freedom_train.train_carts[1].add_passenger("Nina Matviyenko", "Zaporizhzhia", 15),
freedom_train.train_carts[1].add_passenger("Borys Hrinchenko", "Kharkiv", 16),
freedom_train.train_carts[1].add_passenger("Panteleimon Kulish", "Melitopol", 17),
freedom_train.train_carts[1].add_passenger("Hnat Khotkevych", "Mariupol", 18),
freedom_train.train_carts[1].add_passenger("Mykhailo Drahomanov", "Berdyansk", 19),
freedom_train.train_carts[1].add_passenger("Ostap Vyshnya", "Melitopol", 20),
freedom_train.train_carts[2].add_passenger("Petro Mohyla", "Zaporizhzhia", 21),
freedom_train.train_carts[2].add_passenger("Solomiya Krushelnytska", "Berdyansk", 22),
freedom_train.train_carts[2].add_passenger("Mykola Amosov", "Melitopol", 23),
freedom_train.train_carts[2].add_passenger("Ivan Kotliarevsky", "Berdyansk", 24),
freedom_train.train_carts[2].add_passenger("Vasyl Stus", "Berdyansk", 25),
freedom_train.train_carts[2].add_passenger("Olga Kobylianska", "Chernivtsi", 26),
freedom_train.train_carts[2].add_passenger("Mykola Lysenko", "Melitopol", 27),
freedom_train.train_carts[2].add_passenger("Volodymyr Zelensky", "Melitopol", 28),
freedom_train.train_carts[3].add_passenger("Serhiy Nigoyan", "Donetsk", 39),
freedom_train.train_carts[3].add_passenger("Ivan Kozhedub", "Melitopol", 40)
freedom_train.traincarts()