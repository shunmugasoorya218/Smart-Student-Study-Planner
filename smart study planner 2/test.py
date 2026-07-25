from google import genai

client = genai.Client(api_key="AIzaSyAw0E5NDzoLh-3MNpM_w2gHrvOITF1_K-g")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say hello"
)

print(response.text)