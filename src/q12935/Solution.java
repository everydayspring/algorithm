package q12935;

// 제일 작은 수 제거하기
// https://school.programmers.co.kr/learn/courses/30/lessons/12935

import java.util.*;

class Solution {
    public int[] solution(int[] arr) {

        if(arr.length == 1) {
            return new int[] {-1};
        }

        LinkedList<Integer> list = new LinkedList<>();
        for(int n : arr) {
            list.add(n);
        }
        list.remove(Collections.min(list));
        int[] answer = new int[list.size()];
        for(int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}
