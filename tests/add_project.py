from fixture.common import generate_project, get_all_projects_for_user_by_soap
from fixture.project_operations import ProjectOps


def test_add_project(app, db):
    po = ProjectOps(app)
    app.navigation.home_page()
    app.navigation.projects_page()
    old_project_list = db.get_project_list_from_db()
    new_project = generate_project()
    po.create_project(new_project)
    old_project_list.append(new_project)
    new_project_list = db.get_project_list_from_db()
    assert sorted(new_project_list) == sorted(old_project_list)


def test_add_project_soap_check(soap, app):
    po = ProjectOps(app)
    app.navigation.home_page()
    app.navigation.projects_page()
    old_project_list = get_all_projects_for_user_by_soap(soap, "administrator", "root1")
    new_project = generate_project()
    po.create_project(new_project)
    old_project_list.append(new_project)
    new_project_list = get_all_projects_for_user_by_soap(soap, "administrator", "root1")
    assert sorted(new_project_list) == sorted(old_project_list)

