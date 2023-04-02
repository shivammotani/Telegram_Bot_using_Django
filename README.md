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

### Step 4 : Talk to the BotFather and get and set your bot token

Start telegram, and search for the Botfather. Talk to the Botfather on Telegram and give the command `/newbot` to create a bot and follow the instructions to get a token.

Copy the token and paste in "TOKEN" variable present in jokebot/cred.py

### Step 5: Create a Webhook
We need to have a webhook to allow Telegram to send POST request to our Django code. For this we'll use Ngrok.
Install ngrok on your system and hit the following commnand

`ngrok http 8000`

You should now see a log screen with all your session details.
Copy the whole URL (ending with ngrok.io) next to Forwarding in the same screen.
You need to paste this URL in "URL" variable present in jokebot/cred.py.

### Step 6: Patch Webhook to Telegram Server
Now that we have our webhook details configured in the project, let's link the same with Telegram server.
We need to tell telegram to what address it needs to send POST request once there is any query made on the Bot.
For this replace the parameters in the below URL and run it in any browser:

`https://api.telegram.org/bot<your_bot_token>/setWebhook?url=<your_ngrok_url>/getpost/'

You should now see a message stating 
" {"ok":true,"result":true,"description":"Webhook is already set"} "
This means your telegram bot is successully linked with our webhook and can talk with your code.

### Step 7: Start the local server

Let's fire the below code and see the bot interaction in real time.
`python manage.py runserver`

### Step 8: Talk to the bot

You should now be able to talk to the bot and get responses from it

### Step 9: See the databse getting updated in real time

Visit http://127.0.0.1:8000/ and see the Query results by all the users in a tabular format.
Note: You might have to refresh the webpage to see the updated data
