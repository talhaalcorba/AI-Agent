# AI-Agent
AI Agent

## Tic-Tac-Toe Game

<<<<<<< qm1n8z-codex/x-o-x-oyunu-hazırla
This repository includes a simple Tic-Tac-Toe (XOX) game. A Spring Boot version
is provided alongside the original Python script.
=======
This repository includes a simple Tic-Tac-Toe (XOX) game. A Spring Boot version is provided alongside the original Python script.
>>>>>>> main

### Running the Spring Boot game

Ensure you have Java 17 and Maven installed. Start the application with:

```bash
mvn spring-boot:run
```

You can interact with the game using HTTP requests. For example:

```bash
# Get the current board
curl http://localhost:8080/game

# Place a move
curl -X POST "http://localhost:8080/game/move?position=1"
```

### Running the Python game

Execute the script using Python 3:

```bash
python tic_tac_toe.py
```

Follow the on-screen prompts to place your X or O on the board. The game ends when a player wins or the board is full.
<<<<<<< qm1n8z-codex/x-o-x-oyunu-hazırla

### Using the web front-end

After starting the Spring Boot application, open `http://localhost:8080/index.html`
in your browser to play the game with a graphical interface. X markers appear in
yellow and O markers appear in navy blue.
=======
>>>>>>> main
