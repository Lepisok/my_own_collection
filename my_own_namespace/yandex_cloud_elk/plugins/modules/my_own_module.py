#!/usr/bin/python

# Copyright: (c) 2023, Aleksandr Podkopaev
# MIT License
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import os

DOCUMENTATION = r'''
---
module: create_file

short_description: Create .txt file

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description:  Create .txt file with content at the specified path

options:
    content:
        description: Content for txt file
        required: true
        type: str
    path:
        description: The path to the target file
        required: true
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - apodkopaev.my_collection.my_doc_fragment_name

author:
    - Aleksandr Podkopaev
'''

EXAMPLES = r'''
# Create
- name: Create file
  apodkopaev.my_collection.my_test:
    content: "Test text"
    path: "/tmp/test_my_own_module"
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
if_created:
    description: done
    type: bool
    returned: always
    sample: True
'''
from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        content=dict(type='str', required=True),
        path=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        if_created=False,
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
# if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications

    if not os.path.exists(module.params.get('path')):
        result['changed'] = True
    else:
        with open(module.params['path'], 'r') as f:
            data = file.read()
        result['changed'] = not data == module.params.get('content')

    if module.check_mode:
        module.exit_json(**result)

    with open(module.params['path'], 'w+') as f:
        f.write(module.params.get('content'))
        result['if_created'] = True

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()