import csv
import constants as v
import classes as c

# Date MM-dd-yyyy HH:mm:ss


# Reads from specified CSV file (specified in settings file)
# Outputs analysis to output file
def parse_file():
    temp_user = c.User('0','0')
    user_array = []

    print('Loading from CSV channel.csv')
    file = open('channel2.csv', encoding="utf8")
    with file as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                parse_user(row, user_array)
                line_count +=1
    print(f'Done. {line_count} messages read')
    print(f'Users found: {len(user_array)}')

    for user in user_array:
        percentage = user.number_messages / line_count
        print(f'Username: {user.username}   Messages: {user.number_messages}    Contribution: {percentage * 100}%')


# Parses current line stats and updates user_array accordingly
def parse_user(current_row, user_array):
    user_id = current_row[v.USER_ID]
    user_index = 0
    user_found = 0
    for user in user_array:
        if user.user_id == user_id:
            user_found = 1
            break
        user_index += 1

    if user_found:
        # Update user stats
        user_array[user_index].number_messages += 1
    else:
        # If user not found, add them to array
        user_array.append(c.User(user_id, current_row[v.USERNAME]))


# Loads settings file.
# Configures what information should be calculated and printed to output file
def load_settings():
    print('settings placeholder')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_file()


