from fastapi import APIRouter, HTTPException, Query
from typing import List, Any

from app.schemas import NoteRead, NoteUpdate, NoteCreate
from app.services.note import (
    get_note_by_id,
    get_notes,
    create_note,
    update_note,
    delete_note
)
from app.core.database import SessionDep

router = APIRouter(prefix='/notes', tags=['Note'])

@router.get("/", response_model=List[NoteRead])
async def read_notes(
    db: SessionDep,
    filter_tag: str = Query(None, title='Filter tag is required'),
    page: int = Query(1, title='Page number is required'),
    limit: int = Query(20, title='Limit of notes is required')
) -> Any:
    """Get notes with pagination and filtration."""
    db_notes = await get_notes(db, filter_tag=filter_tag, page=page, limit=limit)
    
    if not db_notes:
        raise HTTPException(status_code=404, detail='Notes not found!')
    
    return db_notes


@router.get("/{note_id}", response_model=NoteRead)
async def read_note_by_id(db: SessionDep, note_id: int) -> Any:
    """Get note by id."""
    db_note = await get_note_by_id(db, note_id)
    
    if not db_note:
        raise HTTPException(status_code=404, detail='Note not found!')
    
    return db_note


@router.post('/', response_model=NoteRead)
async def create_new_note(db: SessionDep, note_create: NoteCreate) -> Any:
    """Create new note."""
    new_note = await create_note(db, note_create)
    
    if not new_note:
        raise HTTPException(status_code=400, detail='Something went wrong!')
    
    return new_note


@router.put("/{note_id}", response_model=NoteRead)
async def update_existing_note(
    db: SessionDep,
    note_id: int,
    note_update: NoteUpdate
) -> Any:
    """Update as existing note by id."""
    db_note = await get_note_by_id(db, note_id)

    if not db_note:
        raise HTTPException(status_code=404, detail='Note not found!')
    
    updated_note = await update_note(db, note_id, note_update)
    
    return updated_note


@router.delete("/{note_id}", response_model=NoteRead)
async def delete_existing_note(db: SessionDep, note_id: int) -> Any:
    """Delete an existing note by id."""
    db_note = await get_note_by_id(db, note_id)

    if not db_note:
        raise HTTPException(status_code=404, detail='Note not found!')
    
    deleted_note = await delete_note(db, note_id)

    return deleted_note