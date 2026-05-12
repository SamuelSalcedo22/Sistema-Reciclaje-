"""
views/
Ventanas o pantallas completas del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from components.navbar import AppNavbar


class CollectionView(ctk.CTkFrame):
    """Recolecciones: solicitudes pendientes (placeholder)."""

    def __init__(self, master: ctk.CTkFrame, controller) -> None:
        super().__init__(master, fg_color="transparent")
        self._controller = controller
        AppNavbar(
            self,
            "Recolecciones",
            "Gestión de solicitudes pendientes y programación.",
        ).pack(fill="x", pady=(0, 16))
        ctk.CTkLabel(
            self,
            text="Lista de solicitudes y estados. Aprobar/cancelar vía MainController.approve_collection_placeholder().",
            wraplength=480,
            justify="left",
            text_color=("#bdc3c7", "#bdc3c7"),
        ).pack(anchor="w")
        ctk.CTkButton(
            self,
            text="Procesar solicitud (stub)",
            fg_color="#27ae60",
            hover_color="#219a52",
            command=self._controller.approve_collection_placeholder,
        ).pack(anchor="w", pady=12)
