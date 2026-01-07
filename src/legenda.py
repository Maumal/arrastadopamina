import whisper
import os

def gerar_legendas(caminho_audio, modelo="small"):
    """
    Transcreve o áudio e retorna os timestamps das palavras.
    Retorna: lista de dicts {'word': str, 'start': float, 'end': float}
    """
    print(f"   🎧 Carregando modelo Whisper ({modelo})...")
    model = whisper.load_model(modelo)
    
    print(f"   🎙️  Transcrevendo áudio...")
    result = model.transcribe(caminho_audio, word_timestamps=True)
    
    palavras = []
    for segment in result["segments"]:
        for word in segment["words"]:
            palavras.append({
                "word": word["word"].strip(),
                "start": word["start"],
                "end": word["end"]
            })
            
    return palavras

if __name__ == "__main__":
    # Teste
    import sys
    if len(sys.argv) > 1:
        audio = sys.argv[1]
        print(gerar_legendas(audio))
    else:
        print("Uso: python legenda.py <arquivo_audio>")
