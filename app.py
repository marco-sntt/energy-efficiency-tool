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

# import streamlit as st
# import qrcode
# import io
# from utils.predict import predizione_intervento

# # Configurazione iniziale della pagina
# st.set_page_config(page_title="Tool di Efficientamento Energetico", layout="centered")
# st.title("Tool di Efficientamento Energetico")
# st.markdown("Compila i campi seguenti per calcolare l’impatto stimato di un intervento energetico sull’edificio.")

# # Generazione e visualizzazione del QR Code (nella barra laterale)
# url_streamlit = "https://energy-efficiency-tool-uhca9wtuujygnendua7ljl.streamlit.app/"  # URL del tuo sito
# qr_img = qrcode.make(url_streamlit)
# buf = io.BytesIO()
# qr_img.save(buf)
# byte_im = buf.getvalue()
# st.sidebar.image(byte_im, caption="📱 Scansiona per accedere rapidamente")

# # Da qui in poi tutto il resto del tuo codice esistente (form, predizioni, ecc.)
# with st.form("input_form"):
#     st.subheader("Dati dell’edificio")

#     EP_GL_NREN = st.number_input(
#         "EP_GL_NREN", min_value=0.0, help="Indice di prestazione energetica globale non rinnovabile (kWh/m² anno)"
#     )
#     EP_H_ND = st.number_input(
#         "EP_H_ND", min_value=0.0, help="Fabbisogno di energia termica per il riscaldamento (kWh/m² anno)"
#     )
#     CLASSE_ENERGETICA = st.selectbox(
#         "Classe Energetica (da 1 = A4 a 8 = G)", options=list(range(1, 9)),
#         help="Classe energetica attuale dell’edificio (A1, A2, A3, A4, B, C, D, E,F,G)"
#     )
#     RAPPORTO_SV = st.number_input(
#         "Rapporto S/V", min_value=0.0, help="Rapporto tra superficie disperdente e volume riscaldato"
#     )
#     SUPERFICIE_DISPERDENTE = st.number_input(
#         "Superficie Disperdente (m²)", min_value=0.0, help="Superficie totale dell'involucro che disperde energia"
#     )
#     Y_IE = st.number_input(
#         "Y_IE", min_value=0.0, help="Indice di efficienza dell’edificio rispetto all’involucro"
#     )
#     VOLUME_LORDO_RISCALDATO = st.number_input(
#         "Volume Lordo Riscaldato (m³)", min_value=0.0, help="Volume interno riscaldato"
#     )
#     CATEGORIA_INTERVENTO = st.selectbox(
#         "Categoria di Intervento (1–6)", options=list(range(1, 7)),
#         help="Seleziona la categoria dell’intervento proposto"
#     )

#     submit = st.form_submit_button("Calcola Risparmio Energetico")

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

#QUARTA VERSIONE

# import streamlit as st
# import qrcode
# import io
# import pandas as pd
# import pickle
# import os

# # Caricamento dei modelli
# MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "models"))
# models = {}
# for i in range(1, 7):
#     with open(os.path.join(MODELS_DIR, f"XGBoost_{i}.pkl"), "rb") as f:
#         models[i] = pickle.load(f)

# # Feature richieste da ciascun modello
# feature_sets = {
#     1: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE', 'Y_IE', 'VOLUME_LORDO_RISCALDATO'],
#     2: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE', 'Y_IE'],
#     3: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'Y_IE', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE'],
#     4: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'Y_IE', 'RAPPORTO_SV', 'EP_GL_REN', 'SUPERFICIE_DISPERDENTE'],
#     5: ['EP_GL_NREN', 'EP_H_ND', 'RAPPORTO_SV', 'CLASSE_ENERGETICA', 'EP_GL_REN', 'VOLUME_LORDO_RISCALDATO', 'Y_IE', 'SUPERFICIE_DISPERDENTE', 'SUPERF_UTILE_RISCALDATA', 'A_SOL_EST_A_SUP_UTILE', 'VOLUME_LORDO_RAFFRESCATO', 'SUPERF_UTILE_RAFFRESCATA'],
#     6: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'EP_GL_REN', 'Y_IE', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE', 'SUPERF_UTILE_RISCALDATA', 'VOLUME_LORDO_RISCALDATO', 'A_SOL_EST_A_SUP_UTILE']
# }

# def predizione_intervento(input_data):
#     categoria = input_data.pop("CATEGORIA_INTERVENTO", None)

#     if categoria not in models:
#         raise ValueError(f"Categoria {categoria} non valida")

#     features = feature_sets[categoria]
#     filtered_data = {key: input_data[key] for key in features}
#     X_input = pd.DataFrame([filtered_data])

#     modello = models[categoria]
#     predizione = modello.predict(X_input)

#     return predizione[0]

# # Configurazione iniziale della pagina
# st.set_page_config(page_title="ENERGY EFFICIENCY TOOL", layout="centered")
# st.title("ENERGY EFFICIENCY TOOL")
# st.markdown("Fill in the fields below to estimate the impact of an energy efficiency intervention on the building.")

# # Generazione e visualizzazione del QR Code (nella barra laterale)
# url_streamlit = "https://energy-efficiency-tool-uhca9wtuujygnendua7ljl.streamlit.app/"
# qr_img = qrcode.make(url_streamlit)
# buf = io.BytesIO()
# qr_img.save(buf)
# byte_im = buf.getvalue()
# st.sidebar.image(byte_im, caption="🔳 Scan to access quickly")

# # Da qui in poi tutto il resto del tuo codice esistente (form, predizioni, ecc.)
# with st.form("input_form"):
#     st.subheader("Building data")

#     EP_GL_NREN = st.number_input(
#         "EP_GL_NREN (kWh/m² year)", min_value=0.0, help="Non-renewable global energy performance index (kWh/m² year)"
#     )
#     EP_GL_REN = st.number_input(
#         "EP_GL_REN (kWh/m² year)", min_value=0.0, help="Renewable global energy performance index (kWh/m² year)"
#     )
#     EP_H_ND = st.number_input(
#         "EP_H_ND (kWh/m² year)", min_value=0.0, help="Thermal energy demand for heating (kWh/m² year)"
#     )
#     CLASSE_ENERGETICA = st.selectbox(
#         "Energy class (from 1 = A4 to 10 = G)", options=list(range(1, 9)),
#         help="Current energy class of the building (A1, A2, A3, A4, B, C, D, E, F, G)"
#     )
#     RAPPORTO_SV = st.number_input(
#         "S/V ratio", min_value=0.0, help="Ratio between heat loss surface and heated volume"
#     )
#     SUPERFICIE_DISPERDENTE = st.number_input(
#         "Dispersing surface of the building (m²)", min_value=0.0, help="Total surface area of the energy-dispersing envelope"
#     )
#     Y_IE = st.number_input(
#         "Y_IE", min_value=0.0, help="Periodic thermal transmittance"
#     )
#     VOLUME_LORDO_RISCALDATO = st.number_input(
#         "Gross heated volume of the building (m³)", min_value=0.0, help="Net heated volume"
#     )
#     CATEGORIA_INTERVENTO = st.selectbox(
#         "Type of intervention (1–6)", options=list(range(1, 7)),
#         help="Select the type of intervention"
#     )

#     submit = st.form_submit_button("Calculate energy savings")

# if submit:
#     input_data = {
#         'EP_GL_NREN': EP_GL_NREN,
#         'EP_H_ND': EP_H_ND,
#         'CLASSE_ENERGETICA': CLASSE_ENERGETICA,
#         'RAPPORTO_SV': RAPPORTO_SV,
#         'SUPERFICIE_DISPERDENTE': SUPERFICIE_DISPERDENTE,
#         'Y_IE': Y_IE,
#         'VOLUME_LORDO_RISCALDATO': VOLUME_LORDO_RISCALDATO,
#         'CATEGORIA_INTERVENTO': CATEGORIA_INTERVENTO,
#         'EP_GL_REN': EP_GL_REN
#     }

#     try:
#         risultato = predizione_intervento(input_data.copy())
#         st.success(f"Predicted non-renewable global energy performance index (EP_GL_NREN) after intervention of type {CATEGORIA_INTERVENTO}: **{risultato:.2f}** kWh/m² year")
#         st.metric(
#             label="Delta relative to the original EP_GL_NREN",
#             value=f"{risultato:.2f}",
#             delta=f"{EP_GL_NREN - risultato:.2f}"
#         )
#     except Exception as e:
#         st.error(f"An error occurred during prediction: {e}")

# git add requirements.txt
# git commit -m "Aggiunto qrcode a requirements.txt"
# git push origin maingi

# QUINTA VERSIONE: versione con range sulla base del MAE 

import streamlit as st
import qrcode
import io
import pandas as pd
import pickle
import os

# Caricamento dei modelli
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "models"))
models = {}
for i in range(1, 7):
    with open(os.path.join(MODELS_DIR, f"XGBoost_{i}.pkl"), "rb") as f:
        models[i] = pickle.load(f)

# Feature richieste da ciascun modello
feature_sets = {
    1: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE', 'Y_IE', 'VOLUME_LORDO_RISCALDATO'],
    2: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE', 'Y_IE'],
    3: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'Y_IE', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE'],
    4: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'Y_IE', 'RAPPORTO_SV', 'EP_GL_REN', 'SUPERFICIE_DISPERDENTE'],
    5: ['EP_GL_NREN', 'EP_H_ND', 'RAPPORTO_SV', 'CLASSE_ENERGETICA', 'EP_GL_REN', 'VOLUME_LORDO_RISCALDATO', 'Y_IE', 'SUPERFICIE_DISPERDENTE', 'SUPERF_UTILE_RISCALDATA', 'A_SOL_EST_A_SUP_UTILE', 'VOLUME_LORDO_RAFFRESCATO', 'SUPERF_UTILE_RAFFRESCATA'],
    6: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'EP_GL_REN', 'Y_IE', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE', 'SUPERF_UTILE_RISCALDATA', 'VOLUME_LORDO_RISCALDATO', 'A_SOL_EST_A_SUP_UTILE']
}

def predizione_intervento(input_data):
    categoria = input_data.pop("CATEGORIA_INTERVENTO", None)

    if categoria not in models:
        raise ValueError(f"Categoria {categoria} non valida")

    features = feature_sets[categoria]
    filtered_data = {key: input_data[key] for key in features}
    X_input = pd.DataFrame([filtered_data])

    modello = models[categoria]
    predizione = modello.predict(X_input)

    return predizione[0]

# Configurazione iniziale della pagina
st.set_page_config(page_title="ENERGY EFFICIENCY TOOL", layout="centered")
st.title("ENERGY EFFICIENCY TOOL")
st.markdown("Fill in the fields below to estimate the impact of an energy efficiency intervention on the building.")

# Generazione e visualizzazione del QR Code (nella barra laterale)
url_streamlit = "https://energy-efficiency-tool-uhca9wtuujygnendua7ljl.streamlit.app/"
qr_img = qrcode.make(url_streamlit)
buf = io.BytesIO()
qr_img.save(buf)
byte_im = buf.getvalue()
st.sidebar.image(byte_im, caption="🔳 Scan to access quickly")

# Da qui in poi tutto il resto del tuo codice esistente (form, predizioni, ecc.)
with st.form("input_form"):
    st.subheader("Building data")

    EP_GL_NREN = st.number_input(
        "EP_GL_NREN (kWh/m²·year)", min_value=0.0, help="Non-renewable global energy performance index (kWh/m²·year)"
    )
    EP_GL_REN = st.number_input(
        "EP_GL_REN (kWh/m²·year)", min_value=0.0, help="Renewable global energy performance index (kWh/m²·year)"
    )
    EP_H_ND = st.number_input(
        "EP_H_ND (kWh/m²·year)", min_value=0.0, help="Thermal energy demand for heating (kWh/m²·year)"
    )
    CLASSE_ENERGETICA = st.selectbox(
        "Energy class (from 1 = A4 to 10 = G)", options=list(range(1, 9)),
        help="Current energy class of the building (A1, A2, A3, A4, B, C, D, E, F, G)"
    )
    RAPPORTO_SV = st.number_input(
        "S/V ratio", min_value=0.0, help="Ratio between heat loss surface and heated volume"
    )
    SUPERFICIE_DISPERDENTE = st.number_input(
        "Dispersing surface of the building (m²)", min_value=0.0, help="Total surface area of the energy-dispersing envelope"
    )
    Y_IE = st.number_input(
        "Y_IE", min_value=0.0, help="Periodic thermal transmittance"
    )
    VOLUME_LORDO_RISCALDATO = st.number_input(
        "Gross heated volume of the building (m³)", min_value=0.0, help="Net heated volume"
    )
    CATEGORIA_INTERVENTO = st.selectbox(
        "Type of intervention (1–6)", options=list(range(1, 7)),
        help="Select the type of intervention"
    )

    submit = st.form_submit_button("Calculate energy savings")

if submit:
    input_data = {
        'EP_GL_NREN': EP_GL_NREN,
        'EP_H_ND': EP_H_ND,
        'CLASSE_ENERGETICA': CLASSE_ENERGETICA,
        'RAPPORTO_SV': RAPPORTO_SV,
        'SUPERFICIE_DISPERDENTE': SUPERFICIE_DISPERDENTE,
        'Y_IE': Y_IE,
        'VOLUME_LORDO_RISCALDATO': VOLUME_LORDO_RISCALDATO,
        'CATEGORIA_INTERVENTO': CATEGORIA_INTERVENTO,
        'EP_GL_REN': EP_GL_REN
    }

 # Dizionario dei MAE per ogni categoria
    mae_dict = {
        1: 28.25,
        2: 10.03,
        3: 18.83,
        4: 17.08,
        5: 13.06,
        6: 10.17
    }

    try:
        risultato = predizione_intervento(input_data.copy())
        mae = mae_dict.get(CATEGORIA_INTERVENTO, 28.0)  # Default di sicurezza

        lower_bound = max(risultato - mae, 0)  # Evita valori negativi
        upper_bound = risultato + mae
        delta = EP_GL_NREN - risultato

        st.success(
            f"Predicted range of the non-renewable global energy performance index (EP_GL_NREN) after intervention of type {CATEGORIA_INTERVENTO}:\n\n"
            f"**{lower_bound:.2f} – {upper_bound:.2f}** kWh/m²·year ({risultato:.2f} ± {mae:.2f} kWh/m²·year)"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label="Mean case delta",
                value=f"{risultato:.2f}",
                delta=f"{delta:.2f}",
                delta_color="inverse"
            )

        with col2:
            st.metric(
                label="Best case delta",
                value=f"{lower_bound:.2f}",
                delta=f"{EP_GL_NREN - lower_bound:.2f}",
                delta_color="inverse"
            )

        with col3:
            st.metric(
                label="Worst case delta",
                value=f"{upper_bound:.2f}",
                delta=f"{EP_GL_NREN - upper_bound:.2f}",
                delta_color="inverse"
            )

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")