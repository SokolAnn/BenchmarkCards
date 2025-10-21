# Redeﬁning Simplicity: Benchmarking Large Language Models from Lexical to Document Simpliﬁcation

## 📊 Benchmark Details

**Name**: Redeﬁning Simplicity: Benchmarking Large Language Models from Lexical to Document Simpliﬁcation

**Overview**: This paper presents a comprehensive analysis and comparison of LLM performance across four text simplification tasks: lexical, syntactic, sentence, and document simplification, demonstrating that LLMs outperform traditional methods in all tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Portuguese

**Resources**:
- [GitHub Repository](https://github.com/9624219/A-Comprehensive-Study-of-Large-Language-Models-in-Text-Simpliﬁcation)
- [Resource](https://huggingface.co/google/Gemma2-2b)
- [Resource](https://ollama.com/)
- [Resource](https://platform.openai.com/docs/models)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models in text simplification tasks and benchmark their capabilities across different types of simplification.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Lexical Simplification
- Syntactic Simplification
- Sentence Simplification
- Document Simplification

**Limitations**: N/A

## 💾 Data

**Source**: The TSAR-2022 shared task and Newsela dataset consisting of complex and simplified text pairs.

**Size**: 1,445,159 pairs for WEBSPLIT dataset, 2,359 sentences for ASSET dataset, and a sampled set of 200 documents from Newsela.

**Format**: Various formats including text files

**Annotation**: Human-annotated simplifications and crowdsourced references.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- SARI
- BERTScore
- FKGL

**Calculation**: Metrics such as SARI and BERTScore are calculated based on the alignment of generated sentences with reference sentences.

**Interpretation**: Higher scores indicate better performance in maintaining meaning and simplification.

**Baseline Results**: GPT-4o achieves the highest performance across tasks.

**Validation**: Experimental settings validated using multiple datasets and evaluation metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
