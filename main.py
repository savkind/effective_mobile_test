from funcs import *


try:
    data = pd.read_csv(Constants.default_file_name,
                       encoding=Constants.encoding, sep=Constants.sep)

except FileNotFoundError:
    data = pd.DataFrame(columns=[Constants.column_id, Constants.column_date,
                        Constants.column_cat, Constants.column_sum, Constants.column_desc])
    write_file(data)

prepare_dataframe(data)

print(Messages.msg_commands)

while True:
    try:
        command = input(Messages.user_input)

        match command:
            case '1':
                balance = read_balance(data)
                print(balance)
            case '2':
                data = add_record(data)
            case '3':
                print(data)
                print(Messages.msg_input_id)
                id = int(input())
                data = edit_record(id, data)
            case '4':
                search_record(data)
            case _:
                print(Messages.msg_uncor_command)

    except Exception as err:
        print(err)
