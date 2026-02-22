import anthropic
from anthropic.types import TextBlock
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

def get_client() -> anthropic.Anthropic:
    settings = get_settings()
    return anthropic.Anthropic(api_key=settings.anthropic_api_key)

def generate_for_platform(platform:str, content:str) -> str:
    prompt_template = PLATFORM_PROMPTS[platform]
    prompt = prompt_template.format(content=content)

    client = get_client()
    message = client.messages.create(
        model = "claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    block = message.content[0]
    if not isinstance(block, TextBlock):
        raise ValueError(f"Expected a TextBlock, but got {type(block)}")
    return block.text

    