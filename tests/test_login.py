
from fixture.project_operations import ProjectOps
# def test_login(app):
#     print("success")


def test_get_pr_list_by_soap(app):
    po = ProjectOps(app)
    print(po.get_all_projects_by_soap("administrator", "root"))


# def test_login_soap(app):
#     po = ProjectOps(app)
#     assert po.can_login("administrator", "root")
