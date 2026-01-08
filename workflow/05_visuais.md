# 🎬 FASE 5: VISUAIS (~15 min)

## Objetivo
Gerar 6 imagens/vídeos surrealistas sincronizados com o roteiro.

---

## NOVO WORKFLOW: Visual Surrealista

### Stack de Ferramentas
| Etapa | Ferramenta | Observação |
|-------|-----------|------------|
| Roteiro + Cenas | GPT | Usa prompt_gerar_roteiro_v2.txt |
| Imagens | GPT/DALL-E | Melhor qualidade |
| Vídeos | Gemini Veo | Boa qualidade, tem marca d'água |
| Alternativa | Ideogram | Grátis, estilo mais ilustrativo |

---

## PASSO 1: Gerar Roteiro + Cenas (já feito na Fase 1)

O prompt `assets/roteiros/prompt_gerar_roteiro_v2.txt` já gera:
- Roteiro narrável
- 6 cenas com descrição
- Prompt de geração pronto para cada cena

---

## PASSO 2: Gerar Imagens/Vídeos

### Opção A: Imagens (GPT/DALL-E)
1. Abra o GPT
2. Cole cada `prompt_geracao` do JSON
3. Salve as 6 imagens

### Opção B: Vídeos (Gemini Veo)
1. Abra o Gemini
2. Peça: "Gere um vídeo vertical 9:16 de 5 segundos: [prompt]"
3. Baixe os vídeos (terá marca d'água)

---

## Estilo Visual Padrão

```
Surrealist digital painting, Dalí style, vertical 9:16, 
dark misty background, golden and blood red tones. 
[DESCRIÇÃO DA CENA]. 
Dreamlike atmosphere, dramatic lighting. No text.
```

### Regras do Estilo:
- Surrealismo estilo Salvador Dalí
- Tons: dourado, vermelho sangue, azul profundo
- Fundo: escuro com neblina
- Formato: vertical (9:16)
- SEM texto na imagem

---

## Estrutura das 6 Cenas

| Cena | Tempo | Função |
|------|-------|--------|
| 1 | 0-5s | HOOK - impacto visual imediato |
| 2 | 5-13s | Cena cotidiana com tensão |
| 3 | 13-21s | Compra impulsiva visual |
| 4 | 21-29s | Revelação científica |
| 5 | 29-37s | Regra prática visual |
| 6 | 37-45s | Encerramento + CTA |

---

## Salvar os Arquivos

```
assets/temp/
├── cena1_hook.png (ou .mp4)
├── cena2_tensao.png
├── cena3_impulso.png
├── cena4_ciencia.png
├── cena5_regra.png
└── cena6_cta.png
```

---

## Efeito Ken Burns (se usar imagens)

No Kdenlive, aplique movimento em cada imagem:
- Zoom lento (5% em 5 segundos)
- Pan suave de um lado ao outro
- Evita sensação de "slideshow estático"

---

## Checklist

- [ ] JSON do roteiro tem os 6 `prompt_geracao`
- [ ] 6 imagens/vídeos gerados
- [ ] Todos em formato vertical (9:16)
- [ ] Estilo consistente (Dalí, escuro, dourado/vermelho)
- [ ] Salvos em assets/temp/
