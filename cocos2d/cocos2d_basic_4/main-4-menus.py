from __future__ import division

from cocos.actions import AccelDeccel
from cocos.actions import Delay
from cocos.actions import JumpBy
from cocos.actions import Move
from cocos.actions import MoveBy
from cocos.actions import Repeat
from cocos.actions import Reverse
from cocos.actions import RotateBy
from pyglet.window import key

import cocos
import cocos.collision_model as cm
import pyglet
import resources


class Game(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Game, self).__init__(102, 102, 225, 255)

        self.collision_manager = cm.CollisionManagerBruteForce()

        self.player = cocos.sprite.Sprite(resources.player)
        self.player.position = 400, 25
        self.player.velocity = 0, 0
        self.player.speed = 150
        self.add(self.player, z=2)

        self.player.cshape = cm.AARectShape(
            self.player.position,
            self.player.width//2,
            self.player.height//2
        )
        self.collision_manager.add(self.player)

        self.boss = cocos.sprite.Sprite(resources.boss)
        self.boss.position = 400, 600
        self.boss.scale = 0.4
        self.add(self.boss, z=1)

        self.boss.cshape = cm.AARectShape(
            self.boss.position,
            self.boss.width//2,
            self.boss.height//2
        )
        self.collision_manager.add(self.boss)

        self.batch = cocos.batch.BatchNode()
        self.enemies = [cocos.sprite.Sprite(resources.enemy)
                        for i in range(6)]
        positions = ((250, 125), (550, 125), (300, 325), (500, 325),
                     (150, 475), (650, 475))
        for num, enem in enumerate(self.enemies):
            enem.position = positions[num]
            enem.cshape = cm.AARectShape(
                enem.position,
                enem.width//2,
                enem.height//2
            )
            self.collision_manager.add(enem)
            self.batch.add(enem)

        self.add(self.batch, z=1)
        self.player.do(Move())

        move_basic = MoveBy((120, 0), 1)
        self.enemies[0].do(Repeat(move_basic + Reverse(move_basic)))
        self.enemies[1].do(Repeat(Reverse(move_basic) + move_basic))

        move_complex = (MoveBy((-75, 75), 1) +
                        Delay(0.5) +
                        MoveBy((-75, -75), 1) +
                        Delay(0.5) +
                        MoveBy((75, -75), 1) +
                        Delay(0.5) +
                        MoveBy((75, 75), 1) +
                        Delay(0.5))
        self.enemies[2].do(Repeat(move_complex))
        self.enemies[3].do(Repeat(Reverse(move_complex)))

        move_jump = AccelDeccel(JumpBy((200, 0), 75, 3, 3))
        move_jump_rot = AccelDeccel(RotateBy(360, 3))
        self.enemies[4].do(Repeat(move_jump + Reverse(move_jump)))
        self.enemies[4].do(Repeat(move_jump_rot + Reverse(move_jump_rot)))
        self.enemies[5].do(Repeat(Reverse(move_jump) + move_jump))
        self.enemies[5].do(Repeat(Reverse(move_jump_rot) + move_jump_rot))

        self.schedule(self.update)

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

    def update(self, dt):
        self.player.cshape.center = self.player.position
        for enem in self.enemies:
            enem.cshape.center = enem.position

        collisions = self.collision_manager.objs_colliding(self.player)
        if collisions:
            if self.boss in collisions:
                print("You won!")
            cocos.director.director.pop()


class MainMenu(cocos.menu.Menu):

    def __init__(self):
        super(MainMenu, self).__init__('Catch your husband!')

        items = []

        items.append(cocos.menu.MenuItem('New game', self.on_new_game))
        items.append(cocos.menu.MenuItem('Options', self.on_options))
        items.append(cocos.menu.MenuItem('Quit', self.on_quit))

        self.create_menu(items)

    def on_new_game(self):
        game_layer = Game()
        game_scene = cocos.scene.Scene(game_layer)

        cocos.director.director.push(game_scene)

    def on_options(self):
        self.parent.switch_to(1)

    def on_quit(self):
        pyglet.app.exit()


class OptionsMenu(cocos.menu.Menu):
    def __init__(self):
        super(OptionsMenu, self).__init__('Catch your husband!')

        items = []

        items.append(cocos.menu.ToggleMenuItem(
            'Show FPS:',
            self.on_show_fps,
            cocos.director.director.show_FPS)
        )
        items.append(cocos.menu.MenuItem('Fullscreen', self.on_fullscreen))
        items.append(cocos.menu.MenuItem('Back', self.on_quit))
        self.create_menu(items)

    def on_fullscreen(self):
        cocos.director.director.window.set_fullscreen(
            not cocos.director.director.window.fullscreen)

    def on_quit(self):
        self.parent.switch_to(0)

    def on_show_fps(self, value):
        cocos.director.director.show_FPS = value


if __name__ == '__main__':
    cocos.director.director.init(
        width=800,
        height=650,
        caption="Catch your husband!"
    )

    scene = cocos.scene.Scene()
    scene.add(cocos.layer.MultiplexLayer(MainMenu(), OptionsMenu()), z=1)
    cocos.director.director.run(scene)
