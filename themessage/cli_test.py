import themessage
from themessage import cli
from click.testing import CliRunner
import pytest


@pytest.mark.parametrize('command', (
    'login',
    'publish',
    'version',
))
def test_blank(command):
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert command in result.output


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--version'])
    assert result.exit_code == 0
    assert themessage.__version__ in result.output
