import asyncio
import os
import json
import time
import glob
from roteiro import gerar_roteiro
from audio import run_tts
from visual import buscar_video, baixar_video
from edicao import criar_video
from legenda import gerar_legendas

ROTEIROS_DIR = "assets/roteiros"

def carregar_roteiro_manual():
    """Busca arquivos JSON manuais em assets/roteiros/ (ignora _template.json)."""
    arquivos = glob.glob(f"{ROTEIROS_DIR}/*.json")
    arquivos = [f for f in arquivos if not f.endswith("_template.json")]
    
    if arquivos:
        # Usa o mais recente
        arquivo = max(arquivos, key=os.path.getmtime)
        print(f"   📄 Usando roteiro manual: {arquivo}")
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f), arquivo
    return None, None

def main():
    print("🏭 Iniciando Fábrica de Vídeos...")
    
    # 1. Roteiro (Verifica se há roteiro manual primeiro)
    print("\n📜 Buscando roteiro...")
    dados, arquivo_usado = carregar_roteiro_manual()
    
    if dados:
        titulo = dados.get("titulo", "Sem título")
        conteudo = dados.get("conteudo", "")
        print(f"   ✅ Roteiro MANUAL carregado: {titulo}")
    else:
        print("   🤖 Nenhum roteiro manual encontrado. Gerando com IA...")
        roteiro_json = gerar_roteiro()
        try:
            dados = json.loads(roteiro_json)
            titulo = dados.get("titulo", "Sem título")
            conteudo = dados.get("conteudo", "")
            print(f"   Título: {titulo}")
        except json.JSONDecodeError:
            print(f"Erro ao decodificar roteiro: {roteiro_json}")
            return

    # 2. Áudio
    print("\n🗣️  Gerando narração...")
    arquivo_audio = f"assets/temp/audio_{int(time.time())}.mp3"
    run_tts(conteudo, arquivo_audio)
    print(f"   Áudio salvo: {arquivo_audio}")

    # 2.5. Legendas (Novo!)
    print("\n📝 Gerando legendas (Whisper)...")
    legendas = gerar_legendas(arquivo_audio)
    print(f"   Legendas geradas: {len(legendas)} palavras")

    # 3. Visual
    print("\n👁️  Buscando visual...")
    termo_busca = titulo.split(":")[0] if ":" in titulo else "Technology"
    
    link_video = buscar_video(termo_busca)
    arquivo_video = f"assets/temp/video_bg_{int(time.time())}.mp4"
    
    if link_video:
        print(f"   Baixando vídeo: {link_video}")
        if not baixar_video(link_video, arquivo_video):
            print("   Falha no download. Usando placeholder se houver.")
            arquivo_video = None
    else:
        print("   Sem chave do Pexels ou vídeo não encontrado. Por favor, coloque um vídeo manually em assets/temp/placeholder.mp4 se quiser testar.")
        if os.path.exists("assets/temp/placeholder.mp4"):
            arquivo_video = "assets/temp/placeholder.mp4"
        else:
            print("❌ Falha: Nenhum vídeo para background.")
            return

    # 4. Edição
    if arquivo_video and os.path.exists(arquivo_audio):
        print("\n🎬 Editando vídeo final...")
        output = f"assets/output/video_final_{int(time.time())}.mp4"
        final = criar_video(arquivo_audio, arquivo_video, legendas, output)
        if final:
            print(f"\n✅ VÍDEO PRONTO: {final}")
        else:
            print("\n❌ Erro na edição.")

if __name__ == "__main__":
    main()
