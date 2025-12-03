# Ask yourself these fundamental questions:

## 🎯 What skill should the agent learn?
- **Navigate through a maze?** Yes
- **Balance and control a system?** Control ghost positions
- **Optimize resource allocation?** When to eat "Power Pellets"
-  **Play a strategic game?** No

## 👀 What information does the agent need?
- **Position and velocity?** Yes
- **Current state of the system?** Yes
- **Historical data?** A few frames to see last movements of player and ghosts
- **Partial or full observability?** Full but we can make player not see ghost as a aditional chalange

## 🎮 What actions can the agent take?
- **Discrete choices (move up/down/left/right)?** Yes
- **Continuous control (steering angle, throttle)?** No
- **Multiple simultaneous actions?** No

## 🏆 How do we measure success?
- **Reaching a specific goal?** Higher Score, less Deaths and less tie
- **Minimizing time or energy?** Minimizing time
- **Maximizing a score?** Yes
- **Avoiding failures?** Yes
- **More:**
    - Pellets eaten (efficiency metric)
    - Ghost evasion (survival skill)
    - Power pellet timing (strategic skill)


## ⏰ When should episodes end?
- **Task completion (success/failure)?** Yes
- **Time limits?** We can add
- **Safety constraints?** No



# Aqui está o significado de cada campo do `info`:

**`lives: 0`**
- Vidas restantes do Pacman
- 0 = Game Over (morreu todas as vidas)

**`episode_frame_number: 1841`**
- Número de frames **neste episódio** específico
- 1841 frames ≈ 30 segundos (60 fps)

**`frame_number: 11865`**
- Número **total** de frames desde que o ambiente foi criado
- Conta através de múltiplos episódios

## 🎮 Informação do Episódio (Stable Baselines3):

**`episode: {'r': 270.0, 'l': 461, 't': 226.557548}`**
- **`r` (reward)**: Score total do episódio = **270 pontos** 🎯
- **`l` (length)**: Duração do episódio = **461 steps**
- **`t` (time)**: Tempo real decorrido = **226.56 segundos**

**`TimeLimit.truncated: False`**
- `False` = Episódio terminou naturalmente (game over)
- `True` = Episódio foi interrompido por limite de tempo/steps

## 🖼️ Observação Terminal:

**`terminal_observation: array([[[...]], shape=(3, 210, 160)])`**
- **Último frame** do jogo antes de terminar
- Shape `(3, 210, 160)` = 3 canais RGB, 210 altura, 160 largura
- Útil para análise post-mortem do estado final

**Resumo deste episódio:**
- ✅ Score: **270 pontos**
- ⏱️ Duração: **461 steps** (~7.7 segundos de jogo real)
- 💀 Terminou por **game over** (não por timeout)