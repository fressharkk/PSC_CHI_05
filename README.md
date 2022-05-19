# PSC-CHI05
# Chimie et Machine Learning : Etude de la rétrosynthèse

Ce GitHub présente le travail réalisé au cours du PSC_CHI05 (X20). Il s'agit notamment d'une étude réalisée sur la rétrosynthèse via l'utiliation du machine learning.
Après avoir tenté de développer des modèles "simples" de notre côté, nous avons ensuite tenté de développer des modèles de Tranfer Learning basé sur l'algorithme AiZynthFinder dont le code se trouve dans le dossier Autres. 

Nous avons tenté de rendre les résultats au maximum reproductibles par ceux qui le souhaitent. Nous décrivons ainsi les étapes pour parvenir à exploiter ce GitHub.
Il faut noter entre autres que dans la section Résultats, tous les résultats ne sont pas présentés mais ils sont tous reproductibles. 

Nous joignons également le rapport en PDF de ce PSC. 

## Installation 

Il faut d'abord installer certaines bibliothèques et/ou modules. Pour les bibliothèques habituelles, on peut utiliser l'instruction pip ou anaconda. 

### Bibliothèques de base :
  Numpy
  
  Pandas
  
  Rdkit
  
  Pickle
  
  Tqdm
### Bibliothèques liées au Machine Learning : 
  Scikit-Learn
  
  Tensorflow
  
### Installation de AiZynthFinder :

Il faut d'abord executer la commande suivante dans une console (Linux) ou sur Anaconda Prompt (Windows) :

    conda env create -f https://raw.githubusercontent.com/MolecularAI/aizynthfinder/master/env-users.yml
    
Mettre à jour ensuite avec la commande suivante : 

    conda env update -n aizynth-env -f https://raw.githubusercontent.com/MolecularAI/aizynthfinder/master/env-users.yml
    


    conda activate aizynth-env
## Quick start
The main files you need to read for a quick start are train_model.py and rnn_testing.ipynb, to train you model and then compute the results on some of our test files
