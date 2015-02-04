/*
 Elements of Programming
 13.3 Anonymous letter is constructible
 * 
 */

 public static class Solution {
 	public boolean isConstructible(String letter, String magz) {
 		
 		final int letterLength = letter.length();
 		final int magzLength ＝ magz.length();

 		if(letterLength > magzLength) {
 			return false;
 		}

 		HashMap<Character, Integer> hashMap = 
 			new HashMap<Character, Integer>();

 		for(int i = 0; i < letterLength; i++) {
 			if(hashMap.containsKey(letter.charAt(i)) == true) {
 				hashMap.put(letter.charAt(i), 
 					(hashMap.get(letter.charAt(i)) + 1));
 			} else {
 				hashMap.put(letter.charAt(i), 1);
 			}
 		}

 		for(int i = 0; i < magzLength; i++) {
 			if(hashMap.containsKey(magz.charAt(i))) {
 				hashMap.get(charAt(i))--;
 				if(hashMap.get(charAt(i)) == 0) {
 					hashMap.remove(hashMap.get(charAt(i)));
 				}
 			}
 		}

 		if(hashMap.isEmpty() == true) {
 			return true;
 		} else {
 			return false;
 		}
 	}
 }