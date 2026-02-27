from google import genai
from app.core.config import get_settings
from app.core.prompts import LINKEDIN_PROMPT, TWITTER_PROMPT, EMAIL_PROMPT, SEO_PROMPT


def generate_for_platform(platform:str, content:str, prompt_template:str) -> str:
    settings = get_settings()
    client = genai.Client(api_key=settings.gemini_api_key)

    prompt = prompt_template.format(content=content)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    if not response.text:
        raise ValueError(f"No text response from Gemini for platform: {platform}")
    
    return response.text