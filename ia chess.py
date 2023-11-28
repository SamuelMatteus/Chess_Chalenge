import chess
import chess.svg
import chess.engine

def evaluate_board(board):
    # Função de avaliação simples
    evaluation = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            value = {
                chess.PAWN: 1,
                chess.KNIGHT: 3,
                chess.BISHOP: 3,
                chess.ROOK: 5,
                chess.QUEEN: 9,
                chess.KING: 100
            }[piece.piece_type]

            if piece.color == chess.WHITE:
                evaluation += value
            else:
                evaluation -= value

    return evaluation

def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            max_eval = max(max_eval, eval)
            board.pop()
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            min_eval = min(min_eval, eval)
            board.pop()
        return min_eval

def best_move(board, depth):
    legal_moves = list(board.legal_moves)
    best_move = None
    best_eval = float('-inf')

    for move in legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, False)
        board.pop()

        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move

def play_chess():
    board = chess.Board()
    depth = 2  # Profundidade da busca (ajuste conforme desejado)

    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = best_move(board, depth)
        else:
            move_uci = input("Digite a jogada do oponente em notação UCI: ")
            move = chess.Move.from_uci(move_uci)

        board.push(move)

    print("Fim do jogo.")
    print("Resultado: {}".format(board.result()))

if __name__ == "__main__":
    play_chess()
