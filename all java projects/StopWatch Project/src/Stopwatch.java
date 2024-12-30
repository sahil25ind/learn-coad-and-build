import java.awt.Color;
import java.awt.Font;
import java.awt.event.*;
import javax.swing.*;

public class Stopwatch implements ActionListener{
	
	JFrame frame = new JFrame("Stopwatch");
	JButton startButton = new JButton("START");
	JButton resetButton = new JButton("RESET");
	JLabel label = new JLabel();
	int elapsed_time = 0;
	int hour = 0;
	int minute = 0;
	int second = 0;
	boolean started = false;
	JLabel buttonLabel = new JLabel();
	
	Timer timer = new Timer(1000,new ActionListener() {
		public void actionPerformed(ActionEvent e) {
			elapsed_time +=1000;
			second = (elapsed_time/1000)%60;
			minute = (elapsed_time/60000)%60;
			hour = elapsed_time/3600000;
			label.setText(String.format("%02d:%02d:%02d", hour,minute,second));
		}
	});
	
	Stopwatch(){
		label.setBounds(10, 10, 230, 60);
		label.setBackground(new Color(0x5a5a5a));
		label.setForeground(new Color(0xdbdbdb));
		label.setFont(new Font("calibri",Font.BOLD,60));
		label.setText(String.format("%02d:%02d:%02d",hour,minute,second));
		label.setBorder(BorderFactory.createBevelBorder(1));
		label.setOpaque(true);
		label.setHorizontalAlignment(label.CENTER);
		label.setVerticalAlignment(label.TOP);
		
		buttonLabel.setBounds(0,80,250, 40);
		
		startButton.setBounds(5,0,115,40);
		startButton.addActionListener(this);
		startButton.setFont(new Font("calibri",Font.BOLD,30));
		startButton.setFocusable(false);
		startButton.setBorder(BorderFactory.createEtchedBorder(1));
		startButton.setBackground(new Color(0x4f4f4f));
		startButton.setForeground(new Color(0xcfcfcf));
		
		resetButton.setBounds(125,0,115,40);
		resetButton.addActionListener(this);
		resetButton.setFont(new Font("calibri",Font.BOLD,30));
		resetButton.setFocusable(false);
		resetButton.setBorder(BorderFactory.createEtchedBorder(1));
		resetButton.setBackground(new Color(0x4f4f4f));
		resetButton.setForeground(new Color(0xcfcfcf));
		
		frame.getContentPane().setBackground(new Color(0x424242));
		frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
		frame.setSize(260,165);
		frame.setLayout(null);
		frame.setResizable(false);
		
		buttonLabel.add(startButton);
		buttonLabel.add(resetButton);
		frame.add(label);
		frame.add(buttonLabel);
		
		frame.setVisible(true);
	}
	
	void Start() {
		started = true;
		timer.start();
	}
	void Stop() {
		started = false;
		timer.stop();
	}
	void Reset() {
		elapsed_time = 0;
		second = 0;
		minute = 0;
		hour = 0;
		label.setText(String.format("%02d:%02d:%02d",hour,minute,second));
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource() == startButton) {
			if(started == false) {
				startButton.setText("STOP");
				Start();
			}else if(started == true) {
				startButton.setText("START");
				Stop();
			}
		}else if(e.getSource()==resetButton) {
			Reset();
		}
		
	}
	
}
