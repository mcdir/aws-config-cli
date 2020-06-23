# AWS CLI CONFIG role for Ansible

Installs and configures the AWS CLI for conveniently interacting with AWS services such as S3, EC2, etc.

## Requirements

-   Ansible 2.4+

#### Compatibility matrix


| Ubuntu 14.04 | :no_entry: | :no_entry:| :no_entry:| :no_entry:| :no_entry:| :no_entry:| :no_entry:|
| Ubuntu 16.04 | :no_entry: | :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:|
| Debian 8.x | :no_entry: | :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:|
| Debian 9.x | :no_entry: | :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:|
| CentOS 6.x | :no_entry: | :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:|
| CentOS 7.x | :no_entry: | :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:| :white_check_mark:|
| CentOS 8.x | :no_entry: | :grey_question:| :grey_question:| :grey_question:| :grey_question:| :grey_question:| :grey_question:|
| Fedora latest | :no_entry: | :x:| :x:| :x:| :x:| :x:| :x:|

- :white_check_mark: - tested, works fine
- :warning: - Not for production use
- :grey_question: - will work in the future (help out if you can)
- :interrobang: - maybe works, not tested
- :no_entry: - Has reached End of Life (EOL)

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

