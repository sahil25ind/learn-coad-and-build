import java.awt.*;
import java.awt.event.*;
import java.util.Random;

import javax.swing.*;

public class GamePanel extends JPanel implements ActionListener{

	int GamePanel_Width = 800;
	int GamePanel_Height = 800;
	int UnitSize = 25;
	int GameUnit = (GamePanel_Width*GamePanel_Height)/UnitSize;
	int delay = 70;
	int snakeBody = 1; //total bodyParts including head
	int appleEaten = 0;
	int[] x = new int[GameUnit];
	int[] y = new int[GameUnit];
	char direction = 'R';
	int appleX;
	int appleY;
	boolean GameStarted = false;
	Timer timer;
	Random random;
	
	GamePanel(){
		random = new Random();
		this.setPreferredSize(new Dimension(GamePanel_Width,GamePanel_Height));
		this.setBackground(Color.black);
		this.setFocusable(true);
		this.addKeyListener(new myKeyAdapter());
		//set snake position to random
		x[0]=random.nextInt((int)GamePanel_Width/UnitSize)*UnitSize;
		y[0]=random.nextInt((int)GamePanel_Height/UnitSize)*UnitSize;
		gameStart();
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if(GameStarted) {
		move();
		checkApple();
		checkCollision();		
		}
		repaint();
	}
	public void paintComponent(Graphics g) {
		System.out.println("paintComponents has been trigered");
		super.paintComponent(g);
		draw(g);
	}
	public void draw(Graphics g) {
		System.out.println("draw has been trigered");
		if(GameStarted) {
			//draw the Lines
			for(int i =0;i<GamePanel_Width;i++) {
				g.drawLine(i*UnitSize, 0, i*UnitSize, GamePanel_Height); //draw Vertical Lines
				g.drawLine(0, i*UnitSize, GamePanel_Width, i*UnitSize);  //draw Horizontal Lines
			}	

			//draw the apple with red Color
			g.setColor(Color.red);
			g.fillOval(appleX, appleY, UnitSize, UnitSize);
		
			//draw the snake body
			for(int i = 0;i<snakeBody;i++) { //needs to be fixed
				if(i==0) { //head Color
					g.setColor(new Color(0,255,0));
				}else { //body Color
					g.setColor(new Color(0,230,0));
				}
				//draw the snake
				g.fillRect(x[i], y[i], UnitSize, UnitSize);
			}
			g.setColor(Color.red);
			g.setFont(new Font("Ink Free",Font.BOLD,40));
			FontMetrics fontMetrics2 = g.getFontMetrics(g.getFont());
			g.drawString("Score: "+appleEaten, (GamePanel_Width-fontMetrics2.stringWidth("Score: "+appleEaten))/2, g.getFont().getSize());
		}else {
			gameOver(g);
		}
	}
	public void gameStart() {
		GameStarted = true;	
		newApple();		//get new apple after gameStarts
		timer = new Timer(delay,this);	//timer will perform this after every delay time
		timer.start();
	}
	public void newApple() { //generate random coordinate for apple
		int x;
		int y;
		for(int i = 0;i<snakeBody;i++) {
			x = random.nextInt((int)GamePanel_Width/UnitSize)*UnitSize;
			y = random.nextInt((int)GamePanel_Height/UnitSize)*UnitSize;
			if(!(this.x[i] == x && this.y[i] == y)) {
				appleX = x;
				appleY = y;
				break;
			}

		}
	}
	public void checkApple() {
		if(x[0] == appleX && y[0] == appleY) { //if snake eats the apple then spawn new apple and snake grows
			snakeBody++;
			appleEaten++;
			System.out.println("Snake eat the apple");
			newApple();
		}
	}
	public void move() {
		//mapOut the entire snake body
		for(int i = snakeBody;i>0;i--) {
			x[i]=x[i-1];
			y[i]=y[i-1];
		}
		//move the head according to direction
		switch(direction) {
		case 'R':
			x[0] = x[0]+UnitSize;
			break;
		case 'L':
			x[0] = x[0]-UnitSize;
			break;
		case 'U':
			y[0] = y[0]-UnitSize;
			break;
		case 'D':
			y[0] = y[0]+UnitSize;
			break;
		}
	}
	public void checkCollision() {
		//check collision with snake body
		for(int i = snakeBody;i>0;i--) {
			if(x[0] == x[i] && y[0] == y[i]) {
				GameStarted = false;
			}
		}
		if(x[0] >= GamePanel_Width || y[0] >= GamePanel_Height || x[0] < 0 || y[0] < 0 ) {
			//if head collides with walls then what
			System.out.println();
			System.out.println("Snake Collided with the wall at x: "+x[0]+" y: "+y[0]);
			System.out.println();
			headInWall();
		}
		
		if(!GameStarted) {
			timer.stop();
		}
	}
	public void headInWall() {
		if(x[0] < 0) {
			x[0] = GamePanel_Width-UnitSize;
		}
		if(x[0] >= GamePanel_Width) {
			x[0] = 0;
		}
		if(y[0] < 0) {
			y[0] = GamePanel_Height-UnitSize;
		}
		if(y[0] >= GamePanel_Width) {
			y[0] = 0;
		}
	}
	public void gameOver(Graphics g) {
		//display GameOver Screen
		g.setColor(Color.red);
		g.setFont(new Font("Ink Free",Font.BOLD,80));
		FontMetrics fontMetrics = g.getFontMetrics(g.getFont());
		g.drawString("Game Over", (GamePanel_Width - fontMetrics.stringWidth("Game Over"))/2, (GamePanel_Height/2)-(fontMetrics.getHeight())/2);
		//display Score on GameOver Screen
		g.setColor(Color.red);
		g.setFont(new Font("Ink Free",Font.BOLD,60));
		FontMetrics fontMetrics1 = g.getFontMetrics(g.getFont());
		g.drawString("Score: "+appleEaten, (GamePanel_Width - fontMetrics1.stringWidth("Score: "+appleEaten))/2, (GamePanel_Height/2)+(fontMetrics1.getHeight())/2);
	}
//KeyAdapter allows for only one or multiple method @Override Unlike KeyListener which force you to override all the methods(3)
	public class myKeyAdapter extends KeyAdapter{
		
		@Override
		public void keyPressed(KeyEvent e) {
			
			switch(e.getKeyCode()) {
			case KeyEvent.VK_LEFT:
				if(direction!='R') {
					direction = 'L';
					System.out.println("direction is set to: LEFT");
				}
				break;
			case KeyEvent.VK_RIGHT:
				if(direction != 'L') {
					direction = 'R';
					System.out.println("direction is set to: RIGHT");
				}
				break;
			case KeyEvent.VK_UP:
				if(direction!='D') {
					direction = 'U';
					System.out.println("direction is set to: UP");
				}
				break;
			case KeyEvent.VK_DOWN:
				if(direction!='U') {
					direction = 'D';
					System.out.println("direction is set to: DOWN");
				}
				break;
			case KeyEvent.VK_A:
				if(direction!='R') {
					direction = 'L';
					System.out.println("direction is set to: LEFT");
				}
				break;
			case KeyEvent.VK_D:
				if(direction != 'L') {
					direction = 'R';
					System.out.println("direction is set to: RIGHT");
				}
				break;
			case KeyEvent.VK_W:
				if(direction!='D') {
					direction = 'U';
					System.out.println("direction is set to: UP");
				}
				break;
			case KeyEvent.VK_S:
				if(direction!='U') {
					direction = 'D';
					System.out.println("direction is set to: DOWN");
				}
				break;
			}
		}
	}
}
