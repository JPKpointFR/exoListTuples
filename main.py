noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]


def element_dans_liste(e, l):
    """for el in l:
        if e.lower() == el.lower():
            return True
    return False"""
    l_lower = [el.lower() for el in l]
    return e.lower() in l_lower


if element_dans_liste("jean", noms):
    print("Trouvé")
else:
    print("Pas Trouvé")
