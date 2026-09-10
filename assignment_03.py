class Car:

    def __init__(self, name, speedLimit):
        self.name = name
        self.speedLimit = speedLimit
        self.speed = 0
        self.isStarted = False

    def start(self):
        self.isStarted = True
        print(self.name, "started.")

    def stop(self):
        self.speed = 0
        self.isStarted = False
        print(self.name, "stopped.")

    def speedUp(self):
        if not self.isStarted:
            print("Please start the car first.")
        elif self.speed + 10 <= self.speedLimit:
            self.speed += 10
            print("Speed increased to:", self.speed, "km/h")
        else:
            print("Cannot exceed speed limit.")

    def speedDown(self):
        if not self.isStarted:
            print("Please start the car first.")
        elif self.speed >= 10:
            self.speed -= 10
            print("Speed decreased to:", self.speed, "km/h")
        else:
            print("Car is already at 0 km/h.")

    def showSpeed(self):
        print("Current Speed:", self.speed, "km/h")


# Creating object
car = Car("BMW", 100)

# Using methods
car.start()

car.showSpeed()

car.speedUp()
car.speedUp()
car.speedUp()

car.showSpeed()

car.speedDown()

car.showSpeed()

car.stop()