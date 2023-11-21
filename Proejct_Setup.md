# First, create a directory for your project
; mkdir your-project-directory
; cd your-project-directory

# Next, install pytest using pipenv
; pipenv install pytest --python 3.11
# This may take a few minutes

# Create a folder for your testing files
; mkdir tests
; mkdir lib

# Create module init files in both `tests/` and `lib/` directories
; $null tests/__init__.py
; $null lib/__init__.py
# These might seem pointless, but they're important for Python to find
# all of your files.

# Verify your setup by running pytest
; pipenv run pytest
================================ test session starts ================================
platform darwin -- Python 3.1, pytest-7.2.0, pluggy-1.0.0
rootdir: .../your-project-directory
collected 0 items

=============================== no tests ran in 0.01s ===============================

# And create a repository for your changes
; git init .
; git add .
; git commit -m "Project setup"

# Then go and create a repository on github.com
# On the next screen after you have created the repository,
# follow the "Push an existing repository from the command line" section
# To push your project to your github repository
# It will look something like this...
; git remote add origin YOUR_REMOTE_ADDRESS
; git branch -M main
; git push -u origin main