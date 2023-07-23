from tkinter import Tk


def get_window_size() -> tuple[int, int]:
    _ = Tk()
    _.withdraw()
    return _.winfo_screenwidth(), \
        _.winfo_screenheight()
