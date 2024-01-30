import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

class DataCleaner:

    def __init__(self, df):
        self.df = df

    def fill_missing_values(self, method='mean'):
        if method == 'mean':
            self.df.fillna(self.df.mean(), inplace=True)
        elif method == 'median':
            self.df.fillna(self.df.median(), inplace=True)
        elif method == 'mode':
            self.df.fillna(self.df.mode().iloc[0], inplace=True)
        return self.df

    def drop_missing_values(self):
        self.df.dropna(inplace=True)
        return self.df

    def convert_data_type(self, column, new_type):
        self.df[column] = self.df[column].astype(new_type)
        return self.df

    def normalize_data(self, columns):
        scaler = MinMaxScaler()
        self.df[columns] = scaler.fit_transform(self.df[columns])
        return self.df

    def encode_categorical_data(self, column):
        encoder = OneHotEncoder(sparse=False)
        encoded = encoder.fit_transform(self.df[[column]])
        encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names([column]))
        self.df = pd.concat([self.df, encoded_df], axis=1).drop(column, axis=1)
        return self.df

    def remove_duplicates(self):
        self.df.drop_duplicates(inplace=True)
        return self.df

    def clean_text(self, column):
        self.df[column] = self.df[column].str.lower().str.replace('[^\w\s]', '')
        return self.df
