import streamlit as st
from gemini_api import GeminiAPI
from analysis_utils import HallucinationAnalyzer
from visualizations import HallucinationVisualizer
from data_manager import DataManager

def main():
    st.title("AI Hallucination Analysis Tool")
    
    # Sidebar configuration
    st.sidebar.header("Configuration")
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
    num_iterations = st.sidebar.slider("Number of Response Iterations", 3, 8, 5)
    
    if not api_key:
        st.warning("Please enter your Gemini API Key in the sidebar")
        return

    gemini = GeminiAPI(api_key)
    analyzer = HallucinationAnalyzer()
    visualizer = HallucinationVisualizer()
    data_manager = DataManager()

    # Question input
    st.subheader("Enter a Question or Select from Predefined")
    use_predefined = st.checkbox("Use predefined hallucination-prone questions")
    
    if use_predefined:
        questions = gemini.get_hallucination_prone_questions()
        selected_question = st.selectbox("Select a question", questions)
    else:
        selected_question = st.text_input("Enter your question")

    if st.button("Analyze") and selected_question:
        with st.spinner("Generating and analyzing responses..."):
            # Generate responses
            responses = gemini.generate_responses(selected_question, num_iterations)
            
            # Analyze responses
            similarity_matrix = analyzer.compute_similarity_matrix(responses)
            consistency_score = analyzer.calculate_consistency_score(responses)
            entities = analyzer.extract_entities(responses)
            
            # Save responses
            data_manager.save_responses(
                selected_question, 
                responses, 
                consistency_score, 
                entities
            )
            
            # Display results
            st.subheader("Analysis Results")
            
            # Display consistency score
            st.metric("Response Consistency Score", f"{consistency_score:.2f}")
            
            # Display responses
            st.subheader("Generated Responses")
            for i, response in enumerate(responses, 1):
                with st.expander(f"Response {i}"):
                    st.write(response)
            
            # Visualizations
            st.subheader("Visualizations")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("Response Similarity Heatmap")
                visualizer.plot_similarity_heatmap(similarity_matrix)
                
            with col2:
                st.write("Response Word Cloud")
                visualizer.generate_wordcloud(responses)
            
            # Entity Analysis
            st.subheader("Named Entity Analysis")
            for i, ents in enumerate(entities, 1):
                if ents:
                    st.write(f"Response {i} Entities:")
                    st.json(ents)

    # View historical data
    st.subheader("Historical Analysis")
    if st.button("View Previous Analyses"):
        df = data_manager.load_responses()
        if not df.empty:
            st.dataframe(df)
        else:
            st.info("No historical data available")

if __name__ == "__main__":
    main()
