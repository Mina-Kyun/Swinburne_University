import pygame
import time

# COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)

# FORMAT TIME (seconds -> mm:ss)
def format_time(seconds):
    seconds = int(seconds)
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02}:{secs:02}"

# BACKGROUND
def draw_background(screen):
    # Fill entire screen with background color
    screen.fill((215, 125, 242))

# HEADER (top bar)
def draw_header(screen, title_font):
    pygame.draw.rect(screen, (30, 30, 60), (0, 0, 900, 60))
    screen.blit(title_font.render("Albums Library", True, WHITE), (20, 15))

# DRAW ALL ALBUMS (grid layout)
def draw_albums(screen, albums, track_font):
    x_start = 20
    y_start = 90
    x = x_start
    y = y_start

    max_per_row = 5   # number of albums per row
    count = 0

    for i, album in enumerate(albums):
        # load album image
        image = pygame.image.load(f"pic{i+1}.png")
        image = pygame.transform.scale(image, (150, 150))
        # draw image
        screen.blit(image, (x, y))
        # draw album name
        screen.blit(track_font.render(album.album_name, True, BLACK), (x, y+160))
        # move to next position
        count += 1
        x += 180
        # move to next row if needed
        if count % max_per_row == 0:
            x = x_start
            y += 220

# PROGRESS BAR (song timeline)
def draw_progress_bar(screen, song_start_time, is_playing, pause_time, song_length):
    # if no song -> do not draw
    if song_start_time == 0 or song_length == 0:
        return
    # calculate elapsed time
    if is_playing:
        elapsed = time.time() - song_start_time
    else:
        elapsed = pause_time - song_start_time
    # progress ratio (0 → 1)
    progress = min(elapsed / song_length, 1)
    # background bar
    pygame.draw.rect(screen, (100,100,100), (200, 515, 500, 8))
    # progress fill
    pygame.draw.rect(screen, (0,200,255), (200, 515, int(500 * progress), 8))
    # circle indicator
    pygame.draw.circle(screen, WHITE, (200 + int(500 * progress), 518), 5)
    # clamp elapsed time
    elapsed = min(elapsed, song_length)
    # draw time text
    font = pygame.font.SysFont(None, 24)
    screen.blit(font.render(format_time(elapsed), True, WHITE), (200, 530))
    screen.blit(font.render(format_time(song_length), True, WHITE), (650, 530))

# CONTROL PANEL (buttons + volume)
def draw_controls(screen, title_font, volume, track_font, repeat):

    # control bar background
    pygame.draw.rect(screen, (50,50,80), (0, 500, 900, 100))
    center_x = 450
    # button positions (prev, play, next, repeat)
    buttons = [
        ("|<<", center_x - 80),
        (">||", center_x),
        (">>|", center_x + 80),
        ("R", center_x - 160)
    ]
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #BUTTONS
    for text, x in buttons:
        y = 560
        # hover effect
        if x-25 <= mouse_x <= x+25 and y-25 <= mouse_y <= y+25:
            color = (100,200,255)
        else:
            color = WHITE
        # draw button
        pygame.draw.circle(screen, color, (x, y), 25)
        # draw label
        label = title_font.render(text, True, BLACK)
        screen.blit(label, (x-10, y-15))

    #REPEAT STATUS
    if repeat:
        text = "Repeat: ON"
        color = (0,255,0)
    else:
        text = "Repeat: OFF"
        color = WHITE
    screen.blit(track_font.render(text, True, color), (730, 530))

    #VOLUME BAR
    screen.blit(track_font.render("Volume", True, WHITE), (730, 550))
    # volume background
    pygame.draw.rect(screen, (100,100,100), (730, 570, 150, 10))
    # volume knob
    pygame.draw.circle(screen, WHITE, (730 + int(volume*150), 574), 6)

# MAIN DRAW FUNCTION (LIBRARY SCREEN)
def draw(screen, albums, state, track_font, title_font):

    # background + UI
    draw_background(screen)
    draw_header(screen, title_font)

    # controls + progress
    draw_controls(screen, title_font, state.volume, track_font, state.repeat)
    draw_progress_bar(screen, state.song_start_time, state.is_playing,
                      state.pause_time, state.song_length)

    # show albums if no album selected
    if not state.selected_album:
        draw_albums(screen, albums, track_font)

    # ===== NOW PLAYING TEXT =====
    if state.current_song:
        text = "Now Playing: " + state.current_song
    else:
        text = "No song playing"

    screen.blit(title_font.render(text, True, (255,255,0)), (20, 460))

    pygame.display.flip()

# DRAW SINGLE TRACK (helper)
def display_track(screen, title, xpos, ypos, track_font):
    screen.blit(track_font.render(title, True, BLACK), (xpos, ypos))