"""
Script para frontend de cálculo de préstamos
"""
from dataclasses import dataclass

import pandas as pd
import streamlit as st
from calculator import compound_interest


@dataclass
class Main:
    """
    Clase principal para crear interfaz de la calculadora de préstamos
    """

    titulo: str

    def run(self) -> None:
        st.set_page_config(page_title="Simulador préstamos", page_icon="💰")
        st.title(self.titulo)

        vlr_solicitado = st.number_input(
            label="Valor a pedir prestado (COP)",
            min_value=500000,
            max_value=3000000,
            value=500000,
            step=20000,
            format=None,
            key=None,
            help="Ingrese el valor que desea pedir prestado (COP)",
        )

        plazo = st.slider(
            label="Plazo a diferir (meses)",
            min_value=1,
            max_value=18,
            value=2,
            help="Ingrese el plazo en el que quiere diferir su préstamo",
        )
        if st.button("Calcular/Simular"):
            tasa = self.get_tasa_from_spreadsheets()
            data = {"deuda": int(vlr_solicitado), "rate": tasa, "time": int(plazo)}
            st.write(data)

            self.calcular_valores(**data)

            # st.text(f"{round(self.intereses_generados)=}")

            st.text(
                f"El plan de pago propuesto sería: cuotas de ${round(self.cuota_mensual)} por {data['time']} meses"
            )

            st.warning(
                "📲 Para mayor información puede llamar o enviar Whatsapp al (+57) 3004273839.\
                Si desea adjunte un pantallazo de esta simulación"
            )

    def calcular_valores(self, **kwargs):
        self.cuota_mensual, self.intereses_generados = compound_interest(**kwargs)

    def get_tasa_from_spreadsheets(self) -> float:
        try:
            # google_sheet_id = st.secrets["google_sheet_id"]
            google_sheet_id = "1HBladLXqVVPn7a7AQH-VjnW7AnmLruMPizdLuzMD-Zs"
            URL = f"https://docs.google.com/spreadsheets/d/{google_sheet_id}/gviz/tq?tqx=out:csv&sheet=nm"
            df = pd.read_csv(URL)
            df = df.dropna(axis=1, how="all")
            return float(df.tasa.values[0])
        except Exception:
            st.write("tasa offline")
            return 6.4


if __name__ == "__main__":
    Main(titulo="Simulador de préstamos 💲💰").run()
