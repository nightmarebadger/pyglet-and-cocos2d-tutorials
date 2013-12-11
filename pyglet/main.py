from __future__ import division

from pyglet.window import key
import pyglet
import resources

fps_display = pyglet.clock.ClockDisplay(
    format='%(fps).1f',
    color=(0.5, 0.5, 0.5, 1)
)

game_window = pyglet.window.Window(
    width=800,
    height=650,
    caption="Catch your husband!"
)

game_window.set_mouse_visible(False)
pyglet.gl.glClearColor(0.4, 0.4, 1, 1)

player = pyglet.sprite.Sprite(resources.player, x=400, y=0)
player_x = 0
player_y = 0
player_speed = 150

enemies_batch = pyglet.graphics.Batch()
enemies_sprites = []
enemies_sprites.append(pyglet.sprite.Sprite(
    resources.enemy,
    x=250,
    y=100,
    batch=enemies_batch)
)
enemies_sprites.append(pyglet.sprite.Sprite(
    resources.enemy,
    x=550,
    y=100,
    batch=enemies_batch)
)
enemies_sprites.append(pyglet.sprite.Sprite(
    resources.enemy,
    x=300,
    y=300,
    batch=enemies_batch)
)
enemies_sprites.append(pyglet.sprite.Sprite(
    resources.enemy,
    x=500,
    y=300,
    batch=enemies_batch)
)
enemies_sprites.append(pyglet.sprite.Sprite(
    resources.enemy,
    x=150,
    y=450,
    batch=enemies_batch)
)
enemies_sprites.append(pyglet.sprite.Sprite(
    resources.enemy,
    x=650,
    y=450,
    batch=enemies_batch)
)

boss = pyglet.sprite.Sprite(resources.boss, x=400, y=550)
boss.scale = 0.4


@game_window.event
def on_draw():
    game_window.clear()
    enemies_batch.draw()
    boss.draw()
    player.draw()
    fps_display.draw()


@game_window.event
def on_key_press(symbol, modifiers):
    global player_x, player_y
    if symbol == key.LEFT:
        player_x = -player_speed
        player_y = 0
    elif symbol == key.RIGHT:
        player_x = player_speed
        player_y = 0
    elif symbol == key.UP:
        player_x = 0
        player_y = player_speed
    elif symbol == key.DOWN:
        player_x = 0
        player_y = -player_speed
    elif symbol == key.SPACE:
        player_x = 0
        player_y = 0


def update(dt):
    player.x += player_x * dt
    player.y += player_y * dt


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()
