name = 'Chris'
major = 'Computer Engineering'

def get_my_name():
    first_name = 'Zongru'
    return name


def get_my_major():
    return major


def change_my_name(new_name):
    global name
    name = new_name


def change_my_major(new_major):
    global major
    major = new_major