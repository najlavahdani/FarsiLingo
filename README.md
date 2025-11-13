# FarsiLingo
This project is a comprehensive English learning app designed to help users improve their language skills through structured semesters, interactive lessons, vocabulary practice, and quizzes

---
## Setup

1. Clone the repository:

```bash
git clone https://github.com/najlavahdani/FarsiLingo.git
cd backend
```
2. Create a virtual environment and activate it:

 ```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```
3. Install dependencies:

 ```bash
pip install -r requirements.txt
```
## Environment Variables
1. Copy .env.example to .env:

 ```bash
cp .env.example .env
```
2. Fill in your database credentials:

 ```bash
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=FarsiLingo
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
SECRET_KEY=your_secret_key_here
DEBUG=True
```
## Database Setup
1. Make sure PostgreSQL is installed and running locally.

2. Create the database (if it doesn’t exist):

 ```bash
CREATE DATABASE FarsiLingo;
```
## Running the Server

 ```bash
fastapi dev src.main.py --reload
```
The app will run at: http://127.0.0.1:8000/
