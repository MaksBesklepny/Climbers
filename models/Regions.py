from  models.Model import Model
class Regions(Model):
    __nameTable = 'Regons'
    __id = 'id'
    __country = 'country'
    __region = 'region'

    def get(self):
        return super().get(self.__nameTable)
    def get_oneStroke(self, id):
        return super().get_oneStroke(self.__nameTable, id)
    def get_oneField(self, field):
        return super().get_oneField(self.__nameTable, field)
    def add(self):
        country = input("Введите страну")
        region = input("Введите регион")
        str = f"{self.__country} , {self.__region}"
        super().add(self.__nameTable, str, country, region)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить")
        field = input("Введите название поля")
        values = input("Введите новое значение")
        super().update(self.__nameTable,id,field,values)

