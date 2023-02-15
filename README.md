# todo_list-django-

Feature of the App

The Todo list App is designed to view list of tasks entered by a user. The app has a section where the user
can sign in if he/she has already created an account or register if they are new users.
The app uses authentication & permissions to let only the task onwner to view, delete or update the task. 
When a user is logged in, the app shows his/her own tasks. The user can view, update, delete or add a new task. 
Tasks are ordered depending on the time they were created. The most recent tasks will show up first then the old ones. 
Once the task is completed, the user can update the task & mark it “Complete”.

Technologies & technique used

Pillow: the python library is used to modify pictures uploaded by the user for their profiles. Also I used it to resize large pictures
to smaller ones to save space in the file system and avoid latency openning the page.
Pagination: By limmiting the number of tasks viewed on each page, and adding links to other task pages. This helped better showing the tasks.
ORM: Used in constructing database tables for users and tasks.
Signals: Used to automatically create a profile for each user once that user is created. 
Class-based views: Using CBV & mixins made my code more powerful, cleaner and easier to read. 
I also added forms to let users reset their password (if they forget it). But an email server should be configured first. So they are not fully functioning.  

