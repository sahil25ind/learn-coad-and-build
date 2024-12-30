import java.awt.Dimension;
import java.awt.Font;

import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class Slider implements ChangeListener{

	JFrame frame;
	JPanel panel;
	JLabel label;
	JSlider slider;
	String tempDisplay;
	
	Slider(){
		slider = new JSlider(0,100,28);
		panel = new JPanel();
		label = new JLabel();
		frame = new JFrame("Temprature Slider");
		
		slider.setPreferredSize(new Dimension(250,450));
		slider.setPaintTicks(true);
		slider.setMinorTickSpacing(10);
		slider.setPaintTrack(true);
		slider.setMajorTickSpacing(25);
		slider.setPaintLabels(true);
	//	slider.setOrientation(SwingConstants.VERTICAL);
		slider.setOrientation(slider.VERTICAL); //you can also use SwingConstant.VERTICAL in place of slider.VERTICAL
		slider.setFont(new Font("calibri",Font.BOLD,20));
		slider.addChangeListener(this);
		
		tempDisplay = String.format("= %3d °C",slider.getValue());
		
		label.setText(tempDisplay);
		label.setFont(new Font("calibri",Font.BOLD,25));
		
		frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
		frame.setSize(500,500);
		
		panel.add(slider);
		panel.add(label);
		frame.add(panel);
		
		frame.setVisible(true);
	}
	
	@Override
	public void stateChanged(ChangeEvent e) {
		if(e.getSource()==slider) {
			tempDisplay = String.format("= %3d °C", slider.getValue());
			label.setText(tempDisplay);
		}
		
	}
}
