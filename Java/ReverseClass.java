public package Java

public class ReverseClass {

	public static String reverseMe(String original) {
		Stack<Character> store_string = new Stack<Character>();

		for (int i=0; i<original.length(); i++) {
			store_string.push(original,charAt(i));
		}
	}
}
