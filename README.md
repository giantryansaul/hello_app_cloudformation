# Hello App Cloudformation
Deploys a simple Flask app to Cloudformation. When you navigate to <ip_address>/hello
the app will return "Hello World".

Uses Centos 7.2

## Install
Please install with Python 3.5, other versions of Python have not yet been tested.

To install dependencies:
`pip install -e .`

## Setup

`python deploy_server.py [--aws] [--keyname] [--chef]`

- `--aws`
    - AWS profile name
    - Default: default
- `--keyname`
    - AWS keypair name to login to server with
    - Default: default
- `--chef`
    - Chef server URL
    - Default: none

## Usage
Navigate to the IP Address created in AWS CloudFormation:
`http://<ip_address>/hello`

The app will display "Hello World"

![Final result](https://i.imgur.com/5o13NLl.png)

## Troubleshooting
- Login as the `centos` user when trying to SSH.