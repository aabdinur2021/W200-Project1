import logging
from flask import request, abort, Blueprint
from nb_processor_service import NBService

from invalid_nb_error import InvalidNotebookError
from no_content_nb_error import NoContentNotebookError


nb_controller_blue_print = Blueprint("nb_processor_controller", __name__)


@nb_controller_blue_print.route('/notebook_data', methods=['POST'])
def notebook_data():
    """
    Exposes a single Flask endpoint which gets all the notebook elements to process
        - In case notebook contains no data or no code cells, throw a 400 bad request
    :return: None
    """

    # POST request
    notebook_elements = request.get_json()
    logging.info('The current request received is: ', notebook_elements)
    try:
        logging.info("Starting Processing Notebook Data")

        # Create a Service with the notebook elements and received from the request
        nb_svc = NBService(notebook_elements)

        # Process all the notebook elements
        nb_svc.process()

        logging.info("Completed Processing Notebook Data")
    except (InvalidNotebookError, NoContentNotebookError) as e:
        # In case notebook contains no elements or no code cells, throw a 400 bad request
        logging.error(e)
        abort(400)

    return 'OK', 200

