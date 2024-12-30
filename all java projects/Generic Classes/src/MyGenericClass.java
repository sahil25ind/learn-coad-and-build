//thing is the generic class with the data type Thing and Thing2
public class MyGenericClass <Thing extends Number,Thing2>{
	Thing x;
	Thing2 y;
	
	MyGenericClass(Thing x,Thing2 y){ //Constructor accept a Thing called x and a Thing2 called y
		this.x = x;
		this.y = y;
	}
	public Thing getValue() {
		return x;
	}
	public Thing2 getValue2() {
		return y;
	}
}
