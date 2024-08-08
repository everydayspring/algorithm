package q42840;

// 모의고사
// https://school.programmers.co.kr/learn/courses/30/lessons/42840

import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] stu1 = {1, 2, 3, 4, 5};
        int[] stu2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] stu3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        ArrayList<Integer> list = new ArrayList<>();
        list.add(0);
        list.add(0);
        list.add(0);

        for(int i = 0; i < answers.length; i++){
            if(answers[i] == stu1[i % stu1.length]){
                list.set(0, list.get(0) + 1);
            }
            if(answers[i] == stu2[i % stu2.length]){
                list.set(1, list.get(1) + 1);
            }
            if(answers[i] == stu3[i % stu3.length]){
                list.set(2, list.get(2) + 1);
            }
        }

        int maxCount = 0;
        int max = Collections.max(list);
        if(max == list.get(0)) maxCount++;
        if(max == list.get(1)) maxCount++;
        if(max == list.get(2)) maxCount++;

        answer = new int[maxCount];
        maxCount = 0;
        if(list.get(0) == max) answer[maxCount++] = 1;
        if(list.get(1) == max) answer[maxCount++] = 2;
        if(list.get(2) == max) answer[maxCount++] = 3;

        return answer;
    }
}