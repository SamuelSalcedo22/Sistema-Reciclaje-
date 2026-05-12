"""
views/
Ventanas o pantallas completas del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from components.navbar import AppNavbar


class MaterialView(ctk.CTkFrame):
    """Materiales: catálogo de residuos (placeholder)."""

    def __init__(self, master: ctk.CTkFrame, controller) -> None:
        super().__init__(master, fg_color="transparent")
        self._controller = controller
        AppNavbar(
            self,
            "Catálogo de materiales",
            "Plástico, vidrio, papel, orgánico, etc.",
        ).pack(fill="x", pady=(0, 16))
        ctk.CTkLabel(
            self,
            text="Aquí irá el catálogo editable. Las acciones deben usar MainController.save_material_placeholder().",
            wraplength=480,
            justify="left",
            text_color=("#bdc3c7", "#bdc3c7"),
        ).pack(anchor="w")
        ctk.CTkButton(
            self,
            text="Guardar catálogo (stub)",
            fg_color="#27ae60",
            hover_color="#219a52",
            command=self._controller.save_material_placeholder,
        ).pack(anchor="w", pady=12)
