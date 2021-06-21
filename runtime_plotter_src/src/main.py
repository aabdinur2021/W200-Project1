import getopt
import sys

from flask import Flask
from flask_cors import CORS
from nb_processor_controller import nb_controller_blue_print

app = Flask(__name__)
CORS(app)


def main(argv):
    opts, args = getopt.getopt(argv, "hp:")
    host = 'localhost'
    port = 8000
    for opt in opts:
        if opt[0] == '-h':
            print("python main.py -p <port>")
            exit(0)
        elif opt[0] == '-p':
            port = opt[1]

    app.register_blueprint(nb_controller_blue_print)
    app.run(host, port)


if __name__ == "__main__":
    main(sys.argv[1:])
