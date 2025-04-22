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

# st.markdown("""
# **⚠️ This tool is valid only for buildings located in the Lombardy region, within climate zone E, and specifically of category E.1:**
# - E.1(1): Buildings used as permanent residences (e.g., apartment buildings)
# - E.1(2): Buildings used as non-permanent residences (e.g., holiday homes)
# - E.1(3): Other residential buildings (e.g., student or worker residences)

# ⚠️ Make sure your building meets these criteria before proceeding.
            
# Fill in the fields below to estimate the impact of an energy efficiency intervention on the building.
# """)


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
#         "EP_GL_NREN (kWh/m²·year)", min_value=0.0, help="Non-renewable global energy performance index (kWh/m²·year)"
#     )
#     EP_GL_REN = st.number_input(
#         "EP_GL_REN (kWh/m²·year)", min_value=0.0, help="Renewable global energy performance index (kWh/m²·year)"
#     )
#     EP_H_ND = st.number_input(
#         "EP_H_ND (kWh/m²·year)", min_value=0.0, help="Thermal energy demand for heating (kWh/m²·year)"
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

#  # Dizionario dei MAE per ogni categoria
#     mae_dict = {
#         1: 28.25,
#         2: 10.03,
#         3: 18.83,
#         4: 17.08,
#         5: 13.06,
#         6: 10.17
#     }

#     try:
#         risultato = predizione_intervento(input_data.copy())
#         mae = mae_dict.get(CATEGORIA_INTERVENTO, 28.0)  # Default di sicurezza

#         lower_bound = max(risultato - mae, 0)  # Evita valori negativi
#         upper_bound = risultato + mae
#         delta = EP_GL_NREN - risultato

#         st.success(
#             f"Predicted range of the non-renewable global energy performance index (EP_GL_NREN) after intervention of type {CATEGORIA_INTERVENTO}:\n\n"
#             f"**{lower_bound:.2f} – {upper_bound:.2f}** kWh/m²·year ({risultato:.2f} ± {mae:.2f} kWh/m²·year)"
#         )

#         col1, col2, col3 = st.columns(3)

#         with col1:
#             st.metric(
#                 label="Mean case delta",
#                 value=f"{risultato:.2f}",
#                 delta=f"{delta:.2f}",
#                 delta_color="inverse"
#             )

#         with col2:
#             st.metric(
#                 label="Best case delta",
#                 value=f"{lower_bound:.2f}",
#                 delta=f"{EP_GL_NREN - lower_bound:.2f}",
#                 delta_color="inverse"
#             )

#         with col3:
#             st.metric(
#                 label="Worst case delta",
#                 value=f"{upper_bound:.2f}",
#                 delta=f"{EP_GL_NREN - upper_bound:.2f}",
#                 delta_color="inverse"
#             )

#     except Exception as e:
#         st.error(f"An error occurred during prediction: {e}")

# SESTA VERSIONE: versione migliorata con modello 7

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
#     5: ['EP_GL_NREN', 'EP_H_ND', 'RAPPORTO_SV', 'CLASSE_ENERGETICA', 'EP_GL_REN', 'VOLUME_LORDO_RISCALDATO', 'Y_IE', 'SUPERFICIE_DISPERDENTE',
#         'SUPERF_UTILE_RISCALDATA', 'A_SOL_EST_A_SUP_UTILE', 'VOLUME_LORDO_RAFFRESCATO', 'SUPERF_UTILE_RAFFRESCATA'],
#     6: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'EP_GL_REN', 'Y_IE', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE', 'SUPERF_UTILE_RISCALDATA',
#         'VOLUME_LORDO_RISCALDATO', 'A_SOL_EST_A_SUP_UTILE']
# }

# def predizione_intervento(input_data, categoria):
#     """
#     Data un dizionario con le feature e la categoria di intervento,
#     restituisce la predizione del modello corrispondente.
#     """
#     if categoria not in models:
#         raise ValueError(f"Categoria {categoria} non valida")

#     features = feature_sets[categoria]
#     # Filtra solo le feature necessarie per il modello
#     filtered_data = {key: input_data[key] for key in features if key in input_data}
#     X_input = pd.DataFrame([filtered_data])

#     modello = models[categoria]
#     predizione = modello.predict(X_input)

#     return predizione[0]

# # Dizionario dei MAE per ogni categoria (per costruire gli intervalli)
# mae_dict = {
#     1: 28.25,
#     2: 10.03,
#     3: 18.83,
#     4: 17.08,
#     5: 13.06,
#     6: 10.17
# }

# # Configurazione iniziale della pagina
# st.set_page_config(page_title="ENERGY EFFICIENCY TOOL", layout="centered")
# st.title("ENERGY EFFICIENCY TOOL")

# st.markdown("""
# **⚠️ This tool is valid only for buildings located in the Lombardy region, within climate zone E, and specifically of category E.1:**
# - E.1(1): Buildings used as permanent residences (e.g., apartment buildings)
# - E.1(2): Buildings used as non-permanent residences (e.g., holiday homes)
# - E.1(3): Other residential buildings (e.g., student or worker residences)

# ⚠️ Make sure your building meets these criteria before proceeding.
            
# Fill in the fields below to estimate the impact of an energy efficiency intervention on the building.
# """)

# # Generazione e visualizzazione del QR Code (nella barra laterale)
# url_streamlit = "https://energy-efficiency-tool-uhca9wtuujygnendua7ljl.streamlit.app/"
# qr_img = qrcode.make(url_streamlit)
# buf = io.BytesIO()
# qr_img.save(buf)
# byte_im = buf.getvalue()
# st.sidebar.image(byte_im, caption="🔳 Scan to access quickly")

# # --- BOX 1: Selezione multipla dell'intervento con checkbox --- #
# with st.form("intervention_form"):
#     st.subheader("Type of intervention")
#     # Lista di interventi con checkbox
#     selected_interventions = []

#     check_1 = st.checkbox("1 - Improvement of the opaque envelope", value=False)
#     if check_1: selected_interventions.append(1)

#     check_2 = st.checkbox("2 - Improvement of the transparent envelope", value=False)
#     if check_2: selected_interventions.append(2)

#     check_3 = st.checkbox("3 - Replacement or upgrade of the heating system", value=False)
#     if check_3: selected_interventions.append(3)

#     check_4 = st.checkbox("4 - Replacement or upgrade of the cooling system", value=False)
#     if check_4: selected_interventions.append(4)

#     check_5 = st.checkbox("5 - Use of renewable energy sources", value=False)
#     if check_5: selected_interventions.append(5)

#     check_6 = st.checkbox("6 - Other interventions", value=False)
#     if check_6: selected_interventions.append(6)

#     intervention_submitted = st.form_submit_button("Confirm selection")

# # --- BOX 2: Inserimento dei dati di building --- #
# with st.form("building_data_form"):
#     st.subheader("Building data")

#     EP_GL_NREN = st.number_input(
#         "EP_GL_NREN (kWh/m²·year)", min_value=0.0, 
#         help="Non-renewable global energy performance index (kWh/m²·year)"
#     )
#     EP_GL_REN = st.number_input(
#         "EP_GL_REN (kWh/m²·year)", min_value=0.0, 
#         help="Renewable global energy performance index (kWh/m²·year)"
#     )
#     EP_H_ND = st.number_input(
#         "EP_H_ND (kWh/m²·year)", min_value=0.0, 
#         help="Thermal energy demand for heating (kWh/m²·year)"
#     )
#     CLASSE_ENERGETICA = st.selectbox(
#         "Energy class (from 1 = A4 to 10 = G)",
#         options=list(range(1, 11)),
#         help="Current energy class of the building (A1, A2, A3, A4, B, C, D, E, F, G)"
#     )
#     RAPPORTO_SV = st.number_input(
#         "S/V ratio", min_value=0.0, 
#         help="Ratio between heat loss surface and heated volume"
#     )
#     SUPERFICIE_DISPERDENTE = st.number_input(
#         "Dispersing surface of the building (m²)", min_value=0.0, 
#         help="Total surface area of the energy-dispersing envelope"
#     )
#     Y_IE = st.number_input(
#         "Y_IE", min_value=0.0, 
#         help="Periodic thermal transmittance"
#     )
#     VOLUME_LORDO_RISCALDATO = st.number_input(
#         "Gross heated volume of the building (m³)", min_value=0.0, 
#         help="Gross heated volume"
#     )
#     SUPERF_UTILE_RISCALDATA = st.number_input(
#         "Heated useful area of the building (m²)", min_value=0.0, 
#         help="Heated useful area of the building"
#     )
#     A_SOL_EST_A_SUP_UTILE = st.number_input(
#         "Solar collection area to net usable surface ratio (m²)", min_value=0.0, 
#         help="Summer equivalent solar area per unit of useful surface"
#     )
#     VOLUME_LORDO_RAFFRESCATO = st.number_input(
#         "Gross cooled volume of the building (m³)", min_value=0.0, 
#         help="Gross cooled volume"
#     )
#     SUPERF_UTILE_RAFFRESCATA = st.number_input(
#         "Cooled useful area of the building (m²)", min_value=0.0, 
#         help="Cooled useful area of the building"
#     )

#     submit = st.form_submit_button("Calculate energy savings")

# # --- Se l'utente ha inviato la form dei dati --- #
# if submit:
#     # Controllo che l'utente abbia selezionato almeno un intervento
#     if not selected_interventions:
#         st.error("Please select at least one intervention above before calculating.")
#     else:
#         # Prepara i dati in un dizionario
#         input_data = {
#             'EP_GL_NREN': EP_GL_NREN,
#             'EP_H_ND': EP_H_ND,
#             'CLASSE_ENERGETICA': CLASSE_ENERGETICA,
#             'RAPPORTO_SV': RAPPORTO_SV,
#             'SUPERFICIE_DISPERDENTE': SUPERFICIE_DISPERDENTE,
#             'Y_IE': Y_IE,
#             'VOLUME_LORDO_RISCALDATO': VOLUME_LORDO_RISCALDATO,
#             'EP_GL_REN': EP_GL_REN
#         }

#         # Esegui la predizione per ogni intervento selezionato
#         for intervention_type in selected_interventions:
#             try:
#                 risultato = predizione_intervento(input_data.copy(), intervention_type)
#                 mae = mae_dict.get(intervention_type, 28.0)  # default di sicurezza

#                 lower_bound = max(risultato - mae, 0)  # Evita valori negativi
#                 upper_bound = risultato + mae
#                 delta = EP_GL_NREN - risultato

#                 st.success(
#                     f"**Intervention {intervention_type}**\n\n"
#                     f"Predicted range of the non-renewable global energy performance index (EP_GL_NREN):\n"
#                     f"**{lower_bound:.2f} – {upper_bound:.2f}** kWh/m²·year "
#                     f"({risultato:.2f} ± {mae:.2f} kWh/m²·year)"
#                 )

#                 col1, col2, col3 = st.columns(3)
#                 with col1:
#                     st.metric(
#                         label=f"Mean case delta (Int. {intervention_type})",
#                         value=f"{risultato:.2f}",
#                         delta=f"{delta:.2f}",
#                         delta_color="inverse"
#                     )
#                 with col2:
#                     (
#                     )
#                 with col3:
#                     (
#                     )
#             except Exception as e:
#                 st.error(f"An error occurred during prediction for intervention {intervention_type}: {e}")

#SETTIMA VERSIONE 

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
#     5: ['EP_GL_NREN', 'EP_H_ND', 'RAPPORTO_SV', 'CLASSE_ENERGETICA', 'EP_GL_REN', 'VOLUME_LORDO_RISCALDATO', 'Y_IE', 'SUPERFICIE_DISPERDENTE',
#         'SUPERF_UTILE_RISCALDATA', 'A_SOL_EST_A_SUP_UTILE', 'VOLUME_LORDO_RAFFRESCATO', 'SUPERF_UTILE_RAFFRESCATA'],
#     6: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'EP_GL_REN', 'Y_IE', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE', 'SUPERF_UTILE_RISCALDATA',
#         'VOLUME_LORDO_RISCALDATO', 'A_SOL_EST_A_SUP_UTILE']
# }

# def predizione_intervento(input_data, categoria):
#     """
#     Data un dizionario con le feature e la categoria di intervento,
#     restituisce la predizione del modello corrispondente.
#     """
#     if categoria not in models:
#         raise ValueError(f"Categoria {categoria} non valida")

#     features = feature_sets[categoria]
#     # Filtra solo le feature necessarie per il modello
#     filtered_data = {key: input_data[key] for key in features if key in input_data}
#     X_input = pd.DataFrame([filtered_data])

#     modello = models[categoria]
#     predizione = modello.predict(X_input)

#     return predizione[0]

# # Dizionario dei MAE per ogni categoria (per costruire gli intervalli)
# mae_dict = {
#     1: 28.25,
#     2: 10.03,
#     3: 18.83,
#     4: 17.08,
#     5: 13.06,
#     6: 10.17
# }

# # Configurazione iniziale della pagina
# st.set_page_config(page_title="ENERGY EFFICIENCY TOOL", layout="centered")
# st.title("ENERGY EFFICIENCY TOOL")

# st.markdown("""
# **⚠️ This tool is valid only for buildings located in the Lombardy region, within climate zone E, and specifically of category E.1:**
# - E.1(1): Buildings used as permanent residences (e.g., apartment buildings)
# - E.1(2): Buildings used as non-permanent residences (e.g., holiday homes)
# - E.1(3): Other residential buildings (e.g., student or worker residences)

# ⚠️ Make sure your building meets these criteria before proceeding.
            
# Fill in the fields below to estimate the impact of an energy efficiency intervention on the building.
# """)

# # Generazione e visualizzazione del QR Code (nella barra laterale)
# url_streamlit = "https://energy-efficiency-tool-uhca9wtuujygnendua7ljl.streamlit.app/"
# qr_img = qrcode.make(url_streamlit)
# buf = io.BytesIO()
# qr_img.save(buf)
# byte_im = buf.getvalue()
# st.sidebar.image(byte_im, caption="🔳 Scan to access quickly")

# # --- BOX 1: Selezione multipla dell'intervento con checkbox --- #
# with st.form("intervention_form"):
#     st.subheader("Type of intervention")
#     # Lista di interventi con checkbox
#     selected_interventions = []

#     check_1 = st.checkbox("1 - Improvement of the opaque envelope", value=False)
#     if check_1: selected_interventions.append(1)

#     check_2 = st.checkbox("2 - Improvement of the transparent envelope", value=False)
#     if check_2: selected_interventions.append(2)

#     check_3 = st.checkbox("3 - Replacement or upgrade of the heating system", value=False)
#     if check_3: selected_interventions.append(3)

#     check_4 = st.checkbox("4 - Replacement or upgrade of the cooling system", value=False)
#     if check_4: selected_interventions.append(4)

#     check_5 = st.checkbox("5 - Use of renewable energy sources", value=False)
#     if check_5: selected_interventions.append(5)

#     check_6 = st.checkbox("6 - Other interventions", value=False)
#     if check_6: selected_interventions.append(6)

#     intervention_submitted = st.form_submit_button("Confirm selection")

# # Una volta che l'utente conferma la selezione degli interventi...
# if intervention_submitted:
#     if not selected_interventions:
#         st.error("Please select at least one intervention before proceeding.")
#     else:
#         # Calcoliamo l'unione delle feature di tutti gli interventi selezionati
#         needed_fields = set()
#         for i in selected_interventions:
#             needed_fields.update(feature_sets[i])

#         # --- BOX 2: Inserimento dei dati di building SOLO per le feature necessarie --- #
#         with st.form("building_data_form"):
#             st.subheader("Building data")

#             # Dichiariamo un dizionario che conterrà i valori inseriti dall'utente
#             input_data = {}

#             if "EP_GL_NREN" in needed_fields:
#                 input_data["EP_GL_NREN"] = st.number_input(
#                     "EP_GL_NREN (kWh/m²·year)", min_value=0.0, 
#                     help="Non-renewable global energy performance index (kWh/m²·year)"
#                 )
#             if "EP_GL_REN" in needed_fields:
#                 input_data["EP_GL_REN"] = st.number_input(
#                     "EP_GL_REN (kWh/m²·year)", min_value=0.0, 
#                     help="Renewable global energy performance index (kWh/m²·year)"
#                 )
#             if "EP_H_ND" in needed_fields:
#                 input_data["EP_H_ND"] = st.number_input(
#                     "EP_H_ND (kWh/m²·year)", min_value=0.0, 
#                     help="Thermal energy demand for heating (kWh/m²·year)"
#                 )
#             if "CLASSE_ENERGETICA" in needed_fields:
#                 input_data["CLASSE_ENERGETICA"] = st.selectbox(
#                     "Energy class (from 1 = A4 to 10 = G)",
#                     options=list(range(1, 11)),
#                     help="Current energy class of the building (A1..G)"
#                 )
#             if "RAPPORTO_SV" in needed_fields:
#                 input_data["RAPPORTO_SV"] = st.number_input(
#                     "S/V ratio", min_value=0.0, 
#                     help="Ratio between heat loss surface and heated volume"
#                 )
#             if "SUPERFICIE_DISPERDENTE" in needed_fields:
#                 input_data["SUPERFICIE_DISPERDENTE"] = st.number_input(
#                     "Dispersing surface (m²)", min_value=0.0, 
#                     help="Total surface area of the energy-dispersing envelope"
#                 )
#             if "Y_IE" in needed_fields:
#                 input_data["Y_IE"] = st.number_input(
#                     "Y_IE", min_value=0.0, 
#                     help="Periodic thermal transmittance"
#                 )
#             if "VOLUME_LORDO_RISCALDATO" in needed_fields:
#                 input_data["VOLUME_LORDO_RISCALDATO"] = st.number_input(
#                     "Gross heated volume (m³)", min_value=0.0, 
#                     help="Gross heated volume"
#                 )
#             if "SUPERF_UTILE_RISCALDATA" in needed_fields:
#                 input_data["SUPERF_UTILE_RISCALDATA"] = st.number_input(
#                     "Heated useful area (m²)", min_value=0.0, 
#                     help="Heated useful floor area of the building"
#                 )
#             if "A_SOL_EST_A_SUP_UTILE" in needed_fields:
#                 input_data["A_SOL_EST_A_SUP_UTILE"] = st.number_input(
#                     "Solar collection area to net usable surface ratio", min_value=0.0, 
#                     help="Summer equivalent solar area per unit of useful surface"
#                 )
#             if "VOLUME_LORDO_RAFFRESCATO" in needed_fields:
#                 input_data["VOLUME_LORDO_RAFFRESCATO"] = st.number_input(
#                     "Gross cooled volume (m³)", min_value=0.0, 
#                     help="Gross cooled volume"
#                 )
#             if "SUPERF_UTILE_RAFFRESCATA" in needed_fields:
#                 input_data["SUPERF_UTILE_RAFFRESCATA"] = st.number_input(
#                     "Cooled useful area (m²)", min_value=0.0, 
#                     help="Cooled useful floor area of the building"
#                 )

#             submit = st.form_submit_button("Calculate energy savings")

#         # Solo se l'utente invia i dati di building
#         if submit:
#             # Eseguiamo la predizione per ogni intervento selezionato
#             for intervention_type in selected_interventions:
#                 try:
#                     risultato = predizione_intervento(input_data.copy(), intervention_type)
#                     mae = mae_dict.get(intervention_type, 28.0)  # default di sicurezza

#                     lower_bound = max(risultato - mae, 0)  # Evita valori negativi
#                     upper_bound = risultato + mae

#                     # Se "EP_GL_NREN" era tra le needed_fields, possiamo calcolare la differenza
#                     # altrimenti, se non c'è EP_GL_NREN, saltiamo il calcolo di delta
#                     delta = None
#                     if "EP_GL_NREN" in needed_fields:
#                         delta = input_data["EP_GL_NREN"] - risultato

#                     st.success(
#                         f"**Intervention {intervention_type}**\n\n"
#                         f"Predicted range of EP_GL_NREN:\n"
#                         f"**{lower_bound:.2f} – {upper_bound:.2f}** kWh/m²·year "
#                         f"({risultato:.2f} ± {mae:.2f} kWh/m²·year)"
#                     )

#                     if delta is not None:
#                         col1, col2, col3 = st.columns(3)
#                         with col1:
#                             st.metric(
#                                 label=f"Mean case delta (Int. {intervention_type})",
#                                 value=f"{risultato:.2f}",
#                                 delta=f"{delta:.2f}",
#                                 delta_color="inverse"
#                             )
#                 except Exception as e:
#                     st.error(f"An error occurred during prediction for intervention {intervention_type}: {e}")

#OTTAVA VERSIONE: con classe energetica 

# import streamlit as st
# import qrcode
# import io
# import pandas as pd
# import pickle
# import os

# # Caricamento dei modelli per NM_EP_GL_NREN
# MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "models"))
# models = {}
# for i in range(1, 7):
#     with open(os.path.join(MODELS_DIR, f"XGBoost_{i}.pkl"), "rb") as f:
#         models[i] = pickle.load(f)

# # Caricamento dei modelli per predire la nuova classe energetica
# models_en = {}
# for i in range(1, 7):
#     with open(os.path.join(MODELS_DIR, f"XGBoost_EN_{i}.pkl"), "rb") as f:
#         models_en[i] = pickle.load(f)

# # Feature richieste da ciascun modello (prima predizione)
# feature_sets = {
#     1: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'RAPPORTO_SV',
#         'SUPERFICIE_DISPERDENTE', 'Y_IE', 'VOLUME_LORDO_RISCALDATO'],
#     2: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'RAPPORTO_SV',
#         'SUPERFICIE_DISPERDENTE', 'Y_IE'],
#     3: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'Y_IE',
#         'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE'],
#     4: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'Y_IE',
#         'RAPPORTO_SV', 'EP_GL_REN', 'SUPERFICIE_DISPERDENTE'],
#     5: ['EP_GL_NREN', 'EP_H_ND', 'RAPPORTO_SV', 'CLASSE_ENERGETICA',
#         'EP_GL_REN', 'VOLUME_LORDO_RISCALDATO', 'Y_IE',
#         'SUPERFICIE_DISPERDENTE', 'SUPERF_UTILE_RISCALDATA',
#         'A_SOL_EST_A_SUP_UTILE', 'VOLUME_LORDO_RAFFRESCATO',
#         'SUPERF_UTILE_RAFFRESCATA'],
#     6: ['EP_GL_NREN', 'EP_H_ND', 'CLASSE_ENERGETICA', 'EP_GL_REN',
#         'Y_IE', 'RAPPORTO_SV', 'SUPERFICIE_DISPERDENTE',
#         'SUPERF_UTILE_RISCALDATA', 'VOLUME_LORDO_RISCALDATO',
#         'A_SOL_EST_A_SUP_UTILE']
# }

# def predizione_intervento(input_data, categoria):
#     """
#     Data un dizionario con le feature e la categoria di intervento,
#     restituisce la predizione del modello corrispondente (NM_EP_GL_NREN_RAGGIUNG_n).
#     """
#     if categoria not in models:
#         raise ValueError(f"Categoria {categoria} non valida")

#     features = feature_sets[categoria]
#     # Filtra solo le feature necessarie per il modello
#     filtered_data = {key: input_data[key] for key in features if key in input_data}
#     X_input = pd.DataFrame([filtered_data])

#     modello = models[categoria]
#     predizione = modello.predict(X_input)

#     return predizione[0]

# def predizione_classe_energetica(nm_ep_gl_nren_raggiung, ep_gl_nren, classe_energetica, categoria):
#     # Costruiamo il DataFrame con le 3 feature richieste
#     col_nm = f"NM_EP_GL_NREN_RAGGIUNG_{categoria}"
#     X_en = pd.DataFrame([{
#         col_nm: nm_ep_gl_nren_raggiung,
#         "CLASSE_ENERGETICA": classe_energetica,
#         "EP_GL_NREN": ep_gl_nren
#     }])

#     # --- NUOVO: riallinea le colonne come il modello si aspetta ---
#     model_en = models_en[categoria]
#     # se usi lo sklearn wrapper:
#     feature_order = model_en.feature_names_in_
#     # altrimenti, per un Booster puro:
#     # feature_order = model_en.get_booster().feature_names
#     X_en = X_en[feature_order]

#     # Ora la predizione non darà più mismatch
#     new_class = model_en.predict(X_en)
#     return new_class[0]

# # Dizionario dei MAE per ogni categoria (per costruire gli intervalli)
# mae_dict = {
#     1: 28.25,
#     2: 10.03,
#     3: 18.83,
#     4: 17.08,
#     5: 13.06,
#     6: 10.17
# }

# # Configurazione iniziale della pagina
# st.set_page_config(
#     page_title="ENERGY EFFICIENCY TOOL", 
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # crea due colonne: la prima (4 parti) per il contenuto principale,
# # la seconda (1 parte) per il pannello a destra
# col_main, col_right = st.columns([4, 1])

# with col_main:
#     st.title("ENERGY EFFICIENCY TOOL")
#     st.markdown("""
#     **⚠️ This tool is valid only for buildings located in the Lombardy region, within climate zone E, and specifically of category E.1:**
#     - E.1(1): Buildings used as permanent residences (e.g., apartment buildings)
#     - E.1(2): Buildings used as non-permanent residences (e.g., holiday homes)
#     - E.1(3): Other residential buildings (e.g., student or worker residences)

#     ⚠️ Make sure your building meets these criteria before proceeding.
            
#     Fill in the fields below to estimate the impact of an energy efficiency intervention on the building.
#     """)

# with col_right:
#     # puoi anche mettere un expander per avere la tendina
#     with st.expander("🔳 QR Code", expanded=False):
#         url_streamlit = "https://energy-efficiency-tool-uhca9wtuujygnendua7ljl.streamlit.app/"
#         qr_img = qrcode.make(url_streamlit)
#         buf = io.BytesIO()
#         qr_img.save(buf)
#         st.image(buf.getvalue(), use_column_width=True)

# # 1) Inizializza la chiave di session_state per la lista interventi
# if "selected_interventions" not in st.session_state:
#     st.session_state.selected_interventions = []

# # --- BOX 1: Selezione multipla dell'intervento con checkbox --- #
# with st.form("intervention_form"):
#     st.subheader("Type of intervention")

#     # Creiamo una lista temporanea dei nuovi interventi selezionati
#     temp_selected = []

#     check_1 = st.checkbox("1 - Improvement of the opaque envelope",
#                           value=(1 in st.session_state.selected_interventions))
#     if check_1: temp_selected.append(1)

#     check_2 = st.checkbox("2 - Improvement of the transparent envelope",
#                           value=(2 in st.session_state.selected_interventions))
#     if check_2: temp_selected.append(2)

#     check_3 = st.checkbox("3 - Replacement or upgrade of the heating system",
#                           value=(3 in st.session_state.selected_interventions))
#     if check_3: temp_selected.append(3)

#     check_4 = st.checkbox("4 - Replacement or upgrade of the cooling system",
#                           value=(4 in st.session_state.selected_interventions))
#     if check_4: temp_selected.append(4)

#     check_5 = st.checkbox("5 - Use of renewable energy sources",
#                           value=(5 in st.session_state.selected_interventions))
#     if check_5: temp_selected.append(5)

#     check_6 = st.checkbox("6 - Other interventions",
#                           value=(6 in st.session_state.selected_interventions))
#     if check_6: temp_selected.append(6)

#     intervention_submitted = st.form_submit_button("Confirm selection")

# # 2) Se l'utente ha premuto "Confirm selection",
# #    salviamo la lista temp_selected in st.session_state.selected_interventions
# if intervention_submitted:
#     st.session_state.selected_interventions = temp_selected
#     if not temp_selected:
#         st.error("Please select at least one intervention before proceeding.")

# # 3) Se ci sono interventi selezionati, calcoliamo i campi necessari e mostriamo la seconda form
# if st.session_state.selected_interventions:
#     needed_fields = set()
#     for i in st.session_state.selected_interventions:
#         needed_fields.update(feature_sets[i])

#     with st.form("building_data_form"):
#         st.subheader("Building data")

#         input_data = {}

#         # EP_GL_NREN
#         # Se uno dei modelli selezionati la richiede, la rendiamo disponibile
#         if "EP_GL_NREN" in needed_fields:
#             input_data["EP_GL_NREN"] = st.number_input(
#                 "EP_GL_NREN (kWh/m²·year)", 
#                 min_value=0.0,
#                 help="Non-renewable global energy performance index (kWh/m²·year)"
#             )

#         # EP_GL_REN
#         if "EP_GL_REN" in needed_fields:
#             input_data["EP_GL_REN"] = st.number_input(
#                 "EP_GL_REN (kWh/m²·year)",
#                 min_value=0.0,
#                 help="Renewable global energy performance index (kWh/m²·year)"
#             )

#         # EP_H_ND
#         if "EP_H_ND" in needed_fields:
#             input_data["EP_H_ND"] = st.number_input(
#                 "EP_H_ND (kWh/m²·year)", 
#                 min_value=0.0,
#                 help="Thermal energy demand for heating (kWh/m²·year)"
#             )

#         # CLASSE_ENERGETICA
#         if "CLASSE_ENERGETICA" in needed_fields:
#             selected = st.selectbox(
#                 "Energy class (from 1 = A4 to 10 = G)",
#                 options=list(range(1, 11)),
#                 help="Current energy class of the building (1=A4 .. 10=G)"
#             )
#             # Passa al regressore il valore zero‑based
#             input_data["CLASSE_ENERGETICA"] = selected - 1

#         # RAPPORTO_SV
#         if "RAPPORTO_SV" in needed_fields:
#             input_data["RAPPORTO_SV"] = st.number_input(
#                 "S/V ratio",
#                 min_value=0.0,
#                 help="Ratio between heat loss surface and heated volume"
#             )

#         # SUPERFICIE_DISPERDENTE
#         if "SUPERFICIE_DISPERDENTE" in needed_fields:
#             input_data["SUPERFICIE_DISPERDENTE"] = st.number_input(
#                 "Dispersing surface (m²)",
#                 min_value=0.0,
#                 help="Total surface area of the energy-dispersing envelope"
#             )

#         # Y_IE
#         if "Y_IE" in needed_fields:
#             input_data["Y_IE"] = st.number_input(
#                 "Y_IE",
#                 min_value=0.0,
#                 help="Periodic thermal transmittance"
#             )

#         # VOLUME_LORDO_RISCALDATO
#         if "VOLUME_LORDO_RISCALDATO" in needed_fields:
#             input_data["VOLUME_LORDO_RISCALDATO"] = st.number_input(
#                 "Gross heated volume (m³)",
#                 min_value=0.0,
#                 help="Gross heated volume"
#             )

#         # SUPERF_UTILE_RISCALDATA
#         if "SUPERF_UTILE_RISCALDATA" in needed_fields:
#             input_data["SUPERF_UTILE_RISCALDATA"] = st.number_input(
#                 "Heated useful area (m²)",
#                 min_value=0.0,
#                 help="Heated useful floor area of the building"
#             )

#         # A_SOL_EST_A_SUP_UTILE
#         if "A_SOL_EST_A_SUP_UTILE" in needed_fields:
#             input_data["A_SOL_EST_A_SUP_UTILE"] = st.number_input(
#                 "Solar collection area to net usable surface ratio",
#                 min_value=0.0,
#                 help="Summer equivalent solar area per unit of useful surface"
#             )

#         # VOLUME_LORDO_RAFFRESCATO
#         if "VOLUME_LORDO_RAFFRESCATO" in needed_fields:
#             input_data["VOLUME_LORDO_RAFFRESCATO"] = st.number_input(
#                 "Gross cooled volume (m³)",
#                 min_value=0.0,
#                 help="Gross cooled volume"
#             )

#         # SUPERF_UTILE_RAFFRESCATA
#         if "SUPERF_UTILE_RAFFRESCATA" in needed_fields:
#             input_data["SUPERF_UTILE_RAFFRESCATA"] = st.number_input(
#                 "Cooled useful area (m²)",
#                 min_value=0.0,
#                 help="Cooled useful floor area of the building"
#             )

#         # Tasto di submit per la seconda form
#         submit_building = st.form_submit_button("Calculate energy savings")

#     # 4) Se l'utente ha inviato i dati di building
#     if submit_building:
#         # Controllo minimo: se i modelli EN necessitano CLASSE_ENERGETICA e EP_GL_NREN
#         # e non sono stati inseriti, segnaliamo un errore
#         if any(x in st.session_state.selected_interventions for x in range(1, 7)):
#             # Modelli EN possibili => verifichiamo i campi
#             if "EP_GL_NREN" not in input_data or "CLASSE_ENERGETICA" not in input_data:
#                 st.error("EP_GL_NREN and/or CLASSE_ENERGETICA are required for the energy class prediction.")
#                 st.stop()

#         # Eseguiamo la predizione per ogni intervento
#         for intervention_type in st.session_state.selected_interventions:
#             try:
#                 # 1) Prima predizione: NM_EP_GL_NREN_RAGGIUNG_n
#                 risultato = predizione_intervento(input_data.copy(), intervention_type)
#                 mae = mae_dict.get(intervention_type, 28.0)  # default di sicurezza

#                 lower_bound = max(risultato - mae, 0)  # Evita valori negativi
#                 upper_bound = risultato + mae

#                 delta = None
#                 if "EP_GL_NREN" in needed_fields and "EP_GL_NREN" in input_data:
#                     delta = input_data["EP_GL_NREN"] - risultato

#                 # ### Creiamo subito le tre colonne
#                 col1, col2 = st.columns(2)

#                 # ### Nella col1 mostriamo la prima predizione e il suo delta
#                 with col1:
#                     st.success(
#                         f"**Intervention {intervention_type}**\n\n"
#                         f"Predicted EP_GL_NREN:\n"
#                         f"**{risultato:.2f}** kWh/m²·year\n"
#                         #f"MAE: ±{mae:.2f} kWh/m²·year"
#                     )
#                     if delta is not None:
#                         st.metric(
#                             label="Mean case delta",
#                             value=f"{risultato:.2f}",
#                             delta=f"{delta:.2f}",
#                             delta_color="normal"
#                         )

#                 # 2) Seconda predizione => nuova classe energetica
#                 #    Solo se i modelli EN e i campi EP_GL_NREN + CLASSE_ENERGETICA
#                 #    sono effettivamente disponibili
#                 if "EP_GL_NREN" in input_data and "CLASSE_ENERGETICA" in input_data:
#                     new_class = predizione_classe_energetica(
#                         nm_ep_gl_nren_raggiung=risultato,
#                         ep_gl_nren=input_data["EP_GL_NREN"],
#                         classe_energetica=input_data["CLASSE_ENERGETICA"],
#                         categoria=intervention_type
#                     )
                    
#                     # ### Nella col2 mostriamo la nuova classe energetica
#                     with col2:
#                         st.info(f"**Predicted new energy class:** {new_class + 1}")

#             except Exception as e:
#                 st.error(f"An error occurred during prediction for intervention {intervention_type}: {e}")

#NONA VERSIONE: con classe 7
import streamlit as st
import qrcode, io, os, pickle
import pandas as pd

# ------------------------ MODELLI ------------------------ #
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "models"))
models      = {i: pickle.load(open(os.path.join(MODELS_DIR, f"XGBoost_{i}.pkl"),     "rb")) for i in range(1,8)}
models_en   = {i: pickle.load(open(os.path.join(MODELS_DIR, f"XGBoost_EN_{i}.pkl"),  "rb")) for i in range(1,8)}

feature_sets = {
    1: ['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','RAPPORTO_SV',
        'SUPERFICIE_DISPERDENTE','Y_IE','VOLUME_LORDO_RISCALDATO'],
    2: ['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','RAPPORTO_SV',
        'SUPERFICIE_DISPERDENTE','Y_IE'],
    3: ['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','Y_IE',
        'RAPPORTO_SV','SUPERFICIE_DISPERDENTE'],
    4: ['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','Y_IE',
        'RAPPORTO_SV','EP_GL_REN','SUPERFICIE_DISPERDENTE'],
    5: ['EP_GL_NREN','EP_H_ND','RAPPORTO_SV','CLASSE_ENERGETICA',
        'EP_GL_REN','VOLUME_LORDO_RISCALDATO','Y_IE',
        'SUPERFICIE_DISPERDENTE','SUPERF_UTILE_RISCALDATA',
        'A_SOL_EST_A_SUP_UTILE','VOLUME_LORDO_RAFFRESCATO',
        'SUPERF_UTILE_RAFFRESCATA'],
    6: ['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','EP_GL_REN',
        'Y_IE','RAPPORTO_SV','SUPERFICIE_DISPERDENTE',
        'SUPERF_UTILE_RISCALDATA','VOLUME_LORDO_RISCALDATO',
        'A_SOL_EST_A_SUP_UTILE'],
    7: ['CLASSE_ENERGETICA','EP_GL_NREN','EP_GL_REN',
        'NM_EP_GL_NREN_RAGGIUNG_1','NM_EP_GL_NREN_RAGGIUNG_2',
        'NM_EP_GL_NREN_RAGGIUNG_3','NM_EP_GL_NREN_RAGGIUNG_4',
        'NM_EP_GL_NREN_RAGGIUNG_5','NM_EP_GL_NREN_RAGGIUNG_6',
        'SUPERFICIE_DISPERDENTE','RAPPORTO_SV','EP_H_ND','Y_IE'],
}

mae_dict = {1:28.25, 2:10.03, 3:18.83, 4:17.08, 5:13.06, 6:10.17, 7:5.55}

# ------------------------ FUNZIONI ------------------------ #
def predizione_intervento(data:dict, cat:int)->float:
    df = pd.DataFrame([{k:data[k] for k in feature_sets[cat] if k in data}])
    return float(models[cat].predict(df)[0])

def predizione_classe(nm, ep_att, cls_att, cat:int)->int:
    col = f"NM_EP_GL_NREN_RAGGIUNG_{cat}"
    df = pd.DataFrame([{col:nm,"CLASSE_ENERGETICA":cls_att,"EP_GL_NREN":ep_att}])
    df = df[models_en[cat].feature_names_in_]
    return int(models_en[cat].predict(df)[0])

def base_features(selected:list)->list:
    """Unione feature dei modelli selezionati + feature "utente" del modello 7"""
    base = set()
    for i in selected:
        base |= set(feature_sets[i])
    # aggiungo le feature 'generali' del 7 (tutte tranne le NM_EP_*)
    base |= {f for f in feature_sets[7] if not f.startswith("NM_EP_")}
    return sorted(base)

# ------------------------ UI ------------------------ #
st.set_page_config("ENERGY EFFICIENCY TOOL","wide")
col_main,col_right = st.columns([4,1])
with col_main:
    st.title("ENERGY EFFICIENCY TOOL")
    st.write("**⚠️ Valido solo per edifici in Lombardia – zona E – categoria E.1**")
with col_right:
    with st.expander("🔳 QR Code"):
        buf=io.BytesIO(); qrcode.make("https://energy-efficiency-tool-uhca9wtuujygnendua7ljl.streamlit.app/").save(buf)
        st.image(buf.getvalue(),use_column_width=True)

if "selected" not in st.session_state: st.session_state.selected=[]

# --- scelta interventi --- #
with st.form("choose"):
    st.subheader("Seleziona intervento/i")
    tmp=[]
    labels={1:"1 – Involucro opaco",2:"2 – Involucro trasparente",3:"3 – Imp. riscaldamento",
            4:"4 – Imp. raffrescamento",5:"5 – Fonti rinnovabili",6:"6 – Altri interventi"}
    for i,text in labels.items():
        if st.checkbox(text,value=(i in st.session_state.selected)): tmp.append(i)
    ok=st.form_submit_button("Conferma")
if ok:
    st.session_state.selected=tmp
    if not tmp: st.error("Seleziona almeno un intervento")

sel=st.session_state.selected
if sel:
    # -------- input edificio -------- #
    required=base_features(sel)
    with st.form("building"):
        st.subheader("Dati edificio richiesti")
        data={}
        # blocco campi in modo semplice
        def num(label): return st.number_input(label,min_value=0.0)
        if "EP_GL_NREN"              in required: data["EP_GL_NREN"]=num("EP_GL_NREN (kWh/m²·anno)")
        if "EP_GL_REN"               in required: data["EP_GL_REN"]=num("EP_GL_REN (kWh/m²·anno)")
        if "EP_H_ND"                 in required: data["EP_H_ND"]=num("EP_H_ND (kWh/m²·anno)")
        if "CLASSE_ENERGETICA"       in required:
            data["CLASSE_ENERGETICA"]=st.selectbox("Classe (1=A4 … 10=G)",list(range(1,11)))-1
        if "RAPPORTO_SV"             in required: data["RAPPORTO_SV"]=num("S/V ratio")
        if "SUPERFICIE_DISPERDENTE"  in required: data["SUPERFICIE_DISPERDENTE"]=num("Superficie disperdente (m²)")
        if "Y_IE"                    in required: data["Y_IE"]=num("Y_IE")
        if "VOLUME_LORDO_RISCALDATO" in required: data["VOLUME_LORDO_RISCALDATO"]=num("Vol. lordo riscaldato (m³)")
        if "SUPERF_UTILE_RISCALDATA" in required: data["SUPERF_UTILE_RISCALDATA"]=num("Sup. utile riscaldata (m²)")
        if "A_SOL_EST_A_SUP_UTILE"   in required: data["A_SOL_EST_A_SUP_UTILE"]=num("Rapporto area solare/utile")
        if "VOLUME_LORDO_RAFFRESCATO" in required:data["VOLUME_LORDO_RAFFRESCATO"]=num("Vol. lordo raffrescato (m³)")
        if "SUPERF_UTILE_RAFFRESCATA" in required:data["SUPERF_UTILE_RAFFRESCATA"]=num("Sup. utile raffrescata (m²)")
        calc=st.form_submit_button("Calcola")

    if calc:
        # check minimi
        need=["EP_GL_NREN","CLASSE_ENERGETICA"]
        if any(n in required for n in need) and any(n not in data for n in need):
            st.error("Sono obbligatori EP_GL_NREN e Classe energetica")
            st.stop()

        try:
            # ---------- predizioni singole ---------- #
            single_preds={}
            for i in sel:
                single_preds[i]=predizione_intervento(data.copy(),i)

            # ---------- predizione combinata ---------- #
            if len(sel)>1:
                nm_inputs={f"NM_EP_GL_NREN_RAGGIUNG_{k}":single_preds.get(k,0.0) for k in range(1,7)}
                comb_in={**{f:data.get(f,0.0) for f in feature_sets[7] if not f.startswith("NM_EP_")},**nm_inputs}
                combined=predizione_intervento(comb_in,7)
            else:
                combined=list(single_preds.values())[0]  # unico intervento

            # ---------- output ---------- #
            if len(sel)>1:
                st.subheader("Predizioni singole")
                for i,val in single_preds.items():
                    st.metric(f"Intervento {i}",f"{val:.2f} kWh/m²·anno")

            mae=mae_dict[7 if len(sel)>1 else sel[0]]
            low=max(combined-mae,0); up=combined+mae
            delta=data.get("EP_GL_NREN",0)-combined if "EP_GL_NREN" in data else None

            st.subheader("Risultato combinato" if len(sel)>1 else "Risultato")
            st.success(f"EP_GL_NREN previsto: {combined:.2f} kWh/m²·anno")
            st.write(f"Intervallo ± MAE: [{low:.2f}, {up:.2f}]")
            if delta is not None: st.metric("Delta vs attuale",f"{delta:+.2f}")

            # classe energetica
            if {"EP_GL_NREN","CLASSE_ENERGETICA"}<=data.keys():
                cat=7 if len(sel)>1 else sel[0]
                new_cls=predizione_classe(combined,data["EP_GL_NREN"],data["CLASSE_ENERGETICA"],cat)
                st.info(f"Nuova classe energetica: {new_cls+1}")

        except Exception as e:
            st.error(f"Errore durante la predizione: {e}")
