import pygame
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher(FileSystemEventHandler):
    def __init__(self):
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.running = True

    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'modified':
            # Handle file modification
            print("File modified:", event.src_path)
            #self.reload_window()

    def reload_window(self):
        # Reload Pygame window
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

if __name__ == '__main__':
    pygame.init()
    observer = Observer()
    observer.schedule(Watcher(), path='.')
    observer.start()

