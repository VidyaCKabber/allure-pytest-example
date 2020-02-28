import pytest
import allure


@pytest.mark.skip
def test_m():
    assert True


def test_n():
    assert False


def test_o():
    assert True


def test_p():
    assert False


def test_q():
    assert True


def test_r():
    assert False


def test_s():
    assert True


@pytest.mark.skip
def test_p():
    assert False


def test_q():
    assert True


def test_r():
    assert True


def test_with_trivial_severity_3():
    assert True


def test_with_normal_severity_3():
    assert False


def test_with_trivial_severity_3():
    assert True
