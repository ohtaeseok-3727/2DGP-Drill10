from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0/0.03)
GRAVITY = 9.8

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, Throwin_speed = 15, Throwin_angle = 45):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.xv = Throwin_speed * math.cos(math.radians(Throwin_angle))
        self.yv = abs(Throwin_speed * math.sin(math.radians(Throwin_angle)))

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.yv -= GRAVITY*game_framework.frame_time

        self.x += self.xv * PIXEL_PER_METER * game_framework.frame_time
        self.y += self.yv * PIXEL_PER_METER * game_framework.frame_time

        if self.y<60:
            game_world.remove_object(self)

