import pytest
import requests.exceptions

from retry_requests import RSession, TSession, retry


def test_retry_failure(caplog):
    """Retries the default number of times an non-existing URL."""
    session = retry()
    with pytest.raises(requests.exceptions.ConnectionError):
        session.get("http://this-does-not-exist.bar")
    assert (
        "Retry(total=0, connect=0, read=3, redirect=None, status=None)"
        in caplog.records[2].message
    )
    assert (
        "Retry(total=1, connect=1, read=3, redirect=None, status=None)"
        in caplog.records[1].message
    )
    assert (
        "Retry(total=2, connect=2, read=3, redirect=None, status=None)"
        in caplog.records[0].message
    )


def test_retry_failure_post(caplog):
    """Retries in a non-idempotent method such as a POST."""
    session = retry(session=RSession(), status_to_retry=(200,), retries=1)
    with pytest.raises(requests.exceptions.RetryError):
        session.post("http://example.com")


def test_retry_success():
    """Gets a successful URL."""
    session = retry()
    session.get("https://example.com")


def test_retry_with_session():
    my_session = requests.Session()
    session = retry(my_session)
    assert session is my_session
    session.get("http://example.com")


def test_t_session():
    my_session = TSession()
    my_session.get("http://example.com")


def test_r_session():
    my_session = RSession()
    with pytest.raises(requests.exceptions.HTTPError):
        my_session.post("https://google.com")
