[Unit]
Description=Gunicorn daemon for Django
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/projects/jbach
ExecStart=/home/ubuntu/projects/jbach/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/ubuntu/projects/jbach/gunicorn.sock \
          project.wsgi:application

[Install]
WantedBy=multi-user.target