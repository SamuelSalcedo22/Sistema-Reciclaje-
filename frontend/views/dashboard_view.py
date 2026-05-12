"""
views/
Ventanas o pantallas completas del sistema.
Dashboard: resumen de impacto ambiental y puntos totales (versión simplificada).
"""

from __future__ import annotations

import random

import customtkinter as ctk

from components.navbar import AppNavbar
from components.stat_card import StatCard


class DashboardView(ctk.CTkFrame):
    """Layout del panel principal; los datos se refrescan vía controlador."""

    def __init__(self, master: ctk.CTkFrame, controller) -> None:
        super().__init__(master, fg_color="transparent")
        self._controller = controller

        AppNavbar(
            self,
            "Dashboard",
            "Resumen de impacto ambiental y puntos de la comunidad.",
        ).pack(fill="x", pady=(0, 16))

        cards = ctk.CTkFrame(self, fg_color="transparent")
        cards.pack(fill="x")
        cards.grid_columnconfigure((0, 1, 2), weight=1)

        self._card_co2 = StatCard(
            cards,
            "CO₂ evitado (kg, estimado)",
            "128.4",
            accent="#2ecc71",
        )
        self._card_co2.grid(row=0, column=0, padx=(0, 8), pady=4, sticky="ew")

        self._card_waste = StatCard(
            cards,
            "Residuos valorizados (kg)",
            "542",
            accent="#58d68d",
        )
        self._card_waste.grid(row=0, column=1, padx=8, pady=4, sticky="ew")

        self._card_points = StatCard(
            cards,
            "Puntos comunitarios",
            "3240",
            accent="#abebc6",
        )
        self._card_points.grid(row=0, column=2, padx=(8, 0), pady=4, sticky="ew")

        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.pack(fill="x", pady=(20, 0))
        ctk.CTkButton(
            actions,
            text="Actualizar datos",
            width=160,
            fg_color="#27ae60",
            hover_color="#219a52",
            command=self._controller.refresh_dashboard,
        ).pack(side="left")

        self._status = ctk.CTkLabel(
            actions,
            text="Listo.",
            text_color=("#7f8c8d", "#95a5a6"),
        )
        self._status.pack(side="left", padx=16)

        self._controller.set_dashboard_refresh_handler(self._simulate_data_refresh)

    def _simulate_data_refresh(self) -> None:
        """Simula llegada de datos del backend; solo demuestra el cableado al controlador."""
        jitter_co2 = 120 + random.random() * 25
        jitter_kg = 500 + int(random.random() * 80)
        jitter_pts = 3000 + int(random.random() * 400)
        self._card_co2.set_value(f"{jitter_co2:.1f}")
        self._card_waste.set_value(str(jitter_kg))
        self._card_points.set_value(str(jitter_pts))
        self._status.configure(text="Datos actualizados (simulación).")
