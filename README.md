# Wolof : Your Library for Wolof Language

**Wolof** is a language spoken in Senegal in neighboring countries, many works are written in Wolof or the need to have a tool that allows us to know better this language. 

This is how the idea of the **Wolof library** was born, which allows us to do several specific tasks in Wolof languages such as text classification, automatic translation, but also automatic speech recognition. 



### Why Wolof library ?:

- simple and easy to use
- customizable 
- clean code
 
...


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

 
install the dependencies for this project by running the following commands in your terminal:

```
 pip install wolof
```


 
```python
from wolof.asr import Speech2Text

asr = Speech2Text(model_name="abdouaziiz/wav2vec2-xls-r-300m-wolof")

audio_file = "audio.wav"

prediction = asr.predict(audio_file)
```



You can checkout examples in `examples/`
