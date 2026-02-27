from fastapi import APIRouter, HTTPException
from app.models.schemas import TransformRequest, TransformResponse, PlatformOutput
from app.services.llm import generate_for_platform
from app.services.scraper import scrape_url

router = APIRouter()

@router.post("/transform", response_model=TransformResponse)
def transform(request:TransformRequest) -> TransformResponse:
    if request.input_type == "url":
        try:
            content = scrape_url(request.content)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error scraping URL: {str(e)}")
    else:
        content = request.content
    
    
    platforms = ["linkedin", "twitter", "email", "seo"]
    outputs = {}
    for platform in platforms:
        outputs[platform] = PlatformOutput(
            platform=platform,
            content=generate_for_platform(platform, content)
        )
        
    return TransformResponse(**outputs)