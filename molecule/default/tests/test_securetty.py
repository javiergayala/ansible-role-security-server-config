"""Test the changes in /etc/securetty to disable anon root logins."""
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# Not using paramterize because this is faster.
def test_valid_securetty(host):
    """Test that certain entries exist in the file."""
    f = host.file('/etc/securetty')
    content = f.content

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert b'console' in content
    assert b'vc/1' in content
    assert b'vc/2' in content
    assert b'vc/3' in content
    assert b'vc/4' in content
    assert b'vc/5' in content
    assert b'vc/6' in content
    assert b'vc/7' in content
    assert b'vc/8' in content
    assert b'vc/9' in content
    assert b'vc/10' in content
    assert b'vc/11' in content
    assert b'tty1' in content
    assert b'tty2' in content
    assert b'tty3' in content
    assert b'tty4' in content
    assert b'tty5' in content
    assert b'tty6' in content
    assert b'tty7' in content
    assert b'tty8' in content
    assert b'tty9' in content
    assert b'tty10' in content
    assert b'tty11' in content


def test_invalid_securetty(host):
    """Test that certain entries do not exist in the file."""
    f = host.file('/etc/securetty')
    content = f.content

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert b'ttyS0' not in content
    assert b'ttysclp0' not in content
    assert b'sclp_line0' not in content
    assert b'3270/tty1' not in content
    assert b'hvc[0-9]+' not in content
    assert b'hvc1' not in content
    assert b'hvc2' not in content
    assert b'hvc3' not in content
    assert b'hvc4' not in content
    assert b'hvc5' not in content
    assert b'hvc6' not in content
    assert b'hvc7' not in content
    assert b'hvsi0' not in content
    assert b'hvsi1' not in content
    assert b'hvsi2' not in content
    assert b'xvc0' not in content
