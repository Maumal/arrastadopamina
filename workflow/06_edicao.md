# ✂️ FASE 6: EDIÇÃO (~15 min)

## Objetivo
Montar o vídeo final no Kdenlive.

---

## Abrir Kdenlive
```bash
kdenlive
```

---

## Passo a Passo

### 1. Criar projeto novo
- Resolução: **1080 x 1920** (vertical 9:16)
- FPS: **30**
- Nome: `shortXX`

### 2. Importar arquivos
Arraste para a biblioteca:
- `assets/temp/teste_shortXX.mp3` (áudio)
- `assets/temp/clipe1_hook.mp4` até `clipe8_cta.mp4`
- `assets/music/lofi_background.mp3` (opcional)

### 3. Montar timeline

```
TRILHA DE VÍDEO:
[clipe1][clipe2][clipe3][clipe4][clipe5][clipe6][clipe7][clipe8]
   8s     8s     8s     8s     8s     8s     8s     8s

TRILHA DE ÁUDIO:
[=================== NARRAÇÃO ===================]

TRILHA DE MÚSICA (opcional):
[=============== LO-FI 8% VOLUME ================]
```

### 4. Ajustar legendas
- Menu: **Projeto > Legendas**
- Importe o arquivo SRT ou adicione manualmente
- Estilo recomendado:
  - Fonte: **Montserrat Bold** ou **Impact**
  - Tamanho: **48-60**
  - Cor: **Amarelo** (#FFD700)
  - Borda: **Preto**, 2px
  - Posição: **Centro-inferior**

### 5. Ajustar clipes
- Cada clipe deve ter **8 segundos**
- Adicione transição suave (cross dissolve 0.5s) se quiser

### 6. Exportar
- Menu: **Projeto > Renderizar**
- Perfil: **YouTube 1080p**
- Codec: **H.264**
- Nome: `shortXX_final.mp4`
- Salvar em: `assets/output/`

---

## Atalhos Úteis

| Ação | Atalho |
|------|--------|
| Play/Pause | Espaço |
| Cortar clipe | Shift + R |
| Desfazer | Ctrl + Z |
| Zoom timeline | Scroll mouse |
| Renderizar | Ctrl + Enter |

---

## Checklist
- [ ] Projeto criado em 1080x1920
- [ ] 8 clipes na timeline
- [ ] Áudio sincronizado
- [ ] Legendas estilizadas
- [ ] Música de fundo (8% volume)
- [ ] Vídeo exportado
