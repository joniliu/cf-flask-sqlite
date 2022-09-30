
## Introduction

A starter CRUD Web App (Skeleton) using Python Flask and SQLite as local datahase.
This code deployable to SAP BTP Cloud Foundry environment.


## Instructions

Do `git clone` this repository, you should have `cf-flask-sqlite` folder.


#### # Cloud Foundry Deployment

Login to your SAP BTP Cloud Foundry account.

```
$ cd cf-flask-sqlite
$ cf push
```

Navigate to `CF AppRoute URL` to access this Web App frontend and `CF AppRoute URL/api/*` to access the REST APIs.

See [app\apis.py](app/apis.py) for complete supported REST APIs operation.

> Additional notes: 
>
> * Above deployment approach is using Cloud Foundry CLI to deploy an application in the Cloud Foundry environment.
> You can find out how to get and use the Cloud Foundry command line interface [here](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/2f1d4abd0f9f4760a301f43513d2efa6.html), or [here](https://docs.cloudfoundry.org/cf-cli/).
> * For using SAP BTP cockpit to deploy application in the Cloud Foundry environment, please refer to this guide [here](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/09fdb9bdc6804c479d634297f1d07e09.html).


#### # Run on Local Machine

Do `git clone` this repository, you should have `cf-flask-sqlite` folder.

```
$ cd cf-flask-sqlite
$ pip install -r requirements.txt
$ python run.py
```

Navigate to `http://localhost:5000/` to access the Web App frontend and `http://localhost:5000/api/*` to access the REST APIs.

See [app\apis.py](app/apis.py) for complete supported REST APIs operation.

Example of REST API endpoints:

```
http://localhost:5000/api/ -- hello world

http://localhost:5000/api/users  -- get list of users

http://localhost:5000/api/user/<id>  -- get user by id

http://localhost:5000/api/add/user  -- add new user with JSON data payload:
{
    "name": "John Doe",
    "email": "john.doe@human.com"
}

http://localhost:5000/api/update/user/<id>  -- update user by id with JSON data payload
{
    "name": "John Doe 1",
    "email": "john.doe1@human.com"
}

http://localhost:5000/api/delete/user/<id>  -- delete user by id
```
