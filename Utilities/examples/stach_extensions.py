import uuid
import math

import pandas as pd

from fds.protobuf.stach.Package_pb2 import Package
from fds.protobuf.stach.NullValues import NullValues
from fds.protobuf.stach.table.DataType_pb2 import DataType

class StachExtensions:
    """The purpose of this class is to provide the helper methods for converting Stach to Tabular format"""

    @staticmethod
    def generate_excel(package):
        for table in StachExtensions.convert_to_table_format(package):
            writer = pd.ExcelWriter(str(uuid.uuid1()) + ".xlsx")
            table.to_excel(excel_writer=writer)
            writer.save()
            writer.close()

    @staticmethod
    def convert_to_table_format(package):
        tables = list()
        for primary_table_id in package.primary_table_ids:
            tables.append(StachExtensions.generate_table(package, primary_table_id))
        return tables

    @staticmethod
    def generate_table(package_response, primary_table_id):

        if isinstance(package_response, Package):
            primary_table = package_response.tables[primary_table_id]
            header_id = primary_table.definition.header_table_id
            header_table = package_response.tables[header_id]
            dimension_columns = list(filter(lambda column_obj: column_obj.is_dimension, primary_table.definition.columns))
            dimension_columns_count = len(dimension_columns)
            row_count = len(primary_table.data.rows)
            header_row_count = len(header_table.data.rows)

            headers = list(list())
            # Constructs the column headers by considering dimension columns and header rows
            for series_definition_column in header_table.definition.columns:
                header_row = list()
                for i in range(0, dimension_columns_count, 1):
                    if dimension_columns[i].description is "":
                        header_row.append(" ")
                    else:
                        header_row.append(dimension_columns[i].description)

                for i in range(0, header_row_count, 1):
                    header_row.append(str(SeriesDataHelper.get_value_helper(header_table.data.columns[series_definition_column.id], series_definition_column.type, i, series_definition_column.format.null_format)))
                headers.append(header_row)

            data = list(list())
            # Constructs the column data
            for i in range(0, row_count, 1):
                data_row = list()
                for series_definition_column in primary_table.definition.columns:
                    data_row.append(str(SeriesDataHelper.get_value_helper(primary_table.data.columns[series_definition_column.id], series_definition_column.type, i, series_definition_column.format.null_format)))
                data.append(data_row)

            if len(header_table.definition.columns) > 1:
                data_frame = pd.DataFrame(data=data)
                data_frame.columns = pd.MultiIndex.from_arrays(headers)
            else:
                data_frame = pd.DataFrame(data=data, columns = headers[0])
            
            return data_frame

        else:
            ValueError("Response data passed should be of package type.")


class SeriesDataHelper:

    @staticmethod
    def get_value_helper(series_data, datatype, index, null_format):
        if DataType.Name(datatype) == "STRING":
            return SeriesDataHelper.null_value_handler(datatype, series_data.string_array.values[index], null_format)
        elif DataType.Name(datatype) == "DOUBLE":
            return SeriesDataHelper.null_value_handler(datatype, series_data.double_array.values[index], null_format)
        elif DataType.Name(datatype) == "FLOAT":
            return SeriesDataHelper.null_value_handler(datatype, series_data.float_array.values[index], null_format)
        elif DataType.Name(datatype) == "INT32":
            return SeriesDataHelper.null_value_handler(datatype, series_data.int32_array.values[index], null_format)
        elif DataType.Name(datatype) == "INT64":
            return SeriesDataHelper.null_value_handler(datatype, series_data.int64_array.values[index], null_format)
        elif DataType.Name(datatype) == "BOOL":
            return SeriesDataHelper.null_value_handler(datatype, series_data.bool_array.values[index], null_format)
        elif DataType.Name(datatype) == "DURATION":
            return SeriesDataHelper.null_value_handler(datatype, series_data.duration_array.values[index], null_format)
        elif DataType.Name(datatype) == "TIMESTAMP":
            return SeriesDataHelper.null_value_handler(datatype, series_data.timestamp_array.values[index], null_format)
        else:
            ValueError("The datatype is not implemented")

    @staticmethod
    def null_value_handler(datatype, value, null_format):
        if DataType.Name(datatype) == "STRING":
            if NullValues.STRING == value:
                return null_format
            return value
        elif DataType.Name(datatype) == "DOUBLE":
            if math.isnan(value):
                return null_format
            return value
        elif DataType.Name(datatype) == "FLOAT":
            if math.isnan(value):
                return null_format
            return value
        elif DataType.Name(datatype) == "INT32":
            if NullValues.INT32 == value:
                return null_format
            return value
        elif DataType.Name(datatype) == "INT64":
            if NullValues.INT64 == value:
                return null_format
            return value
        elif DataType.Name(datatype) == "DURATION":
            if NullValues.DURATION.equals(value):
                return null_format
            return value
        elif DataType.Name(datatype) == "TIMESTAMP":
            if NullValues.TIMESTAMP.equals(value):
                return null_format
            return value
        else:
            return value
