# 📝 DECISÕES - Arrastadopamina

> **Decisões técnicas e de produto.**
> **Última atualização:** 2026-01-06

---

## Decisões

### 2026-01-06 - Modelo de IA (Roteiro)
**Decisão:** Gemini 2.0 Flash Exp (automático) + Modo híbrido (manual)
**Motivo:** Gratuito e rápido. Modo híbrido permite usar IAs premium (Opus, GPT-4o) no navegador sem custo de API.

### 2026-01-06 - Motor de Voz (TTS)
**Decisão:** EdgeTTS com vozes alternadas (Francisca/Antonio)
**Motivo:** Qualidade neural gratuita. Alternância dá variedade ao canal.

### 2026-01-06 - Legendas
**Decisão:** Whisper `small` (local) + TextClip (MoviePy)
**Motivo:** Melhor precisão em português que o modelo `base`. Grátis.

### 2026-01-06 - Música de Fundo
**Decisão:** Lo-fi de Pixabay a 8% do volume
**Motivo:** Aumenta produção percebida sem abafar narração. Licença CC0.

### 2026-01-06 - Busca de Vídeos
**Decisão:** Pexels API com fallbacks (brain, technology, abstract, nature)
**Motivo:** Evita falhas quando query em português não retorna resultados.

### 2026-01-06 - Modo Híbrido
**Decisão:** Detectar JSONs em `assets/roteiros/` antes de gerar automaticamente
**Motivo:** Permite usar IAs premium do navegador sem pagar API, mantendo automação do resto.

---

## Resumo Rápido

| Decisão | Escolha | NÃO fazer |
|---------|---------|-----------|
| Roteiro | Gemini + Híbrido | Pagar API de IAs premium |
| Voz | EdgeTTS alternado | ElevenLabs (cota limitada) |
| Legendas | Whisper small | APIs pagas de transcrição |
| Música | Pixabay CC0 | Músicas com copyright |
| Visual | Pexels + fallbacks | Depender de query exata |
