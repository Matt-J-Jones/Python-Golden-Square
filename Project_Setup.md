# First, create a directory for your project

; mkdir your-project-directory
; cd your-project-directory

## Create a folder for your testing files

; mkdir tests
; mkdir lib

## Create module init files in both `tests/` and `lib/` directories

```PS
; New-Item -Path ./tests/__init__.py -ItemType File
; New-Item -Path ./lib/__init__.py -ItemType File
```

## To Install pipenv

```PS
; pip install pipenv
; pipenv install requests
; pipenv run python -c "import requests"
```

## To activate the virtual environment (Before Running Tests)

```PS
; pipenv shell
; pytest
```

## These might seem pointless, but they're important for Python to find all of your files

## Verify your setup by running pytest

; py -m pytest

=============================== no tests ran in 0.01s ===============================

## And create a repository for your changes

; git init .
; git add .
; git commit -m "Project setup"

; git remote add origin YOUR_REMOTE_ADDRESS
; git branch -M main
; git push -u origin main
