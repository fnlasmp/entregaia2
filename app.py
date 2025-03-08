import streamlit as st
import streamlit.components.v1 as components
import random

def main():
    st.title("Chatbot de la Tienda de Donas")

    # Sidebar
    with st.sidebar:
        st.markdown("<h1 style='color: pink;'>Udonuts!</h1>", unsafe_allow_html=True)
        with st.expander("Sobre nosotros:", expanded=False):
            st.write("Somos una tienda de donas artesanal que ofrece una amplia variedad de sabores y diseños. Utilizamos ingredientes frescos y de alta calidad para crear donas deliciosas y únicas. ¡Visítanos y prueba nuestras creaciones!")

    # Chatbot logic (in Spanish)
    donut_bot = {
        "menu": "¡Tenemos una deliciosa selección de donas! Hoy, te recomiendo probar nuestra clásica dona glaseada, la decadente de chocolate o nuestra especial rellena de jalea. ¡También tenemos sabores de temporada!",
        "horario": "¡Estamos abiertos de 6am a 6pm todos los días! Perfecto para un capricho matutino o un placer por la tarde.",
        "ubicacion": "¡Estamos ubicados en 123 Main Street, Anytown! Visítanos para una experiencia dulce.",
        "ordenar": "¡Sí, puedes hacer un pedido a través de este chatbot! ¿Qué se te antoja hoy?",
        "ofertas": "¡Absolutamente! Hoy tenemos una oferta especial: ¡Compra una docena de donas y obtén un café gratis!",
        "recomienda una dona": "Te recomiendo nuestra dona de crema Boston, ¡es una de las favoritas de nuestros clientes!",
        "default": "Lo siento, no entiendo. Pero déjame recomendarte nuestra deliciosa dona glaseada, ¡es un clásico!"
    }

    def get_response(prompt):
        prompt = prompt.lower()
        if "menu" in prompt or "tipos de donas" in prompt:
            return donut_bot["menu"]
        elif "horario" in prompt or "cuando abren" in prompt:
            return donut_bot["horario"]
        elif "ubicacion" in prompt or "donde estan" in prompt:
            return donut_bot["ubicacion"]
        elif "ordenar" in prompt or "hacer un pedido" in prompt:
            return donut_bot["ordenar"]
        elif "ofertas" in prompt or "promociones" in prompt:
            return donut_bot["ofertas"]
        elif "recomienda" in prompt or "dona favorita" in prompt:
            return donut_bot["recomienda una dona"]
        else:
            return donut_bot["default"]

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Pregúntame cualquier cosa sobre nuestras donas!"):
        # Display user message in chat message container
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get chatbot response
        assistant_response = get_response(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})


if __name__ == "__main__":
    main()