# AWS CLI CONFIG role for Ansible

Installs and configures the AWS CLI for conveniently interacting with AWS services such as S3, EC2, etc.

![CI](https://travis-ci.org/mcdir/aws-config-cli.svg?branch=master)

## Requirements

-   Ansible 2.4+

#### Compatibility matrix

- Ubuntu 16.04 
- Ubuntu 18.04 
- Ubuntu 20.04 
- CentOS 7.x


## Role Variables

The default variables are as follows:

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

