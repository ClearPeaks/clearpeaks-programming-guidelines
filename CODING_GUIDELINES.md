# ClearPeaks coding guidelines

There are several coding guidelines or recommendations we encourage to follow in order to deliver a high quality code to our clients as well as developing readable code for our collegues in ClearPeaks. Although we know that as consultants might be difficult to follow all these requirements and deliver the service in time to the client, we encourage to follow them and get used to them so the next projects you will spend less time adapting.

The first thing every developer should do is **commenting** the code. This is the keystone that sets a code apart. We recommend always, regardless the programming language, to write comments inline and block, and comments explaining each function, its parameters and the return value if needed.

Another relevant recommendation is always **placing your code in a GitHub repository**. We have an unlimited free repository were we can keep in a single place all the code we developed, where any consultant can access, reuse, learn and even improve it. So please, keep track of your code placing it in a GitHub repository.

Moreover, GitHub repositories can (and should) have a **README** file where you can **explain what your code does and how anyone can install and run it**.

Additionally to the GitHub repository, you can integrate **depandabot** to it if you have any dependency to automatically update to newer versions.

Having covered the general aspects, let's delve into specific programming languages guidelines we recommend following.

## Python

Python is one of the most used programming languages around the world, and so is in ClearPeaks. Due to its broad use, there are many guidelines and conventions, most of them gathered in the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/). We really encourage following them. Here, we are only going to mention some of them that we think are relevant.

- Indenting

Indenting in Python is specially important. We recommend following the standard of using spaces, 4 per tab.

- Line length

The recommended PEP8 line length is 80, but as it is quite conservative, we suggest using a maxiumum of 120. We already adapted flake8 to check so.

- Imports

Imports should always be on separate lines except for import of the same module. Furthermore, we recommend sorting them alphabetically. This last thing can be easily achived with the tool isort, already incorported in the template.

- Naming

The naming convention for variables and functions definition in Python is generally [lowercase, with words separated by underscores](https://en.wikipedia.org/wiki/Snake_case). However, you can define variables in uppercase for constants for example. Check this dumb demo:

```python
# Constants
FILE_NAME = 'clearpeaks.csv'

# Functions
def read_csv(csv):
    file = open(csv, "r")
    return file.read()

# Main code
file_content = read_csv(FILE_NAME)
print(file_content)
```

Tip: Additionally, you can *visually* specify private methods or variables adding an underscore at the beginning of its name.

- Typing (only in versions>=3.5)

Typing is a relatively new addition to Python (since version 3.5) that allow specifying types in Python. At first, it can seem to be counterproductive as you are limiting Python flexibility, nonetheless you are making the code extremely more readable as you can specify the types of the function parameters and the return type.

```python
# Without typing (discouraged)
def sum(a, b):
    return a + b
```

```python
# With typing (recommended)
def sum(a: int, b: int) -> int:
    return a + b
```

## Scala


## Other languages?
