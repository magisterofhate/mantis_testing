import random
import re
import string
from fixture.db import DbFixture as db
from model.project import Project
from sys import maxsize


def rnd_string(length):
    symbols = string.ascii_letters + " "*10 + string.digits
    return ''.join(random.choice(symbols) for i in range(random.randrange(length)))


def rnd_big_text_field():
    symbols = string.ascii_letters + " " * 10 + string.digits + "\n" * 5
    return ''.join(random.choice(symbols) for i in range(70))


def clear_data(s):
    return re.sub("\s{2,}", " ", s.strip(' '))


def generate_project(p_id=maxsize, p_type=True):
    if p_type:
        new_name = clear_data(rnd_string(30))
        new_desc = rnd_big_text_field()
        new_state = chose_rnd_state()
        new_inherit = True
        new_visibility = choose_rnd_visibility()
        new_id = p_id
    else:
        new_name = 'New Custom Group'
        new_desc = 'Some description'
        new_state = 10
        new_inherit = True
        new_visibility = 10
        new_id = p_id
    return Project(id=new_id, name=new_name, state=new_state, inherit=new_inherit, visibility=new_visibility,
                   desc=new_desc)


def chose_rnd_state():
    state_list = [10, 30, 50, 70]
    return random.choice(state_list)


def choose_rnd_visibility():
    vis_list = [10, 50]
    return random.choice(vis_list)

