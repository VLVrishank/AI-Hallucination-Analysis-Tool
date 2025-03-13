import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from typing import List

class HallucinationVisualizer:
    @staticmethod
    def plot_similarity_heatmap(similarity_matrix: np.ndarray):
        plt.figure(figsize=(10, 8))
        sns.heatmap(similarity_matrix, annot=True, cmap='YlOrRd')
        st.pyplot(plt.gcf())
        plt.close()

    @staticmethod
    def generate_wordcloud(responses: List[str]):
        text = ' '.join(responses)
        wordcloud = WordCloud(width=800, height=400).generate(text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt.gcf())
        plt.close()
