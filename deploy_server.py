import argparse
from datetime import datetime

import boto3
from jinja2 import Template

parser = argparse.ArgumentParser(description='Deploy Hello App')
parser.add_argument('--aws', type=str, default='default',
                    help='AWS Profile')
parser.add_argument('--keyname', type=str, default='default',
                    help='Keyname to use to connect to server')
parser.add_argument('--chef', type=str, default='none',
                    help='Chef host URL')
cl_args = parser.parse_args()
aws_profile = cl_args.aws

session = boto3.Session(profile_name=aws_profile)
client = session.client('cloudformation')


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
            userdata=format_cf_join(userdata_template.render(
                chef_url=cl_args.chef,
                hello_app=hello_app
            )),
            keyname=cl_args.keyname
    )


def main():
    client.create_stack(
        StackName='hello-app-{}'.format(datetime.today().strftime("%Y%m%d%H%M%S")),
        TemplateBody=create_cloudformation_template()
    )


if __name__ == '__main__':
    main()
