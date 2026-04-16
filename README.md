# IT Help Desk Ticketing System

A full-stack IT support ticketing system built with FastAPI, SQLite, HTML, CSS, and JavaScript. This application allows users to create, manage, assign, and track IT support tickets through a simple dashboard.

GitHub Repo: https://github.com/ShuAyb-cell/it-help-desk-ticketing-system  
Live Demo (Local): file:///Users/shuayb/it-help-desk-ticketing-system/index.html 

---

## Features
- Create new tickets  
- View all tickets  
- Update ticket status (Open, In Progress, Resolved)  
- Assign tickets to technicians  
- Delete tickets  
- Track priority and category  

---

## Tech Stack
- Backend: FastAPI (Python)  
- Database: SQLite  
- Frontend: HTML, CSS, JavaScript  

---

## How to Run

1. Clone the repo:
git clone https://github.com/ShuAyb-cell/it-help-desk-ticketing-system.git  
cd it-help-desk-ticketing-system  

2. Install dependencies:
pip install fastapi uvicorn sqlalchemy pydantic  

3. Start the server:
uvicorn main:app --reload  

4. Open the app:
Open index.html in your browser  
OR go to: http://127.0.0.1:8000/tickets  

---

## API Endpoints
GET /tickets → Get all tickets  
POST /tickets → Create ticket  
PUT /tickets/{id} → Update ticket  
DELETE /tickets/{id} → Delete ticket  

---

## Example Ticket
{
  "requester": "John Doe",
  "title": "Password Reset",
  "description": "I forgot my password",
  "priority": "Medium",
  "category": "Account"
}

---

## What I Learned
- Built REST APIs with FastAPI  
- Connected frontend to backend using fetch  
- Used SQLite for data storage  
- Implemented CRUD operations  
- Debugged real-world issues (server errors, ports, Git conflicts)

---

## Author
Shu’ayb Yusuf  
https://github.com/ShuAyb-cell
