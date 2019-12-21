Retry-requests
##############
Configures the passed-in `requests' <http://python-requests.org>`_ ``Session``
to retry on failed requests due to connection errors, timeouts,
specific HTTP response codes (5XX by default) and 30X redirections
—anything that could fail.

Python 3.6+.

Basic usage:

.. code-block:: python

  from retry_requests import retry
  my_session = retry()
  my_session.get("http://foo.bar")

Using your session and configurations:

.. code-block:: python

  from retry_requests import retry
  from requests import Session
  my_session = retry(Session(), retries=5, backoff_factor=0.2)
  my_session.get('https://foo.bar')

Note that you have a ``TSession``, a ``Session`` with a default timeout,
and ``RSession``, a ``Session`` with a timeout that always ``raise_for_status()``,
for your convenience.

Heavily inspired from `Peterbe.com <https://www.peterbe.com/plog/
best-practice-with-retries-with-requests>`_. Thank you!

Installing
**********
Just ``pip install retry-requests``.

Testing
*******
Clone this project and then, at its root directory, run ``python setup.py test``.
Note that you need an active Internet connection to run the tests.
