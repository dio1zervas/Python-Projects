from random import randint
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import pickle

app = Ursina()
window.fullscreen = True
window.color = color.black
window.title = "Glass Bridge"
window.fps_counter.enable()
window.exit_button = False
mouse.locked = False

score = 500
timer = 500

background_sound = Audio('data/squid_game_sound.mp3',
                         volume=0.5, loop=True, autoplay=True)

player = FirstPersonController(
    collider='box', jump_duration=0.45
)
player.win = False
player.cursor.visible = False
player.dead = 0
ground = Entity(
    model='plane',
    texture='grass',
    collider='mesh',
    position=Vec3(0, 0, -3),
    scale=(30, 0, 10)
)

pill1 = Entity(
    model='cube',
    color=color.violet,
    scale=(0.4, 0.1, 53),
    z=28, x=-0.7
)
pill2 = duplicate(pill1,
                  x=-3.7)
pill3 = duplicate(pill1,
                  x=0.6)
pill4 = duplicate(pill1,
                  x=3.6)


blocks = []
for i in range(12):
    block = Entity(
        model='cube', collider='box',
        color=color.white50,
        position=(2, 0.1, 3+i*4),
        scale=(3, 0.1, 2.5)
    )

    block2 = duplicate(block,
                       x=-2.2)
    blocks.append(
        (block, block2, randint(0, 10) > 7,
         randint(0, 10) > 7)
    )
goal = Entity(
    color=color.brown,
    model='cube',
    z=55,
    scale=(10, 1, 10),
    collider='box',
)
pillar = Entity(
    color=color.brown,
    model='cube',
    z=58,
    scale=(1, 15, 1), y=8,
    collider='box',
)


def reset():
    global score
    score = 0
    with open('data/meta.akl', 'wb') as f:
        f.write(
            pickle.dumps(str(int(500)))
        )


# reset()


def saveScore(path="data/meta.akl"):
    global high_score
    try:
        with open(path, 'rb') as f:
            high_score = pickle.loads(f.read())
    except Exception as error:
        print("ERROR:", error)
        high_score = 0
        quit()

    if int(timer-int(high_score)) < int(timer-int(score)):
        with open(path, 'wb') as f:
            f.write(
                pickle.dumps(str(int(score)))
            )


def quitGame():
    application.quit()
    quit()


break_sound = Audio('data/break.mp3', autoplay=False)
break_sound.volume = 1.5


def restart():
    os.popen('python game.py')
    quitGame()
    # global score, pill1, pill2, pill3, pill4, blocks, goal, pillar, ground

    # player = FirstPersonController(
    #     collider='box', jump_duration=0.45
    # )
    # player.cursor.visible = False
    # player.dead = 0
    # player.win = False
    # ground = Entity(
    #     model='plane',
    #     texture='grass',
    #     collider='mesh',
    #     position=Vec3(0, 0, -3),
    #     scale=(30, 0, 10)
    # )

    # pill1 = Entity(
    #     model='cube',
    #     color=color.violet,
    #     scale=(0.4, 0.1, 53),
    #     z=28, x=-0.7
    # )
    # pill2 = duplicate(pill1,
    #                   x=-3.7)
    # pill3 = duplicate(pill1,
    #                   x=0.6)
    # pill4 = duplicate(pill1,
    #                   x=3.6)

    # blocks = []
    # for i in range(12):
    #     block = Entity(
    #         model='cube', collider='box',
    #         color=color.white50,
    #         position=(2, 0.1, 3+i*4),
    #         scale=(3, 0.1, 2.5)
    #     )
    #     block2 = duplicate(block,
    #                        x=-2.2)
    #     blocks.append(
    #         (block, block2, randint(0, 10) > 7,
    #          randint(0, 10) > 7)
    #     )
    # goal = Entity(
    #     color=color.brown,
    #     model='cube',
    #     z=55,
    #     scale=(10, 1, 10),
    #     collider='box',
    # )
    # pillar = Entity(
    #     color=color.brown,
    #     model='cube',
    #     z=58,
    #     scale=(1, 15, 1), y=8,
    #     collider='box',
    # )

    # menu_button.enable()
    # menu_rect.disable()
    # restart_button.disable()
    # quit_button.disable()
    # mouse.locked = True


saveScore()


Text.size = .1
score_text = Text(text=str(score), origin=(0, 0.50), position=(
    -0.40, 0.45), font='data/orange juice 2.0.ttf', color=color.black)
high_score_text = Text(text=f"Best Time: {str(high_score)}", origin=(
    00, 0.50), position=(-0.55, 0.35), font='data/orange juice 2.0.ttf', color=color.black)

alert_button = Button(icon='data/alert',
                      scale=.25, position=(-0.75, 0))
alert_button.disable()


menu_button = Button(icon='data/menu2',
                     scale=.1, position=(-0.80, -0.40))

menu_rect = Entity(parent=camera, position=(-0.75, 0.0, 0), scale=(0.3, 1), model='quad',
                   color=color.gray, enabled=False)

restart_button = Button(icon='data/restart',
                        scale=.1, position=(-0.80, 0.40), enabled=False, on_click=restart)

quit_button = Button(icon='data/quit',
                     scale=.1, position=(-0.80, 0.20), enabled=False, on_click=quitGame)

win_button = Button(text=f'     You Won!\nYour Score: {int(score)}', color=color.azure,
                    scale=1, position=(0, 0), text_origin=(-.15, 0))
win_button.disable()
win_button.on_click = restart


def update_time(sec):
    global score
    if sec == 0:
        score_text.size = Text.size
        score_text.text = f"Time left {sec} seconds! YOU DIDN'T MAKE IT!"
        # label.create_background()
        player.speed = 0

    if sec > 0 and menu_button.enabled and not player.win:
        score_text.size = Text.size
        win_button.text = f'     You Win!\nYour Score: {int(sec)}'
        invoke(update_time, sec - 1, delay=1)
        score -= 1
        score_text.text = f'Time left {sec} seconds'
        # label.create_background()


update_time(int(score))


def update():
    global score
    # score_text.text = str(int(score))

    for block1, block2, k, n in blocks:
        for x, y in [(block1, k),
                     (block2, n)]:
            if x.intersects() and y:

                invoke(destroy, x,
                       delay=0.25)
                alert_button.enable()
                alert_button.blink()
                break_sound.play()
                x.fade_out(duration=0.15)
                invoke(alert_button.disable, delay=0.5)

    if player.intersects(goal):
        player.win = True
        saveScore()
        win_button.enable()

    if player.y < -20:
        player.position = Vec3(0, 0, 0)
        player.dead += 1


def input(key):
    if key == 'escape' or key == 'q':
        quit()
    if key == "tab":
        if menu_button.enabled:
            menu_button.disable()
            menu_rect.enable()
            restart_button.enable()
            quit_button.enable()
            mouse.locked = False

        else:
            menu_button.enable()
            menu_rect.disable()
            restart_button.disable()
            quit_button.disable()
            update_time(int(score))
            mouse.locked = True


Sky()
app.run()
