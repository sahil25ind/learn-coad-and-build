//use generic methods instead of calling the method again and again use thing or T for the name of generic
public class Main { //generic is <thing> with the name thing use before the return type
	public static void main(String[] args) {
		
		Integer[] intArray = {1,2,3,4,5};
		Double[] doubleArray = {4.1,4.5,5.1,5.5,6.1};
		Character[] charArray = {'f','u','c','k',' ','y','o','u'};
		String[] stringArray = {"B","Y","E"};
		
		displayArray(returnArray(intArray));
		displayArray(returnArray(doubleArray));
		displayArray(returnArray(charArray));
		displayArray(returnArray(stringArray));
		
	}
	public static <T>void displayArray(T array) {
		
	/*	for(T i: array) {
			
			System.out.print(i+" ");
		} */
		System.out.println(array);
	}
	public static <t> t returnArray(t[] array) {
		return array[0];
	}
}
