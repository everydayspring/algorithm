package q77884;

// 약수의 개수와 덧셈
// https://school.programmers.co.kr/learn/courses/30/lessons/77884

class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        int count;

        for(int i = left; i <= right; i++){
            count = 0;
            for(int j = 1; j * j <= i; j++){
                if(j * j == i) {
                    count++;
                } else if(i % j == 0){
                    count+= 2;
                }
            }
            if(count % 2 == 1) {
                answer += (i * -1);
            } else {
                answer += i;
            }
        }
        return answer;
    }
}
