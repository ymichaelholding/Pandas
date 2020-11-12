class RuleCheck:
    def __init__(self,dataframe):
        self.dataframe = dataframe

    def is_unique_calc(self,column_name):
        return self.dataframe[column_name].is_unique

    def not_null_calc(self,column_name):
        return any(self.dataframe[column_name].isnull())

    def char_length_less_calc(self,column_name, length):
        return any(self.dataframe[column_name].str.len() < length)

    def char_length_greater_calc(self,column_name, length):
        return any(self.dataframe[column_name].str.len() > length)

    def is_numeric_calc(self,column_name):
        return any(self.dataframe[column_name].astype(str).str.isnumeric())

    def date_format_check(dataframe,column_name,dateformat):
        return True
