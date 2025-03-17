import React, { useState } from "react";
import { createNote } from "./NotesApp";

const NoteForm = ({setNotes}) => {
    const [note, setNote] = useState({ text: "", tag: "" });

    const handleChange = (e) => {
      setNote({ ...note, [e.target.name]: e.target.value });
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      if (!note.text.trim() || !note.tag.trim()) return;
  
      const newNote = await createNote(note.text, note.tag);
  
      if (newNote) {
        setNotes(newNote); // Добавляем в список заметок
        setNote({ text: "", tag: "" }); // Очищаем поля
      }
    };


    return(
        <form className="note-form-add" onSubmit={handleSubmit}>
            <input
                type="text"
                name="text"
                placeholder="Enter note here"
                value={note.text}
                onChange={handleChange}
            /> 
            <input 
                type="text"
                name="tag"
                placeholder="Enter tag"
                value={note.tag}
                onChange={handleChange}
            />
            <button type="submit">Add Note</button>
        </form>
    )
}

export default NoteForm;
