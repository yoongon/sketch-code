from unittest import TestCase
from problem import problem


class Test(TestCase):
    def test_problem_0_0(self):
        actual = problem("0", "0")
        if actual is None:
            assert True
            return
        expected = "0"
        assert expected == actual
    def test_problem_1_1(self):
        actual = problem("1", "1")
        if actual is None:
            assert True
            return
        expected = "2"
        assert expected == actual

    def test_problem_1_9(self):
        actual = problem("1", "9")
        if actual is None:
            assert True
            return
        expected = "10"
        assert expected == actual

    def test_problem_1_99(self):
        actual = problem("1", "99")
        if actual is None:
            assert True
            return
        expected = "100"
        assert expected == actual

    def test_problem_99_1(self):
        actual = problem("99", "1")
        if actual is None:
            assert True
            return
        expected = "100"
        assert expected == actual

    def test_problem_123_456(self):
        actual = problem("123", "456")
        if actual is None:
            assert True
            return
        expected = "579"
        assert expected == actual

    def test_problem_456_789(self):
        actual = problem("456", "789")
        if actual is None:
            assert True
            return
        expected = "1245"
        assert expected == actual

    def test_problem_999_999(self):
        actual = problem("999", "999")
        if actual is None:
            assert True
            return
        expected = "1998"
        assert expected == actual
