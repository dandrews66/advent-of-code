import bingo

def main():
    setup = bingo.BingoSetup('input.txt')

    called_numbers = iter(setup.get_chosen_numbers())
    boards = setup.get_boards()

    losing_board = None
    while len(boards) > 0:
        number = next(called_numbers)
        
        to_remove = []
        for board in boards:
            board.mark(number)

            if board.isWinner():
                losing_board = board
                to_remove.append(board)

        for board in to_remove:
            boards.remove(board)
    
    losing_board.print()
    print(losing_board.get_sum() * number)

if __name__ == "__main__":
    main()


