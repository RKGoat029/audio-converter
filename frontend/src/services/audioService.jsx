import axios from "axios";

export async function downloadMedia(link, format = "audio") {
    try {
      const res = await axios.get('http://127.0.0.1:8000/download', { params: { link, format } });
      return res.data;
    } catch (err) {
      console.log("Error: " + err);
      return null;
    }
  }

export const getDownloadUrl = (filename) => `http://127.0.0.1:8000/download/file/${encodeURIComponent(filename)}`;