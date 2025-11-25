# RoD-TAL (Romanian Driving Tests and Laws)

## 📊 Benchmark Details

**Name**: RoD-TAL (Romanian Driving Tests and Laws)

**Overview**: RoD-TAL is a novel multimodal dataset comprising Romanian driving test questions, text-based and image-based, alongside annotated legal references and human explanations. It aims to evaluate the capabilities of Large Language Models (LLMs) and Vision-Language Models (VLMs) in understanding and reasoning about Romanian driving law through various tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Romanian

**Resources**:
- [Resource](https://www.scoalarutiera.ro/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs and VLMs in the context of Romanian driving law and various question-answering tasks.

**Target Audience**:
- Researchers in AI
- Educators in Law
- Developers of Legal AI Systems

**Tasks**:
- Information Retrieval
- Question Answering
- Visual Information Retrieval
- Visual Question Answering

**Limitations**: The dataset does not fully address issues of visual reasoning, which remains challenging.

## 💾 Data

**Source**: Curated legal texts from Romanian legislation encompassing traffic regulations and associated driving tests.

**Size**: 1,156 samples (1,200 questions including images)

**Format**: N/A

**Annotation**: Annotated references to applicable legal statutes and explanations.

## 🔬 Methodology

**Methods**:
- Retrieval-augmented generation (RAG)
- Dense retrievers
- Reasoning-optimized models

**Metrics**:
- Precision
- Recall
- F1 Score
- Exact Match

**Calculation**: Metrics calculated based on specific matching with correct answers provided in the dataset.

**Interpretation**: Exact Match requires the answer to precisely match the expected correct response.

**Baseline Results**: Exact Match scores achieve high performance rates employing RAG and fine-tuned models.

**Validation**: Experimentally validated through real-word scenarios and benchmarking against similar datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Potential misinformation in educational settings if models hallucinate incorrect information.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Discussed risks predicated on use cases in educational contexts.
