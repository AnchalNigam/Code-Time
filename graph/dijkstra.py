# in this algo, main scene is use bfs technique but use priority queue why?
# because here edges are coming with weights and weights obvio j kam hga that we will
# take..and if we have visited any node with less weight then why to again wvisit that 
# node with higher wight. ao visited aray to track visited node and always less wight will be at top
# wil give prioerity to viist further node and again heapify will make smaller node at top
# my doubt came why prioerty because aagle jake shorter dis h skta hai but isme scene kya hta hai
# hare paas initially j node 1st node enter ki the queue me toh uska higher wight wala hga 
# but hm prioroty chota wale k de rhe hai and dete rhnge but if we find that further path 
# lesser then will switch to that path and for every node multiple path hga toh chote wale se h
# pahuchnge yahn


# time complexiy - (N+E)log N - (n is nde, e is edges, logn is becaue of priority queue)
# space is o(n)+o(n) - prioerity queue+visited