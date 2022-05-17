import pandas as pd


class IntentExample:
    def __init__(self, text, label, do_lower_case):
        self.original_text = text
        self.text = text
        self.label = label

        if do_lower_case:
            self.text = self.text.lower()


def load_intent_examples(file_path, do_lower_case=True):
    examples = []

    with open('{}/seq.in'.format(file_path), 'r', encoding="utf-8") as f_text, open('{}/label'.format(file_path), 'r',
                                                                                    encoding="utf-8") as f_label:
        for text, label in zip(f_text, f_label):
            e = IntentExample(text.strip(), label.strip(), do_lower_case)
            examples.append(e)

    return examples


def load_dataset_df():
    file_paths = ["dataset/train", "dataset/valid", "dataset/test"]

    examples = []

    for file_path in file_paths:
        ds_name = file_path.split("/")[-1]
        with open(f'{file_path}/seq.in', 'r', encoding="utf-8") as f_text, open(f'{file_path}/label', 'r',
                                                                                encoding="utf-8") as f_label:
            for text, label in zip(f_text, f_label):
                examples.append((text.strip(), label.strip(), ds_name))

    df = pd.DataFrame(examples, columns=["text", "intent", "ds_name"])
    df = df.sample(frac=1.0)
    df = df.reset_index(drop=True)

    return df
