# connexion-example

This is code & installation instructions for Medium article:
https://medium.com/@stefanczykb/connexion-production-grade-rest-api-in-150-lines-of-python-ede3ab7f1555

## Intro

A minimal example of a backend server useful in real world application. The data model is simplistic - we'll have 2 tables: Users and Articles,
where a user has multiple articles and can add/remove/modify them using the following 4 endpoints:
- GET /articles (to get all articles of the user)
- POST /articles (to create a new article)
- PUT /articles/{article_id} (to update an existing article)
- DELETE /articles/{article_id} (delete an existing article)

How the effort is distributed in terms of lines of code:
- Auth (token handling + login endpoint): ~50 lines
- Database definition (2 tables): ~20 lines
- Endpoints code (4 CRUD endpoints with queries): ~50 lines
- Framework & server setup: ~25 lines
- API definition & schema (OpenAPI yaml): 130 lines

## Instalation
After cloning the repository, create a new Python >3.7 virtual env and activate it.

Next, install all requirements with:
```
pip install -r requirements.txt
```

Initialize database and add mock data:
```
python setup_db.py
```

Run with:
```
flask run --reload
```

To enter the Swagger UI, open in your browser:
http://127.0.0.1:5000/api/ui
