package q12977;

// 소수 만들기
// https://school.programmers.co.kr/learn/courses/30/lessons/12977

class Solution {
    public int solution(int[] nums) {
        int answer = 0;

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    int num = nums[i] + nums[j] + nums[k];
                    int sosu = 0;
                    for (int m = 2; m * m <= num; m++) {
                        if (m * m == num) {
                            sosu++;
                        } else if (num % m == 0) {
                            sosu++;
                        }
                    }
                    if (sosu == 0) {
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
}
