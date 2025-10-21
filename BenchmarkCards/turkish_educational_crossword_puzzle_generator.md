# Turkish Educational Crossword Puzzle Generator

## 📊 Benchmark Details

**Name**: Turkish Educational Crossword Puzzle Generator

**Overview**: This paper introduces the first Turkish crossword puzzle generator designed to leverage the capabilities of large language models (LLMs) for educational purposes, providing two new datasets for generating clues and enhancing learning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Turkish

**Resources**:
- [Resource](https://huggingface.co/datasets/Kamyar-zeinalipour/TAC)
- [Resource](https://huggingface.co/datasets/Kamyar-zeinalipour/T4TAC)
- [GitHub Repository](https://github.com/KamyarZeinalipour/CW_Clue_Gen_tr)
- [Resource](https://huggingface.co/Kamyar-zeinalipour/llama7B_turkish_crossword_clue_gen)
- [Resource](https://huggingface.co/Kamyar-zeinalipour/llama13B_turkish_crossword_clue_gen)

## 🎯 Purpose and Intended Users

**Goal**: To create dynamic crosswords in Turkish for educational purposes, providing educators with tools to easily generate subject-specific puzzles.

**Target Audience**:
- Educators
- Language Learners

**Tasks**:
- Crossword Generation

**Limitations**: N/A

## 💾 Data

**Source**: A dataset of Turkish crossword clues and answers compiled from online sources, and another dataset containing categorized Turkish texts.

**Size**: 252,576 Turkish answer-clue pairs and over 35,000 samples in the second dataset

**Format**: N/A

**Annotation**: Crafted by crossword experts and generated using fine-tuned language models.

## 🔬 Methodology

**Methods**:
- Fine-tuning of large language models
- Human evaluation of generated clues

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L

**Calculation**: Metrics were calculated based on comparison of generated clues with established benchmarks.

**Interpretation**: Good performance is indicated by higher ROUGE scores.

**Baseline Results**: GPT3.5 Turbo achieved ROUGE-1: 39.96, ROUGE-2: 18.08, ROUGE-L: 23.48 after fine-tuning.

**Validation**: Evaluated by native Turkish speakers for relevance and linguistic accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
