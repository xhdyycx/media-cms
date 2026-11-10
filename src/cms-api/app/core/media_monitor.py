import os
import threading
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from app.core.env import novaEnv
from app.log import logger
from app.utils.singleton import Singleton

class MediaImgUpload:
    pass

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self._FileEventHandler__media_img_upload = MediaImgUpload()

    def _handle_media_file(self, event):
        _var_var_0, _var_var_1 = os.path.splitext(os.path.basename(event.src_path))
        if event.is_directory and _var_var_0 in novaEnv.MEDIA_IMG_NAMES:
            self._FileEventHandler__media_img_upload.add({
                'p': event.src_path,
                't': int(time.time())
            })

    def on_created(self, event):
        self._handle_media_file(event)

    def on_moved(self, event):
        self._handle_media_file(event)

class MediaImgMonitor(metaclass=Singleton):
    '''MediaImgMonitor'''

    def __init__(self):
        self.name = '媒体图片监控'
        self.observer = None
        self.watchdog_thread = None
        self.watchdog_running = False

    def start(self, path):
        if not path:
            return False
        if not os.path.exists(path):
            logger.info(f'监控路径不存在: {path}')
            return False
        if self.watchdog_running:
            logger.info(f'{self.name}已在运行...')
            return False
        try:
            self.observer = Observer()
            self.observer.schedule(FileEventHandler(), path, recursive=True)
            self.watchdog_thread = threading.Thread(target=self.observer.start)
            self.watchdog_thread.daemon = True
            self.watchdog_thread.start()
            self.watchdog_running = True
            logger.info(f'{self.name}-{path}-启动成功...')
            return True
        except Exception as e:
            logger.exception(e)
            return False

    def stop(self):
        if not self.watchdog_running:
            return True
        try:
            if self.observer:
                self.observer.stop()
                if self.watchdog_thread and self.watchdog_thread.is_alive():
                    time.sleep(0.5)
                    self.watchdog_thread.join()
            self.watchdog_thread = None
            self.watchdog_running = False
            logger.info(f'{self.name}停止成功...')
            return True
        except Exception as e:
            logger.exception(e)
            logger.error(f'{self.name}停止失败')
            return False
