from datetime import datetime

import boto3
from jinja2 import Template

session = boto3.Session(profile_name='grs')
client = boto3.client('cloudformation')


def format_cf_join(multiline):
    formatted_input = '[ '
    for line in multiline.splitlines():
        formatted_input += ("\"{}\\n\" ,".format(line))
    return formatted_input.rstrip(',') + ' ]'


def create_cloudformation_template():

    hello_app = open('hello_app.py').read()
    userdata_template = Template(open('userdata.sh').read())
    cloudformation_template = Template(open('cf.template').read())
    return cloudformation_template.render(
            hello_app=format_cf_join(hello_app),
            userdata=format_cf_join(userdata_template.render())
    )


def main():
    client.create_stack(
        StackName='hello-app-{}'.format(datetime.today().strftime("%Y%m%d%H%M%S")),
        TemplateBody=create_cloudformation_template()
    )


if __name__ == '__main__':
    main()
