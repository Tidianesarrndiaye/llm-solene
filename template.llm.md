# Template LLM Prompt

## Prompt Template

```python
import os
from dotenv import load_dotenv
load_dotenv()

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
```

## Architecture d'une application LLM

La plupart des applications LLM partagent trois composants essentiels :

- **Interface utilisateur** : permet aux utilisateurs de saisir des données et de consulter les réponses.
- **Logique applicative** : construit les prompts, communique avec le LLM via une API et traite les réponses.
- **Fournisseur de LLM** : service externe qui traite les prompts et génère des réponses.

## LangChain

Un framework devenu un standard dans le domaine pour la création d'applications LLM, offrant une méthodologie de conception et des composants modulaires.

**Avantages clés** : vitesse de développement (composants pré-intégrés), abstraction du fournisseur (basculer entre OpenAI, Anthropic, etc., sans modifier le code) et une communauté open-source active.

## Modèles de prompts (Prompt Templates)

Créez des prompts réutilisables avec des emplacements de variables à l'aide de `PromptTemplate` :

```python
from langchain_core.prompts import PromptTemplate

prompt_template_str = "... {input_text} ..."
prompt_template = PromptTemplate.from_template(prompt_template_str)
prompt = prompt_template.format(input_text="your value")
```

Les variables du modèle (par exemple, `{input_text}`) sont remplacées par des valeurs réelles au moment de l'exécution à l'aide de `.format()`.

## Interface du modèle

Initialisez un modèle et appelez-le à l'aide de LangChain :

```python
from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4o-mini", model_provider="openai")
response = model.invoke(prompt)
print(response.text)
```

- `init_chat_model()` crée une interface de modèle pour un fournisseur donné.
- `model.invoke()` envoie le prompt et renvoie la réponse.
- `response.text` contient le contenu généré.

## Gestion des clés API

Chaque fournisseur de LLM nécessite une clé API pour l'authentification — ne codez jamais ces clés en dur dans votre code.

Stockez les clés dans un fichier `.env` et chargez-les avec `dotenv` :

```python
from dotenv import load_dotenv

load_dotenv()
```

- LangChain lit automatiquement les variables d'environnement spécifiques au fournisseur (par exemple, `OPENAI_API_KEY`).
- Ajoutez `.env` au fichier `.gitignore` pour exclure les clés de votre base de code.