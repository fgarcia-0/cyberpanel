import os
import sys
import types
from unittest.mock import patch

# Add current directory to path so install scripts can be imported as top-level modules
sys.path.append(os.path.dirname(__file__))

# Stub out requests module used in installLog to avoid external dependency during tests
sys.modules.setdefault('requests', types.ModuleType('requests'))
# Stub out MySQLdb module to prevent import errors during tests
sys.modules.setdefault('MySQLdb', types.ModuleType('MySQLdb'))

# Provide a minimal stub for the install module so installCyberPanel can reference install.preFlightsChecks
install_stub = types.ModuleType('install')

class _PreFlights:
    debug = 0

install_stub.preFlightsChecks = _PreFlights
sys.modules['install'] = install_stub

import installCyberPanel  # type: ignore
import install_utils  # type: ignore


def _prep_env():
    os.makedirs('/etc/cyberpanel', exist_ok=True)
    try:
        os.remove('/etc/cyberpanel/mysqlPassword')
    except FileNotFoundError:
        pass


def test_skip_mysql_install_for_remote():
    _prep_env()
    with patch('installCyberPanel.install_utils.call'), \
         patch('installCyberPanel.logging.InstallLog.writeToFile'), \
         patch('installCyberPanel.mysqlUtilities.createDatabase'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installPowerDNSConfigurations'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installPowerDNS'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'startPowerDNS'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installPureFTPD'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installPureFTPDConfigurations'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'startPureFTPD'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installAllPHPVersions'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installLiteSpeed'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'changePortTo80'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'fix_ols_configs'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installMySQL') as mock_install, \
         patch.object(installCyberPanel.InstallCyberPanel, 'changeMYSQLRootPassword') as mock_change_pw, \
         patch.object(installCyberPanel.InstallCyberPanel, 'startMariaDB') as mock_start_db, \
         patch.object(installCyberPanel.InstallCyberPanel, 'fixMariaDB') as mock_fix_db:
        installCyberPanel.Main('/tmp', 'One', install_utils.ubuntu, 0, port='8090', ftp=None, dns=None,
                               publicip=None, remotemysql='ON', mysqlhost='remote', mysqldb='db',
                               mysqluser='user', mysqlpassword='pass', mysqlport='3306')
        assert not mock_install.called
        assert not mock_change_pw.called
        assert not mock_start_db.called
        assert not mock_fix_db.called


def test_local_mysql_triggers_install():
    _prep_env()
    with patch('installCyberPanel.install_utils.call'), \
         patch('installCyberPanel.logging.InstallLog.writeToFile'), \
         patch('installCyberPanel.mysqlUtilities.createDatabase'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installPowerDNSConfigurations'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installPowerDNS'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'startPowerDNS'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installPureFTPD'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installPureFTPDConfigurations'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'startPureFTPD'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installAllPHPVersions'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installLiteSpeed'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'changePortTo80'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'fix_ols_configs'), \
         patch.object(installCyberPanel.InstallCyberPanel, 'installMySQL') as mock_install, \
         patch.object(installCyberPanel.InstallCyberPanel, 'changeMYSQLRootPassword') as mock_change_pw, \
         patch.object(installCyberPanel.InstallCyberPanel, 'startMariaDB') as mock_start_db, \
         patch.object(installCyberPanel.InstallCyberPanel, 'fixMariaDB') as mock_fix_db:
        installCyberPanel.Main('/tmp', 'One', install_utils.ubuntu, 0, port='8090', ftp=None, dns=None,
                               publicip=None, remotemysql='OFF')
        assert mock_install.called
        assert mock_change_pw.called
        assert mock_start_db.called
        assert mock_fix_db.called
