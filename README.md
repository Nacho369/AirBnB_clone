# 0x00. AirBnB clone - The console

![Img](https://github.com/Nacho369/AirBnB_clone/blob/main/misc_files/img/65f4a1dd9c51265f49d0.png)

## Background Context
### Welcome to the AirBnB clone project!
Before starting, please read the **AirBnB** concept page.

**First step: Write a command interpreter to manage your AirBnB objects.**
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object


## Installation
For use this console you need to have:

- Linux ubuntu 14.04.3 LTS or higger
- Python 3.7 or higger


## How to Start it
To start the the console, just type in your terminal;
> $ ./console


## How to Use it
The console supports various commmand, which includes:
### help
Usage:
```
(hbnb) help
```

### EOF
Usage:
```
(hbnb) EOF
```

### quit
Usage:
```
(hbnb) quit
```

### all
Usage:
```
(hbnb) all
```
or
```
(hbnb) all <class name>
```

### show
Usage:
```
(hbnb) show <class name> <class id>
```

### create
Usage:
```
(hbnb) create <class name>
```

### destroy
Usage:
```
(hbnb) destroy <class name> <class id>
```

### update
Usage:
```
(hbnb) update <class name> <class id> <attribute name> <attribute id>
```


## Example
### Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
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
```
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

![Img](https://github.com/Nacho369/AirBnB_clone/blob/main/misc_files/img/structure.png)


## AUTHORS
- Fortune Iheanacho - [Nacho369](https://github.com/Nacho369/)