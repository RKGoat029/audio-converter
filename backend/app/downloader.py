import yt_dlp
from app.utils import sanitize_filename, ensure_downloads_dir, is_valid_url

def download_media(link: str, format: str = "audio") -> dict:
    """
    Downloads media from a URL using yt-dlp.
    
    Args:
        link (str): The media URL.
        format (str): 'audio' or 'video'.
    
    Returns:
        dict: Information about the downloaded file.
    """
    if not is_valid_url(link):
        return {"error": "Invalid URL"}

    output_dir = ensure_downloads_dir()

    ydl_opts = {
        'format': 'bestaudio/best' if format == 'audio' else 'best',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'quiet': True,  # suppress CLI output
        'noplaylist': True,
    }

    if format == 'audio':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            title = sanitize_filename(info.get("title", "download"))
            ext = "mp3" if format == "audio" else info.get("ext", "mp4")
            filename = f"{title}.{ext}"
            return {
                "title": info.get("title"),
                "filename": filename,
                "format": format,
                "status": "success"
            }
    except Exception as e:
        return {"error": f"Failed to download media: {str(e)}"}
