class Dimensions:
    def __init__(self,width,height,length):
        self.width = width
        self.height = height
        self.length = length

class Animal:
    def __init__(self, weight, width, heigth, length, age):
        self.weight = weight
        self.dimensions = Dimensions(width, heigth, length)
        self.age = age

    def printanimal(self):
        print(f'Animal weight :{self.weight}')
        print(f'Animal width : {self.dimensions.width}')
        print(f'Animal heigth : {self.dimensions.height}')
        print(f'Animal length : {self.dimensions.length}')
        print(f'Animal age : {self.age}')


Panda = Animal("70 кг", 1420, 70, "1.2 м", 10)
Panda.printanimal()