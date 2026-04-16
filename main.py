from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "sqlite:///./tickets.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class TicketDB(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, default="Open")
    priority = Column(String, default="Medium")
    category = Column(String, default="General")
    assigned_to = Column(String, default="Unassigned")
    requester = Column(String, default="User")
    created_at = Column(
        String,
        default=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


Base.metadata.create_all(bind=engine)


class TicketCreate(BaseModel):
    requester: str
    title: str
    description: str
    priority: str
    category: str


class TicketUpdate(BaseModel):
    status: str
    assigned_to: str


@app.get("/")
def home():
    return {"message": "IT Ticketing System is running"}


@app.get("/tickets")
def get_tickets():
    db = SessionLocal()
    tickets = db.query(TicketDB).all()

    result = []
    for t in tickets:
        result.append({
            "id": t.id,
            "ticket_number": f"INC-{1000 + t.id}",
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "priority": t.priority,
            "category": t.category,
            "assigned_to": t.assigned_to,
            "requester": t.requester,
            "created_at": t.created_at
        })

    db.close()
    return result


@app.post("/tickets")
def create_ticket(ticket: TicketCreate):
    db = SessionLocal()

    new_ticket = TicketDB(
        requester=ticket.requester,
        title=ticket.title,
        description=ticket.description,
        status="Open",
        priority=ticket.priority,
        category=ticket.category,
        assigned_to="Unassigned"
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    result = {
        "id": new_ticket.id,
        "ticket_number": f"INC-{1000 + new_ticket.id}",
        "title": new_ticket.title,
        "description": new_ticket.description,
        "status": new_ticket.status,
        "priority": new_ticket.priority,
        "category": new_ticket.category,
        "assigned_to": new_ticket.assigned_to,
        "requester": new_ticket.requester,
        "created_at": new_ticket.created_at
    }

    db.close()
    return result


@app.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, update: TicketUpdate):
    db = SessionLocal()
    ticket = db.query(TicketDB).filter(TicketDB.id == ticket_id).first()

    if not ticket:
        db.close()
        raise HTTPException(status_code=404, detail="Ticket not found")

    ticket.status = update.status
    ticket.assigned_to = update.assigned_to

    db.commit()
    db.refresh(ticket)

    result = {
        "id": ticket.id,
        "ticket_number": f"INC-{1000 + ticket.id}",
        "title": ticket.title,
        "description": ticket.description,
        "status": ticket.status,
        "priority": ticket.priority,
        "category": ticket.category,
        "assigned_to": ticket.assigned_to,
        "requester": ticket.requester,
        "created_at": ticket.created_at
    }

    db.close()
    return result


@app.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    db = SessionLocal()
    ticket = db.query(TicketDB).filter(TicketDB.id == ticket_id).first()

    if not ticket:
        db.close()
        raise HTTPException(status_code=404, detail="Ticket not found")

    db.delete(ticket)
    db.commit()
    db.close()

    return {"message": "Deleted successfully"}
