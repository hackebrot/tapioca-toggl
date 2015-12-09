Tapioca-Toggl
=============

|gitter| |pypi| |pyversions| |license|

.. |gitter| image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/hackebrot/tapioca-toggl
   :target: https://gitter.im/hackebrot/tapioca-toggl?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |pypi| image:: https://img.shields.io/pypi/v/tapioca-toggl.svg
   :target: https://pypi.python.org/pypi/tapioca-toggl
   :alt: PyPI Package

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/tapioca-toggl.svg
   :target: https://pypi.python.org/pypi/tapioca-toggl/
   :alt: PyPI Python Versions

.. |license| image:: https://img.shields.io/pypi/l/tapioca-toggl.svg
   :target: https://pypi.python.org/pypi/tapioca-toggl
   :alt: PyPI Package License

Python wrapper for `Toggl API v8`_

Installation
------------

**tapioca-toggl** is available for download from `PyPI`_ via `pip`_::

    $ pip install tapioca-toggl

.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi

Usage
-----

Create a new API instance using either ``access_token`` or ``user`` and ``password``.

Now you can simply send requests using the available endpoints as follows:

.. code-block:: python

    from tapioca_toggl import Toggl

    api = Toggl(access_token='{your-access-token}')

    me = api.me_with_related_data().get().data()

Documentation
-------------

For a list of all of the available endpoints, please consult `resource_mapping.py`_.

You can find more information on Tapioca at the `Tapioca-Wrapper docs`_.

.. _`resource_mapping.py`: https://github.com/hackebrot/tapioca-toggl/blob/master/tapioca_toggl/resource_mapping.py
.. _`Tapioca-Wrapper docs`: http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html


Code of Conduct
---------------

Everyone interacting in the Tapioca-Toggl project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/

License
-------

Distributed under the terms of the `MIT`_ license, Tapioca-Toggl is free and open source software

.. _`MIT`: http://opensource.org/licenses/MIT
.. _`Toggl API v8`: https://github.com/toggl/toggl_api_docs
