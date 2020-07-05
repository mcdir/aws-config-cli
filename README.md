- [AWS CLI CONFIG role for Ansible](#aws-cli-config-role-for-ansible)
  - [Description](#description)
  - [This role features](#this-role-features)
  - [Requirements](#requirements)
      - [Compatibility](#compatibility)
- [Installation](#installation)
- [Usage](#usage)
  - [Role variables](#role-variables)
  - [The default variables are as follows](#the-default-variables-are-as-follows)
  - [Example Playbook](#example-playbook)
    - [Results](#results)


# AWS CLI CONFIG role for Ansible

## Description


Installs and configures the [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/) for conveniently 
interacting with AWS services such as S3, EC2, etc.

[![Build Status](https://travis-ci.org/mcdir/aws-config-cli.svg?branch=master)](https://travis-ci.org/mcdir/aws-config-cli)
[![Ansible role](https://img.shields.io/ansible/role/49459.svg?style=flat)](https://galaxy.ansible.com/mcdir/aws_config_cli)
[![Ansible role quality](https://img.shields.io/ansible/quality/49459.svg?style=flat)](https://galaxy.ansible.com/badpacketsllc/aws_cli)
[![License](https://img.shields.io/github/license/mcdir/aws-config-cli.svg?style=flat)](https://github.com/mcdir/aws-config-cli/blob/master/LICENSE)


## This role features
- Full test coverage.
- Support for most major platforms.


## Requirements

- Ansible 2.4+

#### Compatibility

- Ubuntu 16.04 
- Ubuntu 18.04 
- Ubuntu 20.04 
- CentOS 7.x
- Fedora 27
- Fedora 28
- Fedora 29
- Fedora 30
- Debian Stretch
- Debian Buster

# Installation


Using `ansible-galaxy`:

```shell
$ ansible-galaxy install mcdir.aws-config-cli
```

Using `requirements.yml`:

```yaml
---
- src: mcdir.aws-config-cli
```

Using `git`:

```shell
$ git clone https://github.com/mcdir/aws-config-cli.git
```

# Usage

## Role variables


| variable name              | default value                                                                                                                                                    | description                                                                                                   | required |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------|
| aws_cli_user               | [{{ ansible_user }}](https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html?highlight=ansible_user#variables-discovered-from-systems-facts) | name of the user who will run the `aws` command                                                               | no       |
| aws_cli_user_group         | `{{ ansible_user }}`                                                                                                                                             | group of the user who will run the `aws` command                                                              | no       |
| aws_config_cli_config      | none                                                                                                                                                             | `aws` [profile names](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)           | no       |
| aws_config_cli_credentials | none                                                                                                                                                             | aws iam [secret access key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) | no       |


## The default variables are as follows

    aws_config_cli_packages:
      - python3-pip
      - python3-setuptools

    # Package states: ( present | latest )
    aws_config_cli_packages_state: present

    aws_config_cli_user: 'ubuntu'
    aws_config_cli_group: 'ubuntu'
    aws_config_cli_config:
      default:
        output: 'json'
        region: 'ap-southeast-2'
    aws_config_cli_credentials:
      default:
        aws_access_key_id: 'YOUR_ACCESS_KEY_ID'          # Don't version this or put it on pastebin
        aws_secret_access_key: 'YOUR_SECRET_ACCESS_KEY'

## Example Playbook

    - hosts: 'servers'
      roles:
        - role: 'dstil.aws-cli'
          aws_config_cli_user: 'ubuntu'
          aws_config_cli_group: 'ubuntu'
          aws_config_cli_config:
            default:
              output: 'json'
              region: 'ap-southeast-2'
          aws_config_cli_credentials:
            default:
              aws_access_key_id: 'YOUR_ACCESS_KEY_ID'          # Don't version this or put it on pastebin
              aws_secret_access_key: 'YOUR_SECRET_ACCESS_KEY'


### Results

```shell
$ cat ~/.aws/config
# Ansible managed

[default]
region = us-east-1
output = text

$ cat ~/.aws/credentials
# Ansible managed

[default]
aws_access_key_id = AWS_ACCESS_KEY_ID
aws_secret_access_key = AWS_SECRET_ACCESS_KEY

```
