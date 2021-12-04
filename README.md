# <h1 align="center"> Wolof </h1>


<p align="center">

<img src="./input/woloff.jpg">
</p>


## Description

**Wolof** is a language spoken in Senegal in neighboring countries, many works are written in Wolof or the need to have a tool that allows us to know better this language. 

This is how the idea of the **Wolof library** was born, which allows us to do several specific tasks in Wolof languages such as text classification, automatic translation, but also automatic speech recognition. 



### Why Wolof library ?:

- simple and easy to use
- customizable 
- clean code
 
 
### Training using Tez:

- To train a model, define a dataset and model. The dataset class is the same old class you would write when writing pytorch models.

- Create your model class. Instead of inheriting from `nn.Module`, import tez and inherit from `tez.Model` as shown in the following example.


```python
class MyModel(wolof.Model):
    def __init__(self):
        super().__init__()
        .
        .
      
    def fetch_scheduler(self):
        # create your own scheduler

    def fetch_optimizer(self):
        # create your own optimizer

    def forward(self, ids, mask, token_type_ids, targets=None):
        _, o_2 = self.bert(ids, attention_mask=mask, token_type_ids=token_type_ids)
        b_o = self.bert_drop(o_2)
        output = self.out(b_o)

        # calculate loss here
        loss = nn.BCEWithLogitsLoss()(output, targets)

        return output, loss
```

Everything is super-intuitive!

- Now you can train your model!

```python
# init datasets
train_dataset = SomeTrainDataset()
valid_dataset = SomeValidDataset()

# init model
model = MyModel()


# init callbacks, you can also write your own callback
es = tez.callbacks.EarlyStopping(monitor="valid_loss", model_path="model.bin")

# train model. a familiar api!
model.fit(
    train_dataset,
    valid_dataset=valid_dataset,
    train_bs=32,
    device="cuda",
    epochs=50,
    callbacks=[es],
    fp16=True,
)

# save model (with optimizer and scheduler for future!)
model.save("model.bin")
```

You can checkout examples in `examples/`
