import torch, librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
 



class Speech2Text:
    
    def __init__(self, model_name="abdouaziiz/wav2vec2-xls-r-300m-wolof"):
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        
    def wav2feature(self, path):

        speech_array, sampling_rate = librosa.load(path , sr=16000) 
        return self.processor(speech_array, sampling_rate=sampling_rate, padding=True ,return_tensors="pt" ).input_values
        
    def feature2logits(self, features):
        with torch.no_grad():
            return self.model(features).logits
            
    def __call__(self, path):
        
        logits = self.feature2logits(self.wav2feature(path))
        pred_ids = torch.argmax(logits, dim=-1)
        
        return self.processor.decode(pred_ids[0])
	        
