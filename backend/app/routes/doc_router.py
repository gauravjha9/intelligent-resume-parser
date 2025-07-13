import json
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.services.helper import save_upload_to_temp_file, extract_text, chat_prompt
from app.services.llm import llm


router = APIRouter(prefix="", tags=["Resume Parser"])

@router.post('/upload-file')
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save file temporarily
        ext = file.filename.split('.')[-1].lower()
        suffix = f".{ext}"
        temp_file_path = save_upload_to_temp_file(file, suffix=suffix)

        # Extract text from file
        resume_text = extract_text(temp_file_path)
        
        # Generate JSON response via LLM
        chain = chat_prompt | llm
        response = chain.invoke({"resume_text": resume_text})

        # Return parsed JSON response
        parsed_json = json.loads(response.content)
        return JSONResponse(content=parsed_json)
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})