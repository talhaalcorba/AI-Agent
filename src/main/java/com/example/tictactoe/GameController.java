package com.example.tictactoe;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/game")
public class GameController {
    private final GameService service;

    public GameController(GameService service) {
        this.service = service;
    }

    @GetMapping
    public GameState getBoard() {
        return service.getState();
    }

    @PostMapping("/move")
    public GameState makeMove(@RequestParam int position) {
        return service.move(position);
    }
}
