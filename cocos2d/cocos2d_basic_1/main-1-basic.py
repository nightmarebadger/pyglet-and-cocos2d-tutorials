from __future__ import division

from cocos.actions import Move
from pyglet.window import key

import cocos
import resources


class Game(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__(102, 102, 225, 255)

        self.player = cocos.sprite.Sprite(resources.player)
        self.player.position = 400, 25
        self.player.velocity = 0, 0
        self.player.speed = 150
        self.add(self.player, z=2)

        self.boss = cocos.sprite.Sprite(resources.boss)
        self.boss.position = 400, 600
        self.boss.scale = 0.4
        self.add(self.boss, z=1)

        self.batch = cocos.batch.BatchNode()
        self.enemies = [cocos.sprite.Sprite(resources.enemy)
                        for i in range(6)]
        positions = ((250, 125), (550, 125),
                     (300, 325), (500, 325),
                     (150, 475), (650, 475))
        for num, enem in enumerate(self.enemies):
            enem.position = positions[num]
            self.batch.add(enem)

        self.add(self.batch, z=1)

        self.player.do(Move())

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.player.velocity = -self.player.speed, 0
        elif symbol == key.RIGHT:
            self.player.velocity = self.player.speed, 0
        elif symbol == key.UP:
            self.player.velocity = 0, self.player.speed
        elif symbol == key.DOWN:
            self.player.velocity = 0, -self.player.speed
        elif symbol == key.SPACE:
            self.player.velocity = 0, 0

if __name__ == '__main__':
    cocos.director.director.init(
        width=800,
        height=650,
        caption="Catch your husband!"
    )

    game_layer = Game()
    game_scene = cocos.scene.Scene(game_layer)

    cocos.director.director.run(game_scene)
