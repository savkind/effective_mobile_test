import pandas as pd
import datetime
from Constants import *
from Messages import *


def prepare_dataframe(data: pd.DataFrame):
    data[Constants.column_date] = pd.to_datetime(
        data[Constants.column_date], format=Constants.date_format)
    data[Constants.column_sum] = data[Constants.column_sum].astype(float)
    data[Constants.column_id] = data[Constants.column_id].astype(int)


def read_balance(data: pd.DataFrame) -> float:
    incomes: float = sum(data[data[Constants.column_cat] ==
                              Constants.category_plus][Constants.column_sum])
    outcomes: float = sum(data[data[Constants.column_cat] ==
                               Constants.category_minus][Constants.column_sum])
    return incomes - outcomes


def write_file(data: pd.DataFrame):
    data.to_csv(Constants.default_file_name, sep=Constants.sep,
                encoding=Constants.encoding, index=False)


def add_record(data: pd.DataFrame, id: int = None) -> pd.DataFrame:
    print(Messages.msg_add)

    row = input()
    current_date = datetime.datetime.now().strftime(Constants.date_format)

    row = row.split(Constants.sep)
    row[0] = row[0].lower()
    if row[0] != Constants.category_plus and row[0] != Constants.category_minus:
        raise ValueError(Messages.msg_uncor_cat)

    if row[1].isdigit == False:
        raise ValueError(Messages.msg_uncor_sum)

    if id == None:
        last_row = data.tail(1)
        last_id = last_row[Constants.column_id]
        id = last_id + 1
        mode = Constants.mode_create
    else:
        mode = Constants.mode_edit

    record = {Constants.column_id: id, Constants.column_date: current_date,
              Constants.column_cat: row[0], Constants.column_sum: row[1], Constants.column_desc: row[2]}

    if mode == Constants.mode_create:
        record = pd.DataFrame.from_dict(record)
        data = pd.concat([data, record])

    elif mode == Constants.mode_edit:
        row_index = data.loc[data[Constants.column_id] == id].index[0]
        data.at[row_index, Constants.column_cat] = record[Constants.column_cat]
        data.at[row_index, Constants.column_sum] = float(
            record[Constants.column_sum])
        data.at[row_index, Constants.column_desc] = record[Constants.column_desc]

    prepare_dataframe(data)

    write_file(data)

    return data


def search_record(data: pd.DataFrame):

    print(Messages.msg_search)

    row = input()
    row = row.split(Constants.filter_split)

    row[0] = row[0].upper()

    if row[0] != Constants.column_date and row[0] != Constants.column_sum and row[0] != Constants.column_cat:
        raise ValueError(Messages.msg_uncor_filter)

    if row[0] == Constants.column_sum:
        row[1] = float(row[1])
    elif row[0] == Constants.column_date:
        row[1] = datetime.datetime.strptime(row[1], Constants.date_format)

    searched_record = data[data[row[0]] == row[1]]

    print(searched_record)


def edit_record(id: int, data: pd.DataFrame) -> pd.DataFrame:
    data: pd.DataFrame = add_record(data, id)
    return data
