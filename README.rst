++++++++++++++++++++
Cédric, on mange où?
++++++++++++++++++++

Presentation
============

If you don't know where to lunch, you can:

* ask to Cédric and wait for an eventual answer, or;
* simply ``curl https://cedric-onmange-ou.herokuapp.com/json``.

Just create a pull request if you want to add a restaurant.
Available restaurants are specified in the file *restaurants.json*.



Usage
=====

Deployment
----------

This application can be deployed both on Heroku and on Google App Engine.

Deploying the application on Heroku
'''''''''''''''''''''''''''''''''''

In brief:

.. code:: bash

    $ git clone https://gitlab.com/cedric/cedric-onmange-ou.git
    $ cd cedric-onmange-ou/
    $ heroku create --region=eu stegano-web
    $ heroku buildpacks:add --index 1 heroku/python
    $ heroku buildpacks:add --index 2 https://github.com/heroku/heroku-buildpack-nodejs
    $ git push heroku master
    $ heroku ps:scale web=1
    $ heroku open

The JCDecaux and OpenRouteService API keys are not mandatory.

`Heroku demo instance <https://cedric-onmange-ou.herokuapp.com>`_.


Querying the application
------------------------

Basic usage
'''''''''''

.. code:: bash

    $ curl https://cedric-onmange-ou.herokuapp.com/json


Alternatively you can specify your current location:

.. code:: bash

    $ curl https://cedric-onmange-ou.herokuapp.com/json?latitude=<latitude>&longitude=<longitude>


HTML rendering
''''''''''''''

Simply remove the string *json* from the URL:
https://cedric-onmange-ou.herokuapp.com
Your browser will be asked to share your location. You can deny the request.


Speech synthesis
''''''''''''''''

.. code:: bash

    $ sudo apt install espeak jq
    $ curl --silent https://cedric-onmange-ou.herokuapp.com/json | jq '.name' | espeak -v fr-fr --stdin


User preferences
''''''''''''''''

The possibility to send its preferences is offered to the user.
This can be achieved by sending a JSON file which contains weights associated to the restaurants.

.. code:: bash

    $ curl -X POST -d @preferences.json https://cedric-onmange-ou.herokuapp.com/json --header "Content-Type:application/json"

Result:

.. code-block:: javascript

    {
      "coordinates": "",
      "name": "La Perla",
      "url": "http://www.coque.lu/en/page/la-perla"
    }

Here is an example of *preferences.json* file:

.. code-block:: javascript

    [
        {
            "name": "Vapiano",
            "weight": 2
        },
        {
            "name": "EXKi",
            "weight": 3
        },
        {
            "name": "L'Antica-Roma",
            "weight": 1
        },
        {
            "name": "La Perla",
            "weight": 2
        },
        {
            "name": "Chillers",
            "weight": 4
        },
        {
            "name": "Asie Gourmande",
            "weight": 1
        }
    ]

A restaurant with a weight set to 0 won't be proposed to the user.


Get the list of all available restaurants
'''''''''''''''''''''''''''''''''''''''''

.. code:: bash

    $ curl https://cedric-onmange-ou.herokuapp.com/list/json

To view all restaurants on a map point your browser to https://cedric-onmange-ou.herokuapp.com/list.



License
=======

`Cédric, on mange où? <https://gitlab.com/cedric/cedric-onmange-ou>`_
is under `AGPLv3 <http://www.gnu.org/licenses/agpl-3.0.txt>`_ license.



Contact
=======

`My home page <https://www.cedricbonhomme.org/>`_.
