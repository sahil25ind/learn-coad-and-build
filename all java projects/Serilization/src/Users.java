import java.io.Serializable;

public class Users implements Serializable{
	//its actually recommended that you do this
	private static final long serialVersionUID = 1;
	
	String Name;
	transient String Password;
	
	public void sayHello() {
		System.out.println("hello "+Name);
	}
}
