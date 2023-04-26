from watchdog.events import FileSystemEventHandler

class Watcher(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'modified':
            # Handle file modification
            print("File modified:", event.src_path)
