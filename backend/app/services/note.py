from sqlalchemy.future import select
from app.models import Note
from app.schemas import NoteCreate, NoteUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

async def get_note_by_id(db: AsyncSession, note_id: int) -> Note:
    db_note = await db.get(Note, note_id)
    return db_note

async def get_notes(
    db: AsyncSession,
    filter_tag: str,
    page: int = 1,
    limit: int = 20
) -> List[Note]:
    query = select(Note)
    if filter_tag:
        query = query.filter(Note.tag == filter_tag)
    
    offset=(page - 1) * limit
    query = query.offset(offset).limit(limit)
    db_notes = await db.execute(query)
    return db_notes.scalars().all()

async def create_note(db: AsyncSession, note_create: NoteCreate) -> Note:
    new_note = Note(text=note_create.text,
                    tag=note_create.tag
                    )
    
    db.add(new_note)
    await db.commit()
    await db.refresh(new_note)
    return new_note

async def update_note(db: AsyncSession, note_id: int, note_update: NoteUpdate) -> Note:
    db_note = await get_note_by_id(db, note_id)

    if not db_note:
        return None
    
    update_data = note_update.dict(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_note, key, value)
    
    await db.commit()
    await db.refresh(db_note)
    return db_note

async def delete_note(db: AsyncSession, note_id: int) -> Note:
    db_note = await get_note_by_id(db, note_id)

    if not db_note:
        return None
    
    await db.delete(db_note)
    await db.commit()
    return db_note    
