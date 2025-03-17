import React from "react";
import Note from "./Note";

const NoteList = ({notes}) => {
    return(
        <div className="note-list-form">
            {notes.map((note) => (
                <Note
                key={note.id}
                note={note}
                />
            ))}
        </div>
    )
};

export default NoteList;
