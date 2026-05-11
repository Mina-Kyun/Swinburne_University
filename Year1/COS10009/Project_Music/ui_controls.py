import time
import pygame
from controls.player_logic import play_track, toggle_pause

# Helper: Check click area
def area_clicked(leftX, topY, rightX, bottomY):
    x, y = pygame.mouse.get_pos()
    return leftX <= x <= rightX and topY <= y <= bottomY

# Handle album click (Library)
def handle_album_click(state, albums):
    if state.current_screen != "library":
        return

    x_start = 20
    y_start = 90
    x, y = x_start, y_start
    max_per_row = 5
    count = 0

    for album in albums:
        if area_clicked(x, y, x + 150, y + 150):
            state.selected_album = album
            state.selected_tracks = album.tracks
            state.current_screen = "detail"
            return

        count += 1
        x += 180
        if count % max_per_row == 0:
            x = x_start
            y += 220

# Handle track click (Detail)
def handle_track_click(state):
    if state.current_screen != "detail":
        return

    track_y = 150
    for i, track in enumerate(state.selected_tracks):
        if area_clicked(350, track_y, 680, track_y + 30):
            play_track(state, i, state.selected_album)
        track_y += 40

# Handle BACK button
def handle_back_button(state):
    if state.current_screen == "detail":
        if area_clicked(50, 30, 150, 60):
            state.current_screen = "library"
            state.selected_album = None
            state.selected_tracks = []

# Handle playback controls
def handle_playback_controls(state):
    
    # PREVIOUS
    if area_clicked(345, 525, 395, 575):
        state.current_index -= 1
        if state.current_index < 0:
            state.current_index = len(state.selected_tracks) - 1
        play_track(state, state.current_index, state.selected_album)

    # PLAY / PAUSE
    if area_clicked(425, 525, 475, 575):
        toggle_pause(state)

    # NEXT
    if area_clicked(505, 525, 555, 575):
        state.current_index += 1
        if state.current_index >= len(state.selected_tracks):
            state.current_index = 0
        play_track(state, state.current_index, state.selected_album)

# Handle repeat toggle
def handle_repeat(state):
    if area_clicked(265, 535, 315, 585):
        state.repeat = not state.repeat
        print("Repeat:", state.repeat)

# Handle seek bar
def handle_seek(state):
    if area_clicked(200, 510, 700, 530):
        mouse_x = pygame.mouse.get_pos()[0]
        percent = (mouse_x - 200) / 500
        percent = max(0, min(1, percent))

        new_time = percent * state.song_length
        pygame.mixer.music.play(start=new_time)

        state.song_start_time = time.time() - new_time

# Main click handler (CLEAN)
def handle_mouse_click(state, albums):
    now = time.time()

    # chống double click
    if now - state.last_click_time < 0.1:
        return
    state.last_click_time = now

    handle_album_click(state, albums)
    handle_track_click(state)
    handle_back_button(state)
    handle_playback_controls(state)
    handle_seek(state)
    handle_repeat(state)