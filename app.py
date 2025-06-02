### XGreen Code

#[1] Import libraries and configure Streamlit page

import streamlit as st, qrcode, io, os, pickle
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(
     page_title="XGreen – Building Retrofit Impact AI-Based Predictor", 
     layout="wide",
     initial_sidebar_state="collapsed"
)

#[2] Custom CSS to adjust metric font-size in sidebar

st.markdown(
    """
    <style>
    /* ridimensiona SOLO i metric che stanno nella sidebar */
    section[data-testid="stSidebar"] div[data-testid="stMetricValue"] {
        font-size: 0.9rem;     /* valore principale  (default ≃1.25rem) */
    }
    </style>
    """,
    unsafe_allow_html=True
)

#[3] Load pre-trained models from disk 

MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "models"))
models     = {i: pickle.load(open(os.path.join(MODELS_DIR,f"XGBoost_{i}.pkl"),"rb"))  for i in range(1,8)}
models_en  = {i: pickle.load(open(os.path.join(MODELS_DIR,f"XGBoost_EN_{i}.pkl"),"rb"))for i in range(1,8)}

#[4] Define feature sets and performance metrics

feature_sets = {
    1:['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','RAPPORTO_SV',
       'SUPERFICIE_DISPERDENTE','Y_IE','VOLUME_LORDO_RISCALDATO'],
    2:['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','RAPPORTO_SV',
       'SUPERFICIE_DISPERDENTE','Y_IE'],
    3:['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','Y_IE',
       'RAPPORTO_SV','SUPERFICIE_DISPERDENTE'],
    4:['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','Y_IE',
       'RAPPORTO_SV','EP_GL_REN','SUPERFICIE_DISPERDENTE'],
    5:['EP_GL_NREN','EP_H_ND','RAPPORTO_SV','CLASSE_ENERGETICA',
       'EP_GL_REN','VOLUME_LORDO_RISCALDATO','Y_IE',
       'SUPERFICIE_DISPERDENTE','SUPERF_UTILE_RISCALDATA',
       'A_SOL_EST_A_SUP_UTILE','VOLUME_LORDO_RAFFRESCATO',
       'SUPERF_UTILE_RAFFRESCATA'],
    6:['EP_GL_NREN','EP_H_ND','CLASSE_ENERGETICA','EP_GL_REN',
       'Y_IE','RAPPORTO_SV','SUPERFICIE_DISPERDENTE',
       'SUPERF_UTILE_RISCALDATA','VOLUME_LORDO_RISCALDATO',
       'A_SOL_EST_A_SUP_UTILE'],
    7:['CLASSE_ENERGETICA','EP_GL_NREN','EP_GL_REN',
       'NM_EP_GL_NREN_RAGGIUNG_1','DS_CLASSE_RAGGIUNGIBILE_1',
       'NM_EP_GL_NREN_RAGGIUNG_2','DS_CLASSE_RAGGIUNGIBILE_2',
       'NM_EP_GL_NREN_RAGGIUNG_3','DS_CLASSE_RAGGIUNGIBILE_3',
       'NM_EP_GL_NREN_RAGGIUNG_4','DS_CLASSE_RAGGIUNGIBILE_4',
       'NM_EP_GL_NREN_RAGGIUNG_5','DS_CLASSE_RAGGIUNGIBILE_5',
       'NM_EP_GL_NREN_RAGGIUNG_6','DS_CLASSE_RAGGIUNGIBILE_6',
       'NM_EP_GL_NREN_RAGGIUNG_7','DS_CLASSE_RAGGIUNGIBILE_7',
       'SUPERFICIE_DISPERDENTE','RAPPORTO_SV','EP_H_ND','Y_IE']
}
mae_dict={1:28.25,
          2:10.03,
          3:18.83,
          4:17.08,
          5:13.06,
          6:10.17,
          7:5.55
}
accuracy_en={1:69.04,
             2:73.25,
             3:75.80,
             4:64.48,
             5:69.47,
             6:78.05,
             7:88.30
}

# [5] Define numeric limits for each feature in each model

feature_limits = {
    1: {'EP_GL_NREN': (0.66, 579.51), 
        'EP_H_ND': ( 0.01, 345.62), 
        'Y_IE': (0.00, 164.42),
        'RAPPORTO_SV': ( 0.00, 1.56), 
        'SUPERFICIE_DISPERDENTE': ( 0.01, 447.28),
        'VOLUME_LORDO_RISCALDATO': (5.83, 2450.00), 
        'CLASSE_ENERGETICA': (1.00, 10.00)},
    2: {'EP_GL_NREN':( 1.11, 579.62),
        'EP_H_ND':(0.02, 345.62),
        'CLASSE_ENERGETICA':(1.00, 10.00),
        'RAPPORTO_SV':(0.01, 1.55),
        'SUPERFICIE_DISPERDENTE':(3.24, 447.28),
        'Y_IE':(0.00, 160.76)},
    3:  {'EP_GL_NREN': (0.44, 579.57),
        'EP_H_ND': (0.34, 345.58),
        'CLASSE_ENERGETICA': (1.00, 10.00),
        'Y_IE': (0.00, 166.86),
        'RAPPORTO_SV': (0.00, 1.55),
        'SUPERFICIE_DISPERDENTE': (0.10, 447.27)},
    4:  {'EP_GL_NREN': (2.96, 572.57),
        'EP_H_ND': (1.12, 342.31),
        'CLASSE_ENERGETICA': (1.00, 10.00),
        'Y_IE': (0.00, 81.97),
        'RAPPORTO_SV': (0.03, 1.22),
        'EP_GL_REN': (0.00, 146.59),
        'SUPERFICIE_DISPERDENTE': (3.00, 444.68)},
    5:  {'EP_GL_NREN': (3.65, 579.58),
        'EP_H_ND': (0.06, 334.75),
        'RAPPORTO_SV': (0.06, 1.43),
        'CLASSE_ENERGETICA': (1.00, 10.00),
        'EP_GL_REN': (0.00, 150.55),
        'VOLUME_LORDO_RISCALDATO': (24.82, 1030.40),
        'Y_IE': (0.00, 159.60),
        'SUPERFICIE_DISPERDENTE': (9.42, 445.81),
        'SUPERF_UTILE_RISCALDATA': (5.04, 254.46),
        'A_SOL_EST_A_SUP_UTILE': (0.00, 0.11),
        'VOLUME_LORDO_RAFFRESCATO': (0.00, 945.39),
        'SUPERF_UTILE_RAFFRESCATA': (0.00, 254.46)},   
    6:  {'EP_GL_NREN': (1.83, 578.89),
        'EP_H_ND': (0.01, 345.20),
        'CLASSE_ENERGETICA': (1.00, 10.00),
        'EP_GL_REN': (0.00, 152.21),
        'Y_IE': (0.00, 124.24),
        'RAPPORTO_SV': (0.00, 1.56),
        'SUPERFICIE_DISPERDENTE': (0.08, 447.28),
        'SUPERF_UTILE_RISCALDATA': (2.62, 408.00),
        'VOLUME_LORDO_RISCALDATO': (14.02, 1722.55),
        'A_SOL_EST_A_SUP_UTILE': (0.00, 0.11)}, 
    7:  {'CLASSE_ENERGETICA': (1.00, 10.00),
        'EP_GL_NREN': (1.84, 579.58),
        'EP_GL_REN': (0.00, 152.29),
        'NM_EP_GL_NREN_RAGGIUNG_1': (0.00, 565.66),
        'NM_EP_GL_NREN_RAGGIUNG_2': (0.00, 569.74),
        'NM_EP_GL_NREN_RAGGIUNG_3': (0.00, 569.87),
        'NM_EP_GL_NREN_RAGGIUNG_4': (0.00, 561.46),
        'NM_EP_GL_NREN_RAGGIUNG_5': (0.00, 570.21),
        'NM_EP_GL_NREN_RAGGIUNG_6': (0.00, 567.96),
        'SUPERFICIE_DISPERDENTE': (4.30, 447.28),
        'RAPPORTO_SV': (0.01, 1.56),
        'EP_H_ND': (0.06, 345.62),
        'Y_IE': (0.00, 169.62)}   
        }

feature_limits_en = {
    1: {'NM_EP_GL_NREN_RAGGIUNG_1': (0.21, 578.48),
        'EP_GL_NREN': (0.66, 579.51)},
    2: {'NM_EP_GL_NREN_RAGGIUNG_2': (0.18, 575.55),
        'EP_GL_NREN': (1.11, 579.62)},
    3: {'NM_EP_GL_NREN_RAGGIUNG_3': (0.05, 575.28),
        'EP_GL_NREN': (1.11, 579.57)},
    4: {'NM_EP_GL_NREN_RAGGIUNG_4': (0.40, 562.92),
        'EP_GL_NREN': (2.96, 572.57)},
    5: {'NM_EP_GL_NREN_RAGGIUNG_5': (0.37, 570.21),
        'EP_GL_NREN': (3.65, 579.58)},
    6: {'NM_EP_GL_NREN_RAGGIUNG_6': (0.01, 569.23),
        'EP_GL_NREN': (1.83, 578.89)},
    7: {'CLASSE_ENERGETICA': (1.00, 10.00),
        'EP_GL_NREN': (1.84, 579.58),
        'EP_GL_REN': (0.00, 152.29),
        'DS_CLASSE_RAGGIUNGIBILE_1': (0.00, 10.00),
        'NM_EP_GL_NREN_RAGGIUNG_1': (0.00, 565.66),
        'DS_CLASSE_RAGGIUNGIBILE_2': (0.00, 10.00),
        'NM_EP_GL_NREN_RAGGIUNG_2': (0.00, 569.74),
        'DS_CLASSE_RAGGIUNGIBILE_3': (0.00, 10.00),
        'NM_EP_GL_NREN_RAGGIUNG_3': (0.00, 569.87),
        'DS_CLASSE_RAGGIUNGIBILE_4': (0.00, 10.00),
        'NM_EP_GL_NREN_RAGGIUNG_4': (0.00, 561.46),
        'DS_CLASSE_RAGGIUNGIBILE_5': (0.00, 10.00),
        'NM_EP_GL_NREN_RAGGIUNG_5': (0.00, 570.21),
        'DS_CLASSE_RAGGIUNGIBILE_6': (0.00, 10.00),
        'NM_EP_GL_NREN_RAGGIUNG_6': (0.00, 567.96),
        'NM_EP_GL_NREN_RAGGIUNG_7': (0.02, 579.33),
        'SUPERFICIE_DISPERDENTE': (4.30, 447.28),
        'RAPPORTO_SV': (0.01, 1.56),
        'EP_H_ND': (0.06, 345.62),
        'Y_IE': (0.00, 169.62)}
        }

def compute_agg_limits(sel):
    """Restituisce {feature: (min_agg, max_agg)} per l’intersezione 
    di tutti i modelli in sel, e – se >1 intervento – include anche 
    i vincoli di feature_limits[7] e feature_limits_en[7]."""
    agg = {}

    feats = union_features(sel)
    for f in feats:
        mins = [feature_limits[i][f][0] for i in sel if f in feature_limits[i]]
        maxs = [feature_limits[i][f][1] for i in sel if f in feature_limits[i]]
        if not mins or not maxs:
            continue
        vmin, vmax = max(mins), min(maxs)
        if vmin > vmax:
            st.error(
                f"Nessun valore possibile per {f}: "
                f"intervalli incompatibili "
                f"{[(i, feature_limits[i][f]) for i in sel if f in feature_limits[i]]}"
            )
            st.stop()
        agg[f] = (vmin, vmax)

    if len(sel) > 1:
        for f, (mn7, mx7) in feature_limits[7].items():
            if f in agg:
                vmin, vmax = agg[f]
                agg[f] = (max(vmin, mn7), min(vmax, mx7))
            else:
                agg[f] = (mn7, mx7)
            vmin2, vmax2 = agg[f]
            if vmin2 > vmax2:
                st.error(
                    f"Nessun valore possibile per {f} "
                    f"dopo unione con feature_limits[7]: "
                    f"[{vmin2:.2f}, {vmax2:.2f}]"
                )
                st.stop()

        for f, (mn7e, mx7e) in feature_limits_en[7].items():
            if f in agg:
                vmin, vmax = agg[f]
                agg[f] = (max(vmin, mn7e), min(vmax, mx7e))
            else:
                agg[f] = (mn7e, mx7e)
            vmin3, vmax3 = agg[f]
            if vmin3 > vmax3:
                st.error(
                    f"Nessun valore possibile per {f} "
                    f"dopo unione con feature_limits_en[7]: "
                    f"[{vmin3:.2f}, {vmax3:.2f}]"
                )
                st.stop()

    return agg

IMG_DIR = "static"
IMG_PATTERN_1 = "mae_{i}.png"
IMG_PATTERN_2 = "acc_{i}.png"
IMG_PATTERN_3 = "sp_{i}.png"
IMG_PATTERN_4 = "cm_{i}.png"

# [6] Sidebar: Show model performance metrics in expanders

with st.sidebar:
    with st.expander("Performance of XGBoost Regressor on Post-Intervention EP_GL_NREN Prediction", expanded=True):
        tabs = st.tabs([str(i) for i in range(1, 8)])

        for i, tab in enumerate(tabs, start=1):
            with tab:
                st.metric(
                    label=f"MAE Intervention {i}",
                    value=f"± {mae_dict[i]:.2f} kWh/m²·year",
                )

                img_path = os.path.join(IMG_DIR, IMG_PATTERN_1.format(i=i))
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.info(f"Add image: {img_path}")

                img_path = os.path.join(IMG_DIR, IMG_PATTERN_3.format(i=i))
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.info(f"Add image: {img_path}")

    with st.expander("Performance of XGBoost Classifier on Post-Intervention Energy Class Prediction", expanded=True):
        tabs = st.tabs([str(i) for i in range(1, 8)])

        for i, tab in enumerate(tabs, start=1):
            with tab:
                st.metric(
                    label=f"Accuracy Intervention {i}",
                    value=f"{accuracy_en[i]:.2f} %",
                )

                img_path = os.path.join(IMG_DIR, IMG_PATTERN_2.format(i=i))
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.info(f"Add image: {img_path}")
                
                img_path = os.path.join(IMG_DIR, IMG_PATTERN_4.format(i=i))
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.info(f"Add image: {img_path}")

# [7] Define prediction helper functions

def pred_NM(data,cat):
    df=pd.DataFrame([{k:data[k] for k in feature_sets[cat] if k in data}])
    return float(models[cat].predict(df)[0])

def pred_DS(nm,ep0,cls0,cat):
    col=f"NM_EP_GL_NREN_RAGGIUNG_{cat}"
    df=pd.DataFrame([{col:nm,"CLASSE_ENERGETICA":cls0,"EP_GL_NREN":ep0}])
    df=df[models_en[cat].feature_names_in_]
    return int(models_en[cat].predict(df)[0])

def union_features(selected):
    base=set()
    for i in selected: base|=set(feature_sets[i])
    base|={f for f in feature_sets[7] if not f.startswith(("NM_","DS_"))}
    return sorted(base)

# [8] Main UI layout: Title and description

c1,c2=st.columns([4,1])
with c1: 
    st.title("XGreen - Building Retrofit Impact AI-Based Predictor")
    st.markdown("""
    **⚠️ This tool is valid only for buildings located in the Lombardy region, within climate zone E, belonging to category E.1, with a gross floor area below 700 m² and with a gross volume below 2450 m³ :**
    - E.1(1): Buildings used as permanent residences (e.g., apartment buildings)
    - E.1(2): Buildings used as non-permanent residences (e.g., holiday homes)
    - E.1(3): Other residential buildings (e.g., student or worker residences)

    ⚠️ Make sure your building meets **all** of these criteria before proceeding.
                
    
    Visualization of the dataset:     

    """)

    # [9] Display two heatmap expanders side by side

    col_map1, col_map2 = st.columns(2)

    with col_map1.expander("EP_GL_NREN – 1 % Sample", expanded=False):
        html_path = os.path.join(
            os.path.dirname(__file__),
            "static",
            "Heatmap_EP_GL_NREN.html"
        )
        if os.path.exists(html_path):
            with open(html_path, "r", encoding="utf-8") as f:
                components.html(f.read(), height=500, scrolling=True)
        else:
            st.error(f"File non trovato: {html_path}")

    with col_map2.expander("Energy Class – 1 % Sample", expanded=False):
        html_path = os.path.join(
            os.path.dirname(__file__),
            "static",
            "Heatmap_CLASSE.html"
        )
        if os.path.exists(html_path):
            with open(html_path, "r", encoding="utf-8") as f:
                components.html(f.read(), height=500, scrolling=True)
        else:
            st.error(f"File non trovato: {html_path}")

    st.markdown("""
    Fill in the fields below to estimate the impact of an energy-efficiency intervention on the building.
    """)
                
with c2:
    # [10] Display QR code expander
    with st.expander("🔳 QR Code"):
        buf=io.BytesIO(); qrcode.make("https://energy-efficiency-tool-project-management.streamlit.app/").save(buf)
        st.image(buf.getvalue(), use_container_width=True
        )

# [11] Intervention selection form

if "sel" not in st.session_state: st.session_state.sel=[]

with st.form("pick"):
    st.subheader("Select intervention")
    tmp=[]
    lbl={1:"1 - Opaque envelope",2:"2 - Transparent envelope",3:"3 - Heating system",
         4:"4 - Cooling system",5:"5 - Renewable sources",6:"6 - Other intervention"}
    for i,t in lbl.items():
        if st.checkbox(t,value=(i in st.session_state.sel)): tmp.append(i)
    if st.form_submit_button("Confirm"): st.session_state.sel=tmp

sel = st.session_state.sel
if sel:
     # [12] Compute aggregated feature limits based on selection
    agg_limits = compute_agg_limits(sel)

    with st.form("bld"):
        st.subheader("Building data")
        d = {}

        def num(label, hint, feat):
            vmin, vmax = agg_limits.get(feat, (0.0, None))
            full_hint = (
                f"{hint} (min: {vmin:.2f}, max: {vmax:.2f})"
                if vmax is not None else
                hint
            )
            return st.number_input(
                label, min_value=vmin, max_value=vmax,
                value=vmin, help=full_hint
            )
        
        # [13] Input fields for building features

        if "EP_GL_NREN" in agg_limits:
            d["EP_GL_NREN"] = num(
                "EP_GL_NREN (kWh/m²·year)",
                "Non‑renewable global energy performance index (kWh/m²·year)",
                feat="EP_GL_NREN"
            )

        if "EP_GL_REN" in agg_limits:
            d["EP_GL_REN"] = num(
                "EP_GL_REN (kWh/m²·year)",
                "Renewable global energy performance index (kWh/m²·year)",
                feat="EP_GL_REN"
            )

        if "EP_H_ND" in agg_limits:
            d["EP_H_ND"] = num(
                "EP_H_ND (kWh/m²·year)",
                "Thermal energy demand for heating (kWh/m²·year)",
                feat="EP_H_ND"
            )

        if "CLASSE_ENERGETICA" in agg_limits:
            energy_labels = ["A4", "A3", "A2", "A1", "B", "C", "D", "E", "F", "G"]
            choice = st.selectbox(
                "Energy class",
                energy_labels,
                index=0,
                help="Current energy class of the building"
            )
            d["CLASSE_ENERGETICA"] = energy_labels.index(choice)

        if "RAPPORTO_SV" in agg_limits:
            d["RAPPORTO_SV"] = num(
                "S/V ratio (1/m)",
                "Ratio between heat‑loss surface and heated volume (1/m)",
                feat="RAPPORTO_SV"
            )

        if "SUPERFICIE_DISPERDENTE" in agg_limits:
            d["SUPERFICIE_DISPERDENTE"] = num(
                "Dispersing surface (m²)",
                "Total surface area of the energy‑dispersing envelope (m²)",
                feat="SUPERFICIE_DISPERDENTE"
            )

        if "Y_IE" in agg_limits:
            d["Y_IE"] = num(
                "Y_IE (W/m²·K)",
                "Periodic thermal transmittance (W/m²·K)",
                feat="Y_IE"
            )

        if "VOLUME_LORDO_RISCALDATO" in agg_limits:
            d["VOLUME_LORDO_RISCALDATO"] = num(
                "Gross heated volume (m³)",
                "Gross heated volume (m³)",
                feat="VOLUME_LORDO_RISCALDATO"
            )

        if "SUPERF_UTILE_RISCALDATA" in agg_limits:
            d["SUPERF_UTILE_RISCALDATA"] = num(
                "Heated useful area (m²)",
                "Heated useful floor area of the building (m²)",
                feat="SUPERF_UTILE_RISCALDATA"
            )

        if "A_SOL_EST_A_SUP_UTILE" in agg_limits:
            d["A_SOL_EST_A_SUP_UTILE"] = num(
                "Summer equivalent solar area/unit of useful surface",
                "Summer equivalent solar area per unit of useful surface",
                feat="A_SOL_EST_A_SUP_UTILE"
            )

        if "VOLUME_LORDO_RAFFRESCATO" in agg_limits:
            d["VOLUME_LORDO_RAFFRESCATO"] = num(
                "Gross cooled volume (m³)",
                "Gross cooled volume (m³)",
                feat="VOLUME_LORDO_RAFFRESCATO"
            )

        if "SUPERF_UTILE_RAFFRESCATA" in agg_limits:
            d["SUPERF_UTILE_RAFFRESCATA"] = num(
                "Cooled useful area (m²)",
                "Cooled useful floor area of the building (m²)",
                feat="SUPERF_UTILE_RAFFRESCATA"
            )

        go = st.form_submit_button("Run calculation")

        # [14] Validate inputs against limits

        for feat, val in d.items():
            if feat in agg_limits:
                vmin, vmax = agg_limits[feat]
                check_val = val + 1 if feat == "CLASSE_ENERGETICA" else val
                if not (vmin <= check_val <= vmax):
                    st.error(
                        f"Value `{feat}` = {check_val:.2f} out of range "
                        f"[{vmin:.2f}, {vmax:.2f}]. Unable to calculate."
                    )
                    st.stop()

        # [15] Ensure required fields are present

        if {"EP_GL_NREN","CLASSE_ENERGETICA"}-d.keys():
            st.error("EP_GL_NREN and Energy class are required."); st.stop()

        try:
            # [16] Run individual and combined predictions
            nm_sing = {i: pred_NM(d, i) for i in sel}

            for i in sel:
                emin, emax = feature_limits_en[i]['EP_GL_NREN']
                ep0 = d["EP_GL_NREN"]
                if not (emin <= ep0 <= emax):
                    st.error(
                        f"EP_GL_NREN = {ep0:.2f} out of range "
                        f"[{emin:.2f}, {emax:.2f}] required by EN_{i}"
                    )
                    st.stop()

                fnm = f"NM_EP_GL_NREN_RAGGIUNG_{i}"
                nmin, nmax = feature_limits_en[i][fnm]
                nm_val = nm_sing[i]
                if not (nmin <= nm_val <= nmax):
                    st.error(
                        f"{fnm} = {nm_val:.2f} out of range "
                        f"[{nmin:.2f}, {nmax:.2f}] required by EN_{i}"
                    )
                    st.stop()

            ds_sing = {
                i: pred_DS(nm_sing[i], d["EP_GL_NREN"], d["CLASSE_ENERGETICA"], i)
                for i in sel
            }

            for i in sel:

                if nm_sing[i] > d["EP_GL_NREN"]:
                    st.error(
                        f"Predicted EP_GL_NREN for intervention {i} "
                        f"({nm_sing[i]:.2f}) exceeds initial value "
                        f"({d['EP_GL_NREN']:.2f})."
                    )
                    st.stop()

                if ds_sing[i] > d["CLASSE_ENERGETICA"]:
                    st.error(
                        f"Predicted energy class for intervention {i} "
                        f"({ds_sing[i] + 1}) is worse than initial "
                        f"({d['CLASSE_ENERGETICA'] + 1})."
                    )
                    st.stop()

            if len(sel) > 1:

                comb_base = {
                    f: d.get(f, 0.0)
                    for f in feature_sets[7]
                    if not f.startswith(("NM_", "DS_"))
                }
                nm_input = {
                    f"NM_EP_GL_NREN_RAGGIUNG_{k}": nm_sing.get(k, 0.0)
                    for k in range(1, 7)
                }
                nm7 = pred_NM({**comb_base, **nm_input}, 7)
            else:
                nm7 = next(iter(nm_sing.values()))

            if len(sel) > 1:
                ds_input = {
                    f"DS_CLASSE_RAGGIUNGIBILE_{k}": ds_sing.get(k, 0)
                    for k in range(1, 7)
                }
                nm_input2 = {
                    f"NM_EP_GL_NREN_RAGGIUNG_{k}": nm_sing.get(k, 0.0)
                    for k in range(1, 7)
                }
                full = {
                    **comb_base,
                    **nm_input2,
                    **ds_input,
                    "NM_EP_GL_NREN_RAGGIUNG_7": nm7
                }

                for feat, (mn, mx) in feature_limits_en[7].items():
                    if feat not in full:
                        continue
                    val = full[feat]
                    if not (mn <= val <= mx):
                        st.error(
                            f"Input `{feat}` per EN_7 = {val:.2f} "
                            f"out of [{mn:.2f}, {mx:.2f}]."
                        )
                        st.stop()

                f_order = models_en[7].feature_names_in_
                df7 = pd.DataFrame([{f: full.get(f, 0.0) for f in f_order}])
                ds7 = int(models_en[7].predict(df7)[0])
            else:
                ds7 = next(iter(ds_sing.values()))

            if nm7 > d["EP_GL_NREN"]:
                st.error(
                    f"Predicted combined EP_GL_NREN ({nm7:.2f}) exceeds "
                    f"initial ({d['EP_GL_NREN']:.2f})."
                )
                st.stop()
            if ds7 > d["CLASSE_ENERGETICA"]:
                st.error(
                    f"Predicted combined energy class ({ds7 + 1}) is worse "
                    f"than initial ({d['CLASSE_ENERGETICA'] + 1})."
                )
                st.stop()

            # [17] Render results in tabs
            energy_labels = ["A4", "A3", "A2", "A1", "B", "C", "D", "E", "F", "G"]

            tabs = st.tabs(
                [f"Intervention {i}" for i in sel] +
                (["Combined"] if len(sel) > 1 else [])
            )

            for idx, i in enumerate(sel):
                with tabs[idx]:
                    st.metric(
                        "EP_GL_NREN achievable (kWh/m²·year)",
                        f"{nm_sing[i]:.2f}"
                    )
                    st.metric(
                        "Energy class achievable",
                        energy_labels[ds_sing[i]]
                    )

            if len(sel) > 1:
                with tabs[-1]:
                    st.metric(
                        "EP_GL_NREN achievable (kWh/m²·year)",
                        f"{nm7:.2f}"
                    )
                    st.metric(
                        "Energy class achievable",
                        energy_labels[ds7]   
                    )

        except Exception as e:
                st.error(f"Error: {e}")