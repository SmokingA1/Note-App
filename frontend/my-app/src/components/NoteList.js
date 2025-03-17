import React from "react";

const NoteList =({notes}) => {
    if (!Array.isArray(notes)) {
        console.error("Expected an array for notes, but got", typeof notes);
        return <p>Something went wrong with the data.</p>;
    }

    return(
        <div>
            {notes.map(note => (
                <div key={note.id}>
                    <p>{note.text}</p>
                    <span>{note.tag}</span>
                </div>
            ))}
        </div>
    );
};


export default NoteList;