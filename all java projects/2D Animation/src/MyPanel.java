import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class MyPanel extends JPanel implements ActionListener{
	int PANEL_WIDTH = 500;
	int PANEL_HEIGHT = 500;
	Image sadFace;
	Image BackgroundImage;
	Timer timer;
	int xVelocity = 2;
	int yVelocity = 3;
	int x = 321;
	int y = 0;

	MyPanel(){
		this.setPreferredSize(new Dimension(PANEL_WIDTH,PANEL_HEIGHT));
		this.setBackground(Color.black);
		sadFace = new ImageIcon("Images//sadFace.png").getImage();
		BackgroundImage = new ImageIcon("Images//Screenshot (142).png").getImage();
		timer = new Timer(1,this); //triggers an Event every 1 milliSecond
		timer.start();	//this is the ActionListener that i implemented
	}
	
	public void paint(Graphics g) {
		
		super.paint(g); //this paint the background using paint method from super class
		Graphics2D g2D = (Graphics2D)g;
		
		g2D.drawImage(BackgroundImage,0 ,0 ,null);
		
		g2D.drawImage(sadFace,x , y , null);
		
	}
//this gets triggered whenever an event is triggered
	@Override
	public void actionPerformed(ActionEvent e) {	
		x = x + xVelocity;
		y = y + yVelocity;
		
		if(x >= PANEL_WIDTH - sadFace.getWidth(null) || x <= 0) {
			xVelocity = xVelocity * -1;
		}else if(y >= PANEL_HEIGHT - sadFace.getHeight(null) || y <= 0) {
			yVelocity = yVelocity * -1;
		}
		
		repaint();
	}
}
