import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Successfully connected...')
    print('#' * 20)

    try:
        # delete table
        # with connection.cursor() as cursor:
        #     delete_query = "DROP TABLE `author`"
        #     cursor.execute(delete_query)
        #     connection.commit()

        # delete data
        with connection.cursor() as cursor:
            delete_data = "DELETE FROM `users` WHERE user_id = 1"
            cursor.execute(delete_data)
            connection.commit()

        # update data
        with connection.cursor() as cursor:
            update_query = "UPDATE `users` SET password = 'xxxxxx' WHERE user_id = 1;"
            cursor.execute(update_query)
            connection.commit()
            print("Update is done!")
            print("#" * 20)

        # select all data from table
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `users`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("#" * 20)

        # creating table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `author`(id int," \
        #                          "name VARCHAR(32)," \
        #                          "password VARCHAR(32));"
        #     cursor.execute(create_table_query)
        #     print("Table create successfully")

        # insert data to table
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users`(user_id, user_name, password)" \
        #                    "VALUES (1, 'Kirill', 'querty');"
        #     cursor.execute(insert_query)
        #     connection.commit()
    finally:
        connection.close()
except Exception as ex:
    print('Connection refused...')
    print(ex)
