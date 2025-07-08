from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from app.downloader import download_media

router = APIRouter()

@router.get("/download")
def download(
    link: str = Query(...), 
    format: str = Query("audio")):
    
    try:
        result = download_media(link, format)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        print(f"Download error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/downloads")
def list_downloads():
    files = [f.name for f in Path("downloads").iterdir() if f.is_file()]
    return {"files": files}

@router.get("/download/file/{filename}")
def get_file(filename: str):
    file_path = Path("downloads") / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(str(file_path))