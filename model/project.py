from sys import maxsize


class Project:
    def __init__(self, id=None, name="New_Project", state=None, inherit=True, visibility=None, desc=None):
        self.name = name
        self.state = state
        self.inherit = inherit
        self.visibility = visibility
        self.desc = desc
        self.id = id

    def __repr__(self):
        return "%s - %s" % (self.id, self.name)

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return (self.id == other.id or self.id == maxsize or other.id == maxsize) \
               and self.name == other.name
