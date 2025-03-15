# CHETGPT: It kinda works, but accuracy is not good. The project then scraped, move to Google Translate (and it's still not 100% accurate either)

# BY CHATGPT

## 📌 Overview
**Hata** is an **Indonesian-Simalungun translator** powered by **OpenAI API**. It provides instant **word translation and explanations** for Simalungun words using an interactive **Streamlit chat interface**.

## 🚀 Features
- 🌐 **Instant Translation**: Translates Indonesian words into Simalungun.
- 📝 **Explanations on Demand**: Ask for explanations by using `"Jelaskan -kata simalungun-"`.
- 🤖 **AI-Powered Responses**: Uses OpenAI's **Assistant API** to generate accurate translations.
- 🖥️ **Interactive Web UI**: Built with **Streamlit** for a smooth user experience.
- 🔑 **Secure API Handling**: Uses environment variables for authentication.

## 📦 Dependencies
Install the required libraries using:
```bash
pip install streamlit openai python-dotenv
```

## 🛠 How to Use
1. **Set Up API Keys**:
   - Create a `.env` file and add:
     ```env
     OPENAI_KEY=your_openai_api_key
     ORG_ID=your_organization_id
     ```
2. **Run the Streamlit App**:
   ```bash
   streamlit run streamlit_app.py
   ```
3. **Start Translating!**
   - Enter an Indonesian word in the chat.
   - For explanations, use `"Jelaskan -kata simalungun-"`.
   - The assistant responds with the **translation and explanation**.

## 🔑 Key Functionalities
### 📖 **Translation & Explanation**
- Provides **word meanings** and **language context**.
- Designed to **preserve cultural significance** in translations.

### 🔗 **AI Assistant with OpenAI API**
- Uses an **OpenAI Assistant** (`asst_W9WhhX3DRDu8e0A5T5TjQMup`).
- **Thread-based messaging** for better conversational flow.

### ⚡ **Fast & Efficient Processing**
- **Real-time responses** with optimized API calls.
- Implements **retry mechanisms** to handle API delays.

## 📁 Project Structure
- **`streamlit_app.py`** → Web app for translation.
- **`hata2.py`** → Backend logic for handling OpenAI API requests.
- **`.env`** → Stores API keys securely.

## 📌 Next Steps
- Improve **translation accuracy** using fine-tuned models.
- Add **sentence translation** support.
- Implement **speech-to-text functionality** for voice input.

## 🤝 Contributing
Feel free to submit **issues or pull requests** for improvements!

---
🌍 *Bridging languages through AI-powered translation!*
