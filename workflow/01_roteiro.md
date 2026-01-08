# 📝 FASE 1: ROTEIRO (~10 min)

## Objetivo
Gerar roteiro + cenas surrealistas em um único passo.

---

## NOVO: Prompt Unificado v2.0

O prompt `assets/roteiros/prompt_gerar_roteiro_v2.txt` gera TUDO de uma vez:
- Roteiro narrável (30-60s)
- 6 cenas surrealistas
- Prompts de geração prontos

---

## Passo a Passo

### 1. Escolha o tema
Abra `assets/roteiros/lista-roteiros.md` e escolha um **não ticado**.

### 2. Abra o GPT e cole

```
[COLE TODO O CONTEÚDO DE prompt_gerar_roteiro_v2.txt]

TEMA: [SEU TEMA AQUI]
```

### 3. Receba o JSON completo

O GPT vai retornar:
```json
{
  "titulo": "...",
  "duracao_total_segundos": 45,
  "conteudo": "...",
  "fonte_cientifica": "...",
  "dica_pratica": "...",
  "cenas": [
    {
      "numero": 1,
      "descricao": "...",
      "duracao_segundos": 5,
      "trecho_narrado": "...",
      "prompt_geracao": "Surrealist digital painting..."
    }
  ]
}
```

### 4. Salve o resultado
`assets/roteiros/shortXX.json`

---

## Estilo Visual (já incluído no prompt)

- Surrealismo estilo Salvador Dalí
- Tons: dourado, vermelho sangue, azul profundo
- Fundo: escuro com neblina
- Formato: vertical 9:16

---

## Ferramentas

| Função | Ferramenta |
|--------|-----------|
| Roteiro + Cenas | GPT-4 |
| Backup roteiro | Claude Sonnet |

---

## Checklist
- [ ] Tema escolhido da lista
- [ ] Prompt v2.0 usado
- [ ] JSON salvo com cenas e prompts
