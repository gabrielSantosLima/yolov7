import cv2
from app.managers import CaptureManager, WindowManager


class Cameo(object):
    def __init__(self, chess):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        self.chess = chess
        self._captureManager = CaptureManager(
            cv2.VideoCapture(1), self._windowManager, True)

    def run(self, chess=None):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            if frame is not None and chess is not None:
                chess.run(frame)

            self._captureManager.exitFrame()
            self._windowManager.processEvents()
           

    def onKeypress(self, keycode):
        """Handle a keypress.

        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit.

        """
        if keycode == 32: # space
            # self._captureManager.writeImage('screenshot.png')
            # self._captureManager.startWritingVideo(
            #         'screencast.avi')
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            self.chess.run(frame)
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo(
                    'screencas.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._captureManager.close_can()
            self._windowManager.destroyWindow()
