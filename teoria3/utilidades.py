def promedioLista(Lista):
    return sum(Lista) / len(Lista) if Lista else 0

def sumaLista(Lista):
    return sum(Lista)


__all__ = ["promedioLista", "sumaLista"]