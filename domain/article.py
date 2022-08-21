from typing import List

from domain.profile import Profile


class Article:
    slug: str  # how-to-train-your-dragon
    title: str  # How to train your dragon
    description: str  # Ever wonder how?
    body: str  # It takes a Jacobian
    tagList: List[str]  # ["dragons", "training"]
    author: Profile
    favorited: bool  # 스펙에 오타가 있는듯...
    favorites_count: int
