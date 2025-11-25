# C3: A Bilingual Benchmark for Spoken Dialogue Models Exploring Challenges in Complex Conversations

## 📊 Benchmark Details

**Name**: C3: A Bilingual Benchmark for Spoken Dialogue Models Exploring Challenges in Complex Conversations

**Overview**: The C3 benchmark is designed to evaluate Spoken Dialogue Models (SDMs) on their capability to handle complexity in spoken dialogue, addressing challenges like phonological ambiguity, semantic ambiguity, omission, coreference, and multi-turn interaction.

**Data Type**: dialogue instances with audio and text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/username/repo)
- [Resource](https://c3benchmark.com)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate SDMs' abilities in handling various complex situations in spoken dialogues.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dialogue Understanding
- Contextual Understanding

**Limitations**: The dataset's phenomena are particularly focused on English and Chinese dialogues; its applicability to other languages is not resolved in this work.

## 💾 Data

**Source**: Real-world spoken dialogues collected from web sources and existing datasets.

**Size**: 1,079 instances comprising 1,586 audio-text pairs

**Format**: Audio and Text

**Annotation**: Manually checked and annotated for ambiguity types.

## 🔬 Methodology

**Methods**:
- LLM-based evaluation
- Human evaluation for accuracy

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the proportion of instances judged correct out of the total number of instances.

**Interpretation**: Higher accuracy indicates better performance in understanding and generating responses in dialogues.

**Validation**: Reliability of the evaluation method confirmed through correlation with human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark includes data from two different language groups (English and Chinese).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
