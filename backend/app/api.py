from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated, Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

notes = [
    {
        "id": 1,
        "title": "Health",
        "description": "Read a book.",
        "pinned": False,
    },
    {
        "id": 2,
        "title": "Exercise",
        "description": "Cycle around town.",
        "pinned": True,
    }
]

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Test"}


class NoteBase(SQLModel):
    title: str
    description: str
    pinned: bool = Field(default=False)


class Note(NoteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    pinned: bool = Field(default=False)


class NotePublic(NoteBase):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    pinned: bool = Field(default=False)


class NoteCreate(NoteBase):
    title: str
    description: str
    pinned: bool = Field(default=False)


class NoteUpdate(NoteBase):
    title: str | None = None
    description: str | None = None
    pinned: bool | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/api/notes/", response_model=NotePublic)
def create_note(note: NoteCreate, session: SessionDep):
    db_note = Note.model_validate(note)
    session.add(db_note)
    session.commit()
    session.refresh(db_note)
    return db_note

@app.get("/api/notes/", response_model=list[NotePublic])
def read_notes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    notes = session.exec(select(Note).offset(offset).limit(limit)).all()
    return notes


@app.get("/api/notes/{note_id}", response_model=NotePublic)
def read_note(note_id: int, session: SessionDep):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.patch("/api/notes/{note_id}", response_model=NotePublic)
def update_note(note_id: int, note: NoteUpdate, session: SessionDep):
    note_db = session.get(Note, note_id)
    if not note_db:
        raise HTTPException(status_code=404, detail="Note not found")
    note_data = note.model_dump(exclude_unset=True)
    note_db.sqlmodel_update(note_data)
    session.add(note_db)
    session.commit()
    session.refresh(note_db)
    return note_db


@app.delete("/api/notes/{note_id}")
def delete_note(note_id: int, session: SessionDep):
    note = session.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    session.delete(note)
    session.commit()
    return {"ok": True}