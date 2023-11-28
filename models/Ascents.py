from datetime import datetime

from  models.Model import Model

class Mountains(Model):
    __nameTable = 'Ascents'
    __id = 'id'
    __name = 'name'
    __start_time = 'start_time'
    __finish_time = 'finish_time'

    def get(self):
        return super().get(self.__nameTable)
    def get_oneStroke(self, id):
        return super().get_oneStroke(self.__nameTable, id)
    def get_oneField(self, field):
        return super().get_oneField(self.__nameTable, field)
    def add(self):
        name = input("Введите название восхождения ")
        start_time = input("Введите время начала по типу (1 окт. 2023 г., 12:00:00)")
        finish_time = input("Введите время завершения по типу (1 окт. 2023 г., 12:00:00) ")
        str = f"{self.__name} , {self.__start_time}, {self.__finish_time}"
        super().add(self.__nameTable, str, name , start_time, finish_time)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить ")
        field = input("Введите название поля ")
        values = input("Введите новое значение ")
        super().update(self.__nameTable,id,field,values)