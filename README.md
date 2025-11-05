# LuxePaws Dog Walking

A sensational, AI-inspired marketing site for a luxury dog walking concierge. Built with Flask so you can expand into full booking and database capabilities.

## Project structure

```
.
├── app.py                # Development entry point
├── wsgi.py               # Production-ready WSGI entry point
├── config.py             # Configuration classes (update secrets here)
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
├── dogwalker/
│   ├── __init__.py       # Flask application factory & extension setup
│   ├── models.py         # SQLAlchemy model stubs (Booking example)
│   ├── routes.py         # Page routes for Home, Services, Booking, About
│   ├── templates/        # Jinja templates for the four site pages
│   └── static/           # Compiled CSS, JS, and image references
└── instance/
    └── (created at runtime for SQLite database)
```

## Getting started

1. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # update SECRET_KEY, DATABASE_URL, and SITE_BASE_URL as needed
   ```
4. **Initialize the database (optional until you add models/migrations)**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
5. **Run the development server**
   ```bash
   flask run
   ```

The site includes all HTML, CSS, and JavaScript required to render four polished pages. Extend the `Booking` model and add forms/controllers as you integrate real scheduling, payments, and automation.

### Deployment URL

Set `SITE_BASE_URL` to the fully qualified domain where you deploy (e.g. `https://dogwalking-opxq.onrender.com`) so canonical tags and share metadata point to the live site.
