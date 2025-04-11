#PRIMA VERSIONE

# import streamlit as st
# from utils.predict import predizione_intervento

# st.title("Tool di Efficientamento Energetico")

# EP_GL_NREN = st.number_input("EP_GL_NREN", min_value=0.0)
# EP_H_ND = st.number_input("EP_H_ND", min_value=0.0)
# CLASSE_ENERGETICA = st.selectbox("Classe Energetica (1=Alta, 8=Bassa)", range(1, 9))
# RAPPORTO_SV = st.number_input("Rapporto S/V", min_value=0.0)
# SUPERFICIE_DISPERDENTE = st.number_input("Superficie Disperdente (m²)", min_value=0.0)
# Y_IE = st.number_input("Y_IE", min_value=0.0)
# VOLUME_LORDO_RISCALDATO = st.number_input("Volume lordo riscaldato (m³)", min_value=0.0)
# CATEGORIA_INTERVENTO = st.selectbox("Categoria Intervento (1–6)", range(1, 7))

# if st.button("Calcola Risparmio Energetico"):
#     input_data = {
#         'EP_GL_NREN': EP_GL_NREN,
#         'EP_H_ND': EP_H_ND,
#         'CLASSE_ENERGETICA': CLASSE_ENERGETICA,
#         'RAPPORTO_SV': RAPPORTO_SV,
#         'SUPERFICIE_DISPERDENTE': SUPERFICIE_DISPERDENTE,
#         'Y_IE': Y_IE,
#         'VOLUME_LORDO_RISCALDATO': VOLUME_LORDO_RISCALDATO,
#         'CATEGORIA_INTERVENTO': CATEGORIA_INTERVENTO
#     }

#     risultato = predizione_intervento(input_data.copy())
#     st.success(f"Valore previsto NM_EP_GL_NREN_RAGGIUNG_{CATEGORIA_INTERVENTO}: {risultato:.4f}")

#SECONDA VERSIONE

# import streamlit as st
# from utils.predict import predizione_intervento

# st.set_page_config(page_title="Tool di Efficientamento Energetico", layout="centered")
# st.title("Tool di Efficientamento Energetico")
# st.markdown("Compila i campi seguenti per calcolare l’impatto stimato di un intervento energetico sull’edificio.")

# # Form di input
# with st.form("input_form"):
#     st.subheader("Dati dell’edificio")

#     EP_GL_NREN = st.number_input(
#         "EP_GL_NREN",
#         min_value=0.0,
#         help="Indice di prestazione energetica globale non rinnovabile (kWh/m² anno)"
#     )
#     EP_H_ND = st.number_input(
#         "EP_H_ND",
#         min_value=0.0,
#         help="Fabbisogno di energia termica per il riscaldamento (kWh/m² anno)"
#     )
#     CLASSE_ENERGETICA = st.selectbox(
#         "Classe Energetica (da 1 = A4 a 8 = G)",
#         options=list(range(1, 9)),
#         help="Classe energetica attuale dell’edificio (A1, A2, A3, A4, B, C, D, E,F,G)"
#     )
#     RAPPORTO_SV = st.number_input(
#         "Rapporto S/V",
#         min_value=0.0,
#         help="Rapporto tra superficie disperdente e volume riscaldato"
#     )
#     SUPERFICIE_DISPERDENTE = st.number_input(
#         "Superficie Disperdente (m²)",
#         min_value=0.0,
#         help="Superficie totale dell'involucro che disperde energia"
#     )
#     Y_IE = st.number_input(
#         "Y_IE",
#         min_value=0.0,
#         help="Indice di efficienza dell’edificio rispetto all’involucro"
#     )
#     VOLUME_LORDO_RISCALDATO = st.number_input(
#         "Volume Lordo Riscaldato (m³)",
#         min_value=0.0,
#         help="Volume interno riscaldato"
#     )
#     CATEGORIA_INTERVENTO = st.selectbox(
#         "Categoria di Intervento (1–6)",
#         options=list(range(1, 7)),
#         help="Seleziona la categoria dell’intervento proposto"
#     )

#     submit = st.form_submit_button("Calcola Risparmio Energetico")

# # Logica di elaborazione
# if submit:
#     input_data = {
#         'EP_GL_NREN': EP_GL_NREN,
#         'EP_H_ND': EP_H_ND,
#         'CLASSE_ENERGETICA': CLASSE_ENERGETICA,
#         'RAPPORTO_SV': RAPPORTO_SV,
#         'SUPERFICIE_DISPERDENTE': SUPERFICIE_DISPERDENTE,
#         'Y_IE': Y_IE,
#         'VOLUME_LORDO_RISCALDATO': VOLUME_LORDO_RISCALDATO,
#         'CATEGORIA_INTERVENTO': CATEGORIA_INTERVENTO
#     }

#     try:
#         risultato = predizione_intervento(input_data.copy())

#         st.success(f"Valore previsto di NM_EP_GL_NREN_RAGGIUNG_{CATEGORIA_INTERVENTO}: **{risultato:.2f}** kWh/m² anno")

#         st.metric(
#             label="Variazione rispetto al valore iniziale",
#             value=f"{risultato:.2f}",
#             delta=f"{EP_GL_NREN - risultato:.2f}"
#         )

#     except Exception as e:
#         st.error(f"Errore durante la predizione: {e}")

#TERZA VERSIONE

import streamlit as st
import qrcode
import io
from utils.predict import predizione_intervento

# Configurazione iniziale della pagina
st.set_page_config(page_title="Tool di Efficientamento Energetico", layout="centered")
st.title("Tool di Efficientamento Energetico")
st.markdown("Compila i campi seguenti per calcolare l’impatto stimato di un intervento energetico sull’edificio.")

# Generazione e visualizzazione del QR Code (nella barra laterale)
url_streamlit = "https://energy-efficiency-tool-uhca9wtuujygnendua7ljl.streamlit.app/"  # URL del tuo sito
qr_img = qrcode.make(url_streamlit)
buf = io.BytesIO()
qr_img.save(buf)
byte_im = buf.getvalue()
st.sidebar.image(byte_im, caption="📱 Scansiona per accedere rapidamente")

# Da qui in poi tutto il resto del tuo codice esistente (form, predizioni, ecc.)
with st.form("input_form"):
    st.subheader("Dati dell’edificio")

    EP_GL_NREN = st.number_input(
        "EP_GL_NREN", min_value=0.0, help="Indice di prestazione energetica globale non rinnovabile (kWh/m² anno)"
    )
    EP_H_ND = st.number_input(
        "EP_H_ND", min_value=0.0, help="Fabbisogno di energia termica per il riscaldamento (kWh/m² anno)"
    )
    CLASSE_ENERGETICA = st.selectbox(
        "Classe Energetica (da 1 = A4 a 8 = G)", options=list(range(1, 9)),
        help="Classe energetica attuale dell’edificio (A1, A2, A3, A4, B, C, D, E,F,G)"
    )
    RAPPORTO_SV = st.number_input(
        "Rapporto S/V", min_value=0.0, help="Rapporto tra superficie disperdente e volume riscaldato"
    )
    SUPERFICIE_DISPERDENTE = st.number_input(
        "Superficie Disperdente (m²)", min_value=0.0, help="Superficie totale dell'involucro che disperde energia"
    )
    Y_IE = st.number_input(
        "Y_IE", min_value=0.0, help="Indice di efficienza dell’edificio rispetto all’involucro"
    )
    VOLUME_LORDO_RISCALDATO = st.number_input(
        "Volume Lordo Riscaldato (m³)", min_value=0.0, help="Volume interno riscaldato"
    )
    CATEGORIA_INTERVENTO = st.selectbox(
        "Categoria di Intervento (1–6)", options=list(range(1, 7)),
        help="Seleziona la categoria dell’intervento proposto"
    )

    submit = st.form_submit_button("Calcola Risparmio Energetico")

if submit:
    input_data = {
        'EP_GL_NREN': EP_GL_NREN,
        'EP_H_ND': EP_H_ND,
        'CLASSE_ENERGETICA': CLASSE_ENERGETICA,
        'RAPPORTO_SV': RAPPORTO_SV,
        'SUPERFICIE_DISPERDENTE': SUPERFICIE_DISPERDENTE,
        'Y_IE': Y_IE,
        'VOLUME_LORDO_RISCALDATO': VOLUME_LORDO_RISCALDATO,
        'CATEGORIA_INTERVENTO': CATEGORIA_INTERVENTO
    }

    try:
        risultato = predizione_intervento(input_data.copy())
        st.success(f"Valore previsto di NM_EP_GL_NREN_RAGGIUNG_{CATEGORIA_INTERVENTO}: **{risultato:.2f}** kWh/m² anno")

        st.metric(
            label="Variazione rispetto al valore iniziale",
            value=f"{risultato:.2f}",
            delta=f"{EP_GL_NREN - risultato:.2f}"
        )
    except Exception as e:
        st.error(f"Errore durante la predizione: {e}")
