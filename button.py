import pygame

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

screen = pygame.display.set_mode((1280, 720))
buttons = pygame.sprite.Group()

class Button2(pygame.sprite.Sprite):
    ''' A button treated like a Sprite... and killed too '''

    def __init__(self, position, text, size,
                 colors="white on blue",
                 hover_colors="red on green",
                 style="button1",
                 borderc=(255, 255, 255),
                 command=lambda: print("No command activated for this button")):

        # the hover_colors attribute needs to be fixed
        super().__init__()
        global num

        self.text = text
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        # hover_colors
        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
        # styles can be button1 or button2 (more simple this one)
        self.style = style
        self.borderc = borderc  # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render(self.text)
        self.x, self.y, self.w, self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, 500, self.h)
        self.position = position
        self.pressed = 1
        # the groups with all the buttons
        buttons.add(self)

    def render(self, text):
        # we have a surface
        self.text_render = self.font.render(text, 1, self.fg)
        # memorize the surface in the image attributes
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == "button1":
            self.draw_button1()
        elif self.style == "button2":
            self.draw_button2()
        if self.command != None:
            self.hover()
            self.click()

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        lcolor = (150, 150, 150)
        lcolor2 = (50, 50, 50)
        pygame.draw.line(screen, lcolor, self.position,
                         (self.x + self.w, self.y), 5)
        pygame.draw.line(screen, lcolor, (self.x, self.y - 2),
                         (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, lcolor2, (self.x, self.y + self.h),
                         (self.x + self.w, self.y + self.h), 5)
        pygame.draw.line(screen, lcolor2, (self.x + self.w, self.y + self.h),
                         [self.x + self.w, self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, self.rect)

    def draw_button2(self):
        ''' a linear border '''
        # the width is set to 500 to have the same size not depending on the text size
        pygame.draw.rect(screen, self.bg, (self.x - 50, self.y, 500, self.h))
        pygame.gfxdraw.rectangle(
            screen, (self.x - 50, self.y, 500, self.h), self.borderc)

    def check_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors
            # pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''

        self.check_collision()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("The answer is:'" + self.text + "'")
                self.command()
                self.pressed = 0

            if pygame.mouse.get_pressed() == (0, 0, 0):
                self.pressed = 1

