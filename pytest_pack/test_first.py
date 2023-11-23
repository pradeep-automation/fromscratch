import unittest

import pytest


@pytest.mark.usefixtures("set_up")
class TestClass:

    def test_one(self):
        print("\n I am first test")

    def test_two(self):
        print("\n I am second test")

    def test_three(self, data_load):
        name = "Pradeep"
        assert name == data_load[0], "name doesn't match"
        print("succeeded")

    def test_four(self, cross_browser):
        print(f"Running for the user---->{cross_browser[1]}")
# @pytest.fixture
# def set_up():
#     print("\n I run before every test")
#     yield
#     print("I run after every test")

    def test_title(self, cross_browser):
        if cross_browser[0] == "chrome":
            title = "Google Chrome"
        elif cross_browser[0] == "ff":
            title = "Mozilla Firefox"
        else:
            title = "Internet Explorer"
        print(f"Testing in {title}")

    @pytest.mark.parametrize("login", ["user1", "user2"])
    def test_login(self, login):
        print(f"logged in as {login}")


