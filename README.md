# 🎂 Interactive Birthday Greeting — Streamlit

A polished, fully interactive birthday greeting website that runs inside Streamlit.

## Features

- 🎉 Animated birthday hero section
- 🎂 Click the cake to cut it
- 🕯️ Blow out candles
- 🎈 Click balloons to pop them
- 🎆 Click the scene for fireworks/spark bursts
- 🎊 Confetti effects
- 🎵 Built-in browser Web Audio birthday-style melody (no audio file required)
- ✨ Animated gradient birthday name
- 🌌 Animated star background
- 🎁 Streamlit sidebar for changing the recipient, message and sender
- 📱 Responsive layout
- 🚫 No external images, fonts, or paid APIs required

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py`, `birthday.html`, and `requirements.txt`.
3. Open Streamlit Community Cloud.
4. Select your GitHub repository and `app.py`.
5. Deploy.

The app uses Streamlit's HTML component so the CSS/JavaScript interactions remain inside the greeting experience. Streamlit documents HTML/custom components for embedding custom HTML and JavaScript in apps. For current Streamlit versions, check the custom-component documentation if the component API changes. 

## Customize

The default recipient/message/sender are at the top of `app.py`:

```python
DEFAULT_NAME = "Birthday Star"
DEFAULT_MESSAGE = "..."
DEFAULT_FROM = "With lots of love ❤️"
```

You can also change them live from the sidebar.

## License

MIT — use and customize freely.
