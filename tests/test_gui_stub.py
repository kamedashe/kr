# Тест чорного ящика через tkinter не виконується тут,
# але драйвер показує, що вікно SupplyWindow створюється без помилок.
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest, tkinter as tk
from ui.supply_window import SupplyWindow

def test_supply_window_creation(monkeypatch):
    root = tk.Tk()
    # Перехоплюємо метод center_window, щоб не відкривалось GUI.
    monkeypatch.setattr(SupplyWindow, 'center_window', lambda self, w, h: None)
    win = tk.Toplevel(root)
    SupplyWindow(win)
    assert win.winfo_exists() == 1
    win.destroy()
    root.destroy()
