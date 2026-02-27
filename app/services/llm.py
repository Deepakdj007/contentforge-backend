from app.core.config import get_settings
from app.core.prompts import (
    LINKEDIN_PROMPT,
    TWITTER_PROMPT,
    EMAIL_PROMPT,
    SEO_PROMPT,
)

PLATFORM_PROMPTS={
    "linkedin": LINKEDIN_PROMPT,
    "twitter": TWITTER_PROMPT,
    "email": EMAIL_PROMPT,
    "seo": SEO_PROMPT,
}

def generate_for_platform(platform:str, content:str) -> str:
    settings = get_settings()

    if settings.llm_provider == "anthropic":
        from app.services.llm_anthropic import generate_for_platform as _generate
    elif settings.llm_provider == "gemini":
        from app.services.llm_gemini import generate_for_platform as _generate
    else:
        raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
    return _generate(platform, content, PLATFORM_PROMPTS[platform])