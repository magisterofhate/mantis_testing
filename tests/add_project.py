from fixture.common import generate_project
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
