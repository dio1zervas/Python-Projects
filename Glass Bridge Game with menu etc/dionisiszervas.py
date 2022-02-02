from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from random import randint

application.development_mode = True


app = Ursina()
Sky()
window.fullscreen = True
window.color = color.black
window.title = "Squid game 5"
window.fps_counter.enable()
window.exit_button = False
mouse.locked = False

player = FirstPersonController(
    collider='box', jump_duration=0.35,
)

player.cursor.visible = False
ground = Entity(
    model='plane',
    texture='grass',
    collider='mesh',
    scale=(30, 0, 3)
)

pill1 = Entity(
    model='cube',
    color=color.black,
    scale=(0.4, 0.1, 53),
    z=28, x=-0.7
)
pill2 = duplicate(pill1,
                  x=-3.7)
pill3 = duplicate(pill1,
                  x=0.6)
pill4 = duplicate(pill1,
                  x=3.7)

blocks = []
for i in range(12):
    block = Entity(
        model='cube',
        collider='box',
        color=color.white33,
        texture="white_cube",
        position=(2, 0.1, 3 + i * 4),
        scale=(3, 0.1, 2.5)
    )
    block2 = duplicate(block,
                       x=-2.2)
    blocks.append(
        (block, block2, randint(0, 10) < 0,
         randint(0, 10) < 0)
    )
goal = Entity(
    model='plane',
    texture='grass',
    collider='mesh',
    z=55,
    scale=(10, 1, 10),
)
pillar = Entity(
    color=color.red,
    model='cube',
    z=55,
    scale=(1, 15, 1), y=7.5
)
txt = Text(text="Welcome to the game!Good luck!", color=color.black, x=-.20, y=0.5)


def update():
    for block1, block2, k, n in blocks:
        for x, y in [(block1, k),
                     (block2, n)]:
            if x.intersects() and y:
                invoke(destroy, x,
                       delay=0.1)
                x.fade_out(duration=0.1)


def input(key):
    if key == 'q':
        quit()



background_sound = Audio('squid_game_sound.mp3', loop=True, autoplay=True)

label = Text(
    size=Text.size,
    text=f'Time left {00} seconds',
    position=(-0.5, 0.4)
)
label.create_background()


def update_time(sec):
    if sec == 0:
        label.size = Text.size
        label.text = f"Time left {sec} seconds! YOU DID'T MAKE IT!"
        label.create_background()

        player.speed = 0

    if sec > 0:
        label.size = Text.size
        invoke(update_time, sec - 1, delay=1)
        label.text = f'Time left {sec} seconds'
        label.create_background()


update_time(600)

app.run()
