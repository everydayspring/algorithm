package q12982;

// 예산
// https://school.programmers.co.kr/learn/courses/30/lessons/12982

import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int sum = 0;

        Arrays.sort(d);

        for (int i : d) {
            if (sum + i > budget) {
                break;
            }
            sum += i;
            answer++;
        }

        return answer;
    }
}