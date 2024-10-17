import openai

# Definir os parâmetros do Azure
openai.api_type = "azure"
openai.azure_endpoint = "https://albuquerque-m295bej7-australiaeast.openai.azure.com/"  # Substitua pelo seu endpoint do Azure
openai.api_version = "2024-05-01-preview"
openai.api_key = "d5w13w15551612eweweffsd56213w72f"
         

# Definir o nome do deployment criado no Azure
deployment_name = "gpt-4-32k" # Verifique o nome do deployment no portal do Azure


chat_prompt = [
{
    "role": "system",
    "content": "Você é um assistente de IA que ajuda as pessoas a encontrar informações."
}
]  

# Incluir resultado de fala se a fala estiver habilitada  
speech_result = chat_prompt  

# Fazer a chamada à API
response = openai.chat.completions.create(
    model=deployment_name,  # Certifique-se de usar 'engine' ao invés de 'model' no Azure
    messages=speech_result,  
    max_tokens=10
)

print(response.to_json())  
    
