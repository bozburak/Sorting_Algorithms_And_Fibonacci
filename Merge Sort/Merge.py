#/usr/bin/env python
# -*- coding: utf-8 -*-


def yonet(ilk_parca, ikinci_parca):
    c = []
    while len(ilk_parca) != 0 and len(ikinci_parca) != 0:
        if ilk_parca[0] < ikinci_parca[0]:
            c.append(ilk_parca[0])
            ilk_parca.remove(ilk_parca[0])
        else:
            c.append(ikinci_parca[0])
            ikinci_parca.remove(ikinci_parca[0])
    if len(ilk_parca) == 0:
        c = c + ikinci_parca
    else:
        c = c + ilk_parca
    return c

def bol(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        kes = len(x)/2
        ilk_parca = bol(x[kes:])
        ikinci_parca = bol(x[:kes])
    return yonet(ilk_parca, ikinci_parca)

print bol([90,80,100,1])