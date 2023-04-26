import pygame
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.game import Game

def main():
    game = Game()
    observer = Observer()

    class Watcher(FileSystemEventHandler):
        def on_any_event(self, event):
            if event.is_directory:
                return
            elif event.event_type == 'modified':
                print("File modified:", event.src_path)
                #self.reload_window()

        def reload_window(self):
            nonlocal game
            new_game = Game()
            new_game.run()

            game = new_game

    observer.schedule(Watcher(), path='.', recursive=True)
    observer.start()

    try:
        game.run()
        time.sleep(1)  # add a delay here to allow Pygame to fully initialize

        while True:
            pygame.time.wait(100)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == '__main__':
    main()
