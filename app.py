from eve import Eve
import json
from pprint import pprint
from tasks import Tasks


# Function to queue tasks when they are created in the API
def tasks_insert_callback(documents):
  # Get name of task to execute, and arguments
  task = documents[0]['task']
  args = documents[0]['args']
  print len(args) 
  
  # Execute the task with the arguments
  taskResult = Tasks.__dict__[task].delay(*args)

  # Update document with task id and current status
  documents[0]['task_id'] = taskResult.id

# Function to update task status when its looked up
def tasks_fetch_callback(response):
  task = Tasks.app.AsyncResult(response['task_id'])
  response['status'] = task.status

# Define app
app = Eve()

# Add task processing hooks
app.on_insert_tasks += tasks_insert_callback
app.on_fetched_item_tasks += tasks_fetch_callback

# Start app
if __name__ == '__main__':
  app.run()
