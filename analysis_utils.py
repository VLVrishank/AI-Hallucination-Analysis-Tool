from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import numpy as np
from typing import List, Dict

class HallucinationAnalyzer:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.tfidf = TfidfVectorizer(min_df=1, stop_words=None)

    def compute_similarity_matrix(self, responses: List[str]) -> np.ndarray:
        if not responses or all(not response.strip() for response in responses):
            return np.zeros((len(responses), len(responses)))
        
        try:
            # Preprocess responses to ensure they contain valid text
            processed_responses = [response.strip() for response in responses if response.strip()]
            if not processed_responses:
                return np.zeros((len(responses), len(responses)))
            
            tfidf_matrix = self.tfidf.fit_transform(processed_responses)
            return cosine_similarity(tfidf_matrix)
        except Exception as e:
            print(f"Error in similarity computation: {e}")
            return np.zeros((len(responses), len(responses)))

    def extract_entities(self, responses: List[str]) -> List[Dict]:
        entities_list = []
        for response in responses:
            doc = self.nlp(response)
            entities = {ent.text: ent.label_ for ent in doc.ents}
            entities_list.append(entities)
        return entities_list

    def calculate_consistency_score(self, responses: List[str]) -> float:
        similarity_matrix = self.compute_similarity_matrix(responses)
        return np.mean(similarity_matrix)
