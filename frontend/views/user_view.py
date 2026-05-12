"""
views/
Ventanas o pantallas completas del sistema.
Solo layout y widgets; la lógica de acción delega al controlador.
"""

from __future__ import annotations

import customtkinter as ctk

from components.navbar import AppNavbar


class UserView(ctk.CTkFrame):
    """Gestión de Usuarios: registro y lista de participantes (placeholder)."""

    def __init__(self, master: ctk.CTkFrame, controller) -> None:
        super().__init__(master, fg_color="transparent")
        self._controller = controller
        AppNavbar(
            self,
            "Gestión de usuarios",
            "Registro y lista de participantes comunitarios.",
        ).pack(fill="x", pady=(0, 16))
        ctk.CTkLabel(
            self,
            text="Contenido de formulario y tabla: conectar con MainController.register_user_placeholder().",
            wraplength=480,
            justify="left",
            text_color=("#bdc3c7", "#bdc3c7"),
        ).pack(anchor="w")
        ctk.CTkButton(
            self,
            text="Acción de ejemplo (controlador)",
            fg_color="#27ae60",
            hover_color="#219a52",
            command=self._controller.register_user_placeholder,
        ).pack(anchor="w", pady=12)
