# Assignment 1 - Todo List Backend

In this first assignment, you will write a backend to service a cloud-based todo list app.  In this day and age, cloud-based products for viewing and saving various forms of content ([photos](https://photos.google.com/), [bookmarks](https://stash.ai/), [todo lists](https://en.todoist.com/), etc.) are becoming increasingly popular, due to their ability to offload data from your local machine to the cloud, service your data to multiple platforms, etc.  


## Learning Objectives

This project aims to help you "ramp up" and get comfortable working with the following tools / technologies / concepts:

* `Python` as a language and a `Flask` as a framework
* [`JSON`](http://www.json.org/) as a means of sending and receiving data
* `HTTP` requests and responses
* Data modeling
* System configuration
* `Python` / `Command-Line-Based` Testing

## Table of Contents

* [Academic Integrity](#academic-integrity)
* [System Configuration](#system-configuration)
* [Organization](#organization)
* [Expected Functionality](#expected-functionality)
* [Testing Your Code](#testing-your-code)
* [Extending the Assignment](#extending-the-assignment)
* [Project Submission](#project-submission)

## Academic Integrity and Collaboration

### Academic Integrity

Note that these projects should be completed **individually**.  As a result, all University-standard AI guidelines should be followed.

### Code Attribution and Collaboration

One of the reasons we chose `Flask` as an initial backend framework for students to use is because of its phenomenal support online.  Looking up framework documentation and adapting the docs' sample code to suite your own needs in something we expect and *want* you to do, as it allows you to explore and increase your self-sufficiency regarding backend development.  However, if you find code in a [`StackOverflow`](`https://stackoverflow.com/`) post or in an open source `Github` repository, then you should cite it accordingly.  See the [project submission](#project-submission) section for guidelines as to where to include those citations.

## System Configuration

Perform the following steps in order:

1. Get [`PyPI`](https://pip.pypa.io/en/stable/installing/) (`Python Package Index`) - In order to easily download `Python` modules required to run the project, as well as ones that may help you perform certain tasks in the future of the course, `PyPI` is **essential**.  
2. Download [`virtualenv`](https://virtualenv.pypa.io/en/stable/installation/) - `virtualenv` helps establish an isolated `Python` environment you work in with its own set of `Python` modules it contains within a directory in your project's root.  Once you have `virtualenv`, run the following:

````bash
virtualenv venv
````

This creates a virtual environment called `venv`.  In order to enter than virtual environment, run the following:

````bash
source venv/bin/activate
````

The following command line prompt will indicate that you’re in the virtual environment:

````bash
(venv) >
````

To deactivate the virtual environment, run the following:

````bash
deactivate
````

Whenever you work with this project, you should **always** be in your virtual environment.  Without this isolation, we might run into module versioning issues and other problems when trying to run your project, which creates administrative overhead.  

3. Install dependencies - At the root of directory of the project skeleton code, run the following:

````bash
pip install -r requirements.txt
````

This installs within your virtual environment all the necessary modules that are required at the beginning of the project.

**NOTE:** The overarching system configuration concepts are explained in more detail in [`this guide`](http://www.joeantonakakis.com/FlaskDevOps/), which we are using as our standard for setting up `Flask` apps in this course.  For information regarding advanced system configuration (which you might need for some of the project extensions, if you tackle them), refer to that guide.

## Organization

The following describes the initial file-structure of the directory `./src`:

````bash
.
├── config.py
├── requirements.txt
├── run.py
└── todo
    ├── __init__.py
    ├── db.py
    ├── models.py
    └── routes.py
````

Below consists of brief discussions of each one of the following files:

* `config.py` defines the configuration for the `Flask` app to run with.  You do not need to touch this file.
* `requirements.txt` outlines the initial module dependencies of the app.  To install these, run `pip install -r requirements.txt`.  If you `pip install` a module during the duration of your project, be sure to `pip freeze > requirements.txt` to add the new module to the `requirements.txt` file, **or else we won't be able to run your project**
* `run.py` is the run script for the `Flask` app.  You do not need to touch this file.
* `todo/__init__.py` defines the `Flask` app instance. You do not need to touch this file.
* `todo/db.py` defines a driver that reads and writes files as a form of persisting the data of your app.  **Read this file to get an idea of what functionalities it affords you**.  
* `todo/models.py` defines is where you should define the models of your application.  All models should inherit from `Model`, which is the base class defining fundamental fields / functions required to store models as files.
* `todo/routes.py` defines all the routes (a.k.a. endpoints) that users will be able to interact with in order to create todo list items, delete todo list items, and list todo list items.

This initial framework is just a guideline to implementing the base features of the app.  Feel free to change / reorganize at will.  However, the expected functionality (listed below) stays the same.  

## Expected Functionality

In this project, we expect you to make an `API` that lets an application make requests to perform operations on todo list items called `"tasks"`.

Essentially, the application is just keeping track of a series of tasks that a person has to do.  Tasks should contain the following:

* A unique ID (see `Model` class that you should be extending from)
* A name
* A description
* A list of tags (like 'laundry', 'urgent', 'etc.')
* A time of creation
* A due date

You should write a model to represent this series of information called `Task`.  In addition, you should write endpoints that let a person do the following:


#### Create a task
`POST /tasks?name={name}&description={description}&tags={tags(comma separated)}&due_date={due date(in unix time)}`

Creates a task given the `URL` params above

#### List all tasks
`GET /tasks`

Get a list of all tasks

#### Get task by ID
`GET /tasks/{id}`

Get a task by its ID

#### Delete a task
`DELETE /tasks/{id}`

Delete a specific task

#### Delete all tasks
`DELETE /tasks/all`

Delete all tasks

## Testing Your Code

We recommend testing your code using [`Flask Testing`](http://flask.pocoo.org/docs/0.12/testing/), or `cURL-ing` from the command line (although we prefer the tool [`httpie`](https://httpie.org/) `:)`).  We'll leave it to you to figure out the details.  

## Extending the Assignment

TODO

## Project Submission

TODO
