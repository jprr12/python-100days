import turtle
import pandas
from scorebox import Scorebox

# GUI setup
screen = turtle.Screen()
screen.title('USA States Game')
# GUI background image
BG_IMG = 'blank_states_img.gif'
screen.addshape(BG_IMG)
turtle.shape(BG_IMG)

# open states data
states_data = pandas.read_csv('50_states.csv')
states_list = states_data.state.to_list()
guessed_states = []

# initialize scorebox
sb = Scorebox()

while len(guessed_states) < 50:
    user_guess = screen.textinput(f'Guessed States: {sb.score}/50', 'Name a US State').title()
    if user_guess == 'Exit':
        missed_states = []
        for state in states_list:
            if state not in guessed_states:
                missed_states.append(state)
        df = pandas.DataFrame(missed_states)
        df.to_csv('missed_states.csv')
        print(f"You got {sb.score} states and missed {50 - sb.score} states. Here are the states you missed:")
        print(df)
        break
    elif user_guess in guessed_states:
        continue
    else:
        if user_guess in states_list:
            coordinates = states_data[states_data.state == user_guess.title()]
            x_pos = int(coordinates.x.iloc[0])
            y_pos = int(coordinates.y.iloc[0])
            sb.show_state(user_guess, x_pos, y_pos)
            guessed_states.append(user_guess)
            sb.update_score()
        else:
            continue

