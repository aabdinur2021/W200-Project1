define([
    'base/js/namespace',
    'base/js/events'
    ], function(Jupyter, events) {

      var build_visualization = function() {
        // Get all the elements in the jupyter notebook
        var notebookData = Jupyter.notebook.get_cells()

        // POST all the notebook elements to the python backend.
        // Currently hard coded to simplify the process
        const url = 'http://localhost:8000/notebook_data'
        fetch(url, {

            // Declare what type of data we're sending
            headers: {
            'Content-Type': 'application/json'
            },

            // Specify the method
            method: 'POST',

            // Provide the notebookData to be sent to the backend service
            body: JSON.stringify(notebookData)
        }).then(function (response) { // At this point, The backend has already processed the request
            return response.text();
        }).then(function (text) {

            console.log('POST response: ');

            // Should be 'OK' if everything was successful
            console.log(text);
        });
      };
      // Add Toolbar button
      var performance_check_button = function () {
          console.log();
          Jupyter.toolbar.add_buttons_group([
              Jupyter.keyboard_manager.actions.register ({
                  'help': 'Check Notebook Performance',
                  'icon' : 'fa-play-circle',
                  'handler': build_visualization
              }, 'addRuntimePlotter-Cell', 'Runtime Plotter')
          ])
      }

    // Run on start
    function load_ipython_extension() {
        performance_check_button()
    }
    return {
        load_ipython_extension: load_ipython_extension
    };
});