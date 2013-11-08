import pyglet

pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()

player = pyglet.resource.image("player.png")
enemy = pyglet.resource.image("enemy.png")
boss = pyglet.resource.image("boss.png")
