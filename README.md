# Recipe_Book
A recipe book program
This program was created during the 2021 KnightHacks Hackathon.
To run on local enverioment: 
# Have python3 and pip up to date
# Clone Repo 
# create virtual enviroment: 
>>$ python3 -m venv .venv
>>$ source .venv/bin/activate

# Install Django
>>(.venv) $ python -m pip install Django==3.2.1

# Create Local Database 
>>(.venv) $ python manage.py migrate

# Run server
>>(.venv) $ python manage.py runserver

#Open Local development host
http://127.0.0.1:8000/
