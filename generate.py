#!/usr/bin/env python
# Simple script to generate aws-vault / aws config files

import hcl
import os

from argparse import ArgumentParser
from jinja2 import Environment, FileSystemLoader

MASTER_ACCOUNT_ID = '177680776199'
MASTER_ACCOUNT_NAME = 'mozilla-itsre'

root = os.path.dirname(os.path.abspath(__file__))
cwd = os.path.dirname(__file__)


def load_tfvars_file(tfvar_file):

    try:
        with open(tfvar_file, 'r') as fp:
            obj = hcl.load(fp)
        return obj['delegated_account_ids_map']
    except Exception as e:
        print(f'There was an error opening file: {e}')
        raise(e)


def render_template(template_dir, template_file, **kwargs):

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)
    return template.render(**kwargs)


if __name__ == '__main__':

    parser = ArgumentParser()

    parser.add_argument('-u', '--username', dest='username',
                        required=True, help='Your username')
    parser.add_argument('-i', '--input', default='terraform.tfvars',
                        dest='input_name', help='Name of terraform tfvar file')
    parser.add_argument('--master-account-id', default=MASTER_ACCOUNT_ID,
                        dest='master_account_id', help='Master account ID')
    parser.add_argument('--master-account-name', default=MASTER_ACCOUNT_NAME,
                        dest='master_account_name', help='Master account name')
    parser.add_argument('--template-directory', default=cwd,
                        dest='template_directory',
                        help='Directory to find templates in')
    parser.add_argument('-t', '--template', default='config.tmpl',
                        dest='template',
                        help='Read jinja2 template from FILE')

    args = parser.parse_args()

    hcl_object = load_tfvars_file(args.input_name)
    rendered_output = render_template(
                        args.template_directory, args.template,
                        username=args.username,
                        master_account_name=args.master_account_name,
                        master_account_id=args.master_account_id,
                        accounts=hcl_object)
    print(f'{rendered_output}')
