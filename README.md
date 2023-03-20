
<div align="center">
    <br>
    <img src="https://www.pngplay.com/wp-content/uploads/10/Senegal-Flag-PNG-Clipart-Background.png" width="100" height="100"/>
    <p>
    Library, built on PyTorch and Transformers, for developing state-of-the-art deep learning models on a wide variety of linguistic tasks in wolof.
    </p>
    <hr/>
</div>
<p align="center">
    <a href="https://github.com/abdouaziz/wolof">
        <img alt="CI" src="https://github.com/allenai/allennlp/workflows/CI/badge.svg?event=push&branch=main">
    </a>
    <a href="https://pypi.org/project/wolof/">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/wolof"
    </a>    
</p>


## Your Library for Wolof Language

**Wolof** is a language spoken in Senegal in neighboring countries, many works are written in Wolof or the need to have a tool that allows us to know better this language. 

**Wolof library** allows us to do several specific tasks in Wolof languages such as text classification, translation, automatic speech recognition. 


### Why Wolof library ?:

- simple and easy to use
- customizable 
- clean code
 
## Installation
### Requirements
- Python >= 3.6 
- Torch 
- Transformers 


### With pip

wolof can be installed using pip as follows:

```
pip install wolof 
```

### From source

```py
pip install git+https://github.com/abdouaziz/wolof.git
```

## Usage



```python
from wolof import Speech2Text

asr = Speech2Text(model_name="abdouaziiz/wav2vec2-xls-r-300m-wolof")

audio_file = "audio.wav"

prediction = asr.predict(audio_file)
```

# Pipeline

The pipelines are a great and easy way to use models for inference. These pipelines are objects that abstract most of the complex code from the library,offering a simple API dedicated to several tasks Masked Language Modeling, Sentiment Analysis .


**bert-base-wolof** is pretrained bert-base model on wolof language  .
**sora-wolof** is pretrained roberta model on wolof language  .
	
## Models in Wolof library
	
| Model name | Number of layers | Attention Heads | Embedding Dimension | Total Parameters |
| :------:       |   :---: | :---: | :---: | :---: |
| `bert-base-wolof` | 6    | 12   | 514   | 56931622 M |
| `soraberta-base` | 6    | 12   | 514   | 83 M |
	 

## Using Soraberta or BERT-base-wolof

Let's use  ***`fill_mask`***  for masked language modeling . We mask a word with the token ***`[MASK]`*** in the given input_text and the unmasker predict the right word corresponding to the token ***`[MASK]`*** .
 	
```python
>>> from wolof import Pipeline
>>> unmasker = Pipeline(task='fill-mask', model_name='abdouaziiz/bert-base-wolof')
>>> unmasker("kuy yoot du [MASK].")

[{'sequence': '[CLS] kuy yoot du seqet. [SEP]',
	'score': 0.09505125880241394,
	'token': 13578},
	{'sequence': '[CLS] kuy yoot du daw. [SEP]',
	'score': 0.08882280439138412,
	'token': 679},
	{'sequence': '[CLS] kuy yoot du yoot. [SEP]',
	'score': 0.057790059596300125,
	'token': 5117},
	{'sequence': '[CLS] kuy yoot du seqat. [SEP]',
	'score': 0.05671025067567825,
	'token': 4992},
	{'sequence': '[CLS] kuy yoot du yaqu. [SEP]',
	'score': 0.0469999685883522,
	'token': 1735}]
```



# Machine Translation in Wolof
...







for ***`task`***  we can have the following values: 'fill-mask', 'sentiment-analysis'






You can checkout examples in `examples/`

<hr>


## Author
- Abdou Aziz DIOP @abdouaziz
- email : abdouaziz@gmail.com
- linkedin : https://www.linkedin.com/in/abdouaziiz/
