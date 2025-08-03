# SEO Master Dashboard

Welcome to the **SEO Master Dashboard**, a modern Flask-based web application designed to help users manage and optimize their SEO performance. This project features a sleek, user-friendly interface with a homepage, feature pages (About, Services, Contact), and a secure dashboard with multiple tools for SEO analysis. User authentication (login/signup) is implemented with data stored in a PostgreSQL database. This README was last updated at 12:42 AM PKT on Monday, August 04, 2025.

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
- **Dependencies**: Managed via `requirements.txt` (see below for package list)

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

2. Install Dependencies
Install the required Python packages listed in requirements.txt:
pip install -r requirements.txt

blinker==1.9.0
breadability==0.1.20
certifi==2025.6.15
chardet==5.2.0
charset-normalizer==3.4.2
click==8.2.1
cmudict==1.0.33
colorama==0.4.6
docopt==0.6.2
Flask==3.1.1
idna==3.10
importlib_metadata==8.7.0
importlib_resources==6.5.2
itsdangerous==2.2.0
Jinja2==3.1.6
joblib==1.5.1
lxml==6.0.0
MarkupSafe==3.0.2
nltk==3.9.1
pycountry==24.6.1
pyphen==0.17.2
python-dotenv==1.1.1
regex==2024.11.6
requests==2.32.4
setuptools==80.9.0
sumy==0.11.0
textblob==0.19.0
textstat==0.7.7
tqdm==4.67.1
urllib3==2.5.0
Werkzeug==3.1.3
zipp==3.23.0


3. Configure Environment Variables
Create a .env file in the root directory with the following variables:
DB_NAME=your_database_name
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
FLASK_SECRET_KEY=your_secret_key_here  # Generate a random string for security

Replace your_database_name, your_postgres_user, your_postgres_password, and your_secret_key_here with appropriate values.
The FLASK_SECRET_KEY is used to secure sessions; you can generate one using import os; os.urandom(24) in Python.

4. Set Up the PostgreSQL Database

Create a PostgreSQL database:
CREATE DATABASE seo_master;

Connect to the database and create a users table:
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

