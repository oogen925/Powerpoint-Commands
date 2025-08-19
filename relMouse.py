from talon import Context, Module, actions, screen

mod = Module()
ctx = Context()

for s in screen.screens():
    w = s.width
    h = s.height

@mod.action_class
class Actions:
    def copy_relative_mouse_position():
        """Copy the current relative mouse position"""
        x, y = actions.mouse_x(), actions.mouse_y()
        x_ratio = x / w
        y_ratio = y / h
        actions.clip.set_text(f"{x_ratio}, {y_ratio}")

    def relative_move(ax: float, ay: float):
        """move to relative position on window"""
        x, y = 0, 0
        actions.mouse_move(x + (ax * w), y + (ay * h))

    