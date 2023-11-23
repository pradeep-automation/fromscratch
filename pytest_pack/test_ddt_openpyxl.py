import pytest

def test_login(user_creds_xl):
    usr = user_creds_xl["Username"]
    pwd = user_creds_xl["Password"]
    print(f"logging with the credentials::: {usr} and {pwd}")
