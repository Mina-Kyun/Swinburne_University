class AppState:
    def __init__(self):
        # UI / Navigation
        self.current_screen = "library" # Which screen is currently displayed ("library" or "detail")
        self.selected_album = None # The album currently selected by the user
        self.selected_tracks = [] # List of tracks belonging to the selected album
        
        # Music Playback
        self.current_song = ""  # Name of the currently playing song        
        self.current_index = 0  # Index of the current song in the track list        
        self.is_playing = False  # True if music is playing, False if paused        
        self.repeat = False  # Repeat mode toggle (True = repeat current song)      

        # Timing
        self.song_start_time = 0  # Time when the song started playing (used for progress bar)       
        self.pause_time = 0  # Time when the song was paused        
        self.song_length = 0  # Duration of the current song (in seconds)
        
        # Audio Settings
        self.volume = 0.5  # Volume level (0.0 to 1.0)
        self.dragging_volume = False  # True when user is dragging the volume slider
    
        # Misc
        self.last_click_time = 0  # Used to prevent accidental double clicks
        
