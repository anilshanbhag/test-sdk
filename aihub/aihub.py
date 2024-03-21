from aihub.api.default_api import DefaultApi
from aihub.api_client import ApiClient
import os

class AIHub:
  def __init__(self, api_key, host='https://aihub.instabase.com', debug=False):
    self.client = ApiClient()
    self.client.configuration.host = host
    self.client.configuration.access_token = api_key
    self.client.configuration.debug = debug
    self.api_instance = DefaultApi(self.client)
    self.batches = self.Batches(self.api_instance)
    self.conversations = self.Conversations(self.api_instance)
    self.apps = self.Apps(self.api_instance)

  class Batches:
    def __init__(self, api_instance):
      self.api_instance = api_instance

    def create(self, name, workspace_name):
      batch = self.api_instance.create_batch({'name': name, 'workspace_name': workspace_name})
      return batch

    def add_file(self, batch_id, file_name, file):
      self.api_instance.add_file_to_batch(batch_id, file_name, file.read())

  class Conversations:
    def __init__(self, api_instance):
      self.api_instance = api_instance

    def create(self, conversation_data):
      response = self.api_instance.create_conversation(conversation_data)
      return response

    def status(self, conversation_id):
      status = self.api_instance.get_conversation(conversation_id)
      return status

    def converse(self, conversation_id, question, document_ids):
      answer = self.api_instance.converse(conversation_id, {'question': question, 'document_ids': document_ids, 'mode': 'default'})
      return answer

  class Runs:
    def __init__(self, api_instance):
      self.api_instance = api_instance

    def create(self, app_name=None, batch_id=None, app_id=None, input_dir=None):
      # Validate that one of app_id or app_name is provided
      if not app_id and not app_name:
          raise ValueError("One of app_id or app_name must be provided.")
      
      # Validate that one of batch_id or input_dir is provided
      if not batch_id and not input_dir:
          raise ValueError("One of batch_id or input_dir must be provided.")
      
      # Construct the dictionary with only the set values
      run_details = {}
      if app_name:
          run_details['name'] = app_name
      elif app_id:  # Use elif because only one of them needs to be set
          run_details['app_id'] = app_id

      if batch_id:
          run_details['batch_id'] = batch_id
      elif input_dir:  # Use elif for the same reason
          run_details['input_dir'] = input_dir
      
      # Call run_app with the constructed dictionary
      job = self.api_instance.run_app(run_details)
      return job

    def status(self, job_id):
      status = self.api_instance.get_run_status(job_id)
      return status

    def list(self):
      # Implement based on your SDK capabilities
      pass

  class Apps:
    def __init__(self, api_instance):
      self.api_instance = api_instance
      self.runs = AIHub.Runs(api_instance)
