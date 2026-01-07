# 📋 CONTEXTO - Arrastadopamina

> **Cole este arquivo no início de novos chats.**
> **Última atualização:** 2026-01-06 21:09
> **Status:** 🏭 Fábrica Operacional (MVP v1.2)

---

## 🎯 VISÃO GERAL

**Projeto:** Fábrica de Vídeos com IA (Arrastadopamina)
**O que faz:** Criação automatizada de vídeos verticais (Shorts/TikTok) com curiosidades.
**Estilo:** "Superinteressante infinita" (Curioso, claro, instigante, viral).
**Pipeline:** Roteiro (Manual ou IA) -> TTS -> Whisper -> Pexels -> MoviePy -> Vídeo Final.

**Links:**
- 📺 YouTube: https://www.youtube.com/@arrastadopamina
- 🎵 TikTok: https://www.tiktok.com/@arrastadopamina
- 📸 Instagram: https://www.instagram.com/arrastadopamina/

---

## 📁 ESTRUTURA

```
arrastadopamina/
├── start.txt / parar.txt / atualiza.txt  # Controle de sessão
├── CONTEXTO.md / DECISOES.md / PROXIMO.md
├── superinteressante.txt        # Prompt de viralização
├── src/
│   ├── main.py         # Orquestrador (modo híbrido)
│   ├── roteiro.py      # Gemini 2.0 Flash
│   ├── audio.py        # EdgeTTS (vozes alternadas)
│   ├── visual.py       # Pexels + fallbacks
│   ├── legenda.py      # Whisper small
│   └── edicao.py       # MoviePy + música
├── assets/
│   ├── roteiros/       # JSONs manuais (modo premium)
│   ├── music/          # Lo-fi background
│   ├── temp/           # Arquivos temporários
│   └── output/         # Vídeos finais
```

---

## 📊 ESTADO ATUAL

### ✅ Funcionando (MVP v1.2)
- **Roteiro:** Gemini 2.0 Flash OU JSON manual (modo híbrido)
- **Áudio:** EdgeTTS com vozes alternadas (Francisca/Antonio)
- **Legendas:** Whisper `small` (melhor precisão PT-BR)
- **Visual:** Pexels API com fallbacks automáticos
- **Edição:** MoviePy + música lo-fi de fundo (8% volume)

### 🔵 Próximos Passos
- Múltiplos clipes por vídeo (trocar a cada parágrafo)
- Legendas semânticas (agrupar por frases, não palavras)

---

## 🛠️ COMO USAR

### Modo Automático (Gemini)
```bash
source .venv/bin/activate
python src/main.py
```

### Modo Premium (IA do Navegador)
1. Gere roteiro no Claude/GPT/Gemini
2. Salve em `assets/roteiros/meu_roteiro.json`
3. Rode `python src/main.py`
