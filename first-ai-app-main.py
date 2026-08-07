# Your code goes here
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
import gradio as gr



prompt_template_str = """
Votre tâche est de m'expliquer le concept de **{concept}** de façon :

1. Claire et intuitive
2. Concise (en moins de 100 mots)
3. Adaptée à mon profil

Voici ce que vous savez sur moi :
- Profil : étudiant en école centrale, parcours data science et développement Python
- Intérêts : développement web, pyhton dev, systèmes d'exploitation, IA
- Niveau : intermédiaire en Python

La personnalisation doit être subtile et naturelle.
"""


#Créer le template de prompt
prompt_template = PromptTemplate.from_template(prompt_template_str)

# Définir le concept à expliquer
#concept = "Scaling Laws"

# Formater le prompt avec la valeur réelle
#prompt = prompt_template.format(concept=concept)

# Créer l'interface du modèle
"""# Pour Mistral (recommandé si tu as une clé Mistral dans .env)
model = init_chat_model("mistral-tiny", model_provider="mistralai")

# Pour Groq (rapide et gratuit)
model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Pour Google
model = init_chat_model("gemini-1.5-flash", model_provider="google_genai")

# Pour OpenAI
model = init_chat_model("gpt-4o-mini", model_provider="openai")

  Returns:
      _type_: _description_
  """
model = init_chat_model("mistral-tiny", model_provider="mistralai")

# Appeler le modèle avec le prompt
#response = model.invoke(prompt)

# Afficher la réponse
# print(response.text)

# moduler le fonctionnement dans une fonction pour #Gradio
def generate_explanation(input_text):
  
  # Formater le prompt avec la valeur réelle
  prompt = prompt_template.format(concept=input_text)
  
  # Appeler le modèle avec le prompt
  response = model.invoke(prompt)
  return response.text


demo = gr.Interface(
    fn=generate_explanation,
    inputs=[gr.Textbox(label="Concept à expliquer", lines=1)],
    outputs=[gr.Textbox(label="Explication", lines=5)],
    flagging_mode="never",
    title="Définisseur de concepts personnalisé",
    description="Entrez un terme pour obtenir une explication adaptée à votre profil"
)

demo.launch()

