import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.ObjectStreamClass;

public class Main {

	public static void main(String[] args) throws IOException {
		
		Users user = new Users();
		
		user.Name = "Sahil Kumar";
		user.Password = "sahil@#123";
		
	//	user.sayHello();
		
		FileOutputStream fileOut = new FileOutputStream("UserObj.ser");
		ObjectOutputStream objectOut = new ObjectOutputStream(fileOut);
		objectOut.writeObject(user);
		
		objectOut.close();
		fileOut.close();
		
		System.out.println("UserObject info Saved...");
		
		long serialVersionUID = ObjectStreamClass.lookup(user.getClass()).getSerialVersionUID();
		
		System.out.println(serialVersionUID);
		
	}

}
