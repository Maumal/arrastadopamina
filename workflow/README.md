# 🏭 WORKFLOW DE PRODUÇÃO v2.0

> **Tempo total:** ~45 minutos por vídeo  
> **Estilo visual:** Surrealismo Dalí  
> **Foco:** Qualidade + Diferenciação

---

## 📋 VISÃO GERAL

| Fase | Tempo | Documento |
|------|-------|-----------|
| 1. Roteiro + Cenas | 10 min | [01_roteiro.md](01_roteiro.md) |
| 2. Fact-check | 5 min | [02_factcheck.md](02_factcheck.md) |
| 3. Revisão | 5 min | [03_revisao.md](03_revisao.md) |
| 4. Narração | 5 min | [04_audio.md](04_audio.md) |
| 5. Visuais | 15 min | [05_visuais.md](05_visuais.md) |
| 6. Edição | 10 min | [06_edicao.md](06_edicao.md) |
| 7. Publicação | 5 min | [07_publicacao.md](07_publicacao.md) |

---

## 🛠️ STACK DE FERRAMENTAS

| Função | Ferramenta Principal | Alternativa |
|--------|---------------------|-------------|
| Roteiro + Cenas | GPT-4 | Claude Sonnet |
| Fact-check | Perplexity | - |
| Revisão | Claude Opus | - |
| Narração | GPT/Perplexity (voz) | EdgeTTS |
| Imagens | GPT/DALL-E | Ideogram |
| Vídeos | Gemini Veo | - |
| Edição | Kdenlive | - |

---

## 🔄 FLUXO VISUAL

```
    ┌─────────────────────────────────────────────┐
    │      FASE 1: ROTEIRO + CENAS (10 min)       │
    │  GPT → JSON com roteiro + 6 cenas Dalí      │
    │  Usa: prompt_gerar_roteiro_v2.txt           │
    └────────────────────┬────────────────────────┘
                         ▼
    ┌─────────────────────────────────────────────┐
    │         FASE 2: FACT-CHECK (5 min)          │
    │              Perplexity                      │
    └────────────────────┬────────────────────────┘
                         ▼
    ┌─────────────────────────────────────────────┐
    │          FASE 3: REVISÃO (5 min)            │
    │         Claude Opus → Humanizar             │
    └────────────────────┬────────────────────────┘
                         ▼
    ┌─────────────────────────────────────────────┐
    │          FASE 4: NARRAÇÃO (5 min)           │
    │    GPT/Perplexity voz → Gravar celular      │
    └────────────────────┬────────────────────────┘
                         ▼
    ┌─────────────────────────────────────────────┐
    │          FASE 5: VISUAIS (15 min)           │
    │  GPT/DALL-E → 6 imagens surrealistas        │
    │  OU Gemini Veo → 6 vídeos curtos            │
    └────────────────────┬────────────────────────┘
                         ▼
    ┌─────────────────────────────────────────────┐
    │          FASE 6: EDIÇÃO (10 min)            │
    │ Kdenlive → Ken Burns + Legenda + Áudio      │
    └────────────────────┬────────────────────────┘
                         ▼
    ┌─────────────────────────────────────────────┐
    │        FASE 7: PUBLICAÇÃO (5 min)           │
    │     YouTube Shorts + TikTok + Reels         │
    └─────────────────────────────────────────────┘
```

---

## 🎨 ESTILO VISUAL PADRÃO

- **Estética:** Surrealismo Salvador Dalí
- **Tons:** Dourado, vermelho sangue, azul profundo
- **Fundo:** Escuro com neblina
- **Formato:** Vertical 9:16
- **Sem texto nas imagens**

---

## ✅ CHECKLIST DIÁRIO

- [ ] Tema escolhido (lista-roteiros.md)
- [ ] JSON gerado (roteiro + 6 cenas)
- [ ] Dados verificados (Perplexity)
- [ ] Texto revisado (Opus)
- [ ] Narração gravada (celular)
- [ ] 6 imagens/vídeos gerados
- [ ] Vídeo editado (Kdenlive)
- [ ] Publicado (Shorts + TikTok + Reels)
- [ ] Tema ticado na lista
