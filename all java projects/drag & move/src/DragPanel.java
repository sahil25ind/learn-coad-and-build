import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;

import javax.swing.ImageIcon;
import javax.swing.JPanel;

public class DragPanel extends JPanel{

	ImageIcon image = new ImageIcon("Images//1Rocket-Emoji.png");
	
//	int WIDTH = image.getIconWidth();
//	int HEIGHT = image.getIconHeight();
	Point imageCorner;
	Point prevPt;
	
	DragPanel(){
		imageCorner = new Point(300,250);
		ClickListener clickListener = new ClickListener();
		DragListener dragListener = new DragListener();

		this.addMouseListener(clickListener);
		this.addMouseMotionListener(dragListener);
		
	}
	
	public void paintComponent(Graphics g) { //this is a method called paintComponent
		super.paintComponent(g);
		image.paintIcon(this, g, (int)imageCorner.getX(), (int)imageCorner.getY());
	}
	
	private class ClickListener extends MouseAdapter{ //this is a class inside a class called inter-class it will wait until we click the mouse
		
		public void mousePressed(MouseEvent e) { //updating previous point with where-ever we click(by getting the new clicked point value by using e.getPoint() )
			prevPt = e.getPoint();
		}
	}
	
	private class DragListener extends MouseMotionAdapter{ //this is also a inter-class it will drag the image
		
		public void mouseDragged(MouseEvent e) {
			Point currentPt = e.getPoint();
			imageCorner.translate(
					(int)(currentPt.getX()-prevPt.getX()),
					(int)(currentPt.getY()-prevPt.getY())
			);
			prevPt = currentPt;
			repaint();
		}
	}
}
