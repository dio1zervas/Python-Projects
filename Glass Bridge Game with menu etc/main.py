from ursina import *
import pickle
app = Ursina()
window.fullscreen = True
window.color = color.azure
window.title = "Glass Bridge"
window.fps_counter.enable()
window.exit_button = False
mouse.locked = False
YOUR_NAME = "Dionisis & Dimos"


def Play():
    os.popen('python game.py')
    application.quit()


Text.default_resolution = 200
title = Text(text="Squid Game", font="data/font.ttf", origin_y=-.5, origin_x=-.5,
             position=(-.60, 0.45), scale=6, color=color.cyan, resolution=Text.default_resolution*5)

Text(text="Glass Bridge", font="data/font.ttf", origin_y=-.5, origin_x=-.5,
     position=(-.25, 0.25), scale=2)


Text(text=f"Made by {YOUR_NAME}", font="data/font.ttf", origin_y=-.5, origin_x=-.5,
     position=(-0.60, -0.15), scale=3, color=color.gold)


play_button = Button(icon='data/play', scale=.15,
                     position=(0, 0.10), on_click=Play)

quit_button = Button(icon='data/quit',
                     scale=.1, position=(0, -0.10), on_click=application.quit)

click_sound = Audio('data/click.mp3', autoplay=False)

quit_button.click_s = True
play_button.click_s = True

try:
    with open('data/meta.akl', 'rb') as f:
        high_score = pickle.loads(f.read())
except Exception as error:
    print("ERROROROROROOR:", error)
    high_score = 0
    quit()

high_score_text = Text(text=f"High Score: {str(high_score)}", origin=(
    00, 0.50), position=(0.0, -0.35), scale=2, font='data/font.ttf', color=color.black)


def click(button):
    if button.hovered and not button.click_s:
        click_sound.play()
        button.click_s = True
    if not button.hovered:
        button.click_s = False


def update():
    if play_button.hovered:
        play_button.scale = .2
    else:
        play_button.scale = .15

    if quit_button.hovered:
        quit_button.scale = .15
    else:
        quit_button.scale = .1

    click(play_button)
    click(quit_button)

    if held_keys['escape']:
        application.quit()


EditorCamera()
app.run()
