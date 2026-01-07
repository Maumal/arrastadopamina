# 📘 MANUAL DE OPERAÇÃO: FÁBRICA DE VÍDEOS (PSICOLOGIA FINANCEIRA) 2026
# SISTEMA: LINUX / WEB
# OBJETIVO: 1 Vídeo Viral e Monetizável a cada 30 min.

---

## 🛠️ 0. CONFIGURAÇÃO INICIAL (FAZER UMA VEZ)

1. NAVEGADOR: Use Google Chrome ou Microsoft Edge (Evite Firefox para o CapCut Web).
2. CONTAS NECESSÁRIAS:
   - Google Gemini (Gratuito): Para roteiros e imagens.
   - Perplexity (Gratuito): Para conferir fatos.
   - CapCut Web (Gratuito): Para editar.
3. PASTA DE TRABALHO (No Linux):
   - Crie uma pasta: "CANAL_FINANCAS".
   - Dentro dela, salve este manual e o script de voz.

---

## 📋 PASSO A PASSO DA PRODUÇÃO (WORKFLOW)

### FASE 1: O ROTEIRO (Criação e Segurança)

1. GERAR TEXTO:
   - Abra o GEMINI.
   - Copie e cole o "PROMPT 1 - ROTEIRO" (localizado no fim deste arquivo).
   - O Gemini vai te dar um título e o texto da narração.

2. AUDITAR DADOS (Obrigatório):
   - Abra o PERPLEXITY.
   - Copie e cole o "PROMPT 2 - AUDITORIA" (localizado no fim deste arquivo) junto com os dados que o Gemini gerou.
   - SE o Perplexity disser que o número está errado -> Corrija o texto manualmente.
   - SE estiver certo -> Siga em frente.
   - *Nunca pule isso. O YouTube pune dados falsos.*

---

### FASE 2: O ÁUDIO (Voz Humanizada no Linux)

1. PREPARAÇÃO:
   - Certifique-se de ter o arquivo "gerar_voz.py" na sua pasta (Código no fim deste arquivo).
   - Abra o terminal na pasta e instale o pacote (uma vez só):
     pip install edge-tts

2. GERAR A VOZ:
   - No terminal, digite:
     python3 gerar_voz.py "COLE AQUI O TEXTO DO ROTEIRO JÁ CORRIGIDO ENTRE ASPAS"
   - Dê Enter.
   - Um arquivo chamado "narracao_final.mp3" vai aparecer na pasta.

---

### FASE 3: O VISUAL (Imagens sem Direitos Autorais)

1. VOLTE AO GEMINI:
   - Você precisa de 4 a 5 imagens para um vídeo de 55 segundos.
   - Não use rostos de famosos.

2. COMANDOS DE IMAGEM:
   - Use o "PROMPT 3 - IMAGENS" (fim do arquivo).
   - Gere:
     - 1 Imagem para o Início (Impactante/Triste/Chocante).
     - 2 Imagens de Contexto (Celular, Boleto, Mercado).
     - 1 Imagem de Gráfico (Abstrato, sem texto).
   - Salve as imagens na pasta.

---

### FASE 4: A MONTAGEM (CapCut Web)

1. IMPORTAÇÃO:
   - Abra o CapCut Web -> Criar Novo Vídeo (9:16 para Celular).
   - Arraste o arquivo "narracao_final.mp3" e as 5 imagens.

2. LINHA DO TEMPO:
   - Coloque o Áudio primeiro na linha de baixo.
   - Coloque as imagens na linha de cima, cobrindo todo o áudio.
   - *Regra:* Mude de imagem a cada 5 a 8 segundos.

3. MOVIMENTO (Essencial):
   - Clique na imagem na tela.
   - No menu à direita, procure "Escala" ou "Zoom".
   - Marque um ponto no início (Keyframe) e aumente um pouco o tamanho no final.
   - *Motivo:* Imagem parada faz a pessoa pular o vídeo.

4. LEGENDAS (O Segredo):
   - Menu lateral esquerdo -> Texto -> Legendas Automáticas -> Criar.
   - Selecione a legenda gerada.
   - Mude a fonte para uma GROSSA (Ex: Montserrat Bold ou The Bold Font).
   - Cor: Amarela ou Branca com borda Preta.
   - Tamanho: Grande e Centralizado.
   - *Correção:* Leia rapidinho para ver se tem erros de português.

5. EXPORTAR:
   - Resolução: 1080p.
   - Taxa de quadros: 30fps.

---

### FASE 5: PUBLICAÇÃO BLINDADA

1. TÍTULO: Use o que o Gemini criou.
2. DESCRIÇÃO:
   - Cole o roteiro.
   - Adicione no final: "Fonte: [Nome da Instituição checada no Perplexity]."
   - Adicione a frase de segurança: "Roteiro e narração gerados com auxílio de IA."
3. YOUTUBE STUDIO:
   - Na opção "Conteúdo Sintético/Alterado", marque "SIM".

---
---

# 🤖 ANEXOS: FERRAMENTAS (COPIE DAQUI)

### [ANEXO 1] PROMPT DE ROTEIRO (Para o Gemini)
Copie e cole isto no Gemini:

"Você é um roteirista sênior de YouTube Shorts sobre Psicologia Financeira.
Crie um roteiro de 50 a 60 segundos sobre o tema: [INSIRA O TEMA AQUI].
ESTRUTURA OBRIGATÓRIA:
1. HOOK (0-5s): Afirmação surpreendente com dado numérico.
2. DOR (5-15s): Exemplo cotidiano brasileiro (ex: iFood, boleto, fila).
3. EXPLICAÇÃO (15-40s): O porquê científico (cite Instituição e Ano).
4. SOLUÇÃO (40-50s): Dica prática de 1 frase.
5. CTA (50-55s): Chamada rápida.
REGRAS: Linguagem falada, natural, brasileira. Sem palavras difíceis."

---

### [ANEXO 2] PROMPT DE AUDITORIA (Para o Perplexity)
Copie e cole isto no Perplexity após ter o roteiro:

"Aja como verificador de fatos (Fact-Checker).
Verifique a veracidade dos dados científicos citados no texto abaixo.
1. O estudo existe?
2. O número está correto?
3. Se estiver errado, me forneça o dado real de uma fonte confiável.
TEXTO: [COLE O ROTEIRO AQUI]"

---

### [ANEXO 3] PROMPTS DE IMAGEM (Para o Gemini)
Use variações disto para gerar as imagens:

- Para o Início: "Foto cinematográfica vertical 9:16, close-up dramático de uma pessoa brasileira com expressão de preocupação segurando uma fatura, iluminação de contraste alto, fundo escuro."
- Para Contexto: "Foto realista vertical 9:16, ponto de vista em primeira pessoa (POV), mãos segurando um celular mostrando aplicativo de banco, fundo sala de estar à noite."
- Para Conceito: "Ilustração 3D conceitual, um cérebro humano feito de ouro, fundo minimalista escuro, alta qualidade."

---

### [ANEXO 4] SCRIPT PYTHON DE VOZ
Salve este código como um arquivo chamado "gerar_voz.py":

import sys
import asyncio
import edge_tts

# Configuração da Voz (Pode mudar para pt-BR-FranciscaNeural se quiser mulher)
VOZ = "pt-BR-AntonioNeural"
ARQUIVO_SAIDA = "narracao_final.mp3"

async def main():
    # Pega o texto que você digitar no terminal
    texto_usuario = sys.argv[1] if len(sys.argv) > 1 else "Teste de voz."
    
    print(f"🎤 Processando voz ({VOZ})...")
    
    communicate = edge_tts.Communicate(texto_usuario, VOZ)
    await communicate.save(ARQUIVO_SAIDA)
    
    print(f"✅ Pronto! Arquivo salvo como: {ARQUIVO_SAIDA}")

if __name__ == "__main__":
    asyncio.run(main())
