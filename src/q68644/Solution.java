package q68644;

// 두 개 뽑아서 더하기
//

import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = {};

        ArrayList<Integer> intList = new ArrayList<Integer>();

        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (!intList.contains(numbers[i] + numbers[j]))
                    intList.add(numbers[i] + numbers[j]);
            }
        }

        Collections.sort(intList);

        answer = new int[intList.size()];
        for (int i = 0; i < intList.size(); i++) {
            answer[i] = intList.get(i);
        }
        return answer;
    }
}