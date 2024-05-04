import pygame 
pygame.init()

class Player():
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect()
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота
    
    def move(self):
        self.rect.x -= 1
        
    
    



window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Гра з персонажем")

# Колір фону
bg_color = (255, 255, 255)
player = Player(100, 100, 100, 100, 'bird.png')
player2 = Player(300, 100, 100, 100, 'bird.png')
# Головний цикл гри
clock = pygame.time.Clock()
game = True
while game:
    # Перевірка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    
    # Оновлення екрану
    window.fill(bg_color)
    window.blit(player.image, (player.rect.x, player.rect.y))  # Відображення зображення гравця
    window.blit(player2.image, (player2.rect.x, player2.rect.y))  # Відображення зображення гравця
    player2.move()
    
    # зіткнення персонажів
    if player.rect.colliderect(player2.rect):
        game = False
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()
