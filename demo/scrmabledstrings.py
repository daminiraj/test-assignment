from filehandler import load_dictionary, load_input
import itertools
import logging
import argparse
import sys

logging.basicConfig(filename='log_information.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--dictionary", metavar='', required=True, help=' [PATH TO DICTIONARY FILE]')
    parser.add_argument("--input", metavar='', required=True, help=' [PATH TO INPUT FILE]')
    parser.parse_args()


def find_length(lines):
    length_of_all_words = 0
    logging.info('Finding lengths of all the dictionary words.')
    for element in lines:
        length_of_all_words += len(element)
        if len(element) < 2 or len(element) > 105 or length_of_all_words > 105:
            logging.error("Exiting the program as dictionary words do not comply with prescribed length.")
            sys.exit(1)


def find_anagrams(data):
    logging.info('Finding anagrams of all the dictionary words.')
    scrambled_list = []
    for word in data:
        mid = list(word[1:-1])
        result = ["".join(perm) for perm in itertools.permutations(mid)]
        for element in (set(result)):
            scrambled_words = u'%c%s%c' % (word[0], ''.join(element), word[-1])
            scrambled_list.append(scrambled_words)
    logging.info('List of all the anagrams for the dictionary. :{}'.format(scrambled_list))
    return scrambled_list


def comparison(scrambled_data,input_data):
    logging.info('Comparing the dictionary words with input strings.')
    for value in input_data.keys():
        count = 0
        for element in scrambled_data:
            if element in value:
                logging.info('Elements which are matched from {} line in input string: {}'.
                             format(input_data.get(value),element))
                count += 1
        print ("Case #{}: {}".format(input_data.get(value), count))


if __name__ == "__main__":
    main(sys.argv)
    words = load_dictionary(sys.argv[2])
    input_string = load_input(sys.argv[4])
    find_length(words)
    scrambled = find_anagrams(words)
    comparison(scrambled, input_string)

