Here’s the **entire README in clean plain text** so you can copy-paste it easily into any text editor or your GitHub `README.md`:

---

# Personal Health Tracker App

A web-based application that helps users track their daily health status, symptoms, medications, and vitals—designed to promote personal wellbeing and health awareness.

---

## Live Demo

* Frontend (Netlify): [https://reliable-cheesecake-01ebcf.netlify.app/](https://reliable-cheesecake-01ebcf.netlify.app/)
* Backend (Render): [https://personal-health-tracker-app-2.onrender.com/](https://personal-health-tracker-app-2.onrender.com/)

---

## Tech Stack

Frontend: HTML, CSS, Vanilla JS, Netlify Hosting
Backend: FastAPI (Python) hosted on Render
Database: PostgreSQL on Render Cloud Database
ORM: SQLAlchemy with psycopg2-binary
Deployment: Netlify (Frontend) + Render (Backend & Database)

---

## Project Structure

Personal\_Health\_Tracker\_app/
│
├── backend/
│   ├── models/
│   │   ├── medication.py
│   │   ├── symptom.py
│   │   ├── user.py
│   │   └── vitals.py
│   ├── routers/
│   │   ├── medication.py
│   │   ├── symptom.py
│   │   ├── user.py
│   │   └── vitals.py
│   ├── schemas/
│   │   └── database.py
│   └── main.py
│
├── frontend/
│   ├── static/
│   │   ├── images/
│   │   └── \*.css
│   ├── \*.html
│   └── \_redirects
│
├── healthtracker.db
├── requirements.txt
├── README.md
└── venv/

---

## Features

* User Registration & Login (HTML forms)
* Symptom Tracking
* Medication Tracking
* Vital Signs Recording
* Daily Health Reports
* Responsive Design with CSS
* RESTful FastAPI Backend

---

## Setup Instructions

### 1. Clone the Repository

git clone [https://github.com/Syaransh-Chaurasia/Personal\_Health\_Tracker\_app.git](https://github.com/Syaransh-Chaurasia/Personal_Health_Tracker_app.git)
cd Personal\_Health\_Tracker\_app

---

### 2. Frontend Setup (HTML + CSS + Netlify)

* No build process needed. Files are in the frontend/ folder.
* Deploy the contents of /frontend to Netlify.
* Make sure your forms or JavaScript (if any) call the correct backend API:

Backend URL: [https://personal-health-tracker-app-2.onrender.com/](https://personal-health-tracker-app-2.onrender.com/)

---

### 3. Backend Setup (FastAPI + Render)

cd backend
python -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt

Create `.env` file inside `/backend` folder with:

DATABASE\_URL=postgresql://healthtracker\_db\_ro1m\_user\:FwEWHi9HeuhhWoDBHd3dhccgXKYaWJQA\@dpg-d1mlgnu3jp1c73dqpqa0-a.frankfurt-postgres.render.com/healthtracker\_db\_ro1m

Run the server locally:

uvicorn main\:app --reload

---

### 4. Database Setup

* Create your PostgreSQL database on Render.
* Use the external database URL for local development.
* Use the internal database URL when running backend on Render.
* Install psycopg2-binary:

pip install psycopg2-binary

---

### 5. Deployment Steps

#### Frontend (Netlify):

* Deploy the `/frontend` folder to Netlify:
  [https://reliable-cheesecake-01ebcf.netlify.app/](https://reliable-cheesecake-01ebcf.netlify.app/)
* Ensure forms or API calls point to:
  [https://personal-health-tracker-app-2.onrender.com/](https://personal-health-tracker-app-2.onrender.com/)

#### Backend (Render):

* Deploy the `/backend` folder to Render.
* Add environment variable:
  DATABASE\_URL = (Render’s internal database URL)
* Set CORS to allow requests from:
  [https://reliable-cheesecake-01ebcf.netlify.app](https://reliable-cheesecake-01ebcf.netlify.app)

---

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.

---

## Contact

Name: Syaransh Chaurasia
Email: [syaransh.chaurasiauk@gmail.com](mailto:syaransh.chaurasiauk@gmail.com)
GitHub: [https://github.com/Syaransh-Chaurasia](https://github.com/Syaransh-Chaurasia)

---

✅ This is now **plain text**—no Markdown formatting—so you can paste it anywhere you like.

Let me know if you’d like `.env.example` or backend CORS setup as well.
