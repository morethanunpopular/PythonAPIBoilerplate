#Global Settings
XML = False
DEBUG = True

#Database Settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'app'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


#Define task schema -- matches celery task spec
TaskSchema = {
  'task_id': {
    'type': 'string'
  },
   'task': {
    'type': 'string',
    'minlength': 1,
    'maxlength': 100,
    'required': True
  },
  'args': {
    'type': 'list'
  },
  'kwargs': {
    'type': 'list'
  },
  'status': {
    'type': 'string'
  }
}

tasks  = {
  'item_title': 'task',

  # Allow lookups by app name
  'additional_lookup': {
    'url': 'regex(".+")',
    'field': 'task_id'
  },

  # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

  # Most global settings can be overridden at resource level
    'resource_methods': ['POST' ],
    'item_methods': ['GET', 'PATCH'],
  'schema': TaskSchema
}
DOMAIN = {'tasks': tasks}
