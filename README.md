# Assignment 1 - Todo List Backend

In this first assignment, you will write a backend to service a cloud-based todo list app.  In this day and age, cloud-based products for viewing and saving various forms of content ([photos](https://photos.google.com/), [bookmarks](https://stash.ai/), [todo lists](https://en.todoist.com/), etc.) are becoming increasingly popular, due to their ability to offload data from your local machine to the cloud, service your data to multiple platforms, etc.  


## Learning Objectives

This project aims to help you "ramp up" and get comfortable working with the following tools / technologies / concepts:

* `Python` as a language and a `Flask` as a framework
* [`JSON`](http://www.json.org/) as a means of sending and receiving data
* `HTTP` requests and responses
* Data modeling
* Basic exposure to SQL querying
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

#### 1. Check your Version of Python (should be 2.7)

You can check via:

````bash
python --version
````

If your version differs, then download `2.7` [`here`](https://www.python.org/downloads/).

#### 2. Get PyPI (Python Package Index)

[`PyPI`](https://pip.pypa.io/en/stable/installing/)  allows one to easily download `Python` modules required to run the project, as well as ones that may help you perform certain tasks in the future of the course.  `PyPI` is **essential**.  

#### 3. Download Virtualenv

[`Virtualenv`](https://virtualenv.pypa.io/en/stable/installation/) helps establish an isolated `Python` environment.  The environment allows you to separate project-specific dependencies and their versions from the `Python` modules installed locally on your computer.  Once you have `virtualenv`, run the following:

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

#### 4. Install Dependencies

At the root of directory of the project skeleton code, run the following:

````bash
pip install -r requirements.txt
````

This installs within your virtual environment all the necessary modules that are required at the beginning of the project.

#### 5. Install SQLite

Having been given some initial exposure to `SQL` databases in class, the concept of "querying" data is one that we expect you to have a basic grasp of when approaching the future lectures on databases.  As a result, we have decided to use `SQLite` in this project as our means of storing and querying data.  It provides a simple interface you can leverage via its `Python` module, which is included, by default, in the version of Python we use for this class `Python 2.7`.  

`SQLite` can be installed by following [`this`](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm) guide.  


**NOTE:** The overarching system configuration concepts are explained in more detail in [`this guide`](http://www.joeantonakakis.com/FlaskDevOps/), which we are using as our standard for setting up `Flask` apps in this course.  For information regarding advanced system configuration (which you might need for some of the project extensions, if you tackle them), refer to that guide.

## Organization

The following describes the initial file-structure of the directory `./src`:

````bash
.
├── config.py
├── requirements.txt
├── run.py
├── test.py
└── todo
    ├── __init__.py
    ├── db.py
    ├── models.py
    └── routes.py
````

Below consists of brief discussions of each one of the above files:

* `config.py` defines the configuration for the `Flask` app to run with.  You do not need to touch this file.
* `requirements.txt` outlines the initial module dependencies of the app.  To install these, run `pip install -r requirements.txt`.  If you `pip install` a module during the duration of your project, be sure to `pip freeze > requirements.txt` to add the new module to the `requirements.txt` file, **or else we won't be able to run your project**
* `run.py` is the run script for the `Flask` app.  You do not need to touch this file.
* `test.py` is the test script for the `Flask` app. You will use this file to monitor your progress as you implement all the necessary functionality.
* `todo/__init__.py` defines the `Flask` app instance. You do not need to touch this file.
* `todo/db.py` defines a driver that reads and writes files as a form of persisting the data of your app.  **Read this file to get an idea of what functionalities it affords you and what you'll need to add to it**.  It outlines examples of how to perform basic storage operations.  You should be writing basic storage operations to manipulate the data of your app.
* `todo/models.py` is where you should define the models of your application.  All models should inherit from `Model`, which is the base class defining fundamental fields / functions required to store models as files.
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

You should write a model to represent this series of information called `Task`.  In addition, you should write endpoints that allow for the following functionality:


#### Create a task
`POST /tasks?name={name}&description={description}&tags={tags (comma separated)}&due_date={due date (in unix time)}`

Creates a task with the following parameters. Testing is done via the `request.form` not `request.args` in `test.py`. As such, you only need to ensure that all the tests pass in `test.py` to get full credit.

```json
{
	"due_date": 100000000,
	"name": "joe",
	"tags": "hi,mom",
	"created_at": 10203030,
	"id": "10001",
	"description": "this is some cool stuff",
}
```

#### List all tasks
`GET /tasks`

Get a list of all tasks

```json
{
	"DUE_DATE": 100000000,
	"NAME": "joe",
	"TAGS": "hi,mom",
	"CREATED_AT": 10203030,
	"ID": "10001",
	"DESCRIPTION": "this is some cool stuff",
}
```

#### Get task by ID
`GET /tasks/{id}`

Get a task by its ID

```json
{
	"DUE_DATE": 100000000,
	"NAME": "joe",
	"TAGS": "hi,mom",
	"CREATED_AT": 10203030,
	"ID": "10001",
	"DESCRIPTION": "this is some cool stuff"
}
```

#### Delete a task
`DELETE /tasks/{id}`

Delete a specific task

```json
{
	"success": "true"
}
```

#### Delete all tasks
`DELETE /tasks/all`

Delete all tasks

```json
{
	"success": "true"
}
```

## Testing Your Code

We recommend testing your code using [`Flask Testing`](http://flask.pocoo.org/docs/0.12/testing/), or `cURL-ing` from the command line (although we prefer the tool [`httpie`](https://httpie.org/) `:)`).  

To make your lives easier we have provided you our test cases in the `test.py` file that you may leverage to test your endpoints. This file uses the `unittest` module extensively and can be extended if you wish to further develop your test suite to handle your own edge cases.

## Extending the Assignment

You can extend this assignment in the following ways:

* Provide endpoints for updating any part of a specific task (name, description, tags, due date)
* Create a `List` model that own tasks (separate tasks into different todo lists).  Create a `CRUD` interface for lists (Create, Read, Update, Delete) and modify the task creation endpoint to specify a `list_id`
* Add a front-end for utilizing your `API` (we recommend `React`, `Angular`, or `jQuery` for making `AJAX` requests to your `API`)
* Anything else you may like!

## Project Submission

You should submit your project along with a `readme.txt` for your citations, project setup information, and any extensions you might have done.  This should be at the root of your project (inside the `src` directory).  Run the following to zip your project:

````bash
zip -r src.zip src -x src/venv\*
````

You can then submit this file to `CMS`.

## Grading

You will be graded based on how many test cases you pass. Our test cases are provided for you in the test.py file.
