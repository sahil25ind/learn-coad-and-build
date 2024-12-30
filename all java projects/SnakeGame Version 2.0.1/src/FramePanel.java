import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

import javax.swing.Timer; //importing timer from swing package

public class FramePanel extends JPanel implements ActionListener{

	int PanelWidth = 600;
	int PanelHeight = 600;
	int unitSize = 25;
	int gameUnit =(int) (PanelWidth * PanelHeight)/unitSize;
	int delay = 70;
	int bodyParts = 5;
	int[] x = new int[gameUnit];
	int[] y = new int[gameUnit];
	boolean gameStarted = false;
	boolean positionSet = false;
	boolean directionSet = false;
	int Score = 0;
	int Applex;
	int Appley;
	char direction = 'R';
	Timer timer;
	Random random;
	
	FramePanel(){
		random = new Random();
		this.setPreferredSize(new Dimension(PanelWidth,PanelHeight));
		this.setBackground(Color.black);
		this.setFocusable(true);
		this.addKeyListener(new myKeyAdapter());
		if(!positionSet) {  //this method must only be called once when program starts
			positionSet = true;
		snakeInitialPosition();
		}
//		System.out.println("calling StartGame() from the constructor at the very end");
		StartGame();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
//		System.out.println("actionPerformed has been triggered");
		move();				//calling move constantly after every delay
		checkApple();		//checking if apple eaten or not after every delay
		checkCollision();	//checking collision after every delay
		
	}
	public void paintComponent(Graphics g) {
//		System.out.println("paintComponent has been trigerred");
		super.paintComponent(g);	//accessing paintComponent from super class (JPanel) to paint all component on screen
		draw(g);	//calling draw method to draw snake and apple on screen
	}
	public void draw(Graphics g) {
		if(gameStarted) {	//if gameStarted is true
			
//			//draw lines
//			for(int i =0;i<PanelWidth;i++) {
//				g.drawLine(0, i*unitSize, PanelWidth,i*unitSize);
//				g.drawLine(i*unitSize, 0, i*unitSize, PanelHeight);
//			}
			
			//draw Apple
			g.setColor(Color.red);
			g.fillOval(Applex, Appley, unitSize, unitSize);
//			System.out.println(Applex+" "+Appley);
			
			//draw the snake
			for(int i = 0;i<bodyParts;i++) {
				if(i == 0) {
					g.setColor(new Color(0,255,0));
					g.fillRect(x[i], y[i], unitSize, unitSize);
//					System.out.println("Head: "+x[i]+" "+y[i]);
				}else {
					g.setColor(new Color(105,128,125));
					g.fillRect(x[i], y[i], unitSize, unitSize);
//					System.out.println("Remaining BodyParts: "+x[i]+" "+y[i]);
				}
			}
			//draw score boad on screen
			g.setColor(Color.red);
			g.setFont(new Font("Ink Free",Font.BOLD,40));
			FontMetrics fontMetrics = g.getFontMetrics();
			g.drawString("Score: "+Score, (PanelWidth-fontMetrics.stringWidth("Score: "+Score))/2, g.getFont().getSize());
			
			repaint();	//repaint all the components
		}else {		//if gameStarted is false
			GameOver(g);
		}
	}
	public void snakeInitialPosition() {
		//assigning snake location randomly
		int j = random.nextInt((int)PanelWidth/unitSize)*unitSize;
		int k = random.nextInt((int)PanelHeight/unitSize)*unitSize;
//		System.out.println(j+","+k);
		
		boolean VerticalSnake = random.nextBoolean();
//		System.out.println(VerticalSnake);
		
		boolean InvertedSnake = random.nextBoolean();
//		System.out.println(InvertedSnake);
		
		if(!VerticalSnake) {
			if(!InvertedSnake) {
				//vertical snake
				for(int i = 0;i<bodyParts;i++) {
					x[i] = j -25;
					y[i] = k;
					j-=unitSize;
				}
				direction = 'R';
			}else {
				//inverted vertical snake
				for(int i = 0;i<bodyParts;i++) {
					x[i] = j +25;
					y[i] = k;
					j+=unitSize;
				}
				direction = 'L';
			}
		}else {
			if(!InvertedSnake) {
				//horizontal snake
				for(int i = 0;i<bodyParts;i++) {
					x[i] = j;
					y[i] = k - 25;
					k-=unitSize;
				}
				direction = 'D';
			}else {
				//inverted horizontal snake
				for(int i = 0;i<bodyParts;i++) {
					x[i] = j;
					y[i] = k + 25;
					k+=unitSize;
				}
				direction = 'U';
			}	
		}		
	}
	public void StartGame() {
		gameStarted = true;
		newApple();
		timer = new Timer(delay,this);
		timer.start();
	}
	public void newApple(){
		System.out.println("generating new Apple");
		//generating random number for newApple
		int x = random.nextInt(PanelWidth/unitSize)*unitSize;
		int y = random.nextInt(PanelHeight/unitSize)*unitSize;
		
		//making sure that apple don't overlap the snake body
		for(int i = 0; i<bodyParts;i++) {
			if(this.x[i] != x && this.y[i] != y) {
				Applex = x;
				Appley = y;
			}
		}
	}
	public void move() {
		if(directionSet) { 	//if directionSet has been set by the user
			//map out snakeBody 
			for(int i = bodyParts;i>0;i--) {
				x[i] = x[i-1];
				y[i] = y[i-1];
			}
			//move the snake according to direction
			switch(direction) {
			case 'R':
				x[0] = x[0] + unitSize;
				break;
			case 'L':
				x[0] = x[0] - unitSize;
				break;
			case 'D':
				y[0] = y[0] + unitSize;
				break;
			case 'U':
				y[0] = y[0] - unitSize;
				break;
			}
		}
	}
	public void checkApple() {
//		System.out.println("checkApple method has been executed skdfjksdfhvjuhnjdhjkadshgkjdsfhgkuhgiufdh");
		//checking if head collides with apple
		if(x[0] == Applex && y[0] == Appley) {
			Score++;
			bodyParts++;
			newApple();		//calling newApple() for new apple if snake eats it
		}
	}
	public void checkCollision() {
//		System.out.println("checking collisions nowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww");
		
		//check collision with the body
		for(int i = bodyParts;i>0;i--) {
			if(x[0] == x[i] && y[0] == y[i]) {
				gameStarted = false;
//			System.out.println("gameStarted is set to false why?????????????????????????????????????????????");
			}
		}
		
		//check collision with the wall
		if(x[0] < 0) {
			gameStarted = false;
		}
		if(y[0] < 0) {
			gameStarted = false;
		}
		if(x[0] >= PanelWidth) {
			gameStarted = false;
		}
		if(y[0] >= PanelHeight) {
			gameStarted = false;
		}
		
		//if snake collided then stop the game
		if(!gameStarted) {
//			System.out.println("timer stoped why!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
			timer.stop();	//if gameStarted is false than stop the game
		}
	}
	public void GameOver(Graphics g) {
		
		//draw GameOver on Screen
		g.setColor(Color.red);
		g.setFont(new Font("Ink Free",Font.BOLD,80));
		FontMetrics fontMetrics = g.getFontMetrics();
		g.drawString("Game Over", (PanelWidth-fontMetrics.stringWidth("Game Over"))/2, (PanelHeight/2)-(fontMetrics.getHeight()/3));
		
		//draw Score on Screen
		g.setFont(new Font("Ink Free",Font.BOLD,55));
		FontMetrics fontMetrics1 = g.getFontMetrics();
		g.drawString("Score: "+Score, (PanelWidth - fontMetrics1.stringWidth("Score: "+Score))/2, (PanelHeight/2)+(fontMetrics1.getHeight()/2));
	}

	//set the user choice of direction
	public class myKeyAdapter extends KeyAdapter{
		
		@Override
		public void keyPressed(KeyEvent e) {
			switch(e.getKeyCode()) {
			case KeyEvent.VK_UP:
				if(direction != 'D') {
					direction = 'U';
					directionSet = true;
				}
				break;
			case KeyEvent.VK_DOWN:
				if(direction != 'U') {
					direction = 'D';
					directionSet = true;
				}
				break;
			case KeyEvent.VK_LEFT:
				if(direction != 'R') {
					direction = 'L';
					directionSet = true;
				}
				break;
			case KeyEvent.VK_RIGHT:
				if(direction != 'L') {
					direction = 'R';
					directionSet = true;
				}
				break;
			}
		}
	}
}
