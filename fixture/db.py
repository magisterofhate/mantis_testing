import pymysql.cursors


class DbFixture:

    def __init__(self, host, name, user, pwd):
        self.host = host
        self.name = name
        self.user = user
        self.pwd = pwd
        self.connection = pymysql.connect(host=host, database=name, user=user, password=pwd, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_group_list_from_db(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list")
            for row in cursor:
                (g_id, g_name) = row
        finally:
            cursor.close()
        return group_list

