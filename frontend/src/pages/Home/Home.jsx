import { useState } from "react";
import "./home.css";

/* Service */
import { downloadMedia, getDownloadUrl } from "../../services/audioService.jsx";

const Home = () => {
  const [urlValue, setUrlValue] = useState("");
  const [response, setResponse] = useState(null);
  const [downloadReady, setDownloadReady] = useState(false);

  const handleChange = (e) => setUrlValue(e.target.value);

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

  return (
    <>
      <input
        type="text"
        value={urlValue}
        onChange={handleChange}
        className="input-container"
        placeholder="Enter URL here"
      />
      <button onClick={handleDownload}>Send!</button>
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