from car import Car

# Constants
CARS = 20


# Class Traffic
class Traffic:

    # Attributes
    car_list = []
    min_velocity = 5
    max_velocity = 10

    def __init__(self):
        self.traffic_list()
        self.limit_line = False

    # Creating a car list
    def traffic_list(self):
        if not self.car_list:
            for i in range(CARS):
                if i % 2 == 0:
                    velocity = self.min_velocity
                else:
                    velocity = self.max_velocity
                car = Car(velocity)
                self.car_list.append(car)

    # Moving all the cars in the car list
    def move_traffic(self):
        for each_car in self.car_list:
            each_car.move()

    # Speeding up all the cars
    def level_up_traffic(self):
        for each_car in self.car_list:
            each_car.set_velocity()

    # Verifying collisions
    def touch(self, turtle_runner):
        for each_car in self.car_list:
            if each_car.distance(turtle_runner) < 30:
                return True
        return False

    # Gets
    def get_car_list(self):
        return self.car_list
