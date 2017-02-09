
import boto3
from jinja2 import Template


def format_cf_join(multiline):
    formatted_input = []
    for line in multiline.splitlines():
        formatted_input.append('\"{}\n\"'.format(line))
    return formatted_input

cloudformation_template = Template(open('cf.template').read())
hello_app = open('hello_app.py').read()

userdata_template = Template(open('userdata.sh').read())

print(cloudformation_template.render(
    hello_app=format_cf_join(hello_app),
    userdata=format_cf_join(userdata_template.render()))
)


