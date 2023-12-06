from enum import Enum


class DarkThemeColor(Enum):
    PRIMARY = "#034e78"
    SECONDARY = "#303030"
    SUCCESS = "#a3e635"
    WARNING = "#ffb400"
    DANGER = "#e21d48"
    INFO = "#17a2b7"
    LIGHT = "#dddddd"
    WHITE = "#ffffff"
    OUTLINE = "#009bf0"
    BACKGROUND = "#111111"
    CONTENT = "#1c1d21"
    HOVER = "#242424"
    DARK_GREEN = "#162827"
    MEDIUM_GREEN = "#173936"


DARK_THEME_GRID = {
    "accent_color": DarkThemeColor.PRIMARY.value,
    "accent_light": "rgba(202, 206, 255, 0.253)",
    "text_dark": DarkThemeColor.WHITE.value,
    "text_medium": DarkThemeColor.LIGHT.value,
    "text_light": DarkThemeColor.LIGHT.value,
    "text_bubble": DarkThemeColor.WHITE.value,
    "bg_icon_header": DarkThemeColor.LIGHT.value,
    "fg_icon_header": DarkThemeColor.BACKGROUND.value,
    "text_header": DarkThemeColor.LIGHT.value,
    "text_header_selected": DarkThemeColor.BACKGROUND.value,
    "bg_cell": DarkThemeColor.BACKGROUND.value,
    "bg_cell_medium": DarkThemeColor.BACKGROUND.value,
    "bg_header": DarkThemeColor.CONTENT.value,
    "bg_header_has_focus": DarkThemeColor.HOVER.value,
    "bg_header_hovered": DarkThemeColor.HOVER.value,
    "bg_bubble": DarkThemeColor.BACKGROUND.value,
    "bg_bubble_selected": DarkThemeColor.BACKGROUND.value,
    "bg_search_result": DarkThemeColor.SECONDARY.value,
    "border_color": "rgba(225,225,225,0.2)",
    "drilldown_border": "rgba(225,225,225,0.4)",
    "link_color": DarkThemeColor.INFO.value,
}
