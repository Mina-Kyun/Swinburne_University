import pygame
import time

# Play a selected track
def play_track(state, index, album):
    try:
        track = album.tracks[index]
        song_path = track.location

        # load and play music
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

        # update state
        state.current_song = track.name
        state.current_index = index
        state.song_start_time = time.time()
        state.is_playing = True

        # get song length
        state.song_length = pygame.mixer.Sound(song_path).get_length()

        print("Playing:", song_path)

    except Exception as e:
        print("Error:", e)

# Toggle play / pause
def toggle_pause(state):
    if state.is_playing:
        pygame.mixer.music.pause()
        state.is_playing = False
        state.pause_time = time.time()
    else:
        pygame.mixer.music.unpause()
        state.is_playing = True

        # adjust start time so progress bar stays correct
        state.song_start_time += time.time() - state.pause_time

# Update player (repeat logic)
def update_player(state):
    if state.repeat and state.is_playing:
        elapsed = time.time() - state.song_start_time

        if elapsed >= state.song_length:
            pygame.mixer.music.play()
            state.song_start_time = time.time()