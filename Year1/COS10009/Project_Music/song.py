import pygame
import sys
import data_files
from controls.app_state import AppState
from controls.ui_controls import handle_mouse_click
from controls.player_logic import toggle_pause, update_player, play_track
from screens.albums_library import draw
from screens.albums_detail import draw_album_detail


# Constants
WIN_WIDTH = 900
WIN_HEIGHT = 600

TOP_COLOR = (30, 177, 250)
BOTTOM_COLOR = (29, 77, 181)

# Initialization
def init():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Music Player")

    track_font = pygame.font.SysFont(None, 24)
    title_font = pygame.font.SysFont(None, 32, bold=True)

    return screen, track_font, title_font

# Put your record definitions here

# Load albums and tracks
def load_albums():
    # Put in your code here to load albums and tracks
    albums = data_files.read_file()
    return albums

# Update
def update(state):
    if state.dragging_volume:
        mouse_x = pygame.mouse.get_pos()[0]
        state.volume = (mouse_x - 730) / 150
        state.volume = max(0, min(1, state.volume))
        pygame.mixer.music.set_volume(state.volume)

def main():
    state = AppState()

    screen, track_font, title_font = init()
    clock = pygame.time.Clock()

    albums = load_albums()

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    handle_mouse_click(state, albums)

                    # start dragging volume
                    if 720 <= pygame.mouse.get_pos()[0] <= 890 and 560 <= pygame.mouse.get_pos()[1] <= 590:
                        state.dragging_volume = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    state.dragging_volume = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state.current_screen = "library"
                    state.selected_album = None
                    state.selected_tracks = []

                if event.key == pygame.K_SPACE:
                    toggle_pause(state)

        # update logic  
        update(state)
        update_player(state)

        # draw
        if state.current_screen == "library":
            draw(screen, albums, state, track_font, title_font)

        elif state.current_screen == "detail":
            draw_album_detail(screen, state, track_font, title_font, albums)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()