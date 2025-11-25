# HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models

**Overview**: A large collection of generated and human-annotated hallucinated samples for evaluating the performance of LLMs in recognizing hallucination. The benchmark contains 35,000 hallucinated/normal samples, including 5,000 general user queries with ChatGPT responses and 30,000 task-specific examples for question answering, knowledge-grounded dialogue, and text summarization. It is constructed via a two-stage automatic generation process (sampling-then-filtering) using ChatGPT and human annotation.

**Data Type**: text (question-answering pairs; knowledge-grounded dialogue pairs; text-summary pairs; user query-response pairs)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- BEGIN
- Attributable to Identified Sources (AIS)
- PARENT
- TRUE

**Resources**:
- [GitHub Repository](https://github.com/RUCAIBox/HaluEval)

## 🎯 Purpose and Intended Users

**Goal**: To understand what types of content and to which extent LLMs tend to hallucinate, and to evaluate the performance of LLMs in recognizing hallucinations.

**Target Audience**:
- Researchers
- Users

**Tasks**:
- Question Answering
- Knowledge-grounded Dialogue
- Text Summarization
- Hallucination detection for general user query-response pairs

**Limitations**: In our approach, we leverage a LLM, i.e., ChatGPT, to automatically generate the hallucinated samples. Therefore, the quality of our hallucinated samples is limited by the capacity of ChatGPT in following the complex instruction of hallucination sampling. ... Besides, our benchmark focuses on evaluating the ability of LLMs in recognizing the hallucinations in text but does not investigate the underlying reasons behind the appearance of hallucinations like prior work (Zheng et al., 2023; Das et al., 2023).

**Out of Scope Uses**:
- the hallucinated samples in our benchmark looks highly similar to the ground-truth samples, which might be misused for an unexpected purpose than we planned.

## 💾 Data

**Source**: 5,000 general user queries with ChatGPT responses annotated from the 52K Alpaca instruction tuning dataset; 30,000 task-specific hallucinated examples automatically generated from seed datasets HotpotQA, OpenDialKG, and CNN/DailyMail using ChatGPT (sampling-then-filtering).

**Size**: 35,000 examples (30,000 generated hallucinated samples: 10,000 per task for QA, Dialogue, Summarization; 5,000 human-annotated ChatGPT responses for general user queries)

**Format**: N/A

**Annotation**: Human annotation by selected labelers: each ChatGPT response labeled by three human labelers with Yes/No hallucination label and corresponding span markings; final label determined by max-voting. Thirty human labelers were selected; Fleiss's Kappa κ = 0.811 computed on 5,000 annotated samples.

## 🔬 Methodology

**Methods**:
- Automated generation (sampling-then-filtering using ChatGPT)
- Human annotation (three annotators per sample, max-voting)
- Model evaluation via automated metrics (classification of hallucination presence)

**Metrics**:
- Accuracy
- Fleiss's Kappa
- BERTScore

**Calculation**: Accuracy: percentage of correct binary classifications of whether a sample contains hallucinated content. Fleiss's Kappa computed to measure inter-annotator agreement on 5,000 annotated samples (κ = 0.811). BERTScore used to compute average semantic similarity among three ChatGPT responses per query for filtering and selection of 5,000 queries with lowest similarity.

**Interpretation**: Performance close to random chance (~50% accuracy) indicates poor ability of LLMs to recognize hallucinations (e.g., the paper reports ChatGPT achieves 58.53% on summarization, described as "barely above chance"). Higher accuracy indicates better hallucination recognition.

**Baseline Results**: Accuracy (%) of classifying whether a sample contains hallucinated contents (Table 5): ChatGPT: QA 62.59, Dialogue 72.40, Summarization 58.53, General 79.44; Claude 2: QA 69.78, Dialogue 64.73, Summarization 57.75, General 75.00; Claude: QA 67.60, Dialogue 64.83, Summarization 53.76, General 73.88; Davinci002: QA 60.05, Dialogue 60.81, Summarization 47.77, General 80.42; Davinci003: QA 49.65, Dialogue 68.37, Summarization 48.07, General 80.40; GPT-3: QA 49.21, Dialogue 50.02, Summarization 51.23, General 72.72; Llama 2: QA 49.60, Dialogue 43.99, Summarization 49.55, General 20.46; ChatGLM: QA 47.93, Dialogue 44.41, Summarization 48.57, General 30.92; Falcon: QA 39.66, Dialogue 29.08, Summarization 42.71, General 18.98; Vicuna: QA 60.34, Dialogue 46.35, Summarization 45.62, General 19.48; Alpaca: QA 6.68, Dialogue 17.55, Summarization 20.63, General 9.54.

**Validation**: Validation via human annotation: each ChatGPT response annotated by three labelers with max-voting; Fleiss's Kappa κ = 0.811 on 5,000 samples indicating high agreement. Sampling selection for user queries used BERTScore to select queries with lowest average similarity among three ChatGPT responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse

**Atlas Risks**:
- **Misuse**: Improper usage

**Potential Harm**: Hallucinated or unverifiable content generated by LLMs; potential misuse of highly similar hallucinated samples.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
