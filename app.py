from eve import Eve
import json
from pprint import pprint
from tasks import Tasks


# Function to queue tasks when they are created in the API
def tasks_insert_callback(documents):
  # Get name of task to execute, and arguments
  task = documents[0]['task']
  args = documents[0]['args']
  
  # Execute the task with the arguments
  taskResult = Tasks.__dict__[task].apply_async(*args)

  # Update document with task id and current status
  documents[0]['_id'] = taskResult.id
 

# Function to update task status when its looked up
def tasks_fetch_callback(response):
  task = Tasks.app.AsyncResult(response['_id'])
  response['status'] = task.status
  response['result'] = {
    "output" : task.result,
    "error" : task.traceback
  }
# Define app
app = Eve()

# Add task processing hooks
app.on_insert_tasks += tasks_insert_callback
app.on_fetched_item_tasks += tasks_fetch_callback

# Start app
if __name__ == '__main__':
  app.run(port=8080)
