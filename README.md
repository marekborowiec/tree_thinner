# tree_thinner.py
Extracts the desired number of trees from a MrBayes posterior tree file

Given burnin and trees_number this program extracts 
the desired number of trees from the posterior 
and writes a new file.

Usage:
```
    tree_thinner.py [your_sample_file] [burnin] [trees_number] [format] > new_file.txt
```
Example:
```
    tree_thinner.py my_ants_20m.run1.t 5000 1000 mrbayes > thinned_my_ants.run1.txt
```
Available formats: `mrbayes` for MrBayes v3.2 and `beast` for BEAST2
