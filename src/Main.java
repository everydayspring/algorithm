import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world");

        // 정수형 to 문자열
        long num1 = 1324L;
        String str1 = Long.toString(num1);
        int num2 = 12342;
        String str2 = Integer.toString(num2);

        // 숫자의 자리수 구하기
        long num3 = 12L;
        Long.toString(num3).length(); // 2
        int num4 = 954;
        Integer.toString(num4).length(); // 3

        // 정수형 to String Array
        long num5 = 17445L;
        String[] strArr1 = Long.toString(num5).split("");
        int num6 = 93;
        String[] strArr2 = Integer.toString(num6).split("");

        // String to Character Array
        String str3 = "apple";
        char[] charArr1 = str3.toCharArray();       // [a, p, p, l, e]

        // String to String Array
        String str4 = "paul bassett";
        String[] atrArr3 = str4.split("");      // [p, a, u, l,  , b, a, s, s, e, t, t]

        // Array sort
        int[] intArr1 = {1, 27, 3, 2, 6, 73, 2, 7, 8};
        char[] charArr2 = {'d', 'e', 'a', 'Q', 'A', 'x', 'f'};
        String[] atrArr4 = {"안녕하세요", "zzzzz", "바나나", "bassett", "paul", "커피", "apple"};

        Arrays.sort(intArr1);       // [1, 2, 2, 3, 6, 7, 8, 27, 73]
        Arrays.sort(charArr2);      // [A, Q, a, d, e, f, x]
        Arrays.sort(atrArr4);       // [apple, bassett, paul, zzzzz, 바나나, 안녕하세요, 커피]

        // Array print
        System.out.println(Arrays.toString(intArr1));
        System.out.println(Arrays.toString(charArr2));
        System.out.println(Arrays.toString(atrArr4));

        // 3진법 계산
        String str5 = "22111";
        int num8 = Integer.parseInt(str5, 3);       // 229

        // 대소문자 변환
        String str6 = "TrY HeLlO WoRlD";
        System.out.println(str6 = str6.toUpperCase());      // TRY HELLO WORLD
        System.out.println(str6 = str6.toLowerCase());      // try hello world

        // Character to Integer
        char char1 = 'A';
        int num9 = (int)char1;      // 65

    }
}