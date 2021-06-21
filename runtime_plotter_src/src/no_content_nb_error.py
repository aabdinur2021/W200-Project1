class NoContentNotebookError(Exception):

    """
    Custom Exception to account for empty notebook
    """

    def __init__(self, size, message="Notebook is empty"):
        self.message = message
        self.size = size
        super().__init__(self.message)

    def __str__(self):
        return f'Notebook size: {self.size}'
