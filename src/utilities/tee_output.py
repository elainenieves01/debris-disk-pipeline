"""
Lets a run's console output be shown on the terminal live, as normal, while
also accumulating it in memory so it can be embedded in a report afterward.
"""

import io
import sys


class _Tee:
    def __init__(self, *streams):
        self._streams = streams

    def write(self, data):
        for stream in self._streams:
            stream.write(data)
        return len(data)

    def flush(self):
        for stream in self._streams:
            stream.flush()


def start_capturing_stdout():
    """
    Redirect sys.stdout so everything printed from here on is both shown on
    the terminal as normal and accumulated in the returned buffer.

    Call stop_capturing_stdout() to restore normal stdout.
    """
    buffer = io.StringIO()
    sys.stdout = _Tee(sys.__stdout__, buffer)

    return buffer


def stop_capturing_stdout():
    """Restore sys.stdout to the real terminal stream."""
    sys.stdout = sys.__stdout__
