import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
BASE_URL = "https://api.pexels.com/videos/search"

def buscar_video(query, orientations="portrait", size="medium"):
    """
    Busca um vídeo no Pexels.
    Retorna a URL do arquivo de vídeo ou None.
    """
    if not PEXELS_API_KEY:
        print("Erro: PEXELS_API_KEY não configurada.")
        return None

    headers = {
        "Authorization": PEXELS_API_KEY
    }
    
    # Tenta a query original primeiro, depois fallbacks em inglês
    queries_to_try = [query, "brain", "technology", "abstract", "nature"]
    
    for q in queries_to_try:
        params = {
            "query": q,
            "orientation": orientations,
            "size": size,
            "per_page": 5
        }

        try:
            response = requests.get(BASE_URL, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get("videos"):
                video = random.choice(data["videos"])
                video_files = video.get("video_files", [])
                mp4_files = [v for v in video_files if v['file_type'] == 'video/mp4']
                if mp4_files:
                    best_video = sorted(mp4_files, key=lambda x: x['width'], reverse=True)[0]
                    if q != query:
                        print(f"   (Usando fallback: {q})")
                    return best_video['link']
                
        except Exception as e:
            print(f"Erro na API do Pexels: {e}")
            continue
    
    print("Nenhum vídeo encontrado mesmo com fallbacks.")
    return None

def baixar_video(url, caminho_saida):
    """Baixa o vídeo da URL para o caminho local."""
    if not url:
        return False
        
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(caminho_saida, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"Erro ao baixar vídeo: {e}")
        return False

if __name__ == "__main__":
    if not PEXELS_API_KEY:
        print("⚠️  AVISO: Configure PEXELS_API_KEY no .env para testar.")
    else:
        print("Buscando vídeo de teste (Natureza)...")
        link = buscar_video("Nature")
        if link:
            print(f"Link encontrado: {link}")
            if baixar_video(link, "assets/temp/video_teste.mp4"):
                print("Vídeo baixado com sucesso!")
