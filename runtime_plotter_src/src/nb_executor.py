import datetime
from invalid_nb_error import InvalidNotebookError
import logging


class NotebookExecutor:

    def __init__(self, notebook_data):
        self.notebook_data = notebook_data
        self.execution_times = {}

    def execute(self):
        """
        Execute all code cells in the notebook
        :return:
        """

        # Store the execution times of all cells
        self.execution_times = {}
        for i in range(len(self.notebook_data)):
            notebook_element = self.notebook_data[i]

            # Only process code cells
            if notebook_element['cell_type'] == 'code':
                try:
                    start_time = datetime.datetime.now()

                    # provide globals to exec so as to use the global context for processing the request
                    exec(notebook_element['source'], None, globals())
                    execution_time = datetime.datetime.now() - start_time

                    # Calculate the execution time
                    self.execution_times[i] = round(execution_time.total_seconds() * 1000)
                except Exception:

                    # If any exception is encountered, log the exception and process the other requests
                    logging.error("Code can't be executed: " + notebook_element['source'])

        # If no code was executed, throw an invalid request
        if len(self.execution_times) < 1:
            logging.error("No Executable Code Found")
            raise InvalidNotebookError(len(self.execution_times))
        return self.execution_times


