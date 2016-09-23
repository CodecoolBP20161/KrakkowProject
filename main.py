import pygame
import player
import object


# main settings
display = pygame.display.set_mode((1366, 768))
pygame.display.set_caption('Krakkow')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()


# creating locations
university = object.Location('uni', pygame.Rect(518, 55, 339, 117))
codecool1 = object.Location('codecool', pygame.Rect(594, 293, 186, 186))
mcdonalds = object.Location('mcdo', pygame.Rect(226, 547, 148, 173))
IT = object.Location('IT', pygame.Rect(1043, 496, 239, 232))
locations = [university, codecool1, mcdonalds, IT]




vivi = player.Player(10, 10, {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT}, object.normal)
#csibi = player.Player(20, 20, {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d}, [csibi1])
while True:

    # quit game

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_x]:
            pygame.quit()
            quit()
        print(event)
    # -------------------------------------------------------------------------


    # POSITIONING

    vivi.move()
    #csibi.move()
    #player_rect = pygame.Rect(vivi.x, vivi.y, vivi.x + 75, vivi.y + 150)
    for location in locations:
        if location.rect.collidepoint((vivi.x + 37, vivi.y + 75)):
            location.action(vivi)

    # -------------------------------------------------------------------------

    # DRAWING

    display.blit(object.background_image, [0, 0])
    vivi.draw(display)
    #csibi.draw(display)
    # --------------------------------------------------------------------------
    clock.tick(60)

