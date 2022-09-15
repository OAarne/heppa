# Moved to https://github.com/TKOaly/heppa
# HEPPA
HEPPA: hyvin edistynyt perjantaipiirretty applikaatio.
Web-app that allows approval voting (with veto), intended for selecting the Gurula friday cartoon. Started as a database application project over winter break 2018-2019.

[App on Heroku](http://heppa.herokuapp.com/)

## Installation Instructions
### Local Setup
Make sure that you have these dependencies installed on your machine:
- Python 3 and its dev packages
- Python 3 venv 
- PostgreSQL and its dev packages (may also work without)

On Debian/Ubuntu
```
sudo apt install python3-dev python3-venv postgresql libpq-dev
```
Run these in the root directory to launch the app at 
```
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> python3 run.py
```

You can then open the app in your browser at `http://127.0.0.1:5000/`

### Docker Setup
Install Docker and add your user to the docker group.

Run this command to build the docker image
```
docker build -t heppa .
```

This command will then start the application in docker
```
docker run --rm -p 8000:8000 heppa
```

You can then open the app in your browser at `http://127.0.0.1:8000/`

### Production docker setup
Install Docker and Docker Compose.

Define POSTGRES_PASSWORD env variable.

Run this command to start the app
```
docker compose up
```

It should now be available at `http://127.0.0.1:8000/`

### Heroku Setup
Simply make sure the application name in the command below is unique
```
heroku create example-heppa
```

You should then be able to open the app in `<example-heppa>.herokuapp.com`

If you've forked this on GitHub, you may want to use [Heroku's GitHub integration](https://devcenter.heroku.com/articles/github-integration).

## User Instructions

**NB: this application is not secure in any way. Any user can log in with your username.**

Before voting, you need to register an account.

After registering, you can add candidates and vote on them. The electoral system is [approval voting](https://en.wikipedia.org/wiki/Approval_voting) with the addition of an unrestricted veto right for everyone. Voting is not anonymous so that the veto cannot be abused.

## Documentation
* [User stories (in Finnish)](https://github.com/OAarne/heppa/blob/master/documentation/k%C3%A4ytt%C3%B6tapaukset.md)
* [Database details](https://github.com/OAarne/heppa/blob/master/documentation/database.md)
* [Database diagram](https://github.com/OAarne/heppa/blob/master/documentation/database_diagram.png)
