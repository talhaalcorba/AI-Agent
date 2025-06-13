package com.example.tictactoe;

import org.springframework.stereotype.Service;

@Service
public class GameService {
    private char[] board = new char[9];
    private char current = 'X';
    private int moves = 0;

    public GameState getState() {
        return new GameState(board.clone(), "Next player: " + current);
    }

    public GameState move(int position) {
        if (position < 1 || position > 9) {
            return new GameState(board.clone(), "Invalid position");
        }
        if (board[position - 1] != '\0') {
            return new GameState(board.clone(), "Position already taken");
        }
        board[position - 1] = current;
        moves++;
        char winner = checkWinner();
        if (winner != '\0') {
            String msg = "Player " + winner + " wins!";
            reset();
            return new GameState(board.clone(), msg);
        }
        if (moves == 9) {
            String msg = "It's a draw!";
            reset();
            return new GameState(board.clone(), msg);
        }
        current = (current == 'X') ? 'O' : 'X';
        return new GameState(board.clone(), "Next player: " + current);
    }

    private char checkWinner() {
        int[][] w = {
            {0,1,2},{3,4,5},{6,7,8},
            {0,3,6},{1,4,7},{2,5,8},
            {0,4,8},{2,4,6}
        };
        for (int[] pos : w) {
            char a = board[pos[0]];
            if (a != '\0' && a == board[pos[1]] && a == board[pos[2]]) {
                return a;
            }
        }
        return '\0';
    }

    private void reset() {
        board = new char[9];
        current = 'X';
        moves = 0;
    }
}
