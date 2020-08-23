def adn(chain1, chain2):
    if(len(chain1) == 0 or len(chain2) == 0):
        return 0
    elif(chain1[len(chain1)-1] == chain2[len(chain2)-1]):
         return adn(chain1[0:len(chain1)-1], chain2[0:len(chain2)-1])+1
    else:
      return max(adn(chain1[0:len(chain1)-1], chain2), adn(chain1, chain2[0:len(chain2)-1]))

