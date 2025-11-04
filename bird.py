from pico2d import load_image

#새의 크기 : 60x60
#새의 속도 : 시속 100km
#새 프레임 개수 : 14(5x3)

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 100.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    def __init__(self):
        self.x, self.y = 0, 400
        self.image = load_image('bird_animation.png')
        self.frame = 0
    def enter(self):
        pass
    def exit(self):
        pass
    def do(self):
        pass
    def draw(self):
        pass
