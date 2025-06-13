# 🏡 Sistema de Controle para Casa Inteligente

Este projeto simula uma central de controle para dispositivos inteligentes em uma residência. Ele utiliza conceitos de **Programação Orientada a Objetos (POO)** em Python para gerenciar dispositivos como lâmpadas, termostatos e fechaduras de forma unificada.

---

## 💡 Objetivo

Implementar um sistema modular e extensível que permita controlar diversos dispositivos inteligentes **sem que a central precise saber como cada um funciona internamente**. O foco é aplicar conceitos fundamentais da POO:

- ✅ Classes Abstratas  
- ✅ Herança  
- ✅ Polimorfismo  
- ✅ Encapsulamento  

---

## 🛠 Tecnologias Utilizadas

- Python 3  
- Programação Orientada a Objetos (POO)

---

## 📁 Estrutura do Projeto

ControladoraCasa/
├── dispositivos.py # Contém as classes Lampada, Termostato e Fechadura
├── controladora.py # Contém a classe ControladoraCasa
├── main.py # Arquivo principal que executa o sistema
└── README.md # Documentação do projeto

---

## 🔧 Funcionalidades

- Adicionar dispositivos à central
- Ligar todos os dispositivos
- Desligar todos os dispositivos
- Exibir status atual de todos os dispositivos

---

## 🧠 Conceitos de POO Aplicados

- Classe Abstrata: DispositivoInteligente define um contrato obrigatório para todos os dispositivos.
- Herança: Lampada, Termostato e Fechadura herdam de DispositivoInteligente.
- Polimorfismo: A central envia comandos genéricos (ligar, desligar, obter_status), mas cada dispositivo reage conforme sua natureza.
- Encapsulamento: O estado interno de cada dispositivo é protegido e manipulado somente através de métodos.

---

## 👨‍💻 Autoria

Desenvolvido por **Leonardo S. Batschauer**  Estudante de **Análise e Desenvolvimento de Sistemas** no **IFSC**
