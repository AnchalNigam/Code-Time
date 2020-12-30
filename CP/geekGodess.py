T = int(input())
pokemonCardsAtDthDay = []
def findNumOfPokemonCards(mistyCardNum, friendCardPerDay, day):
  return mistyCardNum + (day-1)*friendCardPerDay


for t in range(T):
  requiredData = list(map(int,input().split()))
  pokemonCardsAtDthDay.append(findNumOfPokemonCards(requiredData[0], requiredData[1], requiredData[2]))

for cardsNum in pokemonCardsAtDthDay:
  print(cardsNum)

