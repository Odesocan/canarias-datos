# -*- coding: utf-8 -*-
"""
Prepara los CSV (global + gen) que alimentan la visualización D3 de Empleo.

Consolida el dataset modelado (3_modelado/ced_empleo) en un eje ANUAL homogéneo
(media anual para los indicadores trimestrales; valor anual para los anuales),
con dos banderas de origen según la cadencia de cada indicador:
  · origen_q  → indicadores trimestrales (EPA/ETCL): real ≤2025, proyección 2026
  · origen_a  → indicadores anuales (EAES/alquiler): real ≤2024, proyección 2025-26

Salida (mismo directorio): ced_empleo_global.csv y ced_empleo_gen.csv
(separador ';', decimales '.', como el resto de secciones de Canarias en Datos).

Uso:  python preparar_datos_viz.py
"""
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
SRC = BASE.parent / "3_modelado" / "ced_empleo.parquet"
OUT = BASE

METRICA = {
    1:  ("tasa_paro", "q"),          2:  ("tasa_actividad", "q"),
    3:  ("tasa_empleo", "q"),        4:  ("horas_servicios", "q"),
    6:  ("paro_juvenil", "q"),       7:  ("paro_larga_duracion", "q"),
    8:  ("temporalidad", "q"),       9:  ("parcialidad", "q"),
    10: ("brecha_salarial", "a"),    11: ("pct_alquiler_salario", "a"),
}
GENDERED = {1, 2, 3, 6, 7, 8, 9, 11}
GENERO_GLOBAL_NO_GEN = "Total"
# indicadores de cadencia anual (EAES/alquiler): llevan su propio '<metrica>_origen'
ANUAL = ["brecha_salarial", "pct_alquiler_salario"]


def main() -> None:
    df = pd.read_parquet(SRC)
    df = df[df["territorio"] != "Total Nacional"].copy()  # el mapa/media se calculan sobre CCAA

    anual = (df.groupby(["indicador_id", "territorio", "territorio_cod", "genero", "anyo"])
               .agg(valor=("valor", "mean"),
                    proy=("origen", lambda s: (s == "proyeccion").any()))
               .reset_index())
    anual["valor"] = anual["valor"].round(3)

    origen = {}
    for cad in ("q", "a"):
        ids = [i for i, (_, c) in METRICA.items() if c == cad]
        g = (anual[anual["indicador_id"].isin(ids)]
             .groupby(["territorio", "anyo"])["proy"].any().reset_index())
        g["o"] = g["proy"].map(lambda x: "proyeccion" if x else "real")
        origen[cad] = g.set_index(["territorio", "anyo"])["o"]

    def pivota(sexos_ok, generos=None):
        filas = {}
        for _, r in anual.iterrows():
            clave, _ = METRICA[r["indicador_id"]]
            if r["genero"] not in sexos_ok(r["indicador_id"]):
                continue
            gen = None
            if generos is not None:
                gen = {"Hombres": "hombre", "Mujeres": "mujer"}.get(r["genero"])
                if gen not in generos:
                    continue
            key = (r["territorio"], r["territorio_cod"], int(r["anyo"]), gen)
            filas.setdefault(key, {})[clave] = r["valor"]
        rows = []
        for (terr, cod, anyo, gen), vals in filas.items():
            oq = origen["q"].get((terr, anyo), "real")   # cadencia trimestral (EPA/ETCL)
            oa = origen["a"].get((terr, anyo), "real")   # cadencia anual (EAES/alquiler)
            # Modelo del motor unificado: 'origen' general (cadencia trimestral,
            # la mayoritaria) + '<metrica>_origen' para las anuales (brecha, alquiler).
            row = {"ccaa": terr, "ccaa_cod": cod, "periodo": anyo, "origen": oq}
            if gen is not None:
                row["genero"] = gen
            row.update(vals)
            for k in ANUAL:
                if k in vals:
                    row[f"{k}_origen"] = oa
            rows.append(row)
        return pd.DataFrame(rows).sort_values(["ccaa", "periodo"]).reset_index(drop=True)

    col_ind = [c for _, (c, _) in sorted(METRICA.items())]
    glob = pivota(lambda iid: {"Ambos géneros"} if iid in GENDERED else {GENERO_GLOBAL_NO_GEN})
    gen = pivota(lambda iid: {"Hombres", "Mujeres"} if iid in GENDERED else set(),
                 generos={"hombre", "mujer"})

    def ordena(df, base):
        ind = [c for c in col_ind if c in df.columns]
        ori = [f"{k}_origen" for k in ANUAL if f"{k}_origen" in df.columns]
        return df[base + ["origen"] + ind + ori]
    glob = ordena(glob, ["ccaa", "ccaa_cod", "periodo"])
    gen = ordena(gen, ["ccaa", "ccaa_cod", "periodo", "genero"])

    glob.to_csv(OUT / "ced_empleo_global.csv", sep=";", index=False, encoding="utf-8")
    gen.to_csv(OUT / "ced_empleo_gen.csv", sep=";", index=False, encoding="utf-8")
    print(f"✓ ced_empleo_global.csv: {glob.shape[0]} filas · {glob['ccaa'].nunique()} CCAA · "
          f"{glob['periodo'].min()}–{glob['periodo'].max()}")
    print(f"✓ ced_empleo_gen.csv:    {gen.shape[0]} filas · géneros {list(gen['genero'].unique())}")


if __name__ == "__main__":
    main()
