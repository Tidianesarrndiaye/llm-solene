# llm-solene

Ce projet est une application LLM utilisant **LangChain** et **Gradio** pour générer des explications de concepts personnalisées. Voici comment l'installer, le configurer et utiliser des modèles d'IA gratuits.

---

### 1. Installation avec un environnement virtuel (`.venv`)

Il est fortement recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet.

#### **Étape 1 : Création de l'environnement virtuel**
Ouvrez un terminal dans le dossier du projet et exécutez la commande correspondant à votre système :

- **Windows :**
  ```powershell
  python -m venv .venv
  ```
- **macOS / Linux :**
  ```bash
  python3 -m venv .venv
  ```

#### **Étape 2 : Activation de l'environnement**
- **Windows (PowerShell) :**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Windows (Invite de commande) :**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```
- **macOS / Linux :**
  ```bash
  source .venv/bin/activate
  ```

#### **Étape 3 : Installation des dépendances**
Une fois l'environnement activé, installez les bibliothèques nécessaires :
```bash
pip install -r requirements.txt
```

---

### 2. Configuration des API (LLM Gratuits)

Pour utiliser les modèles, vous devez créer un fichier nommé `.env` à la racine du projet pour y stocker vos clés API de façon sécurisée.

#### **Comment obtenir les clés API gratuites ?**
1.  **Groq (Très rapide & gratuit) :** Allez sur [Groq Cloud](https://console.groq.com/keys), créez un compte et générez une clé `gsk_...`.
2.  **Google Gemini :** Allez sur [Google AI Studio](https://aistudio.google.com/), cliquez sur "Get API key".
3.  **Mistral AI :** Allez sur [Mistral Console](https://console.mistral.ai/), ils offrent des crédits gratuits au démarrage.

#### **Structure du fichier `.env`**
Créez le fichier et ajoutez vos clés ainsi :
```env
OPENAI_API_KEY=votre_cle_openai
GROQ_API_KEY=votre_cle_groq
GOOGLE_API_KEY=votre_cle_gemini
MISTRAL_API_KEY=votre_cle_mistral
```

---

### 3. Utilisation de `init_chat_model` avec des modèles gratuits

Voici les paramètres à utiliser dans votre code Python (`first-ai-app-main.py`) pour basculer entre les différents fournisseurs gratuits.

| Fournisseur | Modèle recommandé | `model_provider` | Package requis |
| :--- | :--- | :--- | :--- |
| **Groq** | `llama3-8b-8192` | `"groq"` | `langchain-groq` |
| **Google** | `gemini-1.5-flash` | `"google_genai"` | `langchain-google-genai` |
| **Mistral** | `mistral-tiny` | `"mistralai"` | `langchain-mistralai` |
| **OpenAI** | `gpt-4o-mini` | `"openai"` | `langchain-openai` |

#### **Exemple de modification dans le code :**
```python
from langchain.chat_models import init_chat_model

# Pour utiliser Groq (Gratuit et très rapide)
model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Pour utiliser Google Gemini
# model = init_chat_model("gemini-1.5-flash", model_provider="google_genai")
```

---

### 4. Lancer l'application

Pour démarrer l'interface Gradio, assurez-vous que votre `.venv` est activé et lancez :
```bash
python first-ai-app-main.py
```
L'application vous donnera une URL (généralement `http://127.0.0.1:7860`) pour accéder à l'interface dans votre navigateur.