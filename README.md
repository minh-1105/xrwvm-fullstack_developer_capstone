# fullstack_developer_capstone

Repository name: `xrwvm-fullstack_developer_capstone`

Project name: `fullstack_developer_capstone`

This is the Full Stack Developer Capstone project. The application implements a
national car dealership platform using Django for the backend, static HTML/CSS
pages for About and Contact, and a React registration component for the
frontend source requirement.

## Features

- Dealer listing and state filtering
- Dealer detail pages with customer reviews
- Login, logout, and review submission flows
- REST endpoints for dealers, reviews, cars, and sentiment analysis
- Django admin enabled for the root user

## Run locally

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.
