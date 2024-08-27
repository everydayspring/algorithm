package q150370;

// 개인정보 수집 유효기간
// https://school.programmers.co.kr/learn/courses/30/lessons/150370

import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        int[] answer = {};
        List<Integer> res = new ArrayList<Integer>();
        for (int i = 0; i < privacies.length; i++) {
            for (int j = 0; j < terms.length; j++) {
                if (terms[j].substring(0, 1).equals(privacies[i].substring(11))) {
                    int year = Integer.parseInt(privacies[i].substring(0, 4));
                    int month = Integer.parseInt(privacies[i].substring(5, 7));
                    int day = Integer.parseInt(privacies[i].substring(8, 10));

                    int temp = Integer.parseInt(terms[j].substring(2));

                    month += temp;

                    while (month > 12) {
                        year++;
                        month -= 12;
                    }

                    if (year < Integer.parseInt(today.substring(0, 4))) {
                        res.add(i + 1);
                    } else if (year == Integer.parseInt(today.substring(0, 4)) && month < Integer.parseInt(today.substring(5, 7))) {
                        res.add(i + 1);
                    } else if (year == Integer.parseInt(today.substring(0, 4)) && month == Integer.parseInt(today.substring(5, 7)) && day <= Integer.parseInt(today.substring(8, 10))) {
                        res.add(i + 1);
                    }
                }
            }
        }
        int[] list = new int[res.size()];
        for (int i = 0; i < list.length; i++) {
            list[i] = res.get(i);
        }
        return list;
    }
}