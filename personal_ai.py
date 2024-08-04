import streamlit as st
import ollama

def main():
  st.title("My personal A.I")

  user_input = st.text_area("What do you want to ask?","")

  if st.button("SEND")
    if user_input:
      response = ollama.chat(model='mistral', message=[{'role': 'user', 'content': user_input}])

      st.text("REPLY :")
      st.write(response['message']['content'])
    else:
      st.warning("please ask question !")

if __name__ == "__main__":
  main()
