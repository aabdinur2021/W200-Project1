class InvalidNotebookError(Exception):

    """
    Custom Exception to handle notebook with no code cells
    """

    def __init__(self, size, message="Notebook has no valid code to execute"):
        self.message = message
        self.size = size
        super().__init__(self.message)

    def __str__(self):
        return f'Number of Notebook cells with code: {self.size}'
