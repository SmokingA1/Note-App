import React, { useState } from "react";

const NoteForm = ({addNote}) => {
    const [text, setText] = useState("");
    const [tag, setTag] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (text && tag) {
            console.log({tag, text})
            addNote({
                text,
                tag,
            });
            setText("");
            setTag("");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Enter note here"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <input
            type="text"
            placeholder="Enter tag"
            value={tag}
            onChange={(e) => setTag(e.target.value)}
          />
          <button type="submit">Add Note</button>
        </form>
      );

}

export default NoteForm;

