package q12910;

// 나누어 떨어지는 숫자 배열
// https://school.programmers.co.kr/learn/courses/30/lessons/12910

import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {

        LinkedList<Integer> list = new LinkedList<>();

        for(int n : arr) {
            if(n % divisor == 0) {
                list.add(n);
            }
        }
        Collections.sort(list);

        if(list.isEmpty()) list.add(-1);

        int[] answer = new int[list.size()];

        for(int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}
