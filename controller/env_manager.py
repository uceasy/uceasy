from jinja2 import Environment, FileSystemLoader
import os


def render_conf_file(name, template_file, **fields):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)

    with open(name, 'w') as file:
        settings = template.render(fields)
        file.write(settings)

    return os.path.isfile(name)
