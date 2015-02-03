/*
 Elements of Programming
 13.2 Palindrome Hash
 * Check whether a string can be a palindrome
 */

 public static class Solution {
 	public boolean canPalindrome(String str) {
 		if(str == null || str.length() == 0) {
 			return false;
 		}

 		HashMap<Character, Integer> hashMap = new HashMap<Character, Integer>();
 		char[] charArray = str.toCharArray();
 		for(int i = 0; i < str.length(); i++) {
 			if(hashMap.containsKey(charArray[i])) {
 				hashMap.put(charArray[i], (hashMap.get(charArray)+1));
 			} else {
 				hashMap.put(charArray[i], 1);
 			}
 		}

 		if(str.length()/2 == 0) {
 			if(validHashMap(hashMap) == 0) {
 				return true;
 			}
 		} else if(str.length()%2 == 1 && validHashMap(hashMap) == 1){
 			return true;
 		}
 		return false;

 	}

 	public int validHashMap(HashMap<Character, Integer> hashMap) {
 		int countOdd = 0;

 		for(int v : hashMap.values()) {
 			if(v%2 == 1) {
 				countOdd++;
 			}
 		}

 		if(countOdd == 0) {
 			return 0;
 		} else if (countOdd == 1) {
 			return 1;
 		}
 		return 2;
 	}
 }