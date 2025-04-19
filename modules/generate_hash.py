import streamlit_authenticator as stauth

passwords = ["1234"]
hashed = stauth.Hasher(passwords).generate()
print(hashed)
