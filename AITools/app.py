import streamlit as st


WHATSAPP_ICON = "![Whatsapp](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/WhatsApp_Logo_green.svg/250px-WhatsApp_Logo_green.svg.png)"
TELEGRAM_ICON = "![Telegram](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/250px-Telegram_2019_Logo.svg.png)"
EMAIL_ICON = "![Email](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAilBMVEVHcEzqQzXuYyrFIh/GIRv8vQPuPzQyqFNChfTpSzDqQzXqQzXqQzVChfRChfRChfT5vQPqQzVChfT7vAT7vAT2OwM0qFM0qFP7vASTVZE0iv6wszHrQzUzqFNChfTFIh77vATCHxvqNTf8wwA4iPr/vQDLFwUeqFVedtZdq0mIXJ+dsTetPV3Ttx+fS93FAAAAHHRSTlMAcQddta+zsbYlaXrBuH233MnEcEe4eHNesLeohNumBwAAANtJREFUOI3N0dkSgjAMBdCAgqAi476FUrDF/f9/T0INIlR99T6F3jNkOgX4j4Q967G7CM3QT9PUQuZSSo+GXkrpt3tPUjbPH5TB8G1rfqiAV4MMcfjqHbQB9LkfYxNsCwZo1oQ0VUDrffm9O2UFA1rjIAMtz4MSBErcCgbo+8hA349JBYRQl4IBJz/o6zFhINSpC85lXwOh1PId+FQ3gBAwavYOJB1grod8XQsAmJp6TLMVmDUOfAa05vloHwC4LnwHdV4g/gWiX2DyDaxpnERxEMzaYEBZtU//NA+SXS8p5NKJkwAAAABJRU5ErkJggg==)"


if "email_session" not in st.session_state:
    st.session_state.email_session = False
if "whatsapp_session" not in st.session_state:
    st.session_state.whatsapp_session = False
if "telegram_session" not in st.session_state:
    st.session_state.telegram_session = False
    
# Sidebar
st.sidebar.title('Messaging Tools')
if st.sidebar.button(WHATSAPP_ICON):
    st.write("Whatsapp clicked")
    st.session_state.whatsapp_session = True
    
    
if st.sidebar.button(TELEGRAM_ICON):
    st.write("Telegram clicked")


if st.sidebar.button(EMAIL_ICON):
    st.write("Email button clicked")
    
    
