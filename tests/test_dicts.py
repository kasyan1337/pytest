import pytest

from utils import dicts


@pytest.fixture
def data():
    return [[{"vcs": "mercurial"}, "vcs", None, "mercurial"],
            [{"vcs": "mercurial"}, "vcs", "git", "mercurial"],
            [{}, "vcs", "git", "git"],
            [{}, "vcs", "bazaar", "bazaar"]]


def test_get_val(data):
    for dict_input, key, def_val, expected in data:
        if def_val is None:
            assert dicts.get_val(dict_input, key) == expected
        else:
            assert dicts.get_val(dict_input, key, def_val) == expected
