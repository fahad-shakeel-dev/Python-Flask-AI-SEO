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
