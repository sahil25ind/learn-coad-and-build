import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

public class TicTacToe implements ActionListener {

	Image icon = new ImageIcon("Images//TicTacToe_gameIcon.png").getImage(); //creating Image out of ImageIcon
    JFrame frame = new JFrame("Tic-Tac-Toe Game");
    JPanel titlePanel = new JPanel();
    JPanel buttonPanel = new JPanel();
    JLabel textField = new JLabel();
    JButton[] buttons = new JButton[9];
    JButton playAgainButton = new JButton("Play Again");
    Color buttonsDefaultColor = playAgainButton.getBackground();

    Random random = new Random();
    boolean player1Turn = false;
    boolean gameOver = false;

    TicTacToe() {
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 800);
//      frame.setResizable(false);
        frame.setLocationRelativeTo(null);
        frame.setIconImage(icon); //setting the image as the application Icon
        frame.setLayout(new BorderLayout());
        frame.getContentPane().setBackground(new Color(50, 50, 50));

        playAgainButton.setFocusable(false);
        playAgainButton.addActionListener(this);
        playAgainButton.setFont(new Font("Mv Boli", Font.BOLD, 35));

        textField.setText("Tic-Tac-Toe");
        textField.setBackground(new Color(25, 25, 25));
        textField.setForeground(new Color(25, 255, 0));
        textField.setFont(new Font("Ink Free", Font.BOLD, 75));
        textField.setVerticalAlignment(textField.BOTTOM);
        textField.setHorizontalAlignment(textField.CENTER);
        textField.setOpaque(true);

        titlePanel.setBounds(0, 0, 800, 100);
        titlePanel.setLayout(new BorderLayout());

        buttonPanel.setLayout(new GridLayout(3, 3, 5, 5));
        buttonPanel.setBackground(Color.black);

        for (int i = 0; i < 9; i++) {
            buttons[i] = new JButton();
            buttons[i].setFocusable(false);
            buttons[i].setFont(new Font("Mv Boli", Font.BOLD, 120));
            buttons[i].addActionListener(this);
            buttonPanel.add(buttons[i]);
        }

        titlePanel.add(textField);
        frame.add(titlePanel, BorderLayout.NORTH);
        frame.add(buttonPanel);
        frame.setVisible(true);
        firstTurn();
    }

    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == playAgainButton) {
            System.out.println("playAgainButton has been pressed");

            for (int i = 0; i < 9; i++) {
                buttons[i].setText("");
                buttons[i].setEnabled(true);
                buttons[i].setBackground(buttonsDefaultColor);
            }
            titlePanel.remove(playAgainButton);
            firstTurn();
        }

        for (int i = 0; i < 9; i++) {
            if (e.getSource() == buttons[i]) {
                if (buttons[i].getText().isEmpty()) { // Prevent overwriting
                    if (player1Turn) {
                        buttons[i].setForeground(Color.red);
                        buttons[i].setText("X");
                        player1Turn = false;
                        textField.setText("O turn");
                    } else {
                        buttons[i].setForeground(Color.blue);
                        buttons[i].setText("O");
                        player1Turn = true;
                        textField.setText("X turn");
                    }
                    check(); // Check the game state after every move
                }
            }
        }
    }

    public void firstTurn() {
    	
    	textField.setText("TicTacToe");
    	 
    	try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
        if (random.nextInt(2) == 0) {
            player1Turn = true;
            textField.setText("X turn");
        } else {
            player1Turn = false;
            textField.setText("O turn");
        }
    }

    public void check() {
        // Check for wins first
        if (checkWin("X")) {
            xWins();
        } else if (checkWin("O")) {
            oWins();
        } else if (isDraw()) { // Check for draw only if no one has won
            draw();
        }
    }

    public boolean checkWin(String player) {
        // Rows
        if (buttons[0].getText().equals(player) && buttons[1].getText().equals(player) && buttons[2].getText().equals(player)) {
        	
        	buttons[0].setBackground(Color.green);
        	buttons[1].setBackground(Color.green);
        	buttons[2].setBackground(Color.green);
        	       	
        	return true;
        	}
        if (buttons[3].getText().equals(player) && buttons[4].getText().equals(player) && buttons[5].getText().equals(player)) {
        	
        	buttons[3].setBackground(Color.green);
        	buttons[4].setBackground(Color.green);
        	buttons[5].setBackground(Color.green);
        	       	
        	return true;
        	}
        if (buttons[6].getText().equals(player) && buttons[7].getText().equals(player) && buttons[8].getText().equals(player)) {
        	
        	buttons[6].setBackground(Color.green);
        	buttons[7].setBackground(Color.green);
        	buttons[8].setBackground(Color.green);
        	       	
        	return true;
        	}

        // Columns
        if (buttons[0].getText().equals(player) && buttons[3].getText().equals(player) && buttons[6].getText().equals(player)) {
        	
        	buttons[0].setBackground(Color.green);
        	buttons[3].setBackground(Color.green);
        	buttons[6].setBackground(Color.green);
        	       	
        	return true;
        	}
        if (buttons[1].getText().equals(player) && buttons[4].getText().equals(player) && buttons[7].getText().equals(player)) {
        	
        	buttons[1].setBackground(Color.green);
        	buttons[4].setBackground(Color.green);
        	buttons[7].setBackground(Color.green);
        	       	
        	return true;
        	}
        if (buttons[2].getText().equals(player) && buttons[5].getText().equals(player) && buttons[8].getText().equals(player)) {
        	
        	buttons[2].setBackground(Color.green);
        	buttons[5].setBackground(Color.green);
        	buttons[8].setBackground(Color.green);
        	       	
        	return true;
        	}

        // Diagonals
        if (buttons[0].getText().equals(player) && buttons[4].getText().equals(player) && buttons[8].getText().equals(player)) {
        	
        	buttons[0].setBackground(Color.green);
        	buttons[4].setBackground(Color.green);
        	buttons[8].setBackground(Color.green);
        	       	
        	return true;
        	}
        if (buttons[2].getText().equals(player) && buttons[4].getText().equals(player) && buttons[6].getText().equals(player)) {
        	
        	buttons[2].setBackground(Color.green);
        	buttons[4].setBackground(Color.green);
        	buttons[6].setBackground(Color.green);
        	       	
        	return true;
        	}

        return false;
    }

    public boolean isDraw() {
        for (JButton button : buttons) {
            if (button.getText().isEmpty()) return false; // Empty space exists
        }
        return true; // All spaces are filled
    }

    public void xWins() {
        textField.setText("X Wins");
        disableButtons();
        titlePanel.add(playAgainButton, BorderLayout.EAST);
    }

    public void oWins() {
        textField.setText("O Wins");
        disableButtons();
        titlePanel.add(playAgainButton, BorderLayout.EAST);
    }

    public void draw() {
        textField.setText("It's a draw");
        for (JButton button : buttons) {
            button.setBackground(Color.red);
        }
        disableButtons();
        titlePanel.add(playAgainButton, BorderLayout.EAST);
    }

    public void disableButtons() {
        for (JButton button : buttons) {
            button.setEnabled(false);
        }
    }
}
