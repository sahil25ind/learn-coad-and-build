import java.util.Calendar;
import java.util.Timer;
import java.util.TimerTask;

public class Main {
	public static void main(String[] args) {
		
		Timer timer = new Timer();
		TimerTask timerTask = new TimerTask() {
			int count = 10;

			@Override
			public void run() {
				if(count > 0) {
					System.out.println(count+" Second");
					count--;
				}else if(count == 0) {
					System.out.println("HAPPY NEW YEAR!");
					timer.cancel();
				}

			//	System.out.println("the task is completed :)");
				
			}
		};
	//this is Calendar its different from Timer or TimerTask
	/*	
		Calendar date = Calendar.getInstance();
		
		date.set(Calendar.YEAR,2024);
		date.set(Calendar.MONTH, Calendar.DECEMBER);
		date.set(Calendar.DAY_OF_MONTH,12);
		date.set(Calendar.HOUR_OF_DAY, 15);
		date.set(Calendar.MINUTE, 31);
		date.set(Calendar.SECOND, 50);
		date.set(Calendar.MILLISECOND, 0);
	*/	
		
	//Calendar is only up to here
		
	//	timer.schedule(timerTask, 1000);
	//	timer.schedule(timerTask,date.getTime());
	//	timer.scheduleAtFixedRate(timerTask, date.getTime(), 1000);
		
		
	}
}
