In this problem, we have been given a directed weighted graph containing no negative cycles. 
We will consider a source node S from which we will calculate the distance to another 
destination node V which will also be given. In this problem the edge weight denotes the to be 
covered distance between two nodes by traversing through that edge. Here, we also need to find 
the path that will help us to reach the destination. As there can be multiple paths, to reach a 
destination, our solution needs to be able to find all the shortest paths or routes. For this problem, 
we can safely assume that, there will not be more than 10 shortest paths between any two nodes. 
 
To solve this problem, we initialize a vector array for traversing all the node using Dijkstra and a 
2D path vector to store multiple path. After iterating over Dijkstra algorithm we find the 
minimum distance and store it in d[]. Then we use a pathPrinting function to print all the possible 
paths for a minimum distance. 
