# 🎤 FASE 4: ÁUDIO/NARRAÇÃO (~5 min)

## Objetivo
Gravar narração natural usando IA de voz.

---

## NOVO: Narração com IA Conversacional

### Ferramentas de Voz (ordem de qualidade)
| Ferramenta | Qualidade | Como usar |
|-----------|-----------|-----------|
| GPT (voz) | ⭐⭐⭐⭐⭐ | Celular, modo voz |
| Perplexity (voz) | ⭐⭐⭐⭐ | Celular, modo voz |
| Copilot (voz) | ⭐⭐⭐⭐ | Celular, modo voz |
| EdgeTTS | ⭐⭐⭐ | Script local |

---

## Passo a Passo (Celular)

### 1. Abra o app (GPT/Perplexity/Copilot)

### 2. Ative modo voz

### 3. Cole o texto com instrução:
```
APENAS LEIA. Não comente. Não explique.
Leia como um narrador calmo e pausado:

[COLE O CONTEÚDO DO JSON]
```

### 4. Grave a tela do celular
- Android: Gravação de tela nativa
- iOS: Central de Controle > Gravação

### 5. Mande o vídeo pro PC
- WhatsApp Web
- Google Drive
- Cabo USB

### 6. Extraia o áudio
No Kdenlive:
1. Importe o vídeo
2. Clique direito > Extrair áudio
3. Salve como MP3

---

## Alternativa: EdgeTTS (Local)

```bash
cd /home/mauricio/Documentos/git/arrastadopamina
source .venv/bin/activate
python src/testar_audio.py assets/roteiros/shortXX.json
```

---

## Dicas de Narração

| Para conseguir | Faça isso |
|----------------|-----------|
| Pausas | Adicione "..." no texto |
| Ênfase | Use MAIÚSCULAS |
| Naturalidade | Use "né?", "sabe?", "[pausa]" |

---

## Salvar

```
assets/temp/narracao_shortXX.mp3
```

---

## Checklist
- [ ] Narração gravada
- [ ] Áudio extraído (se gravou vídeo)
- [ ] Qualidade aprovada
- [ ] Salvo em assets/temp/
