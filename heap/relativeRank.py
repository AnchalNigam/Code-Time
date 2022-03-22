def relativeRank(score):
  dic = {}
  for i in score:
      dic[i] = ""
  # print(dic)
  sortScore = sorted(score, reverse=True)
  # print(sortScore)
  n = len(score)
  for i in range(n):
      if i == 0:
          dic[sortScore[i]] = "Gold Medal"
      elif i == 1:
            dic[sortScore[i]] = "Silver Medal"
      elif i == 2:
            dic[sortScore[i]] = "Bronze Medal"
      else:                
          dic[sortScore[i]] = str(i+1)
  # print(dic)
  res = []
  for i in score:
      res.append(dic[i])
  return res
      
        
        
                
        