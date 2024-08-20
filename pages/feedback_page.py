from dataclasses import dataclass


@dataclass()
class FeedbackPage:
    heading: str = "Отзывы"
    url: str = "https://stc.innopolis.university/feedback"
