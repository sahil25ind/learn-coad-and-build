import java.io.Serializable;
//in order to deserialize the serialize object the serialVersionUID must match and if you dont explecetly assign it then it get calculated and generated
public class Users implements Serializable{ 
	// but its actually recomonded that you explecitly declare and assign it and you can give it any number like i did just 1
	private static final long serialVersionUID = 1;
	
	String Name; //anything has transient keyword does not serialized its get ignored
	transient String Password; //adding transient allows you to stop the flow of any value
	
	public void sayHello() {
		System.out.println("hello "+Name);
	}
}
