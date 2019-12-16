from fixture.helpers import Helpers as helpers


class ProjectOps:
    def __init__(self, app):
        self.app = app
        self.helpers = helpers(self.app)

    def create_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[@class='btn btn-primary btn-white btn-round']").click()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").send_keys(project.desc)
        self.pick_state(project.state)
        self.pick_visibility(project.visibility)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()


    def pick_state(self, state_id):
        wd = self.app.wd
        select = self.app.select
        dropdown = select(wd.find_element_by_xpath("//select[@name='status']"))
        dropdown.select_by_value(str(state_id))

    def pick_visibility(self, vis_id):
        wd = self.app.wd
        select = self.app.select
        dropdown = select(wd.find_element_by_xpath("//select[@name='view_state']"))
        dropdown.select_by_value(str(vis_id))

    def delete_project(self, name):
        # name = 'Test_project_1'
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        self.helpers.wait_for_element("//input[@type='submit']")
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()

