++++++++++++++++++++
stegano web
++++++++++++++++++++

Presentation
============


Usage
=====

Deployment
----------

This application can be deployed on Heroku.

Deploying the application on Heroku
'''''''''''''''''''''''''''''''''''

In brief:

.. code:: bash

    $ git clone https://github.com/cedric/stegano-web.git
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
