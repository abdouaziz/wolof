import torch, librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
 



class Speech2Text:
    """
    Speech2Text class for Speech Recognition in Wolof language
    """
    def __init__(self, model_name="abdouaziiz/wav2vec2-xls-r-300m-wolof"):
        """
        Initialize the model

        Args:
            model_name (str): The name of the model to load
        
        """
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        
    def wav2feature(self, path):
        """
        Convert a wav file to a feature vector
            
            Args:
                path (str): The path to the wav file
    
            Returns:
                torch.tensor: The feature vector
        """
     
        speech_array, sampling_rate = librosa.load(path , sr=16000) 
        return self.processor(speech_array, sampling_rate=sampling_rate, padding=True ,return_tensors="pt" ).input_values
        
    def feature2logits(self, features):
        """
        Convert a feature vector to logits
                
                Args:
                    features (torch.tensor): The feature vector
        
                Returns:
                    torch.tensor: The logits
            """
        with torch.no_grad():
            return self.model(features).logits
            
    def __call__(self, path):
 
     
        logits = self.feature2logits(self.wav2feature(path))
        pred_ids = torch.argmax(logits, dim=-1)
        
        return self.processor.decode(pred_ids[0])
	        
