import streamlit as st

def load_default_albu_json() -> str:
  with open("default_albu.json", "r") as f:
    return f.read()

def main():
  st.title("Albumentations testing Web UI")

  default_albu_json: str = load_default_albu_json()
  st.text_area(label="code", value=default_albu_json)


if __name__ == "__main__":
  main()
