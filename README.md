
<h1 align="center">
  <br>

  <img width="317" alt="Capture d’écran 2023-01-22 à 16 43 06" src="https://user-images.githubusercontent.com/28122432/213942189-b2e31bf3-9d14-4f8a-9d3d-7d92357e4ce9.png">

  <br>
  MECC
  <br>
</h1>

<h3 align="center">Miscellaneous Educational Cybersecurity Chatbot.</h3>
<h4 align="center">Specialized chatbot for cybersecurity education and sensibilization.</h4>
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#license">License</a>
</p>

<h1 align="center">
<img width="529" alt="Capture d’écran 2023-02-02 à 17 57 48" src="https://user-images.githubusercontent.com/28122432/216470220-cc47d3f4-65c3-4bbe-9a24-1c25fd69cb19.png">
</h1>

## Key Features

* Take a quiz to see how much you know about cybersecurity
* Cybersecurity teacher on various themes.
* Senzibilization on data shared online.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. 

### Setting up environment variable

Create an `.env` file in the `backend/` folder based on the `.env.template` file.

You have to define : 

- DIALOGFLOW_PROJECT_ID -> ID of the dialogflow app for your chatbot
- DIALOGFLOW_SESSION_ID -> Random string 
- DIALOGFLOW_LANGUAGE_CODE -> Set up to the preferred language

Learn more [here](https://cloud.google.com/dialogflow/es/docs/quick/setup?hl=fr)

### Starting the app

From a first command line:

```bash
# Clone this repository
$ git clone https://github.com/Scylidose/MECC

# Go into the repository
$ cd MECC/

# Create virtual environment
$ python3 -m venv venv

# Activate virtual environment
$ source ./venv/bin/activate

# Go into the backend repository
$ cd backend/

# run the Flask app in the background
./bootstrap.sh &
```

From another command line:

```bash
# Go into the frontend repository
$ cd frontend/

# Install dependencies
$ npm install

# run the Angular application
$ ng serve

```

## Download

You can [download](https://github.com/Scylidose/MECC/archive/refs/heads/master.zip) the latest installable version of MECC.

## License

MIT
