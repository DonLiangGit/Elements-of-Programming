/*
 Elements of Programming
 13.1 Partition into anagrams
 * Takes as input a dictionary then return a partition 
 *of the dict into subset of

 */

 public static class Solution {
 	public static ArrayList<String> partitionIntoAnagrams(String[] str) {
 		HashMap<String, ArrayList<String>> hashMap = new HashMap<String, ArrayList<String>>();

 		for(String s : str) {
 			char[] word = s.toCharArray();
 			Array.sort(word);
 			if(hashMap.containsKey(new String(word)) == true) {
 				ArrayList<String> anagramList = hashMap.get(new String(word));
 				anagramList.add(s);
 			} else {
 				ArrayList<String> sInList = new ArrayList<String>();
 				sInList.add(s);
 				hashMap.put((new Sting(word)), sInList);
 			}
 		}

 		ArrayList<String> outputList = new ArrayList<String>();
 		for(Map.Entry<String, ArrayList<String>> entry : hashMap.entrySet() ) {
 			String key = entry.getKey();
 			ArrayList<String> val = entry.getValue();
 			outputList.add(val);
 		}
 		return outputList;

 	}
 }