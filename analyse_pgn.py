import chess.pgn
import chess.engine

# Lade die PGN-Datei
pgn = open("game.pgn")
game = chess.pgn.read_game(pgn)

# Starte die Stockfish-Engine
engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")  # Stockfish-Pfad in GitHub Actions

# Analysiere das Spiel
for move in game.mainline_moves():
    board = game.board()
    board.push(chess.Move.from_uci(move))
    result = engine.analyse(board, chess.engine.Limit(time=2.0))  # Analysezeit: 2 Sekunden pro Zug
    print(f"Zug: {move} - Bewertung: {result['score']}")

engine.quit()
