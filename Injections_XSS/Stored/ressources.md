Injections de HTML sont aussi appelées Cross-Site Scripting (XSS).

Pour se proteger echapper les caracteres speciaux <, >, &, ", ', …  ce qui est fait ici avec certains caracteres.

L'input ne peut contenir qu'une seule lettre parmi p, a, r, t, i, c, l, e, s

The flag is : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e

Comment l'éviter :
htmlspecialchars en PHP par exemple