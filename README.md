# React Frontend and Python Backend Demo Application

This demo application showcases a simple web application built with a React frontend and a Python (Flask) backend. It provides a basic structure for building full-stack web applications and demonstrates communication between the frontend and backend.

## Features

* **React Frontend:**
  * A user-friendly interface built with React.
  * Demonstrates how to make asynchronous API calls to the Python backend.
  * Simple component structure for easy understanding.
* **Python (Flask) Backend:**
  * A lightweight RESTful API built with Flask.
  * Handles requests from the React frontend.
  * Provides example endpoints for data retrieval and processing.
  * Uses CORS to allow cross origin requests.

## Technologies Used

* **Frontend:**
  * React
  * JavaScript (ES6+)
  * Axios (for API requests)
* **Backend:**
  * Python 3
  * Flask
  * Flask-CORS

## Setup and Installation

1. **Backend Setup (Python):**

    * Ensure Python 3 is installed.
    * Navigate to the `backend` directory.
    * Create a virtual environment (recommended):

        ```bash
        python3 -m venv venv
        source venv/bin/activate  # On macOS/Linux
        venv\Scripts\activate  # On Windows
        ```

    * Install the required Python packages:

        ```bash
        pip install Flask Flask-CORS
        ```

    * Run the Flask application:

        ```bash
        python app/__init__.py
        ```

    * The backend will start running on `http://127.0.0.1:5000/`.

2. **Frontend Setup (React):**

    * Ensure Node.js and npm (Node Package Manager) are installed.
    * Navigate to the `frontend` directory.
    * Install the required npm packages:

        ```bash
        npm install
        ```

    * Start the React development server:

        ```bash
        npm start
        ```

    * The React application will open in your browser, typically at `http://localhost:3000`.

## Project Structure

<pre>
oLzlDRHtw8/
    ├── README.md
    ├── backend
    │   ├── app
    │   │   ├── __init__.py
    │   │   └── api.py
    │   ├── database.db
    │   └── main.py
    └── frontend
        ├── README.md
        ├── package-lock.json
        ├── package.json
        ├── public
        │   ├── favicon.ico
        │   ├── index.html
        │   ├── logo192.png
        │   ├── logo512.png
        │   ├── manifest.json
        │   └── robots.txt
        └── src
            ├── App.css
            ├── App.js
            ├── App.test.js
            ├── components
            │   └── Modal.js
            ├── index.css
            ├── index.js
            ├── logo.svg
            ├── reportWebVitals.js
            └── setupTests.js
</pre>

## Usage

* The React frontend will display data fetched from the Python backend.
* Interact with the frontend to trigger API calls and observe the responses.
* Modify the React components and Python endpoints to experiment with different functionalities.

## Customization

* Modify the React components in the `frontend/src` directory to change the user interface.
* Modify the Python endpoints in the `backend/app/__init__.py` file to add or change backend logic.
* Adjust the CORS settings within the python backend, to allow for different origins.

## Notes

* This is a basic demo application and can be extended with more features and functionalities.
* Ensure the backend and frontend are running simultaneously for proper communication.
* For production, consider using a more robust web server for the backend, and creating a production build of the react application.

## Author

Peter Obiechina

## License

This project is provided as-is. Please use it responsibly and ethically. No warranties are provided.
