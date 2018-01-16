import os
import themessage


def test_themessage_has_current_version_of_module():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'version.txt')) as version_file:
        assert themessage.__version__ == version_file.read().strip()
