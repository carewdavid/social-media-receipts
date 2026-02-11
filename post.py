from dataclasses import dataclass
from pillow import Image

@dataclass()
class Post:
    """Basic representation of an item to print. This is potentially coming from multiple sources with different formats, so only has a lowest common denominator of data"""
    user_handle: str
    body: str
    attachments: list[Image]

