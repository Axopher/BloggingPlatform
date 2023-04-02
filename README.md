# BloggingPlatform
Steps to run the application:
a) First, make sure python is installed in your machine and then, simply clone the project using this command:
   >git clone "https://github.com/Axopher/BloggingPlatform.git"
b) Then, run these commands to setup virtual environment if you like or else go to step c):
   >pip install virtualenv
   >python -m venv <name_of_virtualenv>
   > myvenv/scripts/<name_of_virtualenv>
c) run this command:
   >pip install -r requirements.txt
d) Finally, run the server:
   >python manage.py runserver

Login Credentials:- 
admin: username/password = aman/aman
staff: username/password = staff/mystaff123

Notes:-
Only staff and Admin(i.e. aman) have the permission to view the APIs since they are part of 'StaffPostEditor' group which you can see in the django in-built Admin panel. And, also only author of the post have the permission to update/delete their posts/comments on APIs views. Alhough I could have used different approach to make APIs like using viewsets and JWT but I wanted to do using generic views to have more granular control over the url link of the APIs.

Here are all the Api links:
1.http://127.0.0.1:8000/api/list-posts/
2.http://127.0.0.1:8000/api/list-comments/
3.http://127.0.0.1:8000/api/create-post/
4.http://127.0.0.1:8000/api/detail-post/<id_of_the_post>/
5.http://127.0.0.1:8000/api/update-post/<id_of_the_post>/
6.http://127.0.0.1:8000/api/delete-post/<id_of_the_post>/
7.http://127.0.0.1:8000/api/create-comment/
8.http://127.0.0.1:8000/api/detail-comment/<id_of_the_comment>/
9.http://127.0.0.1:8000/api/update-comment/<id_of_the_comment>/
10http://127.0.0.1:8000/api/delete-comment/<id_of_the_comment>/


Some more features are yet to be added here like:
                                                  1) User Profile
                                                  2) Notifications about comments on the Front End
                                                  3) Likes on the post
                                                  4) Blogs Category and category related searches
                                                  5) Much better UI/UX and many more features as per the requirements.

