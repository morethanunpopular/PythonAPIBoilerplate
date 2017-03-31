# Python API Boilerplate

This repository contains a Python API boilerplate that combines Eve.py, Celery, and Flask-SocketIO. The purpose of this Boilerplate is to create a flexibile starting place from which the backend of most modern web applications can be built -- including CRUD operations on backend data, the execution of background tasks, and the creation of Pub/Sub endpoints. 

Eve.py powers CRUD operations via a highly explicit and well structured RESTful API. This is the core of this boilerplate. Eve makes it super easy to specify the schemas of a data object, and then run CRUD operations on instances of these data objects.

To avoid REST and RPC cross polination, this boilerplates thinks of background tasks as "creating instances of a given task" and not directly performing a remote procedue. To this end, the code in this repository creates a "tasks" endpoint for the creation and reading of background tasks. You can then poll the new resource representing the task for its status to see once it completes. 

If polling to check a tasks status is not optimal for your usecase, or you need a background task to return data to the client in real time, you can use the simple pubsub application included in this repository as a starting place for pushing data to the client side in real time. 
