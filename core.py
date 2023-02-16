import json
import os
import threading
from typing import Optional

from PIL import ImageQt
import pytesseract
import shutil
import webbrowser
import urllib.parse
import time

from PySide6.QtGui import QClipboard
from PySide6.QtWidgets import QApplication

from pyclip import copy as copy_to_clipboard

CLIPBOARD: Optional[QClipboard] = None


def get_clipboardimg():
    global CLIPBOARD
    if CLIPBOARD is None:
        CLIPBOARD = QApplication.clipboard()
    image = CLIPBOARD.image()
    if image:
        return ImageQt.fromqimage(image)
    else:
        return None


def find_tesseract():
    if os.path.exists("tesseract"):
        if os.path.isdir("tesseract"):
            for file in os.listdir("tesseract"):
                if file.lower().startswith("tesseract"):
                    filepath = os.path.join("tesseract", file)
                    if os.access(filepath, os.X_OK):
                        print("Found local binary of tesseract library")
                        return filepath
    return shutil.which("tesseract")


class JSONSettings(dict):
    def __init__(self, filename):
        self._filename = filename
        if os.path.exists(self._filename):
            self.load()
        else:
            super().__init__({
                "langs": [],
                "engine": 0,
                "copy": True,
                "webSearch": False
            })
            self.save()

    def save(self):
        with open(self._filename, "w", encoding="utf-8") as fobj:
            json.dump(self, fobj, ensure_ascii=False)

    def load(self):
        with open(self._filename, "r", encoding="utf-8") as fobj:
            super().__init__(json.load(fobj))


class ClipboardImageListener(threading.Thread):
    def __init__(self, handler):
        super().__init__(target=self.loop)
        self._handler = handler
        self.__alive = True
        self._tmpimg = get_clipboardimg()

    def destroy(self):
        self.__alive = False

    def loop(self) -> None:
        while self.__alive:
            try:
                time.sleep(1)
                img = get_clipboardimg()
            except OSError:
                time.sleep(0.5)
                continue
            if img != self._tmpimg and img is not None:
                self._tmpimg = img
                self._handler(img)

    @property
    def handler(self):
        return self._handler

    @handler.setter
    def handler(self, value):
        if callable(value):
            self._handler = value


class TesseractEngine:
    WEBENGINE_TEMPLATES = [
        "https://yandex.ru/search/?lr=38&text={}",
        "https://www.google.com/search?q={}"
    ]

    def __init__(self, path: str):
        self._tesseract_path = path
        self._langs = list(sorted(pytesseract.get_languages()))
        self.selected_langs = []
        self.records = []
        pytesseract.pytesseract.tesseract_cmd = path

    @property
    def langs(self):
        return tuple(self._langs)

    def img2tesseract(self, img,
                      web_search=False, clipboard_copy=True, store=True, webengine_index=0):
        text = pytesseract.image_to_string(img, lang="+".join(self.selected_langs)).strip()
        if web_search:
            safe_string = urllib.parse.quote_plus(text)
            url = self.WEBENGINE_TEMPLATES[webengine_index].format(safe_string)
            webbrowser.open(url)
        if clipboard_copy:
            copy_to_clipboard(text)
        if store:
            self.records.append(text)
        print(f"Copied text: {text}")
        return text

