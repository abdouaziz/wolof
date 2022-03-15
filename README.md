
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
from wolof.asr import Speech2Text

asr = Speech2Text(model_name="abdouaziiz/wav2vec2-xls-r-300m-wolof")

audio_file = "audio.wav"

prediction = asr.predict(audio_file)
```

You can checkout examples in `examples/`

<hr>

## Author
- Abdou Aziz DIOP @abdouaziz
- email : abdouaziz.g@gmail.com
- linkedin : https://www.linkedin.com/in/abdouaziiz/