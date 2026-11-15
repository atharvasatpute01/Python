# What is a Virtual Environment?
# A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

# It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

# Think of a virtual environment as a separate container for each Python project. Each container:

# Has its own Python interpreter
# Has its own set of installed packages
# Is isolated from other virtual environments
# Can have different versions of the same package


# Using virtual environments is important because:

# It prevents package version conflicts between projects
# Makes projects more portable and reproducible
# Keeps your system Python installation clean
# Allows testing with different Python versions




# Creating a Virtual Environment
# Python has the built-in venv module for creating virtual environments.

# To create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command:

# python -m venv myfirstproject

# Activate Virtual Environment:

# myfirstproject\Scripts\activate

# Install Packages
# Once your virtual environment is activated, you can install packages in it, using pip.

# We will install a package called 'cowsay':

# pip install cowsay

# Using Package
# Now that the 'cowsay' module is installed in your virtual environment, lets use it to display a talking cow.

# Create a file called test.py on your computer. You can place it wherever you want, but I will place it in the same location as the myfirstproject folder -not in the folder, but in the same location.

# Open the file and insert these three lines in it:

# import cowsay

# cowsay.cow("Good Mooooorning!")

# Execute test.py in the virtual environment:

# python test.py

# Deactivate Virtual Environment
# To deactivate the virtual environment use this command:

# (myfirstproject) C:\Users\Your Name> deactivate