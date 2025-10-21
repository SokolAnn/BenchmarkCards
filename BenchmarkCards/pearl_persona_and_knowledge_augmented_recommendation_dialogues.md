# PEARL (Persona and knowledgE Augmented Recommendation diaLogues)

## 📊 Benchmark Details

**Name**: PEARL (Persona and knowledgE Augmented Recommendation diaLogues)

**Overview**: PEARL is a large-scale conversational recommendation dataset synthesized with persona- and knowledge-augmented LLM simulators, containing over 57,000 dialogues to address limitations of existing datasets in expressing user preferences and providing explanations for recommendations.

**Data Type**: dialogue pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ReDial
- INSPIRED

**Resources**:
- [Resource](https://huggingface.co/datasets/DLI-Lab/pearl)
- [GitHub Repository](https://github.com/kkmjkim/PEARL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for developing conversational recommender systems that emphasize personalized recommendations and user preferences.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Conversational Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Real-world movie reviews collected from IMDB.

**Size**: 57,277 dialogues

**Format**: JSON

**Annotation**: Synthesized using persona and knowledge from LLM-based simulators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall
- Expertise
- Specificity

**Calculation**: Metrics calculated through comparisons between dialogues from PEARL and existing datasets, as well as performance of downstream models trained on PEARL.

**Interpretation**: Higher scores indicate better performance in conversational recommendation tasks.

**Baseline Results**: Compared performance of models trained on PEARL versus models trained on ReDial and INSPIRED.

**Validation**: Evaluation through human assessments and automatic metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Filtering mechanisms are applied to avoid personal information and maintain user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
