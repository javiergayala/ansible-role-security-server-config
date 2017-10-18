"""Test the changes in sysctl.conf."""
import os
import re
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('config_line', [
    # Disable ICMP Redirects
    'net.ipv4.conf.all.accept_redirects(\s+)?=(\s+)?0',
    'net.ipv4.conf.default.accept_redirects(\s+)?=(\s+)?0',
    'net.ipv4.conf.all.secure_redirects(\s+)?=(\s+)?0',
    'net.ipv4.conf.default.secure_redirects(\s+)?=(\s+)?0',
])
def test_sysctl_file(host, config_line):
    """Test that certain entries exist in the file."""
    f = host.file('/etc/sysctl.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    regex = re.escape(config_line)
    assert f.contains('^{}$'.format(regex))
