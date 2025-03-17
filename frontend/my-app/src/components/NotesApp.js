import axios from "axios";

const API_URL = "http://127.0.0.1:8000/notes"

export const getNotes = async () => {
    const response = await axios.get(API_URL);
    return response.data;
}


export const createNote = async (text, tag) => {
    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text, tag }),
      });
  
      if (!response.ok) {
        throw new Error("Ошибка при создании заметки!");
      }
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Ошибка:", error);
      return null;
    }
  };
  