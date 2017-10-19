# erp-report

# Step 1: Clone project
# Step 2: Create virtual environment
    virtualenv env
    source env/bin/acivate
# Step 3: Install requirement
    pip install -r requirement.txt
# Step 4: migrate data and create superuser
    python manage.py makemigrations
    python manage.py migrate
    python manage.py create superuser
# Step 5: Config IP server and Backend api address
    in erp_report/settings.py:
        find ALLOWED_HOSTS array variable, and add your server ip to ALLOWED_HOSTS (ex: ALLOWED_HOSTS = ['localhost','10.2.8.35'])
        find API_URL variable, and modify backend api address (ex: API_URL = '10.2.8.28:8090')
# Step 6: Run server
    python manage.py runserver 0.0.0.0:8000


