import pyglet

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

player = pyglet.resource.image("player.png")
enemy = pyglet.resource.image("enemy.png")
boss = pyglet.resource.image("boss.png")
background = pyglet.resource.image("background.png")

game_music = pyglet.resource.media('tetris.mp3', streaming=False)
