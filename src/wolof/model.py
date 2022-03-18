
from transformers import pipeline




class Pipeline(object):
    """
    The pipelines are a great and easy way to use models for inference. These pipelines are objects that abstract most of the complex code from the library,
    offering a simple API dedicated to several tasks, including Named Entity Recognition, Masked Language Modeling, 
    Sentiment Analysis, Feature Extraction and Question Answering. 
    """
    def __init__(self, task , model_name="abdouaziiz/bert-base-wolof"):
        """
        Initialize the model
        Args:
            model_name (str): The name of the model to load
        """
        self.task = task
        self.model_name = model_name
        self.pipe = pipeline(self.task, model=self.model_name)


    def __call__(self, text):
        return self.pipe(text)
