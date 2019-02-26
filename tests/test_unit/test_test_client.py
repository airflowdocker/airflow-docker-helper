import pytest

from airflow_docker_helper.testing import test_client as get_client


def test_sensor_true_assertion():
    client = get_client()

    client.sensor(True)
    client.assert_sensor_called_with(True)

    with pytest.raises(AssertionError):
        client.assert_sensor_called_with(False)


def test_sensor_false_assertion():
    client = get_client()
    client.sensor(False)
    client.assert_sensor_called_with(False)

    with pytest.raises(AssertionError):
        client.assert_sensor_called_with(True)


def test_short_circuited():
    client = get_client()
    client.short_circuit()
    client.assert_short_circuited()

    with pytest.raises(AssertionError):
        client.assert_not_short_circuited()


def test_not_short_circuited():
    client = get_client()
    client.assert_not_short_circuited()

    with pytest.raises(AssertionError):
        client.assert_short_circuited()


def test_branch_to_no_tasks_explicit():
    client = get_client()
    client.branch_to_tasks([])

    client.assert_branched_to_tasks([], written=True)

    with pytest.raises(AssertionError):
        client.assert_branched_to_tasks(['foo'])


def test_branch_to_no_tasks_implicit():
    client = get_client()
    client.assert_branched_to_tasks([], written=False)

    with pytest.raises(AssertionError):
        client.assert_branched_to_tasks(['foo'])


def test_branch_to_task_but_not_written_raises():
    client = get_client()

    with pytest.raises(AssertionError):
        client.assert_branched_to_tasks(['foo'], written=False)


def test_branch_to_tasks():
    client = get_client()
    client.branch_to_tasks(['foo', 'bar'])
    client.assert_branched_to_tasks(['bar', 'foo'])


def test_context_accessed_assertion():
    client = get_client()
    client.context()

    client.assert_context_accessed()
