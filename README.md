<<<<<<< HEAD
# Search Algorithm
## Based on Minimum Edit Distance Algorithm

It is dynamic Programming algorithm that is very popular in NLP tasks for creating <em>auto correct</em> and <em>spelg corrector</em> like applications as
=======
# Search Algorithm using the Minimum Edit Distance

## The search algorithm is mainly based on: <em>Minimum Edit Distance</em>

The algorithm is very popular in NLP to help create systems like auto-correct and spell checker just like we see in our smartphones.

### What is Minimum Edit Distance

It is the minimum number of editing operations such as insertion, deletion or substitution needed to transform the source word into the target word. 

### How does it work?

1. The algorithm takes in a query or source word and a target word as input.
2. It uses dynamic programming methodology to compute and store the distances in a matrix notation.
3. There is a cost associated with each operation performed.
4. The value at the nth row and mth column gives the minimum edit distance between the two words (where n and m are the lengths of source and target word respectively).

The below image is an example of how the distance matrix looks.
The source word is <em>intention</em> and target word is <em>execution</em>


<img src = "https://ychai.uk/notes/images/Min-edit-distance.png">
>>>>>>> f44515476f24c89a1dcdcc3a3c1be4822acab61e
