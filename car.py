class Car:
     def __init__(self, year, brand, model, color, movement):
        self.__year = year
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__movement = movement
    
     def set_year(self, year):
        self.__year = year

     def set_brand(self, brand):
        self.__brand = brand
     
     def set_model(self, model):
        self.__model = model

     def set_color(self, color):
        self.__color = color

     def set_movement(self, movement):
        self.__movement = movement

     def get_year(self):
        return self.__year

     def get_brand(self):
        return self.__brand
     
     def get_model(self):
        return self.__model

     def get_color(self):
        return self.__color
     
     def get_movement(self):
        return self.__movement

class Engine(Car):
    def __init__(self, movement, pistons, engine_name):
        super().__init__(movement)
        self.__pistons = pistons
        self.__engine_name = engine_name
        
    def start_engine(self):
        print(f"The {super().get_brand} {super().get_model()}'s engine is now running.")

    def stop_engine(self):
        print(f"The {super().get_brand} {super().get_model()}'s engine has been stopped.")

class Tires(Car):
    def __init__(self, movement, traction, tire_damage):
        super().__init__(movement)
        self.__traction = traction
        self.__tire_damage = tire_damage

    def move_forward(self):
        print(f'Car is moving {super().get_movement()}')

    def move_backwards(self):
        print(f'Car is moving {super().get_movement()}')

class Steering(Car):
     #Edw prepei na einai ypeuthino gia tin kateuthinsi
     def __init__(self, movement, direction):
        super().__init__(movement)
        self.__direction = direction

    def right(self):
        print(f'Car is moving {super().get_movement()} and {self.direction}')

    def left(self):
        print(f'Car is moving {super().get_movement()} and {self.direction}')

class Brakes(Car):
     #Edw prepei na einai ypeuthino gia tin akinitopoihsh
    def __init__(self, stop_movement):
        self.__stop_movement = stop_movement

    def stop_movement(self):
        print(f'Car stops moving {self.stop_movement}')
     
class Gas_Pedal(Car):
     #Edw prepei otan patietai na prepei na peiraxtei to gear shift
    def __init__(self, movement, acceleration):
        super().__init__(movement)
        self.__acceleration = acceleration

    def accelerate(self):
        print(f'Car is moving {super().get_movement()} and {self.acceleration}')


     
'''
class Gear_Shifter(Car):
    def change_shift():
        if(x>0):
            print()
        elif():
            print()
'''

'''
class Chassis(Car):
     print()

class motor:
     print()

class clutch:
     #Edw prepei otan patietai na prepei na peiraxtei to gear shift
     print()

class exhaust:
     #Edw prepei otan patietai na prepei na peiraxtei to gear shift
     print()

class transmition:
     #Edw prepei na einai ypeuthino gia tin metadwsi kinisis
     print()

class suspension:
     #Edw prepei otan patietai na prepei na peiraxtei to gear shift
     print()
'''


