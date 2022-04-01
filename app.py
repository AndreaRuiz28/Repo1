import streamlit as st 
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Escudo_UACH.svg/1200px-Escudo_UACH.svg.png",width=250)
st.sidebar.header("UDA:INTRODUCCIÓN AL MACHINE LEARNING")
st.sidebar.write("""
Integrantes:

* Andrea Chavez Mendez 348990

* Kenneth Porras Romero 349085

* Hugo Iván Gutiérrez Acevedo 349149

* Andrea Ruiz Villalba 349164

* Denisse Arely Vazquez Delgado 349269

""")

st.markdown("<h1 style='text-align: center; color: red;'>IDENTIFICACIÓN DE BACTERIAS</h1>", unsafe_allow_html=True)
st.title("")
st.title("Staphyloccocus-Streptococcus")
st.write("Carga la imagen de tu bacteria")
st.image("https://www.materialdelaboratorio.top/wp-content/uploads/2019/09/Agarplate_redbloodcells_edit-1024x649.jpg")

uploaded_file = st.file_uploader("Coloca una imagen de una de las 3 bacterias, debe de ser una imagen tipo jpg ...", type="jpg")
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption='Uploaded pic.', use_column_width=True)
  st.write("")
  st.write("Clasificando...")
  label = teachable_machine_classification(image, 'keras_model.h5') # Name of the model from Teachablemachine
  if label == 0:
    st.markdown("<h1 style='text-align: center; color: yellow;'>Es una Sthapyloccocus</h1>", unsafe_allow_html=True)
    st.title("Familia")
    st.write("Staphylococcaceae")
    st.title("Patogénesis")
    st.write("Puede causar Neumonía, endocarditis y osteomielitis, forúnculos, impétigo")
    st.title("¿En dónde se encuentra?")
    st.write("Staphylococcus aureus es una bacteria muy resistente en el medio ambiente y ampliamente distribuida en la naturaleza que puede encontrarse en el aire, agua, residuos, maquinaria y superficies de la industria alimentaria, pero su principal reservorio son los animales y humanos, encontrándose en la piel, cabello, fosas nasales")
    st.title("Dominio")
    st.write("Bacteria")
    st.title("Cultivo en laboratorio")
    st.image("https://lh3.googleusercontent.com/proxy/RUlQ_supe2T_dl4kxF2lx-NORj7w364zR-hp3ByUflrJ6m584piHd80X5mEC_480KzQX9drzmSyklneC3O5qlzI86KzBDPG16JWl3BJfM0D1rkLhp8cSD2DL1NpUlZJHhRVp2hc6kd6sxg",width=200)
  if label == 1:
    st.markdown("<h1 style='text-align: center; color: blue;'>Es una Streptococcus</h1>", unsafe_allow_html=True)
    st.title("Familia")
    st.write("Streptococcaceae")
    st.title("Patogénesis")
    st.write("Dependiendo de la especie, puede ocasionar meningitis, neumonía, faringitis, amigdalitis, entre otras infecciones.")
    st.title("¿En dónde se encuentra?")
    st.write("Forman parte de la flora saprofita de la boca, piel, intestino y el tracto respiratorio superior de los humanos.")
    st.title("Dominio")
    st.write("Bacteria")
    st.title("Cultivo en laboratorio")
    st.image("https://images.clarin.com/2018/09/09/streptococcus-pyogenes-una-imagen-de___ryLGXIVum_285x290__1.jpg", width=200)
