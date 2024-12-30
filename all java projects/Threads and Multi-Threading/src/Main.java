
public class Main {
	public static void main(String[] args) throws InterruptedException {
		
		MyThread thread1 = new MyThread();
		
		RunnableThread runnable1 = new RunnableThread();
		Thread thread2 = new Thread(runnable1);
		
		thread1.setDaemon(false);
		thread2.setDaemon(false);
		
		thread1.start();
	//	thread1.join(); 
		thread2.start();
		
	//	System.out.println(1/0);
	}
}
