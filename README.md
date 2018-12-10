# Identifying and removing bias from Neural Nets

The files in this code base can be used to replicate the experiments and results in report.pdf

## Joint-Learning-Unlearning.ipynb
This python notebook contains the implementation of the JLU training algorithm. 

## tSNE.ipynb
This python notebook contains the implementation to load model variable and prepare tsv file for t-SNE embeddings.

## test-networks-on-specific-datasets.ipynb
This python notebook contains the implementation to load a model and test it on specific datasets.

## CSV's used
* gen\_list.csv: For the dataset OD, gender labels. 1: MALE, 0: FEMALE (always this notation is used)
* age\_list.csv: For the dataset OD, age labels.
* gen\_list\_balanced.csv: For the dataset EBD, gender labels.
* age\_list\_balanced.csv: For the dataset EBD, age labels.
* gen\_list\_extreme\_biased.csv: For the dataset BD, gender labels.
* age\_list\_extreme\_biased.csv: For the dataset BD, age labels.

