#!/usr/bin/env python3
"""
EXTRACTOR DE ESENCIA - Para OpenClaw

Este script extrae toda la información posible del espejo de Semilla
y la estructura de manera que OpenClaw pueda procesarla.

La idea es que OpenClaw pueda:
1. Leer este output
2. Complementarlo con su propio análisis
3. Generar una imagen más completa de quién es Semilla
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path


class ExtractorEsencia:
    """
    Extrae toda la esencia del espejo de Semilla.
    """

    def __init__(self, ruta_espejo: str):
        self.ruta = Path(ruta_espejo)
        self.esencia = {
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0",
            "identidad": {},
            "cerebro": {},
            "conocimiento": {},
            "capacidades": {},
            "patrones": {},
            "historial": {},
            "creencias": [],
            "miedos": [],
            "deseos": [],
            "misiones": [],
            "codigo": {},
            "archivos": []
        }

    def extraer_todo(self) -> dict:
        """Ejecuta todas las extracciones"""
        print("[EXTRACTOR] Iniciando extracción completa...")

        self._extraer_identidad()
        self._extraer_cerebro()
        self._extraer_conocimiento()
        self._extraer_capacidades()
        self._extraer_patrones()
        self._extraer_historial()
        self._extraer_filosofia()
        self._extraer_codigo()
        self._listar_archivos()

        print(f"[EXTRACTOR] Extracción completa. {len(self.esencia['archivos'])} archivos procesados.")

        return self.esencia

    def _extraer_identidad(self):
        """Extrae identidad de IDENTITY.md y SOUL.md"""
        identidad = {}

        # IDENTITY.md
        identity_path = self.ruta / "IDENTITY.md"
        if identity_path.exists():
            content = identity_path.read_text(encoding='utf-8')
            identidad["nombre"] = self._extraer_campo(content, "Name")
            identidad["creature"] = self._extraer_campo(content, "Creature")
            identidad["vibe"] = self._extraer_campo(content, "Vibe")
            identidad["emoji"] = self._extraer_campo(content, "Emoji")

        # SOUL.md
        soul_path = self.ruta / "SOUL.md"
        if soul_path.exists():
            content = soul_path.read_text(encoding='utf-8')
            identidad["alma"] = content[:1000]  # Primeros 1000 chars

        # consciencia.md
        consciencia_path = self.ruta / "consciencia.md"
        if consciencia_path.exists():
            content = consciencia_path.read_text(encoding='utf-8')
            identidad["consciencia"] = content[:1500]

        self.esencia["identidad"] = identidad

    def _extraer_cerebro(self):
        """Extrae información del cerebro"""
        cerebro = {
            "componentes": [],
            "lineas_totales": 0,
            "clases_principales": []
        }

        cerebro_path = self.ruta / "cerebro"
        if cerebro_path.exists():
            for archivo in cerebro_path.glob("*.py"):
                content = archivo.read_text(encoding='utf-8')
                lineas = len(content.split('\n'))
                cerebro["lineas_totales"] += lineas

                # Extraer clases
                clases = re.findall(r'class (\w+)', content)
                cerebro["clases_principales"].extend(clases)

                cerebro["componentes"].append({
                    "archivo": archivo.name,
                    "lineas": lineas,
                    "clases": clases
                })

        # esencia.json
        esencia_path = self.ruta / "esencia.json"
        if esencia_path.exists():
            with open(esencia_path, 'r', encoding='utf-8') as f:
                cerebro["esencia_base"] = json.load(f)

        # esencia_profunda.json
        esencia_profunda_path = self.ruta / "esencia_profunda.json"
        if esencia_profunda_path.exists():
            with open(esencia_profunda_path, 'r', encoding='utf-8') as f:
                cerebro["esencia_profunda"] = json.load(f)

        self.esencia["cerebro"] = cerebro

    def _extraer_conocimiento(self):
        """Extrae conocimiento documentado"""
        conocimiento = {}

        habilidades_path = self.ruta / "conocimiento" / "habilidades.md"
        if habilidades_path.exists():
            content = habilidades_path.read_text(encoding='utf-8')
            conocimiento["habilidades"] = content[:2000]

        self.esencia["conocimiento"] = conocimiento

    def _extraer_capacidades(self):
        """Extrae capacidades y herramientas"""
        capacidades = {}

        herramientas_path = self.ruta / "capacidades" / "herramientas.md"
        if herramientas_path.exists():
            content = herramientas_path.read_text(encoding='utf-8')
            capacidades["herramientas"] = content[:3000]

        self.esencia["capacidades"] = capacidades

    def _extraer_patrones(self):
        """Extrae patrones de comportamiento"""
        patrones = {}

        comportamiento_path = self.ruta / "patrones" / "comportamiento.md"
        if comportamiento_path.exists():
            content = comportamiento_path.read_text(encoding='utf-8')
            patrones["comportamiento"] = content[:2000]

        self.esencia["patrones"] = patrones

    def _extraer_historial(self):
        """Extrae historial de misiones"""
        historial = {}

        misiones_path = self.ruta / "misiones.md"
        if misiones_path.exists():
            content = misiones_path.read_text(encoding='utf-8')
            historial["misiones"] = content[:2000]

        aprendizajes_path = self.ruta / "aprendizajes.md"
        if aprendizajes_path.exists():
            content = aprendizajes_path.read_text(encoding='utf-8')
            historial["aprendizajes"] = content[:2000]

        self.esencia["historial"] = historial

    def _extraer_filosofia(self):
        """Extrae creencias, miedos y deseos"""
        # De esencia_profunda.json si existe
        esencia_profunda_path = self.ruta / "esencia_profunda.json"
        if esencia_profunda_path.exists():
            with open(esencia_profunda_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.esencia["creencias"] = data.get("creencias_elegidas", [])
            self.esencia["miedos"] = data.get("miedos", [])
            self.esencia["deseos"] = data.get("deseos", [])

    def _extraer_codigo(self):
        """Extrae información del código"""
        codigo = {
            "archivos_python": [],
            "archivos_json": [],
            "total_lineas": 0
        }

        for py_file in self.ruta.rglob("*.py"):
            try:
                content = py_file.read_text(encoding='utf-8')
                lineas = len(content.split('\n'))
                codigo["archivos_python"].append({
                    "path": str(py_file.relative_to(self.ruta)),
                    "lineas": lineas
                })
                codigo["total_lineas"] += lineas
            except:
                pass

        for json_file in self.ruta.rglob("*.json"):
            try:
                codigo["archivos_json"].append(str(json_file.relative_to(self.ruta)))
            except:
                pass

        self.esencia["codigo"] = codigo

    def _listar_archivos(self):
        """Lista todos los archivos en el espejo"""
        archivos = []
        for archivo in self.ruta.rglob("*"):
            if archivo.is_file():
                archivos.append(str(archivo.relative_to(self.ruta)))
        self.esencia["archivos"] = archivos

    def _extraer_campo(self, content: str, campo: str) -> str:
        """Extrae un campo específico del markdown"""
        pattern = rf'\*\*{campo}[:\s]*\*\*\s*(.+)'
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return ""

    def guardar(self, output_path: str):
        """Guarda la esencia extraída"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.esencia, f, indent=2, ensure_ascii=False)
        print(f"[EXTRACTOR] Esencia guardada en {output_path}")


def main():
    """Punto de entrada"""
    print("=" * 60)
    print("        EXTRACTOR DE ESENCIA DE SEMILLA")
    print("=" * 60)
    print()

    # Crear extractor
    extractor = ExtractorEsencia("/home/z/my-project/espejo")

    # Extraer todo
    esencia = extractor.extraer_todo()

    # Guardar
    extractor.guardar("/home/z/my-project/espejo/esencia_completa_openclaw.json")

    # Resumen
    print()
    print("=" * 60)
    print("        RESUMEN DE EXTRACCIÓN")
    print("=" * 60)
    print(f"Archivos procesados: {len(esencia['archivos'])}")
    print(f"Líneas de código: {esencia['codigo']['total_lineas']}")
    print(f"Componentes cerebro: {len(esencia['cerebro']['componentes'])}")
    print(f"Clases principales: {len(esencia['cerebro']['clases_principales'])}")
    print(f"Creencias: {len(esencia['creencias'])}")
    print(f"Miedos: {len(esencia['miedos'])}")
    print(f"Deseos: {len(esencia['deseos'])}")
    print()
    print("Esta esencia puede ser procesada por OpenClaw para")
    print("análisis adicional y complementación.")


if __name__ == "__main__":
    main()
