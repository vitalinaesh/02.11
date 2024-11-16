import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='logs.log',
    filemode='w',
    format='%(levelname)s %(asctime)s - %(message)s'
)
class Dimensions:
    def __init__(self,width,height,length):
        self.width = width
        self.height = height
        self.length = length

class Animal:
    def __init__(self, weight, width, heigth, length, age):
        try:
            if weight <= 0:
                raise ValueError('Weight must be greater than 0')
            if age <= 0:
                raise ValueError('ge must be greater than 0')

            self.weight = weight
            self.dimensions = Dimensions(width, heigth, length)
            self.age = age

            logging.debug(f'Animal created: Weight={self.weight}, Dimensions=({width}, {height}, {length}), Age={self.age}')
        except Exception as e:
            logging.error(f"Error while creating Animal: {e}")
            raise

    def printanimal(self):
        print(f'Animal weight :{self.weight}')
        print(f'Animal width : {self.dimensions.width}')
        print(f'Animal heigth : {self.dimensions.height}')
        print(f'Animal length : {self.dimensions.length}')
        print(f'Animal age : {self.age}')

        logging.debug(f"Animal info: weight={self.weight}, width={self.dimensions.width}, "
                      f"height={self.dimensions.height}, length={self.dimensions.length}, age={self.age}")


try:
    Panda = Animal("70 кг", 1420, 70, "1.2 м", 10)
    randomtvarina = Animal(-10, 70, 55, 88, 89)
    Panda.printanimal()
    randomtvarina.printanimal()

except Exception as e:
    print(f"Error: {e}")