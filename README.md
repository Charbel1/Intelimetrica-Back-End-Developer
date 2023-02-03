 Intelimétrica Back-end Developer


# Summary
We are expecting to receive a simple application that shows your programming
skills and knowledge. We consider that the average time to implement this project is about 5 
hours but because we understand you are a busy person you have a maximum of 48 hours after 
you receive the test to send us your answer.



We will evaluate the following:

REST API with CRUD operations.

Link to the repository (Github, Render, Bitbucket or Railway).

# Important Instructions
- Please ensure that your application meets the following requirements:

- Add a README file.

- Complete your test using the Heroku cloud platform, Render, Railway and/or Dockerize your application.

# Assignment Description

You are working for a startup called Melp, which has a revolutionary idea about building an app that will provide useful information about restaurants to users.
You were provided with a CSV which contains raw data about the restaurants. 
# Task 1:
- The first task consists in importing the raw data into a relational database 
- REST API that implements CRUD (Create, Read, Update, Delete) operations.
id TEXT PRIMARY KEY, -- Unique Identifier of Restaurant

            rating INTEGER, -- Number between 0 and 4

            name TEXT, -- Name of the restaurant

            site TEXT, -- Url of the restaurant

            email TEXT,

            phone TEXT,

            street TEXT,

            city TEXT,

            state TEXT,

            lat FLOAT, -- Latitude

            lng FLOAT) -- Longitude


# Task 2
- The second task consists in implementing the following endpoint:
    
      /restaurants/statistics?latitude=x&longitude=y&radius=z
- It receives a latitude and a longitude as parameters, which correspond to the center of a circle,
and a third parameter that corresponds to a radius in METERS.
- {

        	count: Count of restaurants that fall inside the circle with center [x,y] and radius z,

        	avg: Average rating of restaurant inside the circle,

        	std: Standard deviation of rating of restaurants inside the circle

}

# Bonus Points:

- Good use of Git.

- Documentation of the API.

- Correct use of HTTP verbs.

- Good programming practices.


# GoCardless sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Charbel1/Intelimetrica-Back-End-Developer.git
$ cd Intelimetrica-Back-End-Developer

```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2  env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r req.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```



