from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Test"}

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

class Note(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    pinned: bool
  
@app.get("/api/notes", tags=["notes"])
async def get_notes() -> list:
    return notes
  
@app.get("/api/notes/{note_id}", tags=["notes"])
async def get_note(note_id: str):
    try:
        note_id = int(note_id)
    except ValueError:
        pass
    if isinstance(note_id, int):
        for note in notes:
            if note["id"] == note_id:
                return note
        raise HTTPException(status_code=404, detail="Note not found")
    
    raise HTTPException(status_code=400, detail="Invalid ID")
  
@app.post("/api/notes", tags=["notes"])
async def create_note(note: Note):
    note_id = notes[-1]["id"] + 1 if notes else 1
    for existing_note in notes:
        if existing_note["id"] == note_id:
            raise HTTPException(status_code=400, detail="Note with this ID already exists")
    
    new_note = note.dict()
    new_note["id"] = note_id  # Assign the generated ID
    
    notes.append(new_note)
    return {"message": "Note added successfully", "note": note}

@app.put("/api/notes/{note_id}", tags=["notes"])
async def update_note(note_id: int, updated_note: Note):
    for index, note in enumerate(notes):
        if note["id"] == note_id:
            notes[index] = updated_note.dict()
            return {"message": "Note updated successfully", "note": updated_note}
    
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/api/notes/{note_id}", tags=["notes"])
async def delete_note(note_id: int):
    for index, note in enumerate(notes):
        if note["id"] == note_id:
            deleted_note = notes.pop(index)
            return {"message": "Note deleted successfully", "note": deleted_note}
    
    raise HTTPException(status_code=404, detail="Note not found")