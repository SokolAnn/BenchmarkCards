# ContextDeP (Context-Dependent Paraphrases in news interviews)

## 📊 Benchmark Details

**Name**: ContextDeP (Context-Dependent Paraphrases in news interviews)

**Overview**: We operationalize context-dependent paraphrases in dialog with a definition and a hands-on training for annotators. We release ContextDeP, a dataset with 5,581 annotations on 600 utterance pairs from NPR and CNN news interviews.

**Data Type**: paraphrase pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- PAWS

**Resources**:
- [GitHub Repository](https://github.com/nlpsoc/Paraphrases-in-News-Interviews)
- [Resource](https://huggingface.co/datasets/AnnaWegmann/Paraphrases-in-Interviews)
- [Resource](https://huggingface.co/AnnaWegmann/Highlight-Paraphrases-in-Dialog)

## 🎯 Purpose and Intended Users

**Goal**: To advance dialog based evaluations of LLMs and automate the detection of context-dependent paraphrases in dialogs.

**Target Audience**:
- ML Researchers
- Social Science Researchers

**Tasks**:
- Paraphrase Detection

**Limitations**: Dataset size is relatively small.

## 💾 Data

**Source**: Adapted utterance pairs from NPR and CNN news interview transcripts.

**Size**: 5,581 annotations on 600 utterance pairs

**Format**: JSON

**Annotation**: Annotation was performed by crowd-workers trained to identify context-dependent paraphrases.

## 🔬 Methodology

**Methods**:
- Token classification
- In-context learning

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: F1 scores were calculated based on majority vote classification by annotators.

**Interpretation**: F1 scores above thresholds indicate better agreement and classification quality.

**Baseline Results**: Achieved F1 scores between 0.73 and 0.81 using generative models and a DeBERTa token classifier.

**Validation**: Quality assurance through multiple annotations per item and training for annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Potential biases exist as the dataset is from U.S. news interviews.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participant data was anonymized; identifiers of crowd-workers were replaced with non-identifiable IDs.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants consented to the use of their data for research purposes.

**Compliance With Regulations**: Study complied with ACL Code of Ethics.
