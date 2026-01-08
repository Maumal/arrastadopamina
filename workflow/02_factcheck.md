# 🔍 FASE 2: FACT-CHECK (~5 min)

## Objetivo
Verificar se os dados científicos do roteiro são reais.

---

## Passo a Passo

### 1. Abra o Perplexity
https://www.perplexity.ai

### 2. Cole este prompt + seu roteiro

```
Aja como verificador de fatos (Fact-Checker).

Verifique a veracidade dos dados científicos citados no texto abaixo:
1. O estudo/pesquisa existe?
2. A instituição é real?
3. O número/percentual está correto?
4. O ano está correto?

SE ENCONTRAR ERRO: Forneça o dado correto.
SE ESTIVER CORRETO: Confirme "✅ Dados verificados"

TEXTO PARA VERIFICAR:
[COLE O CONTEÚDO DO SEU JSON AQUI]
```

### 3. Analise a resposta
- ✅ **Confirmado**: Prossiga
- ❌ **Erro encontrado**: Corrija o JSON antes de continuar

---

## Checklist
- [ ] Perplexity verificou os dados
- [ ] Correções aplicadas (se necessário)
- [ ] JSON atualizado
