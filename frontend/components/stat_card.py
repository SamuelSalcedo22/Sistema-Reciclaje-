"""
components/
Elementos reutilizables (botones, tablas, formularios).
Tarjeta de métrica para resúmenes (impacto, puntos, etc.).
"""

from __future__ import annotations

import customtkinter as ctk


class StatCard(ctk.CTkFrame):
    """Tarjeta compacta con etiqueta y valor destacado."""

    def __init__(
        self,
        master: ctk.CTkFrame,
        label: str,
        value: str,
        *,
        accent: str = "#27ae60",
    ) -> None:
        super().__init__(
            master,
            corner_radius=12,
            fg_color=("#2b2b2b", "#252526"),
            border_width=1,
            border_color=("#3d3d3d", "#3d3d3d"),
        )
        self._accent = accent
        self._label = ctk.CTkLabel(
            self,
            text=label,
            font=ctk.CTkFont(size=12),
            text_color=("#95a5a6", "#bdc3c7"),
        )
        self._label.pack(anchor="w", padx=16, pady=(14, 4))
        self._value = ctk.CTkLabel(
            self,
            text=value,
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color=(accent, accent),
        )
        self._value.pack(anchor="w", padx=16, pady=(0, 14))

    def set_value(self, text: str) -> None:
        self._value.configure(text=text)
