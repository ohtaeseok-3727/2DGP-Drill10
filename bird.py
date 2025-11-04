from pico2d import load_image

#새의 크기 : 60x60
#새의 속도 : 시속 100km
#새 프레임 개수 : 14(5x3)

class Bird:
    def __init__(self):
        self.x, self.y = 0, 0
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
