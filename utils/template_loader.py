from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))


def load_template(name):
    return env.get_template(name)