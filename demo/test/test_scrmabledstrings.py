import scrmabledstrings
import sys
import pytest
from filehandler import load_input,load_dictionary


def test_find_anagrams():
    data = load_dictionary("test/test_dictionary.txt")
    input_data = load_dictionary("test/test_scrambled.txt")
    result = scrmabledstrings.find_anagrams(data)
    assert sorted(result) == sorted(input_data)


def test_comparison(capsys):
    scrambled_data = load_dictionary("test/test_scrambled.txt")
    input_string = load_input("test/test_input.txt")
    scrmabledstrings.comparison(scrambled_data,input_string)
    out, err = capsys.readouterr()
    assert out.rstrip() == "Case #1: 2"
