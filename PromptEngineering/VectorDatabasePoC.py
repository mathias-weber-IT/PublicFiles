# Databricks notebook source
# DBTITLE 1,Vektorisierung
# Schritt 1: Installieren Sie die benötigten Pakete
# Dies können Sie in Ihrem Azure Databricks Cluster ausführen.
# !pip install openai sklearn

# Schritt 2: Erstellen Sie das Dictionary und generieren Sie die Embeddings

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


texts = {
    "text1": "Pizza ist lecker",
    "text2": "Gefängnisse sind meist aus Stein",
    "text10": "Blumen sind schön"
}

vectorizer = TfidfVectorizer().fit(list(texts.values()))
text_embeddings = {key: vectorizer.transform([value]) for key, value in texts.items()}

# COMMAND ----------

print(text_embeddings)

# COMMAND ----------

# DBTITLE 1,Finde ähnlichsten Eintrag (Blume)
# Schritt 3: Generieren Sie das Embedding für die Frage und vergleichen Sie die Ähnlichkeit

question = "Was kannst du über Blumen sagen?"
question_embedding = vectorizer.transform([question])

similarities = {key: cosine_similarity(value, question_embedding)[0][0] for key, value in text_embeddings.items()}
most_similar_key = max(similarities, key=similarities.get)

print(similarities)
print(texts[most_similar_key])

# COMMAND ----------

# DBTITLE 1,Finde ähnlichsten Eintrag (Gefängnis)
# Schritt 3: Generieren Sie das Embedding für die Frage und vergleichen Sie die Ähnlichkeit

question = "Was kannst du über Gefängnisse sagen?"
question_embedding = vectorizer.transform([question])

similarities = {key: cosine_similarity(value, question_embedding)[0][0] for key, value in text_embeddings.items()}
most_similar_key = max(similarities, key=similarities.get)

print(similarities)
print(texts[most_similar_key])

# COMMAND ----------

prompt=f"Basierend auf diesem Kontext: {texts[most_similar_key]}, beantworte bitte meine Frage: {question}"
print(prompt)

# COMMAND ----------

pip install openai

# COMMAND ----------

# DBTITLE 1,Chat-GPT Part
import os
import openai

# Ersetzen Sie dies durch Ihren OpenAI API-Schlüssel
os.environ["OPENAI_API_KEY"] = "YOUR-KEY"
openai.api_key = os.getenv("OPENAI_API_KEY")
#print(openai.Model.list())
# Schritt 4: Senden Sie die Frage und den am ähnlichsten Text an ChatGPT und drucken Sie die Antwort

#response = openai.Completion.create(model="gpt-3.5-turbo-0301",prompt=prompt)
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-0301",
  messages=[
    {
      "role": "user",
      "content": prompt
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#print(response)

# COMMAND ----------

print(response.choices[0]["message"]["content"].strip())
