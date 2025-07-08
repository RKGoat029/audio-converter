import { useState } from "react";
import axios from "axios";
import "./home.css";

const Home = () => {
  const [urlValue, setUrlValue] = useState("");
  const [response, setResponse] = useState(null);
  const [downloadReady, setDownloadReady] = useState(false);

  const handleChange = (e) => setUrlValue(e.target.value);

  async function downloadMedia(link, format = "audio") {
    try {
      const res = await axios.get('http://127.0.0.1:8000/download', { params: { link, format } });
      return res.data;
    } catch (err) {
      console.log("Error: " + err);
      return null;
    }
  }

  const handleDownload = async () => {
    setDownloadReady(false);
    setResponse(null);
    const result = await downloadMedia(urlValue, "audio");
    if (result && result.filename) {
      setResponse(result);
      setDownloadReady(true);
    } else {
      setResponse({ error: "Download failed or invalid URL." });
    }
  };

  // This will generate the download link for the file
  const getDownloadUrl = (filename) => `http://127.0.0.1:8000/download/file/${encodeURIComponent(filename)}`;

  return (
    <>
      <input
        type="text"
        value={urlValue}
        onChange={handleChange}
        className="input-container"
        placeholder="Enter URL here"
      />
      <button onClick={handleDownload}>Fetch & Prepare Download</button>
      {response && response.error && (
        <div style={{ color: "red" }}>{response.error}</div>
      )}
      {downloadReady && response && response.filename && (
        <div>
          <p>File ready: {response.filename}</p>
          <a
            href={getDownloadUrl(response.filename)}
            download
            target="_blank"
            rel="noopener noreferrer"
          >
            Download File
          </a>
        </div>
      )}
    </>
  );
};

export default Home;