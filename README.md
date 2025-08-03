
# SEO Master Dashboard

Welcome to the **SEO Master Dashboard**, a modern Flask-based web application designed to help users manage and optimize their SEO performance. This project features a sleek, user-friendly interface with a homepage, feature pages (About, Services, Contact), and a secure dashboard with multiple tools for SEO analysis. User authentication (login/signup) is implemented with data stored in a PostgreSQL database. This README was last updated at 01:00 AM PKT on Monday, August 04, 2025.

## Project Overview

### Features
- **Homepage**: A modern UI showcasing the application's purpose and key offerings.
- **Feature Page**: Details about the application's capabilities.
- **About Page**: Information about the project and its creators.
- **Services Page**: Overview of the SEO services provided.
- **Contact Page**: A form for users to get in touch.
- **Dashboard**: A secure, authenticated dashboard with the following tools:
  - **Dashboard**: Overview of SEO performance metrics (Traffic, SEO Score, Page Views, Click Rate).
  - **Content Analyzer**: Analyze content (currently a "Coming Soon" placeholder).
  - **Keyword Research**: Research keywords (currently a "Coming Soon" placeholder).
  - **Competitor Analysis**: Analyze competitors (currently a "Coming Soon" placeholder).
  - **Site Audit**: Audit website performance (currently a "Coming Soon" placeholder).
  - **Gap Analyzer**: Identify content gaps (currently a "Coming Soon" placeholder with a red "Coming Soon" badge).
  - **SERP Analysis**: Analyze search engine results (currently a "Coming Soon" placeholder with a red "Coming Soon" badge).
  - **Analytics**: View performance metrics (currently a "Coming Soon" placeholder with a red "Coming Soon" badge).
  - **Settings**: Manage account preferences (currently a placeholder).

### Authentication
- **Login/Signup**: Users can register and log in with a name, email, and password.
- **User Data**: Stored securely in a PostgreSQL database with hashed passwords.

### Technologies
- **Framework**: Flask (v3.1.1)
- **Database**: PostgreSQL
- **Frontend**: HTML, Tailwind CSS (v2.2.19), Lucide Icons
- **Dependencies**: Managed via `requirements.txt`

## Prerequisites

Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **PostgreSQL** (v12 or higher recommended)
- **Git** (for cloning the repository)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/seo-master-dashboard.git
cd seo-master-dashboard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

#### requirements.txt Contents:
(textblinker==1.9.0, breadability==0.1.20, Flask==3.1.1, nltk==3.9.1, etc.)

### 3. Configure Environment Variables

Create a `.env` file:
```env
DB_NAME=your_database_name
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432

FLASK_SECRET_KEY=your_secret_key_here
RAPIDAPI_KEY=your_key_here
PSI_TIMEOUT=90
PSI_API_KEY=your_PSI_key_here
FLASK_SECRET_KEY=your_secret_key_here
```

### 4. Set Up the PostgreSQL Database

```sql
CREATE DATABASE seo_master;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

### 5. Run the Application
```bash
python __init__.py
# or
export FLASK_APP=__init__.py  # Windows: set FLASK_APP=__init__.py
flask run
```

## Usage

- **Sign Up**: Visit `/auth/signup`
- **Log In**: Visit `/auth/login`
- **Dashboard**: Visit `/dashboard` after login
- **Logout**: Use the sidebar "Sign Out" option

## Project Structure

```
seo-master-dashboard/
├── __init__.py              # Flask app initialization and configuration, sets up the Flask application, extensions, and app-wide settings
├── analyzer.py              # Contains logic for content analysis, such as evaluating text for SEO optimization, readability, and keyword density
├── competitor.py            # Handles competitor analysis, including comparing backlinks, keyword rankings, and other SEO metrics
├── keyword_difficulty.py    # Calculates keyword difficulty scores to assess the competitiveness of target keywords for SEO
├── routes.py                # Defines core Flask routes and ties together endpoints for the application’s main functionalities
├── site_audit.py            # Performs technical SEO audits, checking for issues like broken links, site speed, and mobile-friendliness
├── models/
│   └── middleware.py        # Contains database models (e.g., SQLAlchemy models) and middleware logic for request handling or authentication
├── routes/
│   ├── auth_routes.py       # Defines routes for authentication-related actions, such as login, signup, and logout
│   └── main_routes.py       # Manages primary application routes for pages like the dashboard, homepage, and other core features
├── static/
│   ├── css/                # CSS files (e.g., styles.css) for styling the application’s user interface
│   ├── js/                 # JavaScript files (e.g., navigation scripts) for client-side interactivity and functionality
│   └── images/             # Images (e.g., logo.png, homepage.jpg, dashboard.png) used across the application for branding and visuals
├── templates/
│   ├── auth/
│   │   ├── login.html      # Login page template for user authentication
│   │   └── signup.html     # Signup page template for user registration
│   ├── dashboard.html      # Main dashboard template displaying SEO tools and user data
│   ├── homepage.html       # Homepage template for the application’s landing page
│   ├── about.html          # About page template providing information about the application or company
│   ├── services.html       # Services page template detailing SEO services offered
│   ├── features.html       # Features page template highlighting key functionalities of the SEO dashboard
│   ├── contact.html        # Contact page template with forms or details for user inquiries
│   └── partials/
│       ├── dashboard/
│       │   ├── content-analyzer.html  # Template for the content analysis section of the dashboard
│       │   ├── keyword-research.html  # Template for the keyword research section of the dashboard
│       │   ├── competitor-analyzer.html  # Template for the competitor analysis section of the dashboard
│       │   ├── site-audit.html        # Template for the site audit section of the dashboard
│       │   ├── gap-analyzer.html      # Template for the gap analysis section, identifying content or keyword gaps
│       │   └── analytics.html         # Template for the analytics section, displaying SEO performance metrics
│       ├── HomeComponents/
│       │   ├── benefits-section.html  # Template for the benefits section on the homepage, showcasing advantages of the tool
│       │   ├── cta-section.html       # Template for the call-to-action section, encouraging user engagement
│       │   ├── feature-section.html   # Template for the features section, detailing key dashboard features
│       │   ├── hero-section.html      # Template for the hero section, a prominent banner on the homepage
│       │   └── testimonials-section.html  # Template for the testimonials section, displaying user reviews or feedback
│       ├── navbar.html      # Reusable navbar partial for consistent navigation across pages
│       └── footer.html      # Reusable footer partial for consistent footer content across pages
├── .env                    # Environment variables (e.g., DB_NAME, FLASK_SECRET_KEY) for secure configuration
├── requirements.txt        # Project dependencies, listing required Python packages (e.g., Flask, SQLAlchemy)
└── README.md               # Project documentation, including setup instructions, features, and usage details
```

## Contributing
Feel free to fork, open issues, or PRs.

## Contact
Email: fahad.shakeel.dev@gmail.com

## Acknowledgments
- Flask community
- Tailwind CSS & Lucide Icons



## 📸 Project Screenshots

Explore the key features and pages of the SEO Dashboard:

---

### 🏠 Home Page
![Home](screenshorts/Home.png)

---

### 📊 Dashboard
![Dashboard](screenshorts/Dashboard.png)

---

### 🔍 Keyword Research
![Keyword Research](screenshorts/Keyword-research.png)

---

### 🧠 Competitor Analysis
![Competitor Analysis](screenshorts/Competitor-analysis.png)

---

### 📑 Content Analyzer
![Content Analyzer](screenshorts/Content-analyzer.png)

---

### 🧩 Features Page
![Features](screenshorts/Features.png)

---

### 🔒 Auth Login / Signup
| Login | Signup |
|-------|--------|
| ![Login](screenshorts/Auth_login.png) | ![Signup](screenshorts/Auth_signup.png) |

---

### 🏢 About & Contact
| About | Contact                              |
|-------|--------------------------------------|
| ![About](screenshorts/About.png) | ![Contact](screenshorts/Contact.png) |

---

### 🛠 Services & Site Audit
| Services | Site Audit |
|----------|------------|
| ![Services](screenshorts/Services.png) | ![Audit](screenshorts/Site-audit.png) |
