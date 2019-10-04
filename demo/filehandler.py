from contextlib import contextmanager
import logging


@contextmanager
def open_file(file,mode):
    try:
        f = open(file,mode)
    except FileNotFoundError:
        logging.error('{} is not present'.format(file))
    else:
        yield f
    finally:
        f.close()


def load_dictionary(d_file):
    with open_file(d_file, "r") as dictFile:
        data = dictFile.read().splitlines()
        words = list(set(data)) # removing duplicate values from dictionary.
    return words


def load_input(i_file):
    with open_file(i_file, "r") as inputFile:
        data = inputFile.read().splitlines()
        counter = 0
        input_data = {}
        for word in data:
            counter += 1
            input_data[word] = counter
    return input_data
