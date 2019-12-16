import pymysql.cursors
from model.project import Project
import itertools


class DbFixture:

    def __init__(self, host, name, user, pwd):
        self.host = host
        self.name = name
        self.user = user
        self.pwd = pwd
        self.connection = pymysql.connect(host=host, database=name, user=user, password=pwd, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_project_list_from_db(self):
        project_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name from mantis_project_table")
            for row in cursor:
                (p_id, p_name) = row
                project_list.append((Project(id=p_id, name=p_name)))
        finally:
            cursor.close()
        return project_list

    def get_all_project_ids(self):
        converter = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from mantis_project_table")
            for row in cursor:
                (p_id) = row
                converter.append(p_id)
        finally:
            cursor.close()
        id_list = list(itertools.chain(*converter))
        return id_list

