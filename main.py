""" Script para frontend de cálculo de préstamos """
import sys
import pandas as pd
import streamlit as st
from calculator import compound_interest

st.set_page_config(page_title="Simulador préstamos", page_icon="💰")


class Main:
    """ Crea interfaz de la calculadora de préstamos"""

    def __init__(self):
        self.tasa, self.tope_minimo, self.tope_maximo = get_data_from_spreadsheets()

    def run(self) -> None:
        st.title("Simulador de préstamos 💰")
        st.write(sys.version)

        vlr_solicitado = st.number_input(
            label="Valor a pedir prestado (COP):",
            min_value=self.tope_minimo,
            max_value=self.tope_maximo,
            value=self.tope_minimo,
            step=50_000,
            help=f"Ingrese el valor que desea pedir prestado. Entre {self.tope_minimo:,} y {self.tope_maximo:,} COP",
        )

        plazo = st.slider(
            label="Plazo a diferir (meses):",
            min_value=1,
            max_value=18,
            value=3,
            help="Elija la cantidad de meses en los que quiere diferir su préstamo",
        )

        if st.button("Simular:"):
            if vlr_solicitado > self.tope_maximo:
                st.error(f"El valor solicitado supera el máximo permitido (${self.tope_maximo:,})", icon="🚨")
                st.stop()
            elif vlr_solicitado < self.tope_minimo:
                st.error(f"El valor solicitado es inferior al mínimo permitido (${self.tope_minimo:,})", icon="🚨")
                st.stop()
            else:
                if vlr_solicitado > 2000000:
                    self.tasa -= 2.0
                elif vlr_solicitado > 1000000:
                    self.tasa -= 1.0

                if plazo >= 12:
                    self.tasa = self.tasa * 1.2

                data = {"deuda": int(vlr_solicitado), "rate": self.tasa, "time": int(plazo)}
                self.cuota_mensual, self.intereses_generados = self.calcular_valores(**data)

                # data.update({"intereses generados": self.intereses_generados})
                # st.write(data)

                st.markdown("**El plan de pago _propuesto_ sería:**")
                st.success(f"{data['time']} cuotas de ${self.cuota_mensual:,} COP")

                st.warning(
                    "Para mayor información puede llamar o enviar un Whatsapp al (+57) 3004273839.\
                    Si desea, por favor, adjunte un pantallazo de esta simulación.",
                    icon="📲",
                )

    @st.cache_data
    def calcular_valores(self, **kwargs):
        cuota_mensual, intereses_generados = compound_interest(**kwargs)
        cuota_mensual = round(cuota_mensual)

        return cuota_mensual, intereses_generados

@st.cache_data
def get_data_from_spreadsheets() -> tuple:
    try:
        google_sheet_id = st.secrets["google_sheet_id"]
        URL = f"https://docs.google.com/spreadsheets/d/{google_sheet_id}/gviz/tq?tqx=out:csv&sheet=nm"
        df = pd.read_csv(URL)
        df = df.dropna(axis=1, how="all")
        df["tasa"] = df["tasa"].str.replace(",",".")
        return float(df.tasa.values[0]), int(df.minimo.values[0]), int(df.maximo.values[0])
    except Exception:
        st.write("Data offline")
        return 5.1, 375_000, 3_750_000

if __name__ == "__main__":
    Main().run()
