from fluxify.helper.yamlparser import apply_value
from fluxify.transformers.transformer import handle_transformations
from fluxify.handler.conditions import handle_conditions
from fluxify.utils import Utils
import pandas as pd
import numpy as np
import parser
import gc


class CSVHandler:

    def __init__(self, filepath, mapping, delimiter=',', skip_blank_lines=False, skip_header=False, error_tolerance=False,
                 bulksize=100, save_unmatched=True, unmatched_key='unmatched'):

        self.filepath = filepath
        self.mapping = mapping
        self.delimiter = delimiter
        self.skip_blank_lines = skip_blank_lines
        self.skip_header = skip_header
        self.bulksize = bulksize
        self.__save_unmatched = save_unmatched
        self.__unmatched_key = unmatched_key

        self.__error_tolerance = error_tolerance

        self.__stats = {
            'header_skipped': False,
            'total_count': 0,
            'total_count_with_header': 0
        }

    def process(self):
        self.csv = pd.read_csv(self.filepath, delimiter=self.delimiter, skip_blank_lines=self.skip_blank_lines, header=None)
        self.csv = self.csv.values

        labels = None
        result = []

        for it, data in enumerate(self.csv):
            # Updating stats
            self.__stats['total_count_with_header'] += 1

            # Skipping the first line if needed
            if self.skip_header and it == 0:
                labels = data

                # Updating stats
                self.__stats['header_skipped'] = True

                continue

            # Updating stats
            self.__stats['total_count'] += 1

            item = {}
            cols_to_delete = []
            for map_key, map_value in self.mapping.items():

                if 'col' in map_value:
                    col = int(map_value['col'])
                    finalvalue = data[col]

                    # Set to None if value is NaN
                    finalvalue = Utils.clean_if_nan(finalvalue)

                    if 'transformations' in map_value:
                        finalvalue = handle_transformations(map_value['transformations'], finalvalue, error_tolerance=self.__error_tolerance)

                    item = apply_value(item, map_key, finalvalue)

                    if 'conditions' in map_value:
                        finalvalue = handle_conditions(map_value['conditions'], item, data)
                        item = apply_value(item, map_key, finalvalue)

                    # To remember which cols have already been retrieved
                    if self.__save_unmatched:
                        cols_to_delete.append(col)
                elif 'value' in map_value:
                    finalvalue = map_value['value']
                    if type(finalvalue) == str:
                        finalvalue = finalvalue.replace('$subject', 'item')
                        expr = parser.expr(finalvalue)
                        finalvalue = eval(expr.compile(''))

                    # Set to None if value is NaN
                    finalvalue = Utils.clean_if_nan(finalvalue)

                    item = apply_value(item, map_key, finalvalue)

                    if 'conditions' in map_value:
                        finalvalue = handle_conditions(map_value['conditions'], item, data)
                        item = apply_value(item, map_key, finalvalue)
                elif 'conditions' in map_value:
                    finalvalue = handle_conditions(map_value['conditions'], item, data)
                    item = apply_value(item, map_key, finalvalue)
                else:
                    text = '{} : No supported options found in mapping. Supported: [col, value, conditions]'.format(map_key)
                    if self.__error_tolerance:
                        Utils.log('error', text)
                        continue
                    else:
                        raise Exception(text)

            # Unmatched
            if self.__save_unmatched:
                for col in cols_to_delete:
                    data[col] = None

                item[self.__unmatched_key] = self.__get_unmatched(data, labels)

            result.append(item)

        return result

    def lazy_process(self):
        self.csv = pd.read_csv(self.filepath, delimiter=self.delimiter, skip_blank_lines=self.skip_blank_lines, header=None)
        csv_generator = self.csv.T.iteritems()

        ix = None
        labels = []
        result = []

        if self.skip_header:
            ix, labels = next(csv_generator)
            # Updating stats
            self.__stats['header_skipped'] = True
            self.__stats['total_count_with_header'] += 1

        for it, data in csv_generator:
            item = {}
            cols_to_delete = []

            # Updating stats
            self.__stats['total_count'] += 1
            self.__stats['total_count_with_header'] += 1

            # Iterating through the mapping
            for map_key, map_value in self.mapping.items():
                if 'col' in map_value:
                    col = int(map_value['col'])
                    finalvalue = data[col]

                    # Set to None if value is NaN
                    finalvalue = Utils.clean_if_nan(finalvalue)

                    if 'transformations' in map_value:
                        finalvalue = handle_transformations(map_value['transformations'], finalvalue, error_tolerance=self.__error_tolerance)

                    item = apply_value(item, map_key, finalvalue)

                    if 'conditions' in map_value:
                        finalvalue = handle_conditions(map_value['conditions'], item, data)
                        item = apply_value(item, map_key, finalvalue)

                    # To remember which cols have already been retrieved
                    if self.__save_unmatched:
                        cols_to_delete.append(col)
                elif 'value' in map_value:
                    finalvalue = map_value['value']
                    if type(finalvalue) == str:
                        finalvalue = finalvalue.replace('$subject', 'item')
                        expr = parser.expr(finalvalue)
                        finalvalue = eval(expr.compile(''))

                    # Set to None if value is NaN
                    finalvalue = Utils.clean_if_nan(finalvalue)

                    if 'transformations' in map_value:
                        finalvalue = handle_transformations(map_value['transformations'], finalvalue, error_tolerance=True)

                    item = apply_value(item, map_key, finalvalue)

                    if 'conditions' in map_value:
                        finalvalue = handle_conditions(map_value['conditions'], item, data)
                        item = apply_value(item, map_key, finalvalue)
                elif 'conditions' in map_value:
                    finalvalue = handle_conditions(map_value['conditions'], item, data)
                    item = apply_value(item, map_key, finalvalue)
                else:
                    text = '{} : No supported options found in mapping. Supported: [col, value, conditions]'.format(map_key)
                    if self.__error_tolerance:
                        Utils.log('error', text)
                        continue
                    else:
                        raise Exception(text)

            # Unmatched
            if self.__save_unmatched:
                for col in cols_to_delete:
                    data[col] = None

                item[self.__unmatched_key] = self.__get_unmatched(data, labels)

            result.append(item)
            if (len(result) % self.bulksize) == 0:
                self.callback(result)
                result = []
                gc.collect()

        if len(result) > 0:
            self.callback(result)
            result = []
            gc.collect()

    def __get_unmatched(self, data, labels):
        unmatched = {}
        for ix, col in enumerate(data):
            if col is not None:
                if self.__has(labels, ix):
                    label = labels[ix]
                else:
                    label = str(ix)

                col = Utils.clean_if_nan(col)
                if col is not None and not Utils.empty(col):
                    unmatched[label] = col

        return unmatched

    def __has(self, list: list, index):
        try:
            list[index]

            return True
        except Exception as e:
            return False

    def set_bulksize(self, size):
        self.bulksize = size

    def set_callback(self, callback):
        self.callback = callback

    def get_stats(self):
        return self.__stats
