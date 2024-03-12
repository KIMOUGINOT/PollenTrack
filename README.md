# PollenTrack

<div style="text-align: right;">
    <img src="image/Logo_Pollentrack.png" alt="Description de l'image" width="200" height="200">
</div>

## Architecture du projet


## Algorithme de prise de photo
Le problème majeur est de réussir à prendre une photo qui n’est pas floue. Je souhaiterai donc créer un code qui permet de faire le focus d’une image. 

Pour déterminer si une image est nette ou pas, on s’intéresse au bord des objets qui se trouvent dans l’image. On les reconnait par une subite forte variation de l’intensité des pixels. Plus la variation est forte, plus l’image est nette. Au contraire, plus la variation est “diffuse”, moins l’image est nette. On a donc affaire à un problème de traitement d’image.

Il existe de nombreux algorithmes de détection de bord comme ‘canny’ par exemple qui sont déjà implémenté en python dans le module opencv.

- On ne veut pas faire le focus de l’image mais se focus sur une partie de l’image seulement qui est la zone où on a détecté un grain de pollen.
Il faudrait donc commencer par détecter un grain de pollen dans l’image puis se concentrer sur cette zone. Pour cela j'effectue la détection des contours de l'image afin de pouvoir ensuite déterminer l'objet le plus grand (jugé plus pertinent). Je découpe maintenant le tour de l'objet et j'obtient ainsi une sous-image qui est celle sur laquelle on déterminera si la photo est floue. Toutes les opérations se feront sur celle-ci.
- Une fois cette zone trouvée, on veut savoir à quel point elle est floue. Pour cela, il faut d’abord créer un algo qui détermine “le taux de netteté” d’une image. Pour l'instant j'utilise la variance du filtre laplacien comme taux de netteté (l'objectif est de maximiser cette variance pour avoir un taux de netteté maximum) mais ce système détermine le taux de netteté en parti en se basant sur les auréoles autour des grains de pollen. Je n'obtient donc pas forcément la meilleure netteté sur le grain de pollen en lui-même. Il semblerait que les auréoles soient causées par une réaction chimique le scotch et les grains de pollen. Une solution peut-être de réaliser plusieurs acquisitions avec différents focus : c'est à dire qu'une fois que le focus est fait, on capture des images en dezoomant un peu et zoomant un peu.
- Connaissant cela, il faut maintenant y aller à tatillon : on actionne le moteur pour zoomer quelque peu (déterminer de combien on bouge) la caméra et à chaque itération on regarde si le taux de netteté est meilleure que précédemment. Si le taux est meilleur, on zoom et si il est pire on dézoom. On itère jusqu’à un taux qui nous convient.
- On peut ainsi prendre la photo.