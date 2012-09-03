django-staticfiles-lessjs
=========================
Less.js meets Django staticfiles


Usage
-----
This application is meant to be used with `django-staticfiles`_.  Make sure
that staticfiles setup and configured, then install this application using
`pip`_:

::

	pip install django-staticfiles-lessjs

Finally, make sure that `lessjs` is listed in your ``INSTALLED_APPS``.  You
can use this oneliner to add it as well:

::

	INSTALLED_APPS += ['lessjs', ]


Build
-----
`Less.js`_ packages pre-built versions of the code in its Git repository.
No further tools are necessary to build it.  See ``support/build.py`` for more
information on how data is transferred from the submodule to the Python
package.



.. _django-staticfiles: https://github.com/jezdez/django-staticfiles
.. _pip: http://www.pip-installer.org/
.. _Less.js: http://lesscss.org/
