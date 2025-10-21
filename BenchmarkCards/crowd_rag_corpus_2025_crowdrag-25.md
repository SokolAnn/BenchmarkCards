# Crowd RAG Corpus 2025 (CrowdRAG-25)

## 📊 Benchmark Details

**Name**: Crowd RAG Corpus 2025 (CrowdRAG-25)

**Overview**: The Crowd RAG Corpus 2025 consists of 903 human-written and 903 LLM-generated responses for 301 topics, including utility judgments across various dimensions, aimed at evaluating retrieval-augmented generation (RAG) scenarios.

**Data Type**: RAG response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://zenodo.org/records/14748980)
- [GitHub Repository](https://github.com/webis-de/sigir25-rag-crowdsourcing)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the efficacy of crowdsourcing for evaluation in retrieval-augmented generation scenarios, analyzing response writing and judgement.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Evaluation
- Response Generation

**Limitations**: The study uses a specific set of topics from TREC RAG'24 which may limit generalizability.

## 💾 Data

**Source**: Crowdsourced human workers and LLM (OpenAI's GPT-4 model) for generating and judging RAG responses.

**Size**: 1,806 RAG responses, 47,320 pairwise human judgments

**Format**: N/A

**Annotation**: Responses written by crowdsourced workers and evaluated by both human and LLM judgments.

## 🔬 Methodology

**Methods**:
- Crowdsourcing
- Pairwise Judgments

**Metrics**:
- Agreement Scores
- Utility Judgment Dimensions

**Calculation**: Metrics calculated using pairwise comparisons for assessing response quality.

**Interpretation**: Higher scores indicate better responses according to utility dimensions such as coherence and coverage.

**Validation**: Validated through expert judgments and inter-rater reliability measures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Informed consent was obtained from participants and measures were taken for data anonymization.

**Data Licensing**: Licensed under a Creative Commons Attribution International 4.0 License.

**Consent Procedures**: Participants were provided with information and consent forms before participation.

**Compliance With Regulations**: Not Applicable
