import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da API (Usando a chave encontrada no ambiente)
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

def ler_regras():
    """Lê o arquivo de estilo para instruir a IA."""
    caminho_regras = os.path.join(os.path.dirname(__file__), "../superinteressante.txt")
    try:
        with open(caminho_regras, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Regras não encontradas. Use o estilo Superinteressante."

def gerar_roteiro(tema=None):
    """
    Gera um roteiro para o vídeo usando Gemini.
    """
    if not API_KEY:
        return "Erro: GEMINI_API_KEY não encontrada nas variáveis de ambiente."

    regras = ler_regras()
    
    if tema:
        prompt_user = f"Tema sugerido: {tema}. Crie a matéria seguindo as regras."
    else:
        prompt_user = "Crie uma matéria aleatória seguindo as regras."

    prompt_system = f"""
    {regras}
    
    ESTRUTURA DE SAÍDA NECESSÁRIA (JSON):
    {{
        "titulo": "Título chamativo",
        "conteudo": "Texto completo da matéria para narração, sem marcadores de 'Narração:' ou 'Cena:'. Apenas o texto falado.",
        "gancho_final": "A pergunta obrigatória do final"
    }}
    Retorne APENAS o JSON válido.
    """

    try:
        # Tenta usar modelos em ordem de preferência (baseado na lista disponível)
        modelos_tentativa = [
            'models/gemini-2.0-flash-exp', 
            'models/gemini-2.5-flash',
            'models/gemini-1.5-flash'
        ]
        
        response = None
        used_model = None

        for modelo_nome in modelos_tentativa:
            try:
                model = genai.GenerativeModel(modelo_nome)
                response = model.generate_content(f"{prompt_system}\n\nUSER: {prompt_user}")
                used_model = modelo_nome
                break
            except Exception:
                continue
        
        if not response:
            # Se falhar tudo, lista o que tem disponível para debug
            try:
                available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                return f"Erro: Nenhum modelo funcionou. Disponíveis: {available}"
            except:
                return "Erro grave: Não foi possível listar modelos ou gerar conteúdo."

        # Limpeza básica do JSON
        texto_limpo = response.text.replace("```json", "").replace("```", "").strip()
        return texto_limpo
        
    except Exception as e:
        return f"Erro ao gerar roteiro: {str(e)}"

if __name__ == "__main__":
    if not API_KEY:
         print("⚠️  AVISO: GEMINI_API_KEY não encontrada.")
    else:
        print("Gerando roteiro de teste com Gemini...")
        print(gerar_roteiro("Brevidade da Vida"))
