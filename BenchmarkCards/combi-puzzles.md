# Combi-Puzzles

## 📊 Benchmark Details

**Name**: Combi-Puzzles

**Overview**: The Combi-Puzzles dataset contains 125 problem variants based on 25 combinatorial reasoning problems, designed to evaluate the mathematical reasoning abilities of large language models (LLMs) and human participants.

**Data Type**: combinatorial problem variants

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Ukrainian

**Resources**:
- [Resource](https://huggingface.co/TheBloke/Llama-2-70B-Chat-GGUF)
- [Resource](https://huggingface.co/bartowski/Meta-Llama-3.1-70B-Instruct-GGUF)
- [Resource](https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF)
- [Resource](https://platform.openai.com/docs/models/#gpt-4-turbo-and-gpt-4)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning ability of established LLMs in combinatorial problems and to compare their performance with human participants.

**Target Audience**:
- ML Researchers
- Mathematicians
- Students

**Tasks**:
- Mathematical Reasoning

**Limitations**: The dataset contains only 125 problem variants, which may not fully capture the diversity of scenarios LLMs can encounter.

## 💾 Data

**Source**: Constructed by the authors for this study using combinatorial problems.

**Size**: 125 problem variants

**Format**: N/A

**Annotation**: Manual annotation by authors

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy was calculated as the number of correct responses over the total number of problems attempted.

**Interpretation**: A higher accuracy indicates better reasoning capabilities in solving combinatorial problems.

**Validation**: Statistical significance was tested using the paired Permutation test.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: Participants were recruited from Ukrainian pupils and undergraduates involved in STEM, with an emphasis on prior experience in combinatorial mathematics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants provided informed consent, and data collection was conducted anonymously.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from participants and parental consent for minor participants.

**Compliance With Regulations**: Study was approved by the university’s Ethics Committee.
