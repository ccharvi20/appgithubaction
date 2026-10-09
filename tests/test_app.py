from githubactions_demo import greet


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_named_user():
    assert greet("Alice") == "Hello, Alice!"
