"""Main application module."""
import pygame
from controller.main_controller import MainController

def main() -> "None":
    """Main function containing application launch logic."""

    pygame.init()
    running: "bool" = True
    dt: "int" = 0
    clock: "pygame.time.Clock" = pygame.time.Clock()

    controller: "MainController" = MainController()

    pygame.display.set_mode()

    while running:
        _ = pygame.event.get()
        pressed_keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

        running = controller.update(pressed_keys, dt)
        controller.render_world()
        dt = clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
