//this is the Use of Generic Class i am using 2 data type of generic class called thing and thing2
public class Main {
	public static void main(String[] args) {
		
		MyGenericClass<Integer,Double> myInt = new MyGenericClass<>(2024,12.10);
		MyGenericClass<Double,Character> myDouble = new MyGenericClass<>(79.6,'%');
	//	MyGenericClass<Character,String> myChar = new MyGenericClass<>('$',"Money Symbol");
	//	MyGenericClass<String ,String> myString = new MyGenericClass<>("1st Semester","1st Year");
		
	//	System.out.println(myString.getValue()+" "+myString.getValue2()+" "+myInt.getValue()+" "+myInt.getValue2());
		
		System.out.println(myDouble.getValue()+" "+myDouble.getValue2());
	//	System.out.println(myChar.getValue()+" "+myChar.getValue2());
	}
}
