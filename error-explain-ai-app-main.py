from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
import gradio as gr


# Model: gpt-4o-mini | Provider: openai



prompt_template_str = """
Votre tâche est d'analyser le code ou le message d'erreur suivant :

**{error_message}**

Répondez de façon :

1. Claire et pédagogique
2. Structurée
3. Adaptée à mon profil

Voici ce que vous savez sur moi :
- Profil : étudiant en école centrale, parcours data science et développement Python
- Intérêts : développement web, Python, systèmes d'exploitation, IA
- Niveau : intermédiaire en Python

La réponse doit contenir les sections suivantes :

### 1. Explication de l'erreur
- Signification du code ou du message d'erreur
- Contexte dans lequel elle apparaît généralement

### 2. Cause probable
- Cause principale la plus probable
- Autres causes possibles

### 3. Comment corriger l'erreur
- Étapes à suivre dans l'ordre
- Vérifications à effectuer après chaque étape

### 4. Exemple pratique
- Exemple concret illustrant l'erreur
- Exemple de correction si applicable

### 5. Conseils de prévention
- Bonnes pratiques pour éviter cette erreur à l'avenir

La personnalisation doit être subtile et naturelle, avec des explications adaptées à un étudiant ayant un niveau intermédiaire en Python.
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
def generate_explanation(error_message):
  
  # Formater le prompt avec la valeur réelle
  prompt = prompt_template.format(error_message=error_message)
  
  # Appeler le modèle avec le prompt
  response = model.invoke(prompt)
  return response.text


demo = gr.Interface(
    fn=generate_explanation,
    inputs=[gr.Textbox(label="Code d'erreur", lines=5)],
    outputs=[gr.Textbox(label="Explication & Debug", lines=5)],
    flagging_mode="never",
    title="Définisseur de concepts personnalisé",
    description="Entrez le code d'erreur et obtennez une explication et les etapes de correction"
)

# demo.launch()

