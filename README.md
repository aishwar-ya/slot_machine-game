<div align="center">

<img src="hero.svg" alt="Slot Machine Game - spin the reels, chase the jackpot" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal](https://img.shields.io/badge/Runs%20in-Terminal-000000?style=for-the-badge&logo=gnometerminal&logoColor=white)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-2E7D32?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-Console%20Game-FF6F00?style=for-the-badge)

<br/>

**[✨ Features](#-features)** &nbsp;|&nbsp;
**[🖥️ Demo](#️-demo)** &nbsp;|&nbsp;
**[🔄 How It Works](#-how-it-works)** &nbsp;|&nbsp;
**[▶️ How to Run](#️-how-to-run)** &nbsp;|&nbsp;
**[🎓 What You Learn](#-what-you-learn)**

</div>

---

## 📖 About

A simple slot machine game built with **Python** using the `random` module.

Each spin randomly selects **three symbols**. Land three `7️⃣` and you hit the **jackpot**! After every spin, you decide whether to play again.

> 🎯 **Goal:** Get **7️⃣ | 7️⃣ | 7️⃣** on the reels.

The game uses four symbols (🍒 🍇 🍉 7️⃣), each equally likely on every reel, so the jackpot comes up about **1 in 64 spins**.

---

## ✨ Features

| | |
|:---|:---|
| 🎲 **Random reels** | Three symbols are picked randomly on every spin |
| 💰 **Jackpot system** | Three `7️⃣` symbols win the jackpot |
| 🔁 **Replay option** | A `while` loop lets you keep playing |
| ⌨️ **Simple input** | Type `N` to quit; any other answer plays another round |
| 🌱 **Beginner-friendly** | Short, readable code, ideal for learning Python |

---

<div align="center"><img src="section-demo.svg" alt="Spin the reels" width="100%"/></div>

## 🖥️ Demo

```text
🍇 | 🍉 | 🍒
Thanks for Playing!!
Play again? (Y/N): Y

7️⃣ | 7️⃣ | 🍒
Thanks for Playing!!
Play again? (Y/N): Y

7️⃣ | 7️⃣ | 7️⃣
Jackpot!!
Play again? (Y/N): N

Game Over!
```

---

<div align="center"><img src="section-how.svg" alt="Chase the jackpot" width="100%"/></div>

## 🔄 How It Works

```mermaid
flowchart TD
    A([🎰 Start game]) --> B[🎲 Pick 3 random symbols]
    B --> C[🖥️ Show the reels]
    C --> D{7️⃣ 7️⃣ 7️⃣ ?}
    D -->|Yes| E[💰 Jackpot!!]
    D -->|No| F[🙂 Thanks for Playing!!]
    E --> G{🔁 Play again? Y/N}
    F --> G
    G -->|Y| B
    G -->|N| H([🛑 Game Over!])

    style A fill:#FFF8E1,stroke:#F9A825,color:#E65100
    style E fill:#E8F5E9,stroke:#388E3C,color:#1B5E20
    style H fill:#FFEBEE,stroke:#C62828,color:#B71C1C
```

---

<div align="center"><img src="section-run.svg" alt="Press play" width="100%"/></div>

## ▶️ How to Run

**Requirements:** [Python 3](https://www.python.org/downloads/) installed on your computer.

**1️⃣ Download or clone the project**

**2️⃣ Open a terminal in the project folder**

**3️⃣ Run the game**

```bash
python slot_machine.py
```

> 💡 On some systems you may need to use `python3 slot_machine.py` instead.

---

## 🎓 What You Learn

| Concept | Where it's used |
|:---|:---|
| 🎲 **`random` module** | Picking random symbols for each spin |
| 🔁 **`while` loop** | Replaying the game until the player quits |
| 🔀 **Conditions (`if` / `else`)** | Checking for the jackpot |
| ⌨️ **User input** | Reading the `Y` / `N` answer |

---

## 🔮 Ideas to Extend

- [ ] 🪙 Add a starting balance and betting
- [ ] 🍋 Add more symbols and smaller prizes
- [ ] 🎨 Add colors to the terminal output
- [ ] 🏆 Track wins and total spins
- [ ] 🔊 Add sound effects

---

<div align="center">

<img src="footer.svg" alt="Thanks for playing" width="100%"/>

*Made with Python & 🍀*

</div>
