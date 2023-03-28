# Telegram_Bot_using_Django_Tutorial

# Intro

This is a simple telegram bot that says three different type of jokes 

# Requirements
See requirements.txt


### Step 0 : Clone the Repository

`git clone https://github.com/shivammotani/Telegram_Bot_using_Django.git`

### Step 1 : Install dependencies

`pip install -r requirements.txt`

### Step 2 : Install and Setup PostGresSQL
You need to install and configure your postgresql and add the connection details in settings.py file.
You only need to replace the following parameters under DATABSES:
{
NAME': '<database_name',
'USER': '<user_name',
'PASSWORD': '<user_pwd>'
}
Do note this is not your root pwd. Simply create a new user and a new database and grant permission to the database to the newly created user

### Step 3 : Run migrations 

This just creates the default stuff for admin, app and models. 

`python manage.py makemigrations`
`python manage.py migrate`

### Step 4 : Start the local server

And start the server with 

`python manage.py runserver`

### Step 5 : Talk to the BotFather and get and set your bot token

Start telegram, and search for the Botfather. Talk to the Botfather on Telegram and give the command `/newbot` to create a bot and follow the instructions to get a token.

Copy the token and paste in API_KEY present in jokebot/views.py

### Step 6: Talk to the bot

You should now be able to talk to the bot and get responses from it

### Step 7: See the bot interactions in real time

Visit http://127.0.0.1:8000/ and see the Query results by all the users in a tabular format.
Note: You might have to refresh the webpage to see the updated data

####SCREEN SHOTS

Before Querying Database Status

![](Images/Before%20Querying.png)


Interacting with Bot

![](Images/Bot%20Interacting%20with%20User.png)

After Interaction Database Status

![](Images/After%20Interaction.png)
