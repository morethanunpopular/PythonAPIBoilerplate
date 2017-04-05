#Global Settings
XML = False
DEBUG = True
X_DOMAINS = [ "http://127.0.0.1:5000"]
X_HEADERS = [ "Origin", "X-Requested-With", "Content-Type", "Accept", "Authorization", "If-Match" ]
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
  '_id': {
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
  'item_url': 'regex("[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}")',

  # Configure endpoint to return task_id when task is created
  'extra_response_fields': ['task_id'],

  # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

  # Most global settings can be overridden at resource level
    'resource_methods': ['POST' ],
    'item_methods': ['GET', 'PATCH'],
  'schema': TaskSchema
}
DOMAIN = {'tasks': tasks}
