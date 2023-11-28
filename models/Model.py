from configuration.config import connection


class Model:
    def get(self,table):
        with connection().cursor() as cursor:
            select_all_rows = f"SELECT * FROM {table}"
            cursor.execute(select_all_rows)
            return cursor.fetchall()
        connection().close()

    def get_oneStroke(self, table, id):
        with connection().cursor() as cursor:
            select_oneStroke = f"SELECT * FROM {table} WHERE id = {id}"
            cursor.execute(select_oneStroke)
            return cursor.fetchone()
        connection().close()

    def get_oneField(self, table, field):
        with connection().cursor() as cursor:
            select_oneField = f"SELECT {field} FROM {table}"
            cursor.execute(select_oneField)
            return cursor.fetchone()
        connection().close()

    def add(self, table, str, *values):
        with connection().cursor() as cursor:
            print(f"INSERT INTO {table} ({str}) VALUES ({values})")
            query = f"INSERT INTO {table} ({str}) VALUES ({values})"
            cursor.execute(query)
            connection().close()
            print(f"Новая запись в таблицу {table} добавлена")

    def delete(self, table, id):
        with connection().cursor() as cursor:
            query_delete = f"DELETE FROM {table} WHERE id = {id}"
            cursor.execute(query_delete)
            connection().commit()
            connection().close()
            print("Запись удалена")

    def update(self, table, id, field, values):
        with connection().cursor() as cursor:
            print(f"UPDATE {table} set {field} = '{values}' where id = {id}")
            query_update = f"UPDATE {table} set {field} = '{values}' where id = {id}"
            cursor.execute(query_update)
            connection().commit()
            connection().close()
            print("Запись обновлена")

