package q178871;

// 달리기 경주
// https://school.programmers.co.kr/learn/courses/30/lessons/178871

import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> map = new HashMap<>();

        for(int i = 0; i < players.length; i++) {
            map.put(players[i], i);
        }

        for(String  calling : callings) {
            int index = map.get(calling);

            players[index] = players[index - 1];
            players[index - 1] = calling;

            map.put(players[index - 1], index - 1);
            map.put(players[index], index);
        }


        return players;
    }
}