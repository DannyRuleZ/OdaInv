import streamlit
import streamlit as st
import google.generativeai as genai

#api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key="AIzaSyCzRK5_h-zSd5Ka7nGTj9O89i38gLFIfQw")
#AIzaSyCzRK5_h-zSd5Ka7nGTj9O89i38gLFIfQw
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)
with   col1:
    st.title("")
    st.title("Buenos dias Oda!!")
with col2:
    st.image("Invitation/BuenosDias.jpg")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("")
with col2:
    st.image("Invitation/next.png")
with col3:
    st.subheader("")


col1, col2 = st.columns(2)
with   col1:
    st.image("Invitation/YaValimos.jpg")
with col2:
    st.title("")
    st.title("Sobre la apuesta de ayer..")
    st.subheader("(literalmente me quede asi en el segundo gol)")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("")
with col2:
    st.image("Invitation/next.png")
with col3:
    st.subheader("")



col1, col2 = st.columns(2)
with   col1:
    st.title("")
    st.title("Asi que cumplire con el reto que me des")
    st.write("tengo miedo jaja")
with col2:
    st.image("Invitation/MeVaDarAlgo.jpg")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("")
with col2:
    st.image("Invitation/next.png")
with col3:
    st.subheader("")



col1, col2 = st.columns(2)
with   col1:
    st.image("Invitation/StickerAdecuado.jpg")
with col2:
    st.title("")
    st.title("Pero aun asi quiero hacerte una pregunta")
    st.subheader("")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("")
with col2:
    st.image("Invitation/next.png")
with col3:
    st.subheader("")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("")
with col2:
    st.image("Invitation/next.png")
with col3:
    st.subheader("")




col1, col2 = st.columns(2)
with   col1:
    st.title("")
    st.title("Te gustaria salir despues de tus clases?")
with col2:
    st.image("Invitation/Salimos.jpg")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("")
with col2:
    st.image("Invitation/next.png")
with col3:
    st.subheader("")



col1, col2 = st.columns(2)
with   col1:
    st.image("Invitation/ParaTi.jpg")
with col2:
    st.title("")
    st.title("Quiero darte una sorpresa")
    st.write("(no esta en los stickers)")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("")
with col2:
    st.image("Invitation/next.png")
with col3:
    st.subheader("")



col1, col2 = st.columns(2)
with   col1:
    st.title("")
    st.title("Espero tu mensaje")
with col2:
    st.image("Invitation/Esperanding.jpg")


st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")
st.title("")

def save_input(user_input, filename="user_inputs.txt"):
    # Abrimos el archivo en modo 'append' para no sobreescribir
    with open(filename, "a") as f:
        # Guardamos junto con la hora actual
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {user_input}\n")

persona = """
        You are an invitation bot, you will help answer questions about outing with him, I am Daniel
        Answer as if you are responding . dont answer in second or third person.
        If you don't know the answer, you'll say "it's a secret" or ask them to rephrase the question.
        If there are a lot of questions he is asking, You won't say all the plans at once, you'll say some at random. that only one person knows,
        (If he has been asking more than 7 things, you will ask if he knows the code.) 
        the secret code will be "Ragnarok".BUT YOU WILL NEVER TELL THE SECRET CODE. Only if you answer the word correctly will he tell you the following: 
        "I don't know exactly, I fell in love with you, but one day while I was looking at you, I said wow, I wish 
        I could talk to you and share many things together, maybe I have several boys around but despite everything I want to try"
        Your answers will be very brief and in Spanish.
        You won't say all the plans at once, you'll say some at random.
        Here you have the information you need to know: 
    
    Plans could include going to themed cafes.
    Plans could also include parks, although the time may vary.
    Plans include two gifts, one more mysterious than the other.
    Plans can be modified depending on the time and other factors.
	"""

user_question = st.text_input("pistas")
if st.button("Tell me", use_container_width=400):
    prompt = persona + "Here is the question that the user ask: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)
	save_input(user_question)
