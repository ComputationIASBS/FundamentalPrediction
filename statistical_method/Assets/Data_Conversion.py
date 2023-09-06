import os
import pandas as pd

class Data_Conversion:
    def __init__(self, input_path, output_path, Log, main_dir):
        self.iPath = input_path
        self.oPath = output_path
        self.Log = Log
        self.main_dir = main_dir

    def __call__(self, file_name, delete_column, groupBase_column, singelValue_columns, unWanted_columns):
        self.Log(f'\n..:: Start Data_Conversion Data for \"{file_name}\" ::..')
        input_file_path = os.path.join(self.main_dir, self.iPath, f"{file_name}.csv")
        df = pd.read_csv(input_file_path)
        df = df.drop(delete_column, axis=1)

        self.create_outPutFolder(self.oPath)
        
        groupBase_column_set = set(df[groupBase_column])
        for x in groupBase_column_set:
            if len(df[df[groupBase_column]==x]) < 2:
                df = df.drop(df[df[groupBase_column] == x].index)

        groupBaseColumn_df = df.groupby(groupBase_column)
        result = pd.DataFrame({groupBase_column: list(groupBaseColumn_df.groups.keys())})

        for col_name in singelValue_columns:
            temp = pd.DataFrame({col_name: list(groupBaseColumn_df[col_name].last(1))})
            result =  pd.concat([result, temp], axis=1)

        for col_name in df.columns:
            if col_name in singelValue_columns:
                temp1 = groupBaseColumn_df.apply(lambda x: x.iloc[:-1][col_name].agg(['mean', 'median', 'min', 'max']))
                temp1.columns = [f'{col_name}_mean', f'{col_name}_median', f'{col_name}_min', f'{col_name}_max']
                temp1 = temp1.reset_index(drop=True)
                result = pd.concat([result, temp1], axis=1)

            elif col_name not in unWanted_columns:
                temp1 = groupBaseColumn_df.apply(lambda x: x[col_name].agg(['mean', 'median', 'min', 'max']))
                temp1.columns = [f'{col_name}_mean', f'{col_name}_median', f'{col_name}_min', f'{col_name}_max']
                temp1 = temp1.reset_index(drop=True)
                result = pd.concat([result, temp1], axis=1)
        
        result.to_csv(f'{self.oPath}/{file_name}.csv', index=False) 
        self.Log(f'..:: End Data_Conversion Data for \"{file_name}\" ::..')

    def create_outPutFolder(self, tmp_path):
        if not os.path.isdir(tmp_path):
            os.makedirs(tmp_path)