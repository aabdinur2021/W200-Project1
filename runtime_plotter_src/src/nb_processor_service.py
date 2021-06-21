from nb_executor import NotebookExecutor
from hist_plotter import HistogramPlotter
from no_content_nb_error import NoContentNotebookError


class NBService:
    """
        Service to process all notebook elements
    """

    def __init__(self, notebook_data):
        self.notebook_data = notebook_data

    def process(self):
        """
        Process all the cells from the notebook provided
        :return: None
        """

        # If the notebook has no cells, return an error
        if len(self.notebook_data) < 1:
            raise NoContentNotebookError(len(self.notebook_data))

        # Setup the executor for this service
        nb_executor = NotebookExecutor(self.notebook_data)
        execution_times = nb_executor.execute()

        # Setup histogram plotter to plot histogram
        hist_plot = HistogramPlotter(execution_times)
        hist_plot.plot()

    def get_notebook_data(self):
        return self.notebook_data
