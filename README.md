
# MKDocs 

Code from the below [Real Python tutorial](https://realpython.com/lessons/build-project-docs-mkdocs-overview/
):

![](img/MKDocs_Real_py.png)


### Installation

Clone from: `git@github.com:keith-taylor/MKdocs.git`

### Results 
The completed documentation can be viewed [here](https://keith-taylor.github.io/MKdocs/). 

### Contact

![twitter](img/twitter.png) `@_thinkmachines_`

![github](img/github.png) https://github.com/keith-taylor

![](img/email.png) 

### Issues Encountered

1. Trying to use `mkdocstrings` plug in didn't work. To do this I added
    ```
    plugins:
     - mkdocstrings
    ```
    to `mkdocs.yml` but this gave me:
    
    ModuleNotFoundError: No module named 'mkdocstrings.handlers.python' when trying to run 'mkdocs serve'.

    ##### Solution
    It seems like the version of mkdocstrings was the issue. Installing version 0.18 seemed to fix it.
    
    ```
    python -m pip install "mkdocstrings[python]"==0.18
    ```
    
    I went from:

    ```
    mkdocstrings               0.19.0
    mkdocstrings-python        0.8.3
    ```

    to

    ```
    mkdocstrings               0.18.0
    mkdocstrings-python        0.6.6
    mkdocstrings-python-legacy 0.2.2
    ```

    and now `mkdocs serve` works just fine.
    
2. Now that I had this working I encountered another problem when trying to generate the Reference document: the docstrings were not importing. I encountered no errors and the pages were served just fine. I had to add the path to the plugin specification in the `.yml` file:
   
    ```
    plugins:
      - mkdocstrings:
          handlers:
            python:
              paths: [/home/my_name/my_code/MKdocs]
    ```
    
    It looks like MKDocs couldn't find the files (I checked the folder layout and file locations).

