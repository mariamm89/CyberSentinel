# 🛡️ CyberSentinel

**Mini-SIEM en Python pour détecter les tentatives de force brute.**

## Présentation

CyberSentinel est un projet pédagogique de cybersécurité qui analyse des journaux de connexion afin de détecter des comportements suspects, notamment plusieurs échecs d'authentification depuis une même adresse IP sur une courte période.

Le projet comprend un moteur de détection Python et un tableau de bord interactif réalisé avec Streamlit.

## Fonctionnalités

- Génération de journaux de connexion fictifs.
- Analyse des événements avec Pandas.
- Détection de tentatives de force brute selon une règle configurable.
- Classification des alertes par niveau de sévérité.
- Visualisation des résultats dans un tableau de bord.
- Export des alertes au format CSV.

## Technologies utilisées

- Python
- Pandas
- Streamlit
- Git et GitHub

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/mariamm89/CyberSentinel.git
cd CyberSentinel
```

Créer un environnement virtuel sous Windows :

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```powershell
python -m pip install pandas streamlit
```

## Exécution

Générer les journaux de test :

```powershell
python generate_logs.py
```

Lancer la détection :

```powershell
python detector.py
```

Démarrer le tableau de bord :

```powershell
streamlit run app.py
```

Ouvrir ensuite l'adresse locale affichée dans le terminal.

## Résultat du test

Sur le jeu de données fictif initial, le système a analysé 12 événements et détecté une alerte correspondant à cinq échecs de connexion en cinq minutes ou moins.

Cette détection signale un comportement suspect compatible avec une tentative de force brute. Elle ne prouve pas, à elle seule, qu'une attaque réelle a eu lieu.

## Limites et améliorations futures

- Ajouter des graphiques de sécurité.
- Enrichir les règles de détection.
- Ajouter des tests automatisés.
- Améliorer la validation des journaux.
- Documenter les limites et les faux positifs.

## Avertissement

Ce projet est destiné à l'apprentissage et utilise des données fictives. Il ne remplace pas une solution SIEM de production.
