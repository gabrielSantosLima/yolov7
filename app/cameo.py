import cv2
from app.managers import CaptureManager, WindowManager


class Cameo(object):
    def __init__(self, chess):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        self.chess = chess
        self._captureManager = CaptureManager(
            cv2.VideoCapture(1), self._windowManager, False)
        
        self._crop_coords = [None]*4
        self._crop_index = 0
        self._mouse_dragging = False

    def run(self, chess=None):
        self._windowManager.createWindow()
        self._windowManager.processMouseEvents(self.onMouseEvent)

        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            for coord in self._crop_coords:
                if coord is not None:
                    cv2.circle(frame, coord, 5, (0,0,255), -1)
            
            if frame is not None and chess is not None:
                frame = chess.run(frame)

            self._captureManager.exitFrame()
            self._windowManager.processKeyEvents()
           

    def onKeypress(self, keycode):
        """Handle a keypress.

        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit.

        """
        if keycode == 32: # space
            # self._captureManager.writeImage('screenshot.png')
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            frame = self.chess.run(frame)
            cv2.imwrite('out.png', frame)
            self._captureManager.exitFrame()
            # self._captureManager.startWritingVideo(
            #         'screencast.avi')
        elif keycode == ord('c') and not self._mouse_dragging:
            self._crop_coords = [None]*4
            self._crop_index = 0
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo(
                    'screencas.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._captureManager.close_can()
            self._windowManager.destroyWindow()

    def onMouseEvent(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE and self._mouse_dragging:
            self._crop_coords[self._crop_index] = (x,y)
        elif event == cv2.EVENT_LBUTTONDOWN:
            self._mouse_dragging = True
            self._crop_coords[self._crop_index] = (x,y)
        elif event == cv2.EVENT_LBUTTONUP:
            self._mouse_dragging = False
            print(f'Crop[{self._crop_index}] - ({x},{y})')
            self._crop_index = (self._crop_index + 1) % 4
