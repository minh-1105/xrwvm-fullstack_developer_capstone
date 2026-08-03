# Cars Dealership

Full-stack development capstone project for a national car dealership. The app
uses Django for the backend, static HTML/CSS pages for About and Contact, and a
React registration component for the frontend source requirement.

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
