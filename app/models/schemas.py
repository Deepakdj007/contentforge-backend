from pydantic import BaseModel
from typing import Literal

class TransformRequest(BaseModel):
    input_type: Literal["url","text"]
    content:str

class PlatformOutput(BaseModel):
    platform: str
    content: str

class TransformResponse(BaseModel):
    linkedin: PlatformOutput
    twitter: PlatformOutput
    email: PlatformOutput
    seo: PlatformOutput