import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Event;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;

import javax.swing.ImageIcon;
import javax.swing.JPanel;

public class DrawOnPanel extends JPanel{
	
	Image BackgroundImage;
	
	DrawOnPanel(){
		BackgroundImage = new ImageIcon("Images//2024-05-10 00-53-20.00_03_39_42.Still001.png").getImage();
		
		this.setPreferredSize(new Dimension(700,700));
		
	}
	
	public void paint(Graphics g) {
		Graphics2D g2D = (Graphics2D)g;
		
		g2D.drawImage(BackgroundImage,0,0,null);
		
		g2D.setPaint(Color.green);
		g2D.setStroke(new BasicStroke(5));
		g2D.drawLine(0, 0, 700, 700);
		
		g2D.setPaint(Color.red);
		g2D.setStroke(new BasicStroke(10));
		g2D.drawRect(56, 75, 456, 544);
		g2D.setPaint(Color.blue);
		g2D.fillRect(56, 75, 456, 544);
		
		g2D.setPaint(Color.yellow);
		g2D.drawOval(50, 50, 100, 100);
		g2D.fillOval(50, 50, 100, 100);
		
		g2D.setStroke(new BasicStroke(1));
		g2D.setPaint(Color.red);
		g2D.drawArc(20, 20, 100, 90, 0, 180);
		g2D.fillArc(20, 20, 100, 90, 0, 180);
		g2D.setPaint(Color.white);
		g2D.drawArc(20, 20, 100, 90, 180, 180);
		g2D.fillArc(20, 20, 100, 90, 180, 180);
		
		int[] xPoints= {240,350,570};
		int[] yPoints= {210,180,420};
		g2D.setPaint(Color.black);
		g2D.drawPolygon(xPoints, yPoints, 3);
		g2D.fillPolygon(xPoints, yPoints, 3);
		
		int[] xPoint= {200,220,300,380,400};
		int[] yPoint= {150,100,50,100,150};
		g2D.setPaint(Color.black);
		g2D.drawPolygon(xPoint, yPoint, 5);
		g2D.fillPolygon(xPoint, yPoint, 5);
		
		g2D.setPaint(Color.magenta);
		g2D.setFont(new Font("calibri",Font.PLAIN,65));
		g2D.drawString("fuck you!",180,540);
		
	}
}