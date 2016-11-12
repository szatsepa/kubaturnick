# -*- coding: utf-8 -*-
from cx_Freeze import setup, Executable

setup(
    name = "Кубатурник",
    version = "0.1",
    description = "Kubaturnick",
    executables = [Executable(script = "kub.py", base = "Win32GUI")]
)
input("Press Enter")