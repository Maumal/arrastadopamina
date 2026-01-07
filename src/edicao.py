from moviepy import *
import os

# Caminho da música de fundo (lo-fi)
MUSIC_PATH = os.path.join(os.path.dirname(__file__), "../assets/music/lofi_background.mp3")
MUSIC_VOLUME = 0.08  # 8% do volume (bem baixinho)

def criar_video(audio_path, video_path, legendas=None, output_path="assets/output/final.mp4"):
    """
    Combina áudio e vídeo. Se legendas (lista de dicts) for passado, adiciona sobreposição.
    Inclui trilha sonora de fundo se disponível.
    """
    try:
        # Carrega narração
        narracao = AudioFileClip(audio_path)
        
        # Tenta carregar música de fundo
        audio_final = narracao
        if os.path.exists(MUSIC_PATH):
            musica = AudioFileClip(MUSIC_PATH)
            # Ajusta duração da música para a narração (loop se precisar)
            if musica.duration < narracao.duration:
                musica = musica.with_effects([afx.AudioLoop(duration=narracao.duration)])
            musica = musica.subclipped(0, narracao.duration)
            # Reduz volume da música
            musica = musica.with_effects([afx.MultiplyVolume(MUSIC_VOLUME)])
            # Mixa narração + música
            audio_final = CompositeAudioClip([narracao, musica])
            print("   🎵 Música de fundo adicionada!")
        
        video = VideoFileClip(video_path)
        
        # Ajusta duração do vídeo para o áudio
        # Se vídeo for curto, faz loop
        if video.duration < narracao.duration:
            video = video.with_effects([vfx.Loop(duration=narracao.duration)])
        
        # Corta no tamanho exato do áudio
        video = video.subclipped(0, narracao.duration)
        
        # Adiciona áudio mixado
        video = video.with_audio(audio_final)
        
        # Redimensiona para vertical (9:16) se necessário
        w, h = video.size
        target_h = 1280
        target_w = int(target_h * (9/16))

        if w > h:
            video = video.cropped(x1=w/2 - h*(9/16)/2, y1=0, width=h*(9/16), height=h)
        
        video = video.resized(height=target_h) # Padroniza altura
        
        clips = [video]

        # Processa Legendas
        if legendas:
            text_clips = []
            font_size = 55 # Reduzido de 70 para caber melhor
            
            # Agrupar legendas de 3 em 3 palavras para não ficar muito rápido
            # (Lógica simples, pode ser melhorada)
            chunk_size = 3
            for i in range(0, len(legendas), chunk_size):
                chunk = legendas[i:i+chunk_size]
                if not chunk: continue
                
                texto = " ".join([w['word'] for w in chunk])
                start = chunk[0]['start']
                end = chunk[-1]['end']
                duration = end - start
                
                if duration <= 0: continue

                # Cria o clip de texto
                # Nota: Em MoviePy 2.0 a API do TextClip mudou um pouco, 
                # mas vamos tentar o padrão. Se der erro de ImageMagick, avisaremos.
                txt_clip = TextClip(
                    text=texto,
                    font="Impact", # Ou Arial-Bold
                    font_size=font_size,
                    color='yellow',
                    stroke_color='black',
                    stroke_width=2,
                    method='caption', # Quebra de linha automática
                    size=(int(target_w * 0.8), None), # 80% da largura
                    text_align='center'
                )
                txt_clip = txt_clip.with_start(start).with_duration(duration).with_position(('center', 'bottom'))
                # Ajuste posição vertical (bottom - margem)
                # Subindo um pouco (0.70) para evitar cortar em telas menores ou se quebrar muitas linhas
                txt_clip = txt_clip.with_position(('center', int(target_h * 0.70)))
                
                text_clips.append(txt_clip)
            
            clips.extend(text_clips)

        # Compõe tudo
        final_video = CompositeVideoClip(clips)
        
        # Salva
        final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
        return output_path
        
    except Exception as e:
        print(f"Erro na edição: {e}")
        return None

if __name__ == "__main__":
    print("Módulo de edição com legendas pronto.")
