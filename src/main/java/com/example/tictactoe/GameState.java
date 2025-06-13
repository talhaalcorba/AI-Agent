package com.example.tictactoe;

public class GameState {
    private char[] board;
    private String message;

    public GameState(char[] board, String message) {
        this.board = board;
        this.message = message;
    }

    public char[] getBoard() {
        return board;
    }

    public String getMessage() {
        return message;
    }
}
