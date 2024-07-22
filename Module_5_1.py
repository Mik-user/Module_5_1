class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def goto(self,new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            return print ('Такого этажа не существует')
        else:
            list_floors = list()
            for i in range(new_floor):
                list_floors.append(i+1) # Судя по заданию, здесь можно было поставить print(i+1) и не создавать список
        print(list_floors)

house1 = House('ЖК Эльбрус', 30)
house1.goto(8)
house2 = House('ЖК Нью - Васюки', 40)
house2.goto(41)