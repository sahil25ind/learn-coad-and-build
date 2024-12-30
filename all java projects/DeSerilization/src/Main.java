import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectStreamClass;

public class Main {

	public static void main(String[] args) throws IOException, ClassNotFoundException {
		
		Users user = null;
		
		FileInputStream fileIn = new FileInputStream("C:\\Users\\sahil\\eclipse-workspace\\Serilization\\UserObj.ser");
		ObjectInputStream ObjectIn = new ObjectInputStream(fileIn);
		user = (Users)ObjectIn.readObject();
		
		ObjectIn.close();
		fileIn.close();
		
		System.out.println("UserObject info Reading...");
		
		System.out.println("User name: "+user.Name);
		System.out.println("User password: "+user.Password);
		user.sayHello();
		
		long serialVersionUID = ObjectStreamClass.lookup(user.getClass()).getSerialVersionUID();
		
		System.out.println(serialVersionUID);
		
	}

}
