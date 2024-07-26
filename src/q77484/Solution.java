package q77484;

// 로또의 최고 순위와 최저 순위
// https://school.programmers.co.kr/learn/courses/30/lessons/77484

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int count = 0;
        int countZero = 0;

        for(int i = 0; i < lottos.length; i++) {
            for(int j = 0; j < win_nums.length; j++) {
                if (lottos[i] == win_nums[j])
                    count++;
            }
            if (lottos[i] == 0)
                countZero++;
        }
        if (count == 0)
            count++;

        answer[0] = 7 - count - countZero;
        answer[0] = (answer[0] == 0) ? 1 : answer[0];
        answer[1] = 7 - count;

        return answer;
    }
}