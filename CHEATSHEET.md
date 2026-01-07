# 🎬 CHEAT SHEET - Produção de Vídeos

## PASSO 1: ROTEIRO (30 segundos)
1. Abre Sonnet/Opus/GPT no navegador
2. Cola o prompt de `superinteressante.txt`
3. Pede: "Crie um vídeo sobre [TEMA]"
4. Copia o JSON da resposta

## PASSO 2: FÁBRICA (15 minutos)
```bash
# Salva o JSON
# Arquivo: assets/roteiros/meu_video.json

# Roda o script
source .venv/bin/activate
python src/main.py

# Resultado em: assets/output/video_final_XXX.mp4
```

## PASSO 3: CAPCUT (15 minutos)
1. Importa o vídeo gerado
2. Deleta as legendas atuais (se quiser)
3. Clica em "Legendas Automáticas"
4. Estiliza: fonte grande, amarelo, contorno preto
5. Adiciona música/efeitos se quiser
6. Exporta 1080x1920 (9:16)

## PASSO 4: POSTA
- YouTube Shorts ✅
- TikTok ✅
- Instagram Reels ✅

---
**Tempo total: ~35 min/vídeo**
