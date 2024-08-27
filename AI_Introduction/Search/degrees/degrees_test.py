# Test for "degrees" challenge of Harvard's CS50AI course

from degrees import load_data, person_id_for_name, shortest_path

load_data("large")


def test0():
    source = person_id_for_name("Jennifer Lawrence")
    target = person_id_for_name("Tom Hanks")
    assert len(shortest_path(source, target)) == 2
