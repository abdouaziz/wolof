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
 
...


## Installation

 
```python
# init datasets
from wolo.data import Dataset
import pandas as pd

df = pd.read_csv("data/train.csv")


train_dataset = Dataset(df.text , df.label)
valid_dataset = Dataset(df.text , df.label)

# init model
model = MyModel()

 
# train model. 
model.fit(
    train_dataset,
    valid_dataset=valid_dataset,
    train_batch=32,
    valid_batch=32,
    device="cuda",
    epochs=50,
    save_path="model.pth",
     
)

 
```