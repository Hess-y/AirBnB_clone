AirBnB clone - The console
![image](https://user-images.githubusercontent.com/113606328/223416158-c7e16fd3-6d94-4202-a5f7-6c931c617949.png)
First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
Each task is linked and will help you to:
   put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
   1.create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
   2.create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
   3.create the first abstracted storage engine of the project: File storage.
   4.create all unittests to validate all our classes and storage engine
   
   What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

    1.Create a new object (ex: a new User or a new Place)
    2.Retrieve an object from a file, a database etc…
    3.Do operations on objects (count, compute stats, etc…)
    4.Update attributes of an object
    5.Destroy an object
    
    Execution
 Your shell should work like this in interactive mode:
 
 $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$


Requirements:
1.Python Scripts
2.Allowed editors: vi, vim, emacs
3.All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
4.All your files should end with a new line
5.The first line of all your files should be exactly #!/usr/bin/python3
6.A README.md file, at the root of the folder of the project, is mandatory
7.Your code should use the pycodestyle (version 2.8.*)
8.All your files must be executable
9.The length of your files will be tested using wc
10.All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
11.All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
12.All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
13.A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Python Unit Tests
1.Allowed editors: vi, vim, emacs
2.All your files should end with a new line
3.All your test files should be inside a folder tests
4.You have to use the unittest module
5.All your test files should be python files (extension: .py)
6.All your test files and folders should start by test_
7.Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
8.All your tests should be executed by using this command: python3 -m unittest discover tests
9.You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
10.All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
11.All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
12.All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
13.We strongly encourage you to work together on test cases, so that you don’t miss any edge case


