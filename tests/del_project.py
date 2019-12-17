from fixture.common import generate_project, get_all_projects_for_user_by_soap
from fixture.project_operations import ProjectOps
import random


def test_delete_project(app, db):
    po = ProjectOps(app)
    app.navigation.home_page()
    app.navigation.projects_page()
    if len(db.get_all_project_ids()) == 0:
        po.create_project(generate_project())
    app.navigation.projects_page()
    old_project_list = db.get_project_list_from_db()
    project_to_delete = random.choice(old_project_list)
    po.delete_project(project_to_delete.name)
    new_project_list = db.get_project_list_from_db()
    assert len(new_project_list) == (len(old_project_list) - 1)
    assert project_to_delete not in new_project_list


def test_delete_project_soap_check(app):
    po = ProjectOps(app)
    app.navigation.home_page()
    app.navigation.projects_page()
    if len(get_all_projects_for_user_by_soap("administrator", "root1")) == 0:
        po.create_project(generate_project())
    app.navigation.projects_page()
    old_project_list = get_all_projects_for_user_by_soap("administrator", "root1")
    project_to_delete = random.choice(old_project_list)
    po.delete_project(project_to_delete.name)
    new_project_list = get_all_projects_for_user_by_soap("administrator", "root1")
    assert len(new_project_list) == (len(old_project_list) - 1)
    assert project_to_delete not in new_project_list
