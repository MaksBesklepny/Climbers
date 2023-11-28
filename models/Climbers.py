from  models.Model import Model
class Climbers(Model):
    __nameTable = 'Climbers'
    __name = 'name'
    __address = 'address'
    def get(self):
        return super().get(self.__nameTable)
    def get_oneStroke(self, id):
        return super().get_oneStroke(self.__nameTable, id)
    def get_oneField(self, field):
        return super().get_oneField(self.__nameTable, field)
    def add(self):
        name = input("Введите имя")
        address = input("Введите адрес")
        str = f"{self.__nameTable}, {self.__address}"
        super().add(self.__nameTable, str, name, address)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("Введите новое значение")
        super().update(self.__nameTable,id,field,values)