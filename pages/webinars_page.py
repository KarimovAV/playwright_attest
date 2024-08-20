from dataclasses import dataclass


@dataclass()
class WebinarsPage:
    heading: str = "БЕСПЛАТНЫЕ ВЕБИНАРЫ "
    url: str = "https://stc.innopolis.university/webinars"
