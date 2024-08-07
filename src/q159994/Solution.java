package q159994;

// 카드 뭉치
// https://school.programmers.co.kr/learn/courses/30/lessons/159994

import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        int index1 = -1;
        int index2 = -1;

        for(String str : goal){
            if(Arrays.asList(cards1).indexOf(str) != -1){
                if(index1 + 1 != Arrays.asList(cards1).indexOf(str)){
                    return "No";
                } else {
                    index1 = Arrays.asList(cards1).indexOf(str);
                }
            } else if(Arrays.asList(cards2).indexOf(str) != -1){
                if(index2 + 1 != Arrays.asList(cards2).indexOf(str)){
                    return "No";
                } else {
                    index2 = Arrays.asList(cards2).indexOf(str);
                }
            }

        }
        return answer;
    }
}

