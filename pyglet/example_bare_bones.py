import pyglet

game_window = pyglet.window.Window()

@game_window.event
def on_draw():
    game_window.clear()

def update(dt):
    pass

if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 0.5)
    pyglet.app.run()
