import java.util.Hashtable;

public class Main {
	public static void main(String[] args) {
		
		Hashtable<String,String> table = new Hashtable<String,String>(10);
		
		table.put("100", "Hundred");
		table.put("101", "HundredOne");
		table.put("102", "HundredTwo");
		table.put("103", "HundredThree");
		table.put("104", "HundredFour");
		table.put("105", "HundredFive");
		
	//	table.clear();
		table.clone();
		
		for(String i: table.keySet()) {
			
			System.out.print(i.hashCode()%10+"\t"+i+"\t"+"= ");
			System.out.println(table.get(i));
			
		}
		
	// 	System.out.println(table.clone());
	}
}
