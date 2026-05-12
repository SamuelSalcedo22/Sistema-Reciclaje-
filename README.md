# EcoGestor — Sistema de Gestión de Reciclaje Comunitario

> Proyecto académico desarrollado en Python para la gestión organizada de actividades de reciclaje en comunidades, conjuntos residenciales e instituciones educativas.

---

## Tabla de contenidos

1. [Descripción general](#descripción-general)
2. [Planteamiento del problema](#planteamiento-del-problema)
3. [Solución propuesta](#solución-propuesta)
4. [Objetivos](#objetivos)
5. [Alcance del proyecto](#alcance-del-proyecto)
6. [Tecnologías utilizadas](#tecnologías-utilizadas)
7. [Estructura del proyecto](#estructura-del-proyecto)
8. [Instalación y ejecución](#instalación-y-ejecución)
9. [Funcionalidades principales](#funcionalidades-principales)
10. [Equipo de desarrollo](#equipo-de-desarrollo)
11. [Estado del proyecto](#estado-del-proyecto)

---

## Descripción general

**EcoGestor** es una aplicación de escritorio desarrollada completamente en **Python**, orientada a comunidades o instituciones que deseen digitalizar y organizar sus procesos de reciclaje. El sistema permite registrar usuarios, clasificar materiales, gestionar entregas, acumular puntos por participación y generar reportes de impacto ambiental.

---

## Planteamiento del problema

En muchas comunidades existen iniciativas de reciclaje que se gestionan de forma manual e informal: cuadernos, hojas de cálculo o mensajes de texto. Esta falta de organización genera:

- Pérdida de información sobre participantes y entregas.
- Dificultad para conocer los materiales recolectados con mayor frecuencia.
- Imposibilidad de registrar puntos o beneficios de manera confiable.
- Ausencia de datos para tomar decisiones o evidenciar resultados.
- Complejidad para priorizar solicitudes de recolección y asignar rutas.

---

## 💡 Solución propuesta

EcoGestor centraliza y digitaliza el proceso de reciclaje comunitario mediante una aplicación local con **frontend y backend en Python dentro de un mismo repositorio**.

- El **backend** maneja la lógica del negocio, validaciones, estructuras de datos y persistencia local.
- El **frontend** ofrece una interfaz gráfica sencilla, clara y en español para que administradores y participantes interactúen con el sistema.

---

## Objetivos

### Objetivo general

Desarrollar un sistema de gestión de reciclaje comunitario utilizando únicamente Python, aplicando programación orientada a objetos, estructuras de datos y una arquitectura organizada con frontend y backend.

### Objetivos específicos

- Registrar usuarios participantes dentro del sistema.
- Gestionar materiales reciclables: plástico, cartón, vidrio, papel y metal.
- Registrar entregas de residuos realizadas por los usuarios.
- Calcular puntos según el tipo y la cantidad de material entregado.
- Administrar y organizar solicitudes de recolección de residuos.
- Generar reportes básicos sobre participación y materiales reciclados.
- Diseñar una interfaz gráfica en Python para facilitar el uso del sistema.
- Mantener separación clara entre lógica de negocio, interfaz y gestión de datos.

---

## Alcance del proyecto

### Incluye

- Registro de usuarios.
- Registro de materiales reciclables.
- Registro de entregas de reciclaje.
- Cálculo automático de puntos.
- Gestión de solicitudes de recolección.
- Visualización de reportes básicos.
- Interfaz gráfica en Python.
- Backend en Python con organización modular.

### No incluye (primera versión)

- Aplicación móvil.
- Autenticación avanzada con roles complejos.
- Integración con mapas reales.
- Conexión con servicios externos o APIs.
- Pasarela de pagos.
- Despliegue en la nube.
- Inteligencia artificial.

---

## Tecnologías utilizadas

### Backend
| Elemento | Descripción |
|---|---|
| Python 3.x | Lenguaje principal |
| Arquitectura modular | Separación en capas (servicios, repositorios, modelos) |
| POO | Programación orientada a objetos |
| JSON / CSV / SQLite | Persistencia local de datos |

### Frontend
| Elemento | Descripción |
|---|---|
| Python 3.x | Lenguaje principal |
| Tkinter / CustomTkinter / PySide6 | Interfaz gráfica de usuario |

---

## Estructura del proyecto


---

## ✨ Funcionalidades principales

| Módulo | Funcionalidad |
|---|---|
| 👤 Usuarios | Registrar, listar y gestionar participantes |
| ♻️ Materiales | Administrar tipos de materiales reciclables |
| 📦 Entregas | Registrar entregas y calcular puntos automáticamente |
| 🚛 Solicitudes | Crear y priorizar solicitudes de recolección |
| 📊 Reportes | Visualizar estadísticas de participación e impacto ambiental |

---


| Módulo | Estado |
|---|---|
| Modelos de datos | 🔲 Pendiente |
| Repositorios | 🔲 Pendiente |
| Servicios de negocio | 🔲 Pendiente |
| Interfaz gráfica | 🔲 Pendiente |
| Reportes | 🔲 Pendiente |
| Pruebas | 🔲 Pendiente |

---
### Requerimientos Funcionales

| ID | Funcionalidad | Descripción |
| :--- | :--- | :--- |
| **RF-01** | Gestión de Usuarios | El sistema debe permitir registrar, consultar, actualizar y dar de baja a los participantes de la comunidad (nombre, documento de identidad, dirección/apartamento). |
| **RF-02** | Gestión de Materiales | El sistema debe permitir registrar los tipos de materiales aceptados (plástico, cartón, vidrio, etc.) y asignarles un factor de conversión o valor en puntos por kilogramo/unidad. |
| **RF-03** | Registro de Entregas | El sistema debe permitir registrar cada vez que un usuario entrega material reciclable, capturando la fecha, el tipo de material, la cantidad y asociándolo al usuario correspondiente. |
| **RF-04** | Cálculo de Puntos | El sistema debe calcular automáticamente los puntos generados en cada entrega y sumarlos al saldo total del usuario. |
| **RF-05** | Gestión de Solicitudes | El sistema debe permitir a los usuarios registrar solicitudes de recolección a domicilio, y a los administradores visualizar, aceptar y marcar estas solicitudes como "completadas" o "canceladas". |
| **RF-06** | Generación de Reportes | El sistema debe generar reportes que muestren métricas como el total reciclado, el top de usuarios con más puntos y el historial de entregas. |

---

### Requerimientos No Funcionales

| ID | Atributo | Descripción |
| :--- | :--- | :--- |
| **RNF-01** | Interfaz de Usuario | La aplicación debe contar con una interfaz gráfica de escritorio (GUI) desarrollada en PySide6, asegurando una experiencia visual moderna e interactiva. |
| **RNF-02** | Arquitectura del Sistema | El código debe estar organizado bajo un patrón de diseño que separe responsabilidades (ej. Capas o MVC), utilizando objetos de transferencia de datos (DTOs). |
| **RNF-03** | Persistencia de Datos | Almacenamiento local mediante bases de datos embebidas (SQLite) o archivos estructurados (JSON/CSV) para garantizar la permanencia de los datos. |
| **RNF-04** | Usabilidad y Lenguaje | Interfaz gráfica completamente en idioma español, con un diseño intuitivo para minimizar la curva de aprendizaje. |
| **RNF-05** | Rendimiento | El sistema debe ser capaz de procesar y recuperar la información en tiempo real, operando eficientemente con las estructuras de datos en memoria. |

---

### Estructuras de Datos Aplicadas

| Estructura de Datos | Aplicación en el Caso de Estudio | Justificación (Lógica) |
| :--- | :--- | :--- |
| **Arreglos (Arrays)** | Catálogo de materiales reciclables. | Almacenamiento de datos estáticos y de acceso rápido por índice. |
| **Pilas (Stacks)** | Función de "Deshacer última acción". | Implementa **LIFO** (*Last In, First Out*) para revertir el último registro en caso de error. |
| **Colas (Queues)** | Solicitudes de recolección. | Implementa **FIFO** (*First In, First Out*) para atender los pedidos en orden de llegada. |
| **Listas Simples** | Directorio de usuarios registrados. | Estructura dinámica que permite insertar y recorrer todos los participantes sin un tamaño fijo. |
| **Listas Dobles** | Historial de entregas por usuario. | Permite la navegación bidireccional para consultar registros anteriores y posteriores fácilmente. |
| **Listas Circulares Dobles** | Carrusel de estadísticas en Dashboard. | Permite una navegación infinita en la interfaz gráfica para mostrar reportes y rankings. |

> *EcoGestor — Transformando el reciclaje comunitario en un proceso digital, ordenado y medible.* 🌱
