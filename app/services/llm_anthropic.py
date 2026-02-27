import anthropic
from anthropic.types import TextBlock
from app.core.config import get_settings


def get_client() -> anthropic.Anthropic:
    settings = get_settings()
    return anthropic.Anthropic(api_key=settings.anthropic_api_key)

def generate_for_platform(platform:str, content:str, prompt_template:str) -> str:
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