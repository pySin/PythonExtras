# Test for "degrees" challenge of Harvard's CS50AI course
from degrees import load_data, person_id_for_name, shortest_path

load_data("large")


def test0():
    source = person_id_for_name("Jennifer Lawrence")
    target = person_id_for_name("Tom Hanks")
    assert len(shortest_path(source, target)) == 2


def test1():
    source = person_id_for_name("Emma Watson")
    target = person_id_for_name("Jennifer Lawrence")
    assert len(shortest_path(source, target)) == 3


def test_zero_degree():
    source = person_id_for_name("Tim Zinnemann")
    target = person_id_for_name("Lahcen Zinoun")
    assert shortest_path(source, target) is None


def test_one_degree():
    source = person_id_for_name("Tom Cruise")
    target = person_id_for_name("Lea Thompson")
    assert len(shortest_path(source, target)) == 1


def test_two_degree():
    source = person_id_for_name("Tom Cruise")
    target = person_id_for_name("Tom Hanks")
    assert len(shortest_path(source, target)) == 2
