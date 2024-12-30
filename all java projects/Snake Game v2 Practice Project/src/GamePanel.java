import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import javax.swing.*;

public class GamePanel extends JPanel implements ActionListener{
	
	int GamePanelWidth = 600;
	int GamePanelHeight = 600;
	int UnitSize = 20;
	int GameUnits = (GamePanelWidth*GamePanelHeight)/UnitSize;
	int delay = 20;
	int snakeBody = 5;
	int[] x;  //these x and y for storing snake body and head coordinates
	int[] y;
	char direction = 'R';
	boolean gameStarted = false;
	int appleCounter =0;
	int applex;
	int appley;
	Random random;
	Timer timer;
	
	GamePanel(){
		random = new Random();
		this.setPreferredSize(new Dimension(GamePanelWidth,GamePanelHeight));
		this.setBackground(Color.black);
		this.setFocusable(true);
		this.addKeyListener(new MyKeyAdapter());
		GameStart();
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(gameStarted) {
			checkApple();
			checkCollisions();
			move();
		}
		repaint();
	}
	
	public void GameStart() {
		gameStarted = true;
		newApple();
		timer = new Timer(delay,this);
		timer.start();
	}
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		draw(g);
	}
	public void draw(Graphics g) {

		if(gameStarted) {
			//display the apple
			g.setColor(Color.red);
			g.fillOval(applex, appley, UnitSize, UnitSize);
			//display the snake
			for(int i=0;i<snakeBody;i++) {
				if(i==0) {  //means its a head
					g.setColor(Color.GREEN);
				}else {
					g.setColor(new Color(45,180,0));
				}
				g.fillRect(x[i], y[i], UnitSize, UnitSize);
			}
			
		}else {
			gameOver(g);
		}
		
	}
	public void move() {
		//map out snake entire body except the head if its greater than 0
		for(int i = snakeBody;i>0;i--) {
			x[i] = x[i - 1];
			y[i] = y[i - 1];
		}
		//moving the snake head according to the direction
		switch(direction) {
		case 'R':
			x[0]+=UnitSize;
			break;
		case 'L':
			x[0]-=UnitSize;
			break;
		case 'U':
			y[0]-=UnitSize;
			break;
		case 'D':
			y[0]+=UnitSize;
			break;
		}
	}
	public void checkCollisions() {  //needs to be modified later on
		
		for(int i =0;i<snakeBody;i++) {
			if(x[0] == x[i] && y[0] == y[i]) { //means head collides with the body
				gameStarted = false;
			}
		}
		if(!gameStarted) {
			timer.stop();
		}
	}
	public void newApple() {
		
		applex = random.nextInt((GamePanelWidth/UnitSize))*UnitSize;
		appley = random.nextInt((GamePanelHeight/UnitSize))*UnitSize;
	}
	public void checkApple() {
		//check if snake eat the apple
		if(x[0] == applex && y[0] == appley) {
			snakeBody++;
			appleCounter++;
			newApple();
		}
	}
	public void gameOver(Graphics g) {  //display the string GameOver string
		
		g.setColor(Color.RED);
		g.setFont(new Font("Ink Free",Font.BOLD,70));
		FontMetrics fontMetrics = g.getFontMetrics(g.getFont());
		g.drawString("Game Over", (GamePanelWidth-fontMetrics.stringWidth("Game Over"))/2, (GamePanelHeight)/2);
	}
	
	
	public class MyKeyAdapter extends KeyAdapter{

		@Override
		public void keyTyped(KeyEvent e) {
			
			switch(e.getKeyChar()) {
			case KeyEvent.VK_LEFT:
				if(direction != 'R') {
					direction = 'L';
				}
				break;
			case KeyEvent.VK_RIGHT:
				if(direction != 'L') {
					direction = 'R';
					}
				break;
			case KeyEvent.VK_UP:
				if(direction != 'D') {
					direction = 'U';
					}
				break;
			case KeyEvent.VK_DOWN:
				if(direction != 'U') {
					direction = 'D';
					}
				break;
			}
		}	
	}
}