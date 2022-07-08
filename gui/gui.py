from .interactive import Interactive


class GUI:
    def __init__(self, canvas):
        self.canvas = canvas
        self.controls = []

    def add_control(self, control):
        self.controls.append(control)

    def handle_events(self, event):
        for control in self.controls:
            control.handle_events(event)

    def render(self):
        for control in self.controls:
            control.render(self.canvas)

    def unload(self):
        self.controls.clear()
