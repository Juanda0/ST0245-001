def permutationAux( respuesta,  pregunta):
  if len(pregunta) == 0:
    print(respuesta)
  else:
     for i in range(0, len(pregunta)):
       permutationAux(respuesta + pregunta[i],
       pregunta[0:i] + pregunta[i+1:])

print(permutationAux("", "abcd"))

# -¿Cual es la complejidad asintotica del algoritmo para el peor caso?
# -No lo sé tú dime profe >:C
