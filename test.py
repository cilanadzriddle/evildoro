#!/usr/bin/env python3

from textual.app import App
from textual.widgets import Button, Footer, Header
import time
import argparse
import subprocess

class togore(App):
    def compose(self):
        """
        What widgets is this app composed of?
        """
        yield Button("Pause")

if __name__ == "__main__":
    app = togore()
    app.run()
