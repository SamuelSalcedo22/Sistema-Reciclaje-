"""
components/
Elementos reutilizables (botones, tablas, formularios).
Barra superior opcional con título y subtítulo de la sección actual.
"""

from __future__ import annotations

import customtkinter as ctk


class AppNavbar(ctk.CTkFrame):
    """Barra superior ligera para título de pantalla."""

    def __init__(self, master: ctk.CTkFrame, title: str, subtitle: str = "") -> None:
        super().__init__(master, fg_color="transparent")
        self._title = ctk.CTkLabel(
            self,
            text=title,
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=("#ecf0f1", "#ecf0f1"),
        )
        self._title.pack(anchor="w", padx=4, pady=(0, 2))
        if subtitle:
            self._subtitle = ctk.CTkLabel(
                self,
                text=subtitle,
                font=ctk.CTkFont(size=13),
                text_color=("#95a5a6", "#bdc3c7"),
            )
            self._subtitle.pack(anchor="w", padx=4)

    def set_title(self, title: str, subtitle: str = "") -> None:
        self._title.configure(text=title)
        if hasattr(self, "_subtitle"):
            self._subtitle.configure(text=subtitle)
        elif subtitle:
            self._subtitle = ctk.CTkLabel(
                self,
                text=subtitle,
                font=ctk.CTkFont(size=13),
                text_color=("#95a5a6", "#bdc3c7"),
            )
            self._subtitle.pack(anchor="w", padx=4)
