+++++++++++
stegano web
+++++++++++

Presentation
============

This web application uses the `Stegano <https://pypi.org/project/stegano>`_ library.

Usage
=====

Deployment
----------

Deploying the application on Heroku
'''''''''''''''''''''''''''''''''''

.. code:: bash

    $ git clone https://github.com/cedricbonhomme/stegano-web.git
    $ cd stegano-web/
    $ heroku create --region=eu stegano-web
    $ heroku buildpacks:add --index 1 heroku/python
    $ heroku buildpacks:add --index 2 https://github.com/heroku/heroku-buildpack-nodejs
    $ git push heroku master
    $ heroku ps:scale web=1
    $ heroku open


Contact
=======

`My home page <https://www.cedricbonhomme.org/>`_.
