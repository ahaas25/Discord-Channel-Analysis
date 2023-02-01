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

    return c.Channel(user_array, line_count)


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


# Writes CSV output file
def write_file(user_array, messages):
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        row_text = generate_header()
        writer.writerow(row_text)

        row = 1
        count = 0
        for user in user_array:
            if v.show_id:
                row_text[count] = user.user_id
                count += 1
            if v.show_username:
                row_text[count] = user.username
                count += 1
            if v.show_number_messages:
                row_text[count] = user.number_messages
                count += 1
            if v.show_contribution:
                row_text[count] = (user.number_messages / messages) * 100
                count += 1
            count = 0
            writer.writerow(row_text)
            row += 1
    print("Wrote to ./output.csv")


# Loads settings, generates header text
def generate_header():
    to_return = []

    if v.show_id:
        to_return.append("USER_ID")
    if v.show_username:
        to_return.append("Username")
    if v.show_number_messages:
        to_return.append("Number of Messages")
    if v.show_contribution:
        to_return.append("Contribution")

    return to_return

# Loads settings file.
# Configures what information should be calculated and printed to output file
def load_settings():
    print('settings placeholder')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    channel = parse_file()
    write_file(channel.user_array, channel.messages)


