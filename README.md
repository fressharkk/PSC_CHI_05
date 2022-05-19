# PSC-CHI05
# Chimie et Machine Learning : Etude de la rétrosynthèse

Ce GitHub présente le travail réalisé au cours du PSC_CHI05 (X20). Il s'agit notamment d'une étude réalisée sur la rétrosynthèse via l'utiliation du machine learning.
Après avoir tenté de développer des modèles "simples" de notre côté, nous avons ensuite tenté de développer des modèles de Tranfer Learning basé sur l'algorithme AiZynthFinder dont le code se trouve dans le dossier Autres. 

Nous avons tenté de rendre les résultats au maximum reproductibles par ceux qui le souhaitent. Nous décrivons ainsi les étapes pour parvenir à exploiter ce GitHub.
Il faut noter entre autres que dans la section Résultats, tous les résultats ne sont pas présentés mais ils sont tous reproductibles. 

Nous joignons également le rapport en PDF de ce PSC. 

## Instalation 
### Dependencies
RDKit [https://github.com/rdkit/rdkit] (recommended version 2018_03_1 or later)

Syba [https://github.com/lich-uct/syba]

Tensorflow [https://www.tensorflow.org/install/pip?hl=fr]  (recommended version 1.15 or later)

## Quick start
The main files you need to read for a quick start are train_model.py and rnn_testing.ipynb, to train you model and then compute the results on some of our test files
