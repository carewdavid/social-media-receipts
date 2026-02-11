#Basic representation of an item to print. This is potentially coming from multiple sources with different formats, so only has a lowest common denominator of data
class Post:
    user_handle: str
    body: str

    def __init__(self, user_handle: str, body: str) -> None:
        self.body = body
        self.user_handle = user_handle
