import pygame
from screens.albums_library import draw_controls, draw_progress_bar

# COLORS
BLACK = (0, 0, 0)

# DRAW ALBUM DETAIL SCREEN
def draw_album_detail(screen, state, track_font, title_font, albums):
    #BACKGROUND
    screen.fill((215, 125, 242))
    # get mouse position (for hover effect)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # if no album selected → stop drawing
    if not state.selected_album:
        return
    album = state.selected_album

    # BACK BUTTON
    pygame.draw.rect(screen, (238,108,169), (40, 15, 80, 50))
    back_text = title_font.render("Back", True, (255,0,119))
    screen.blit(back_text, (50, 30))

    # ALBUM INFO
    # album name
    screen.blit(title_font.render(album.album_name, True, BLACK), (50, 80))
    # album image
    image = pygame.image.load(f"pic{albums.index(album)+1}.png")
    image = pygame.transform.scale(image, (200, 200))
    screen.blit(image, (50, 120))
    # artist name
    screen.blit(track_font.render(f"Artist: {album.artist_name}", True, BLACK), (50, 340))
    # release year
    screen.blit(track_font.render(f"Year: {album.release_date}", True, BLACK), (50, 370))

    # TRACK LIST
    y = 150
    for track in state.selected_tracks:
        # hover effect
        if 350 <= mouse_x <= 680 and y <= mouse_y <= y + 30:
            color = (0, 100, 255)
        # highlight current playing song
        elif track.name == state.current_song:
            color = (255, 0, 0)
        else:
            color = BLACK
        screen.blit(track_font.render(track.name, True, color), (350, y))
        y += 40

    # NOW PLAYING TEXT
    if state.current_song:
        screen.blit(
            title_font.render("Now Playing: " + state.current_song, True, (255,255,0)),
            (20, 460)
        )

    # CONTROLS + PROGRESS BAR
    draw_controls(screen, title_font, state.volume, track_font, state.repeat)
    draw_progress_bar(
        screen,
        state.song_start_time,
        state.is_playing,
        state.pause_time,
        state.song_length
    )

    pygame.display.flip()