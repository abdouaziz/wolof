import torch
from torch.utils.data import Dataset
from utils.config import WolofConfig
from transformers import BertTokenizer


class Dataset(Dataset):
    def __init__(self, texts, targets=None, is_test=False):
        self.texts = texts
        self.texts = texts
        self.config = WolofConfig().load()
        self.is_test = is_test
        self.tokenizer = BertTokenizer.from_pretrained(self.config.model_name)
        self.max_len = self.config.max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = str(self.text[idx])
        text = ' '.join(text.split())
        global inputs

        inputs = self.tokenizer(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            padding="max_length",
            truncation=True,
            pad_to_max_length=True,
        )

        ids = torch.tensor(inputs['input_ids'], dtype=torch.long)
        mask = torch.tensor(inputs['attention_mask'], dtype=torch.long)
        token_type = torch.tensor(inputs['token_type_ids'], dtype=torch.long)

        if self.is_test:
            return {
                'ids': ids,
                'mask': mask,
                'token_type': token_type

            }
        else:
            target = torch.tensor(self.targets[idx], dtype=torch.long)
            return {
                'ids': ids,
                'mask': mask,
                'token_type': token_type,
                'targets': target
            }


class DataLoader:
    def __init__(self, dataset, batch_size=32, shuffle=True, num_workers=0):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.num_workers = num_workers

    def __iter__(self):
        return iter(torch.utils.data.DataLoader(
            self.dataset,
            batch_size=self.batch_size,
            shuffle=self.shuffle,
            num_workers=self.num_workers
        ))
