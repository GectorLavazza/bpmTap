from pygame.font import SysFont


class Text:
    def __init__(self, screen, font_size, color='white',
                 pos=(0, 0), center_align=False, right_align=False):
        self.screen = screen
        self.font = SysFont('verdana', font_size)

        self.pos = pos
        self.color = color
        self.center_align = center_align
        self.right_align = right_align

        self.render = self.font.render('', True, self.color)
        self.rect = self.render.get_rect()

        self.prev = ''

    def update(self, message):

        if message != self.prev:
            self.render = self.font.render(str(message), True, self.color)
            self.rect = self.render.get_rect()

            if self.center_align:
                self.rect.topleft = (self.pos[0] - self.render.get_width() // 2,
                                     self.pos[1] - self.render.get_height() // 2)
            elif self.right_align:
                self.rect.topleft = (self.pos[0] - self.render.get_width(),
                                     self.pos[1])
            else:
                self.rect.topleft = (self.pos[0],
                                     self.pos[1])

        self.screen.blit(self.render, self.rect.topleft)

        self.prev = message
