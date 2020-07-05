import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def config_file(host):
    return host.file('/home/user/.aws/config')


@pytest.fixture()
def credentials_file(host):
    return host.file('/home/user/.aws/credentials')


def test_aws_cli_should_be_installed(host):
    assert host.run('aws --v').rc == 0


def test_aws_cli_files_should_exist(host, config_file, credentials_file):
    assert config_file.exists, credentials_file.exists


def test_region_configured_json_output(host, config_file, credentials_file):
    # print(config_file.content_string)
    # print(credentials_file.content_string)
    assert config_file.contains(
        "[default]\nregion = ap-southeast-2"
    )

    assert credentials_file.contains(
        '[default]\naws_access_key_id = YOUR_ACCESS_KEY_ID'
    )


def test_no_aws_access_key_id_configured_aws_secret_access_key(
        host, credentials_file):
    assert credentials_file.contains(
        '[no_aws_access_key_id]'
    )


def test_no_aws_secret_key_configured_aws_key(host, credentials_file):
    assert credentials_file.contains(
        'YOUR_SECRET_ACCESS_KEY_NO'
    )


def test_no_aws_secret_key_configured_aws_key_id(host, credentials_file):
    assert credentials_file.contains(
        '[no_aws_secret_access_key]'
    )


def test_no_region_configured_json_output(host, config_file):
    assert config_file.contains(
        '[no_region]\noutput = test'
    )


def test_no_output_configured_region(host, config_file):
    assert config_file.contains(
        '[no_output]\nregion = eu-central-1'
    )
