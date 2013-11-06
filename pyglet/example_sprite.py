import pyglet
import resources

game_window = pyglet.window.Window()

@game_window.event
def on_draw():
    game_window.clear()
    sprite.draw()

def update(dt):
    pass

if __name__ == '__main__':
    sprite = pyglet.sprite.Sprite(resources.enemy, x=100, y=100)

    pyglet.clock.schedule_interval(update, 0.5)
    pyglet.app.run()
