Django Chat Application
======================

Welcome to the Django Chat Application! This sophisticated application allows users to engage in real-time communication through text messages, leveraging the power of Django Channels for WebSocket implementation.

Feature
-------------

- User Authentication: Secure user registration and authentication system to ensure data privacy.
- Real-time Messaging: Utilizes WebSocket protocol for instant message delivery, providing a seamless chatting experience.
- Chat Rooms: Facilitates group conversations by allowing users to create or join chat rooms.
- Message History: Access message history for a comprehensive overview of conversations.
- User Profiles: Users can customize their profiles to add personal details and preferences.

Documentation
-------------

The full documentation **will be** at <https://channels.readthedocs.io>.

Installation
----------

Clone the Repository:

    git clone https://github.com/Aaditya110711/chat-application.git

Navigate to the Project Directory:

    cd chat-application


Install Dependencies:

    pip install -r requirements.txt

Set Up Environment Variables:

- Create a .env file in the project root directory and add the following variables:
- Replace <your_secret_key> with your Django secret key.
```
SECRET_KEY=<your_secret_key>
DEBUG=True
```

Configure PostgreSQL Database:

- Ensure you have PostgreSQL installed and running. Then, add the following database 
- configuration in your .env file:


```
DB_NAME=<your_database_name>
DB_USER=<your_database_user>
DB_PASSWORD=<your_database_password>
DB_HOST=localhost
DB_PORT=5432
```

Apply Migrations:

    python manage.py migrate

Run the Development Server:

    python manage.py runserver


Usage
--------

  1. User Registration/Login:
      - Register for a new account or log in with existing credentials to access the chat 
      - For dialogs
  2. Real-time Messaging:
      - Exchange messages with other users in real-time, enhancing the interactive chatting experience.


Configuration
-------------

Configure the application settings in the settings.py file to tailor the application according to your specific requirements. Customize database settings, security measures, static file handling, and more to align with your project needs.


Dependencies
--------------------
- Django
- Django Channels
- Redis (Asynchronous Message Broker)
- PostgreSQL
