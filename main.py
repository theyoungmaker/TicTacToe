import turtle

EAST, NORTH = 0, 90
LINE_LEN = 6
L1_X, L1_Y = -3, 1
L2_X, L2_Y = -3, -1
L3_X, L3_Y = -1, -3
L4_X, L4_Y = 1, -3


def main():
  global board, turn, isGameOver
  board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  setup()
  turn = 1
  isGameOver = False
  screen.onclick(play)

  if (isGameOver):
    turtle.bye()


def setup():
  global screen
  screen = turtle.Screen()
  screen.setup(800, 800)
  screen.title("The Young Maker Python Beginner - Tic Tac Toe")
  screen.setworldcoordinates(-5, -5, 5, 5)
  turtle.speed("fastest")
  turtle.hideturtle()
  draw_lines()


def draw_lines():
  turtle.pencolor("black")
  turtle.pensize(10)

  turtle.penup()
  turtle.goto(L1_X, L1_Y)
  turtle.setheading(EAST)
  turtle.pendown()
  turtle.forward(LINE_LEN)

  turtle.penup()
  turtle.goto(L2_X, L2_Y)
  turtle.setheading(EAST)
  turtle.pendown()
  turtle.forward(LINE_LEN)

  turtle.penup()
  turtle.goto(L3_X, L3_Y)
  turtle.setheading(NORTH)
  turtle.pendown()
  turtle.forward(LINE_LEN)

  turtle.penup()
  turtle.goto(L4_X, L4_Y)
  turtle.setheading(NORTH)
  turtle.pendown()
  turtle.forward(LINE_LEN)


def draw(board):
  draw_lines()
  for row_index in range(3):
    for col_index in range(3):
      draw_move(row_index, col_index, board[row_index][col_index])


def draw_move(row_index, col_index, move):
  if move == 0: return

  intermediate_x = 2 * (col_index - 1)
  intermediate_y = -2 * (row_index - 1)

  if move == 1: draw_cross(intermediate_x, intermediate_y)
  else: draw_circle(intermediate_x, intermediate_y)


def draw_cross(x, y):
  turtle.color('blue')
  turtle.up()
  turtle.goto(x - 0.75, y - 0.75)
  turtle.down()
  turtle.goto(x + 0.75, y + 0.75)
  turtle.up()
  turtle.goto(x - 0.75, y + 0.75)
  turtle.down()
  turtle.goto(x + 0.75, y - 0.75)


def draw_circle(x, y):
  turtle.color('red')
  turtle.up()
  turtle.goto(x, y - 0.75)
  turtle.setheading(EAST)
  turtle.down()
  turtle.circle(0.75, steps=100)


def play(x, y):
  global turn, isGameOver
  is_first_row = 1 < y and y < 3
  is_second_row = -1 < y and y < 1
  is_third_row = -3 < y and y < -1

  is_first_col = -3 < x and x < -1
  is_second_col = -1 < x and x < 1
  is_third_col = 1 < x and x < 3

  if is_first_row:
    row_index = 0
  elif is_second_row:
    row_index = 1
  elif is_third_row:
    row_index = 2
  else:
    return

  if is_first_col:
    col_index = 0
  elif is_second_col:
    col_index = 1
  elif is_third_col:
    col_index = 2
  else:
    return

  if board[row_index][col_index] != 0: return

  if (turn == 1):
    # assign value of turn to board[row_index][col_index]
    # in this case, a value of 1 (representing 'x') is assigned
    board[row_index][col_index] = turn
    turn = 2
  else:
    # assign value of turn to board[row_index][col_index]
    # in this case, a value of 2 (representing 'o') is assigned
    board[row_index][col_index] = turn
    turn = 1

  draw(board)
  outcome = check_outcome(board)
  if outcome == 1:
    screen.textinput("Game over!", "X won!")
  elif outcome == 2:
    screen.textinput("Game over!", "O won!")
  elif outcome == 3:
    screen.textinput("Game over!", "Tie!")

  if outcome != 0:
    isGameOver = True


# Returns the following:
#    0: No one win yet
#    1: Player 1 wins
#    2: Player 2 wins
#    3: Tie
def check_outcome(board):

  if board[0][0] > 0 and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
    return board[0][0]

  if board[1][0] > 0 and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
    return board[1][0]

  if board[2][0] > 0 and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
    return board[2][0]

  if board[0][0] > 0 and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
    return board[0][0]

  if board[0][1] > 0 and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
    return board[0][1]

  if board[0][2] > 0 and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
    return board[0][2]

  if board[0][0] > 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    return board[0][0]

  if board[2][0] > 0 and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
    return board[2][0]

  if check_tie(board):
    return 3
  else:
    return 0


def check_tie(board):
  num_pieces = 0
  for row_index in range(3):
    for col_index in range(3):
      if (board[row_index][col_index] > 0):
        num_pieces += 1

  if (num_pieces == 9):
    return True

  return False


if __name__ == "__main__":
  main()
