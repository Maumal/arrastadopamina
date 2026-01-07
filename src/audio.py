import asyncio
import edge_tts
import os
import random

# Vozes disponíveis (alternância automática)
VOZES = [
    "pt-BR-FranciscaNeural",  # Feminina
    "pt-BR-AntonioNeural",     # Masculina
]

def escolher_voz():
    """Escolhe uma voz aleatória."""
    return random.choice(VOZES)

async def gerar_audio(texto, arquivo_saida):
    """
    Gera áudio a partir do texto usando Microsoft Edge TTS.
    Trata marcadores de pausa simples. Alterna vozes automaticamente.
    """
    # Substitui marcador [pausa] por silêncio natural (reticências longas) e remove *
    texto_tratado = texto.replace("[pausa]", "... ...").replace("[Pausa]", "... ...").replace("*", "")
    
    voz = escolher_voz()
    print(f"   🎤 Voz selecionada: {voz.split('-')[2].replace('Neural', '')}")
    
    communicate = edge_tts.Communicate(texto_tratado, voz)
    await communicate.save(arquivo_saida)
    return arquivo_saida

def run_tts(texto, arquivo_saida="assets/temp/audio.mp3"):
    """Wrapper síncrono para chamar a função async."""
    # Garante que o diretório existe
    os.makedirs(os.path.dirname(arquivo_saida), exist_ok=True)
    
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(gerar_audio(texto, arquivo_saida))
    return arquivo_saida

if __name__ == "__main__":
    print("Gerando áudio de teste...")
    texto_teste = "Olá! Esta é uma voz neural gerada gratuitamente pela fábrica de vídeos."
    caminho = run_tts(texto_teste)
    print(f"Áudio salvo em: {caminho}")
