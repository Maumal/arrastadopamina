# 🔄 PRÓXIMA SESSÃO - Arrastadopamina

> **Documento de transferência entre sessões.**
> **Última atualização:** 2026-01-06 21:09

---

## 🎯 OBJETIVO ATUAL

### Produzir vídeos de qualidade viral
- MVP v1.2 funcionando com legendas, música e vozes alternadas.
- Modo híbrido permite usar IAs premium (Opus, GPT-4o) no navegador.

---

## ✅ O QUE FOI FEITO (Sessão 2026-01-06)

### MVP v1.0
- ✅ Pipeline completo: Roteiro -> Áudio -> Visual -> Edição
- ✅ Integração Gemini 2.0 Flash, EdgeTTS, Pexels, MoviePy

### MVP v1.1
- ✅ Legendas automáticas (Whisper + TextClip)
- ✅ Regras de viralização no prompt
- ✅ Fix: Asteriscos removidos do áudio
- ✅ Fix: Legendas reposicionadas

### MVP v1.2
- ✅ Whisper `small` (legendas mais precisas)
- ✅ Vozes alternadas (Francisca/Antonio)
- ✅ Música lo-fi de fundo (8% volume)
- ✅ Fallback de busca no Pexels (brain, technology, abstract, nature)
- ✅ Modo híbrido: roteiro manual via `assets/roteiros/*.json`

### Documentação
- ✅ `start.txt`, `parar.txt`, `atualiza.txt` criados
- ✅ `CONTEXTO.md`, `DECISOES.md`, `PROXIMO.md` atualizados

---

## 📍 ESTADO ATUAL

**Onde paramos:** Fábrica completa v1.2. Modo híbrido implementado.
**Branch:** `main`
**Próxima ação:** Testar roteiros manuais ou adicionar múltiplos clipes.

---

## 🚀 PARA CONTINUAR

Cole `start.txt` no início do próximo chat.

**Backlog:**
1. Múltiplos clipes por vídeo (trocar a cada X segundos)
2. Legendas semânticas (frases, não palavras fixas)
3. Animação de legendas (fade, scale)
