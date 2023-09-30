<h1 align="center">
  MECC
  <br>
</h1>
<p align="center">
	<img src="https://img.shields.io/badge/angular-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white"> <img src="https://img.shields.io/badge/less-2B4C80?style=for-the-badge&logo=less&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"> <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white"><br>
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/dialogflow-FF9800?style=for-the-badge&logo=dialogflow&logoColor=white"><br>
 <img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white">
</p>

<h3 align="center">Miscellaneous Educational Cybersecurity Chatbot.</h3>
<h4 align="center">Specialized chatbot for cybersecurity education and sensibilization.</h4>
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#license">License</a>
</p>

<h2 align="center">If available, you can discuss with MECC <a href="https://mecc.herokuapp.com/">here</a>.</h2>

<h1 align="center">
<img width="800" alt="MECC image" src="https://user-images.githubusercontent.com/28122432/220011878-d60605aa-b438-4d79-92f8-85af25ab05fd.png">
</h1>

## Key Features

<ul>
  <li><h3>Display usefull ressources about protecting personal data.</h3></li>
  <img width="1244" alt="Capture d’écran 2023-02-19 à 19 05 47" src="https://user-images.githubusercontent.com/28122432/219983676-b87a311a-d376-4cb6-b09f-64cefb22e41f.png">

  <li><h3>Take a quiz to see how much you know about cybersecurity and see your weaknesses.</h3></li>
  <img width="1241" alt="Capture d’écran 2023-02-19 à 19 06 59" src="https://user-images.githubusercontent.com/28122432/219983719-f1c5f71f-86bc-4261-912c-1d2fb9787fc8.png">

  <li><h3>Cybersecurity teacher on various themes.</h3></li>

  <li><h3>Text and video capsule to learn more about cybersecurity.</h3></li>

  <img width="1253" alt="Capture d’écran 2023-02-19 à 18 57 57" src="https://user-images.githubusercontent.com/28122432/220011878-d60605aa-b438-4d79-92f8-85af25ab05fd.png">

  <li><h3>Senzibilization on data shared online.</h3></li>
  <img width="1257" alt="Capture d’écran 2023-02-19 à 19 16 46" src="https://user-images.githubusercontent.com/28122432/219984199-63a36e89-464a-4e5c-8f4f-db53c3498977.png">

</ul>

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

# Install requirements
$ pip install -r requirements.txt

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

You can [download](https://github.com/Scylidose/MECC/archive/refs/tags/v2.0.0.zip) the latest installable version of MECC.

## License

MIT
