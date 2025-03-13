#  AI Hallucination Analysis Tool


##  Overview

The AI Hallucination Analysis Tool is a sophisticated platform designed to study and visualize how large language models (specifically Google's Gemini) respond to hallucination-prone questions. By generating multiple responses to the same prompt and analyzing their consistency, we can better understand when and how AI models might hallucinate or generate fictional information.

## ✨ Features

- 🎯 **Predefined Hallucination-Prone Questions**: Carefully crafted questions designed to test AI boundaries
- 📊 **Real-time Analysis**: Compute similarity scores and consistency metrics across multiple AI responses
- 🎨 **Visual Insights**: 
  - Interactive heatmaps showing response similarities
  - Dynamic word clouds highlighting key themes
- 🔍 **Named Entity Recognition**: Automatic detection and analysis of entities in responses
- 📝 **Historical Analysis**: Track and compare results over time
- 💾 **Data Persistence**: Save and retrieve previous analyses

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini API
- **Analysis**: 
  - scikit-learn (TF-IDF, Cosine Similarity)
  - spaCy (Named Entity Recognition)
- **Visualization**: 
  - Seaborn
  - Matplotlib
  - WordCloud


## 📝 License

MIT License - feel free to use this tool for your own research and projects!

## 🙋‍♂️ Author

Created by [VLVrishank](https://github.com/VLVrishank)

---
> "Understanding AI hallucinations is the first step to building more reliable AI systems."
