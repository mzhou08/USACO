#include <vector>
#include <iostream>
/*
Sample Input:
2
5 2
1 2
4 5
5 3
1 2
2 3
4 5

Sample Output:
2
1
*/
int shortest_to_1(int start, std::vector< std::vector<int> > connections, int curr_cost, std::vector<bool> visited) {
    visited[start - 1] = true;

    if (start == 1) return curr_cost;

    for (int i = 0; i < connections[start - 1].size(); i++) {
        if (!visited[i]) {
            curr_cost = std::min(shortest_to_1(connections[start - 1][i], connections, curr_cost, visited), curr_cost);
        }
    }


    visited[start - 1] = false;
    return curr_cost;
}


int main() {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        int M;
        std::cin >> N >> M;
        
        std::vector< std::vector<int> > connections(M);
        for (int j = 0; j < M; j++) {
            int end1;
            int end2;

            std::cin >> end1 >> end2;

            connections[end1].push_back(end2);
            connections[end2].push_back(end1);
        }

        std::vector<bool> visited(M, false);
        std::cout << shortest_to_1(M - 1, connections, 0, visited);
    }
}