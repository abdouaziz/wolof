
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
        # <img alt="PyPI" src="https://pypi.org/project/wolof/">
    </a>    
</p>


## Your Library for Wolof Language

**Wolof** is a language spoken in Senegal in neighboring countries, many works are written in Wolof or the need to have a tool that allows us to know better this language. 

This is how the idea of the **Wolof library** was born, which allows us to do several specific tasks in Wolof languages such as text classification, automatic translation, but also automatic speech recognition. 



### Why Wolof library ?:

- simple and easy to use
- customizable 
- clean code
 
...



## Installation

This repo is tested on Python 3.6+.

### With pip

wolof can be installed by pip as follows:

```py
pip install wolof
```

### From source


```py
pip install git+https://github.com/abdouaziz/wolof.git
```


## Use 
 
```python
from wolof.asr import Speech2Text

asr = Speech2Text(model_name="abdouaziiz/wav2vec2-xls-r-300m-wolof")

audio_file = "audio.wav"

prediction = asr.predict(audio_file)
```

You can checkout examples in `examples/`
