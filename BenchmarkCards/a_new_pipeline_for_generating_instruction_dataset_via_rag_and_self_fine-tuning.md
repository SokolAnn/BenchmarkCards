# A New Pipeline For Generating Instruction Dataset via RAG and Self Fine-tuning

## 📊 Benchmark Details

**Name**: A New Pipeline For Generating Instruction Dataset via RAG and Self Fine-tuning

**Overview**: This research proposes a pipeline that leverages the power of LLMs and the Retrieval-Augmented Generation (RAG) related framework to construct high-quality instruction datasets for fine-tuning on specific domains using custom document collections. The approach addresses the challenge of data scarcity by enabling the generation of instruction datasets from a limited set of initial documents.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://www.langchain.com/)
- [GitHub Repository](https://github.com/kermitt2/grobid)
- [Resource](https://www.llamaindex.ai/)

## 🎯 Purpose and Intended Users

**Goal**: To create domain-specific instruction datasets efficiently for fine-tuning large language models (LLMs).

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Desk Reference to the Diagnostic Criteria from DSM-5, converted into structured JSON format using GROBID.

**Size**: 2,000 entries

**Format**: JSON

**Annotation**: Generated question-answer pairs through prompts based on domain-specific documents.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the performance of the fine-tuned model compared to baseline models.

**Interpretation**: Higher scores indicate better performance in generating accurate and relevant responses to psychiatric queries.

**Baseline Results**: The fine-tuned Mistral-7B-dsm5 model scored 726 while the GPT-3.5-turbo-0125 model scored 592.

**Validation**: Evaluation performed by GPT-4 as an expert judge, scoring generated responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
