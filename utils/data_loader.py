import json


class DataLoader:

    @staticmethod
    def load(file_name):

        with open(
            f"testdata/{file_name}"
        ) as file:

            return json.load(file)