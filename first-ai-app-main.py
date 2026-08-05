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
model = init_chat_model("gpt-4o-mini", model_provider="openai")

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

# demo.launch()

