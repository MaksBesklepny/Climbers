from  models.Model import Model

class Mountains(Model):
    __nameTable = 'Mountains'
    __id = 'id'
    __name = 'name'
    __height = 'height'
    __region_id = 'region_id'

    def get(self):
        return super().get(self.__nameTable)
    def get_oneStroke(self, id):
        return super().get_oneStroke(self.__nameTable, id)
    def get_oneField(self, field):
        return super().get_oneField(self.__nameTable, field)
    def add(self):
        name = input("Введите название горы ")
        height = input("Введите высота ")
        region_id = input("Введите id региона ")
        str = f"{self.__name} , {self.__height}, {self.__region_id}"
        super().add(self.__nameTable, str, name , height, region_id)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить ")
        field = input("Введите название поля ")
        values = input("Введите новое значение ")
        super().update(self.__nameTable,id,field,values)