package coding.java;

public class ReverseString {

    public static void main(String[] args) {
        String str = "Hello World !!!";
        System.out.println(str);
        System.out.println("=====Reverse String 111 ======");
        System.out.println(reverseWithStringBuilder(str));
        StringBuffer str1 = new StringBuffer(str);
        System.out.println("===Reverse String 222==" +str1.reverse().toString());
        System.out.println("========= Reverse String 3333 =========");    
        System.out.println(reverseStringManually(str));
    }
    
    private static String reverseWithStringBuilder(String str){
        return new StringBuilder(str).reverse().toString();
    }

    private static String reverseStringManually(String str){
        StringBuilder sb = new StringBuilder();

        for(int i = str.length() - 1; i >= 0; i--){
            sb.append(str.charAt(i));
        }
        return sb.toString();

    }

}
