
import streamlit as st
import random

st.set_page_config(page_title="Radar Mini", layout="centered")

st.title("🔎 Radar Mini")
st.markdown("Bem-vinda, Cris! Esse é o seu radar leve para jogos mais assertivos. ✨🎯")

plataformas = ["PGQ.BET", "U888.COM", "GG666.COM", "69K.COM", "AA123.COM", "AP777", "BR345.COM"]
jogos = ["Tigre da Fortuna", "Coelho da Fortuna", "Dinheiro Chegando", "Cobra", "Dragão", "Gemas", "Mania de Dinheiro"]

plataforma_selecionada = st.selectbox("🎮 Escolha a plataforma:", plataformas)
jogo_selecionado = st.selectbox("🕹️ Escolha o jogo:", jogos)

if st.button("🔍 Verificar momento"):
    resultado = random.choice(["🔥 Pode entrar!", "🕓 Frio agora, pare", "⏳ Aguarde observação"])
    st.success(f"{jogo_selecionado} na plataforma {plataforma_selecionada}: {resultado}")
