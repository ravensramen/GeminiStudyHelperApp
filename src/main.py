from google import genai

client = genai.Client()

response = client.models.generate_content(

    model ="gemini-3-flash-preview", contents="I just ate a banana, how many calories did I ingest?"
)
print(response.text)

