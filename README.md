# erp-report

Step 1: Clone project
Step 2: Create virtual environment
    virtualenv env
    source env/bin/acivate
Step 3: Install requirement
    pip install -r requirement.txt
Step 4: migrate data and create superuser
    python manage.py makemigrations
    python manage.py migrate
    python manage.py create superuser
Step 5: Config IP
    in erp_report/settings.py, add server ip to ALLOWED_HOSTS
Step 6: Run server
    python manage.py runserver 0.0.0.0:8000
Step 7: Config backend address
    login http://localhost:8000/admin/report/setting/1/change/
    with superuser
    key: backend_address
    value: your_server_ip (ex: 10.2.8.163:8090)

