import pyglet

pyglet.options["shadow_window"] = False
pyglet.options["debug_gl"] = False

import pyglet.gl as gl

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_draw(self):
        self.clear()
        
    def on_resize(self, width: int, height: int) -> None:
        return super().on_resize(width, height)
    
class Game:
    def __init__(self):
        self.window = Window(800, 600, "Pyglet Test")

    def run(self):
        pyglet.app.run()

if __name__ == "__main__":
    window = Window(800, 600, "Pyglet Test")
    pyglet.app.run()
