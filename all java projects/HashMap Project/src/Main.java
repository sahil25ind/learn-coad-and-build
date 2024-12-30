import java.util.HashMap;

public class Main {
	public static void main(String[] args) {
		
		HashMap<String,String> livingBeingHashMap = new HashMap<String,String>();
		
		livingBeingHashMap.put("Dog", "CanineSpeciesAnimal");
		livingBeingHashMap.put("cat", "FelionSpeciesAnimal");
		livingBeingHashMap.put("Snake", "LegLessReptile");
		livingBeingHashMap.put("Lizard", "FourLagedReptile");
		
	//	System.out.println(livingBeingHashMap.get("Dog"));
		livingBeingHashMap.replace("Snake", "LegLessLizard");
	//	System.out.println(livingBeingHashMap.get("Snake"));
	//	livingBeingHashMap.clear();
	//	System.out.println(livingBeingHashMap);
	//	livingBeingHashMap.remove("Lizard");
	//	boolean a = livingBeingHashMap.containsKey("cat");
	//	boolean a = livingBeingHashMap.containsValue("LegLessLizard");
	//	System.out.println(a);
		
		for(String i:livingBeingHashMap.keySet()) {
			System.out.print(i+"\t"+"= ");
			System.out.println(livingBeingHashMap.get(i));
		}
		
	}
}
