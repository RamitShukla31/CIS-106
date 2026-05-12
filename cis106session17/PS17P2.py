#Last Name: Ramit Shukla  Date created: 5/11/2026


class Car:

    def __init__(self, make, model, stickerprice):
        self.make = make
        self.model = model
        self.stickerprice = stickerprice

    def discountprice(self):
        return self.stickerprice * 0.90

    def displaycar(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Sticker Price: ${self.stickerprice:.2f}")
        print(f"Discount Price: ${self.discountprice():.2f}")


class Sport(Car):

    def __init__(self, make, model, stickerprice,
                 sportwheels, sportengine, sportinterior):
        
        super().__init__(make, model, stickerprice)

        self.sportwheels = sportwheels
        self.sportengine = sportengine
        self.sportinterior = sportinterior

    def pricewithoptions(self):

        updatedprice = self.discountprice()

        if self.sportwheels.upper() == "Y":
            updatedprice += 1000.00

        if self.sportengine.upper() == "Y":
            updatedprice += 3000.00

        if self.sportinterior.upper() == "Y":
            updatedprice += 2000.00

        return updatedprice


class Luxury(Sport):

    def __init__(self, make, model, stickerprice,
                 sportwheels, sportengine, sportinterior,
                 gpsoption, selfdriving):
        
        super().__init__(make, model, stickerprice,
                         sportwheels, sportengine, sportinterior)

        self.gpsoption = gpsoption
        self.selfdriving = selfdriving

    def pricewithoptions(self):

        updatedprice = super().pricewithoptions()

        if self.gpsoption.upper() == "Y":
            updatedprice += 5000.00

        if self.selfdriving.upper() == "Y":
            updatedprice += 10000.00

        return updatedprice


sportcar = Sport(
    "Ford",
    "Mustang",
    50000,
    "Y",
    "Y",
    "N"
)

luxurycar = Luxury(
    "Tesla",
    "Model S",
    90000,
    "Y",
    "Y",
    "Y",
    "Y",
    "Y"
)

print("Sport Car")
sportcar.displaycar()
print(f"Price With Options: ${sportcar.pricewithoptions():.2f}")

print()

print("Luxury Car")
luxurycar.displaycar()
print(f"Price With Options: ${luxurycar.pricewithoptions():.2f}")

