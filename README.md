# Informations générales

## Introduction
Nous réalisons ce projet dans le cadre d'une étude de cas, nommée "Au bon beurre" d'un module de DevOps.
L’objectif pédagogique est d’amener les équipes de 4 à mettre en commun les compétences de développement, de réseaux, d’infrastructure, d’outil ainsi que de gestion de projet (équipes, compétences, urgent / important). Les deux axes principaux du DevOps sont abordés : intégration multi compétences ainsi que intégration des processus de développement et de production.

## Auteurs
 - Auriane LABILLE, spécialité développement web 
 - Jérémie DELÉCRIN, spécialité développement web 
 - Léone LALLOUÉ, spécialité développement web 
 - Sébastien PLOTTU, spécialité développement cyber sécurité


# Structure

## Fonctionnalités
 - Automates
 - Récupération des données
 - Exploitation des données
 - Plate-forme (Debian, MariaDB, NGINX, GitHub)
 - Interconnexion entre Jenkins et GitHub
 - Gestion des droits des utilisateurs
 - Sécurité des échanges
 - Compression et chiffrement de la base
 - Dump de la base

## Déploiement
**![](https://lh5.googleusercontent.com/b5vm21rWgdLNBSfFVBcvhe9kjnHwPaiTZK4jTJrbWLxnogsYxZVx7_lGkbL-NmeKtsUOWqDkd8hutzYLsZOPMWE7fcpX6So7OCdTK1-MI1xtG8leToDfQcS6IEUL4Hzuhts9TAx8)**

## Compilation
    docker-compose build
    
    docker-compose up

## API
| Chemins | Utilisations |
|--|--|
| / | Tableau de bord d'administration / Dashboard |
| /data | Récupération des données des premiers automates des unités |
| /robot (exemple : `/robot?unit=1&robot=1`) | Récupération des informations d'un automate d'une unité précise, prenant en paramètres "unit" et "robot" |

## Technologies
 - Éditeur de code  : [Visual Studio Code](https://code.visualstudio.com/) 
 - Gestionnaire de code : [GitHub / Github Desktop](https://github.com/) 
 - Gestion de projet : [Notion / Kanban](https://www.notion.so/product) 
 - Création des schémas : [Figma](https://www.figma.com/) 
 - Intégration continue : [Jenkins](https://www.jenkins.io/) 
 - Rédaction du support :  [Google Docs / Google Slide](https://www.google.com/intl/fr-CA/docs/about/) 

## Historique des versions
| Technologies | N° |
|--|--|
| Python | 2.7 |
| Debian | 9.13 |
| Jenkins | 2.249.3 |
| Java | 1.8.0 |
| MariaDB | 10.4 |
| NGINX | 1.10.3 |
et
| Plugins | N° |
|--|--|
| attrs | 20.3.0 |
| bcrypt | 3.1.7 |
| cached-property | 1.5.2 |
| certifi | 2020.11.8 |
| cffi | 1.14.3 |
| chardet | 3.0.4 |
| cryptography | 3.2.1 |
| distro | 1.5.0 |
| docker | 4.3.1 |
| docker-compose | 1.27.4 |
| dockerpty | 0.4.1 |
| docopt | 0.6.2 |
| idna | 2.10 |
| importlib-metadata | 2.0.0 |
| jsonschema | 3.2.0 |
| paramiko | 2.7.2 |
| peewee | 3.14.0 |
| pycparser | 2.20 |
| pycurl | 7.43.0 |
| pygobject | 3.22.0 |
| PyNaCl | 1.4.0 |
| pyrsistent | 0.17.3 |
| python-apt | 1.4.1 |
| python-dotenv | 0.15.0 |
| PyYAML | 5.3.1 |
| requests | 2.24.0 |
| six | 1.15.0 |
| texttable | 1.6.3 |
| unattended-upgrades | 0.1 |
| urllib3 | 1.25.11 |
| websocket-client | 0.57.0 |
| zipp | 1.2.0 |
| Blue Ocean | 1.24.3 |
