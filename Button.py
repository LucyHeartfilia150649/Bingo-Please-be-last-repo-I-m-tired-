from Start import pygame

class Button():
	def __init__(self, image,image_trans, pos, text_input, font, base_color, hovering_color,size):
		self.image = image
		self.image_trans = image_trans
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.size = size
		self.font = font
		self.text_input = text_input
		self.fontrender = self.font.render(self.text_input, True, hovering_color)
		self.img = pygame.transform.scale(self.image,(self.image.get_width()*self.size , self.image.get_height()*self.size))
		self.img_trans = pygame.transform.scale(self.image_trans,(self.image_trans.get_width()*self.size , self.image_trans.get_height()*self.size))
		self.variable = self.img
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.rect = self.img.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.sound = pygame.mixer.Sound('sounds/button mouse.mp3')
		

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.img, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.sound.play()
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
			self.img = self.img_trans
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
			self.img = self.variable