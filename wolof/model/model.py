import torch


class Model(torch.nn.Module):
    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.train_loader = None
        self.valid_loader = None
        self.optimizer = None
        self.scheduler = None
        self.epoch = 0
        self._model_state = None
        self.device = None

    @property
    def model_state(self):
        return self._model_state

    @model_state.setter
    def model_state(self, value):
        self._model_state = value

    def _init_model(self, device, train_dataset, valid_dataset, train_bs, valid_bs,  train_shuffle, valid_shuffle,):

        self.device = device

        if self.train_loader is None:
            self.train_loader = torch.utils.data.DataLoader(
                train_dataset,
                batch_size=train_bs,
                shuffle=train_shuffle,
            )
        if self.valid_loader is None:
            if valid_dataset is not None:
                self.valid_loader = torch.utils.data.DataLoader(
                    valid_dataset,
                    batch_size=valid_bs,
                    shuffle=valid_shuffle,
                )

        if self.optimizer is None:
            self.optimizer = self.fetch_optimizer()

        if self.scheduler is None:
            self.scheduler = self.fetch_scheduler()

    def loss(self, *args, **kwargs):
        return

    def fetch_optimizer(self, *args, **kwargs):
        return

    def fetch_scheduler(self, *args, **kwargs):
        return

    def forward(self, *args, **kwargs):
        return super().forward(*args, **kwargs)

    def train_epoch(self, train_dataset, train_bs, train_shuffle):
        self.train_loader = torch.utils.data.DataLoader(
            train_dataset,
            batch_size=train_bs,
            shuffle=train_shuffle,
        )
        for batch_idx, (data, target) in enumerate(self.train_loader):
            self.train_batch(data, target)

    def valid_epoch(self, valid_dataset, valid_bs, valid_shuffle):
        self.valid_loader = torch.utils.data.DataLoader(
            valid_dataset,
            batch_size=valid_bs,
            shuffle=valid_shuffle,
        )
        for batch_idx, (data, target) in enumerate(self.valid_loader):
            self.valid_batch(data, target)
            

    def save(self, model_path, weights_only=False):
        model_state_dict = self.state_dict()

        if weights_only:

            torch.save(model_state_dict, model_path)

        if self.optimizer is not None:
            opt_state_dict = self.optimizer.state_dict()
        else:
            opt_state_dict = None

        if self.scheduler is not None:
            sch_state_dict = self.scheduler.state_dict()
        else:
            sch_state_dict = None

        model_dict = {}
        model_dict["state_dict"] = model_state_dict
        model_dict["optimizer"] = opt_state_dict
        model_dict["scheduler"] = sch_state_dict

        torch.save(model_dict, model_path)

    def load(self, model_path, weights_only=False, device="cuda"):

        if next(self.parameters()).device != self.device:
            self.to(self.device)
        model_dict = torch.load(model_path, map_location=torch.device(device))
        if weights_only:
            self.load_state_dict(model_dict)
        else:
            self.load_state_dict(model_dict["state_dict"])

    def fit(self, train_dataset, valid_dataset=None, device="cuda", epochs=10, train_bs=16, valid_bs=16, train_shuffle=True, valid_shuffle=False, save_path=None,):

        self._init_model(device, train_dataset, valid_dataset,
                         train_bs, valid_bs, train_shuffle, valid_shuffle)

        for epoch in range(epochs):
            self.epoch = epoch
            self.train()
            self.train_epoch(train_dataset, train_bs, train_shuffle)
            self.eval()
            self.valid_epoch(valid_dataset, valid_bs, valid_shuffle)
            self.scheduler.step()

            if save_path is not None:
                self.save(save_path)
