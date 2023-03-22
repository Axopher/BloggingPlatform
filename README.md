# BloggingPlatform
Steps to run the application:
a) First, make sure python is installed in your machine and then, run this command
   >python -m venv <name_of_virtualenv> 
b) After that, simple clone the project using this command:
   >git clone "https://github.com/Axopher/BloggingPlatform.git"
c) Then, run this command:
   >pip install -r requirements.txt
d) Finally, make migrations:
   >python manage.py makemigrations
   >python manage.py migrate
e) Run the server:
   >python manage.py runserver
