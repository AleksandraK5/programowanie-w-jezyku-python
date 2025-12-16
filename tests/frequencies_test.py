import pytest
from frequencies import word_frequencies


def test_word_frequencies():
    assert (word_frequencies("To be or not to be") ==
            {"to": 2, "be": 2, "or": 1, "not": 1})
    assert word_frequencies("Hello, hello!") == {"hello": 2}
    assert word_frequencies("") == {}
    assert word_frequencies("Python Python python") == {"python": 3}
    assert (word_frequencies("Ala ma kota, a kot ma Ale.") ==
            {"a": 1, "ala": 1, "ale": 1, "kot": 1, "kota": 1, "ma": 2})
