import bingo

def main():
    setup = bingo.BingoSetup('input.txt')

    called_numbers = iter(setup.get_chosen_numbers())
    boards = setup.get_boards()

    winning_board = None
    while winning_board == None:
        number = next(called_numbers)
        
        for board in boards:
            board.mark(number)

            if board.isWinner():
                winning_board = board
                break; 

    print(winning_board.get_sum())
    print(number)
    print(winning_board.get_sum() * number)


if __name__ == "__main__":
    main()


