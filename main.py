"""code en continuité de l'exercice Suites de Siracuse, 
pour stocker les valeurs de la suite"""
#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """afficher le shema de la suite lsyr"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr))) #[ i for i in range(len(lsyr)) ] erreur dans la notation,
    #demande d'ajouter list(range(...)).
    # Quand on modifie, demande d'ajouter encore un list(...) etc
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    # votre code ici

    l = [ ]
    if n==1:
        return 1
    i=0
    while n!=1:
        l.append(n)
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        i+=1
    l.append(1)
    return l
def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    #votre code ici

    return len(l)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    tva=1
    while l[0]<l[tva] :
        tva+=1
    return tva

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # votre code ici

    return max(l)

#### Fonction principale

def main():
    """fonction principale"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))


if __name__ == "__main__":
    main()
