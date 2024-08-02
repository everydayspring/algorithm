package q86491;

// 최소직사각형
// https://school.programmers.co.kr/learn/courses/30/lessons/86491

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int roMax = 0;
        int coMax = 0;

        for(int i = 0; i < sizes.length; i++){
            if(sizes[i][0] < sizes[i][1]){
                int temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }
            roMax = sizes[i][0] > roMax ? sizes[i][0] : roMax;
            coMax = sizes[i][1] > coMax ? sizes[i][1] : coMax;
        }

        answer = roMax * coMax;
        return answer;
    }
}
