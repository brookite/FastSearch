import threading
import time
import pytesseract
import sys
import webbrowser
import urllib.parse

from PIL import ImageGrab
import pyclip

SEARCH_URL = "https://yandex.ru/search/?lr=38&text={}"


class ClipboardImageListener(threading.Thread):
    def __init__(self, handler, *args, **kwargs):
        super().__init__(target=self.loop)
        self._handler = handler
        self._args = args
        self._kwargs = kwargs
        self._tmp = ImageGrab.grabclipboard()

    @property
    def handler(self):
        return self._handler

    @handler.setter
    def handler(self, value):
        if callable(value):
            self._handler = value

    def loop(self):
        while True:
            try:
                time.sleep(1)
                img = ImageGrab.grabclipboard()
            except OSError:
                time.sleep(0.5)
                continue
            if img != self._tmp and img is not None:
                self._tmp = img
                self._handler(img, *self._args, **self._kwargs)


def handler(img, only_copy=False):
    text = pytesseract.image_to_string(img, lang='rus+eng').strip()
    safe_string = urllib.parse.quote_plus(text)
    if not only_copy:
        url = SEARCH_URL.format(safe_string)
        webbrowser.open(url)
    else:
        pyclip.copy(text)
    print(f"Got new text from sceenshot from clipboard: {repr(text)}")


if __name__ == '__main__':
    only_copy = "--only-copy" in sys.argv
    listener = ClipboardImageListener(handler, only_copy=only_copy)
    print("Ready for new screenshots")
    try:
        listener.loop()
    except KeyboardInterrupt:
        print("Finishing listening")
