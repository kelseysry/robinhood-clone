# Flask React Project

This is the starter for the Flask React project.

## Getting started

1. Clone this repository (only this branch)

   ```bash
   git clone https://github.com/appacademy-starters/python-project-starter.git
   ```

2. Install dependencies in pipfile for development. Dockerfile is for production.

      ```bash
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment
4. Setup your PostgreSQL user, password and database and make sure it matches your **.env** file
```bash
CREATE USER robinhood_user WITH PASSWORD 'password';
CREATE DATABASE robinhood_app WITH OWNER robinhood_user;
```
5. Get into your pipenv, migrate your database, seed your database, and run your flask app

- the migrations folder is already created so don't need to run `flask db init`
- migration already generated too with a user table so don't need to run `flask db migrate`

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

- if you want to update the user model, make sure you upgrade first, make changes to the model, then migrate

6. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.

***
*IMPORTANT!*
   If you add any python dependencies to your pipfiles, you'll need to regenerate your requirements.txt before deployment.
   You can do this by running:

   ```bash
   pipenv lock -r > requirements.txt
   ```

*ALSO IMPORTANT!*
   psycopg2-binary MUST remain a dev dependency because you can't install it on apline-linux.
   There is a layer in the Dockerfile that will install psycopg2 (not binary) for us.
***


## Deploy to Heroku

1. Before you deploy, don't forget to run the following command in order to
ensure that your production environment has all of your up-to-date
dependencies. You only have to run this command when you have installed new
Python packages since your last deployment, but if you aren't sure, it won't
hurt to run it again.

   ```bash
   pipenv lock -r > requirements.txt
   ```

2. Create a new project on Heroku
3. Under Resources click "Find more add-ons" and add the add on called "Heroku Postgres"
4. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)
5. Run

   ```bash
   heroku login
   ```

6. Login to the heroku container registry - where we push dockerfile image to. The container registry on heroku will run a container based on that image

   ```bash
   heroku container:login
   ```

7. Update the `REACT_APP_BASE_URL` variable in the Dockerfile.
   This should be the full URL of your Heroku app: i.e. "https://flask-react-aa.herokuapp.com"
8. Push your docker image to heroku from the root directory of your project.
   (If you are using an M1 mac, follow [these steps below](#for-m1-mac-users) instead, then continue on to step 9.)
   This will build the Dockerfile and push the image to your heroku container registry.

   ```bash
   heroku container:push web -a {NAME_OF_HEROKU_APP}
   ```

9. Release your docker container to heroku, release uses the latest pushed version of image when run on the heroku container registry

      ```bash
      heroku container:release web -a {NAME_OF_HEROKU_APP}
      ```

10. set up your database
   - set up production database using heroku command line interface
   - will apply migrations to production db, so tables will show up in production and seed it!

      ```bash
      heroku run -a {NAME_OF_HEROKU_APP} flask db upgrade
      heroku run -a {NAME_OF_HEROKU_APP} flask seed all
      ```

11. Under Settings find "Config Vars" and add any additional/secret .env
variables.
- add SECRET_KEY

12. profit


# side note: so every time you deploy to heroku do:

make sure production dependencies are caught up with development
   ```bash
   pipenv lock -r > requirements.txt
   ```

   ```bash
   heroku container:login
   ```
push and release
   ```bash
   heroku container:push web -a {NAME_OF_HEROKU_APP}
   ```

   ```bash
   heroku container:release web -a {NAME_OF_HEROKU_APP}
   ```

### For M1 Mac users

(Replaces **Step 8**)

1. Build image with linux platform for heroku servers. Replace
{NAME_OF_HEROKU_APP} with your own tag:

   ```bash=
   docker buildx build --platform linux/amd64 -t {NAME_OF_HEROKU_APP} .
   ```

2. Tag your app with the url for your apps registry. Make sure to use the name
of your Heroku app in the url and tag name:

   ```bash=2
   docker tag {NAME_OF_HEROKU_APP} registry.heroku.com/{NAME_OF_HEROKU_APP}/web
   ```

3. Use docker to push the image to the Heroku container registry:

   ```bash=3
   docker push registry.heroku.com/{NAME_OF_HEROKU_APP}/web
   ```


# Steps to clone project starter and push to project repo
Clone the starter repo
!! REMOVE THE .git directory !!
This will remove the git history associated with the a/A starter repo. Do not push to the a/A starter repo!
git init
```bash
rm -r .git/
```

# When add new tables to db
1. create model
2. import model into models/__init__.py
3. create seed file - so this is how you seed it
4. add the seed_stocks() and undo_stocks() function calls to the app/seeds/__init__.py, don't forget to also import the functions first
5. after create model make to unseed table first so easier to reseed
6. run `flask db migrate -m "add stocks model"`
7. run `flask db upgrade`


# Resource for models db.column type
https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.Text
