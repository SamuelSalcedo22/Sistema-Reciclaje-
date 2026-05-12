"""
main.py
Inicialización de la ventana principal y ciclo de vida de la aplicación EcoGestor.
"""

from __future__ import annotations

import sys
from pathlib import Path

import customtkinter as ctk

# Raíz del frontend en sys.path para imports `views`, `components`, `controllers`
_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from controllers.main_controller import MainController  # noqa: E402
from views.collection_view import CollectionView  # noqa: E402
from views.dashboard_view import DashboardView  # noqa: E402
from views.material_view import MaterialView  # noqa: E402
from views.user_view import UserView  # noqa: E402


# Tema oscuro y paleta alineada con reciclaje (verdes, grises, texto claro)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class EcoGestorApp(ctk.CTk):
    """Ventana raíz: sidebar + área de vistas superpuestas."""

    def __init__(self) -> None:
        super().__init__()
        self.title("EcoGestor — Gestión de reciclaje comunitario")
        self.geometry("1000x640")
        self.minsize(880, 560)

        self._controller = MainController(self)
        self._views: dict[str, ctk.CTkFrame] = {}
        self._nav_buttons: dict[str, ctk.CTkButton] = {}

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._build_sidebar()
        self._build_content_area()

        self.show_view("dashboard")

    def _build_sidebar(self) -> None:
        """
        Menú lateral fijo: navegación entre pantallas sin cerrar la app.
        """
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color=("#1e1e1e", "#1e1e1e"))
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        brand = ctk.CTkLabel(
            sidebar,
            text="EcoGestor",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=("#ecf0f1", "#ecf0f1"),
        )
        brand.pack(pady=(24, 8), padx=20, anchor="w")

        tag = ctk.CTkLabel(
            sidebar,
            text="Reciclaje comunitario",
            font=ctk.CTkFont(size=12),
            text_color=("#27ae60", "#58d68d"),
        )
        tag.pack(padx=20, anchor="w", pady=(0, 24))

        for key, label in (
            ("dashboard", "Dashboard"),
            ("users", "Usuarios"),
            ("materials", "Materiales"),
            ("collections", "Recolecciones"),
        ):
            btn = ctk.CTkButton(
                sidebar,
                text=label,
                anchor="w",
                height=40,
                fg_color="transparent",
                text_color=("#ecf0f1", "#ecf0f1"),
                hover_color=("#2d5a3d", "#2d5a3d"),
                command=lambda k=key: self._controller.navigate_to(k),
            )
            btn.pack(fill="x", padx=12, pady=4)
            self._nav_buttons[key] = btn

    def _build_content_area(self) -> None:
        """Contenedor donde las vistas CTkFrame comparten la misma celda y se elevan con tkraise."""
        self._content = ctk.CTkFrame(self, corner_radius=0, fg_color=("#242424", "#242424"))
        self._content.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self._content.grid_rowconfigure(0, weight=1)
        self._content.grid_columnconfigure(0, weight=1)

        self._views["dashboard"] = DashboardView(self._content, self._controller)
        self._views["users"] = UserView(self._content, self._controller)
        self._views["materials"] = MaterialView(self._content, self._controller)
        self._views["collections"] = CollectionView(self._content, self._controller)

        for frame in self._views.values():
            frame.grid(row=0, column=0, sticky="nsew", padx=24, pady=24)

    def show_view(self, name: str) -> None:
        frame = self._views.get(name)
        if frame is None:
            return
        frame.tkraise()
        self._highlight_nav(name)

    def _highlight_nav(self, active: str) -> None:
        """Resalta visualmente la sección activa en el sidebar."""
        for key, btn in self._nav_buttons.items():
            if key == active:
                btn.configure(fg_color=("#27ae60", "#27ae60"), hover_color=("#219a52", "#219a52"))
            else:
                btn.configure(fg_color="transparent", hover_color=("#2d5a3d", "#2d5a3d"))


def main() -> None:
    app = EcoGestorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
