from dataclasses import dataclass


@dataclass()
class BlogPage:
    heading: str = "Блог STC"
    url: str = "https://stc.innopolis.university/blog"
