# Connect Four Game (With a Twist!)

This is a Python-based Connect Four game with multiple modes including:
- **Single-player (vs. Computer)**
- **Two-player mode**
- **Computer with Minimax Algorithm**
- **Alpha-Beta Pruning for enhanced AI**

This game also comes with aesthetics like ASCII art and animations to enhance the gaming experience. Challenge yourself against an AI that uses minimax and alpha-beta pruning, or play against a friend.

### Features

1. **Interactive Loading Screen**:
    - Includes an animated loading bar and witty game commentary to set the mood.
   
2. **Game Modes**:
    - **Two-player mode**: Play against a friend locally.
    - **Single-player mode**: Play against the computer AI which uses a Minimax algorithm with Alpha-Beta pruning.

3. **Game Board**:
    - The game is played on a 7x6 board displayed with clean, simple ASCII art.
    - Players take turns placing their respective tokens ("X" for Player 1 and "O" for the AI).

4. **Alpha-Beta Pruning**:
    - The AI is optimized with the Minimax algorithm, leveraging alpha-beta pruning to reduce computation time without sacrificing decision quality.

### Instructions

1. Run the game from the terminal.
2. You'll see an interactive welcome screen.
3. Choose the game mode:
    - Play (Single Player vs. AI)
    - Exit
    - Options
4. Place your tokens by entering the column number (0-6). The game alternates between the player and the AI.
5. The game will announce the winner, whether it's the player, the AI, or a tie.

### Code Highlights

- **Minimax Algorithm**: Implemented to evaluate the best possible move for the AI.
- **Alpha-Beta Pruning**: Enhances the AI’s decision-making by eliminating unnecessary branches in the game tree.
- **ASCII Art**: Adds fun and visual appeal to the game.
- **Loading Animation**: Custom animated loading sequence to build suspense before the game starts.

### How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/connect-four.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python connect_four.py
   ```

### Authors

- Emily Dogbatse
- Davis Carson
