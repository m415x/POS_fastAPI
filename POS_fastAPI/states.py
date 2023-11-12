import reflex as rx


class State(rx.State):
    """The app state."""
    pass


class HeaderState(State):
    name: str = "Cristian Lahoz"
    color: str = "#9f0"

    def flip_color(self):
        if self.color == "#9f0":
            self.color = "blue"
        else:
            self.color = "#9f0"
