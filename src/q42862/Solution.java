package q42862;

import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;

        Arrays.sort(lost);
        Arrays.sort(reserve);

        for (int i = 0; i < lost.length; i++) {
            for (int j = 0; j < reserve.length; j++) {
                if (lost[i] == reserve[j]) {
                    lost[i] = 200;
                    reserve[j] = 300;
                    answer++;
                }
            }
        }

        for (int k : lost) {
            for (int j = 0; j < reserve.length; j++) {
                if (k == reserve[j] - 1 || k == reserve[j] + 1) {
                    answer++;
                    reserve[j] = 300;
                    break;
                }
            }
        }
        return answer;
    }
}