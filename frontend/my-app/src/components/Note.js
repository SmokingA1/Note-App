import React from "react";
const Note = ({note}) => {
    return (
        <div>
            <div className="note-view">
                    <p>#{note.id} {note.text} (Tag: {note.tag})</p>
                    <div className="note-view-buttons">
                    </div>
            </div>
        </div>
    );
};

export default Note;