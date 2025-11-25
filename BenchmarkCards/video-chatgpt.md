# Video-ChatGPT

## 📊 Benchmark Details

**Name**: Video-ChatGPT

**Overview**: Introduces Video-ChatGPT (a multimodal video conversation model) and (1) a new dataset of 100,000 video-instruction pairs acquired via a manual and semi-automatic pipeline, and (2) a quantitative evaluation framework for video-based dialogue models that evaluates capabilities such as correctness of information, detail orientation, contextual understanding, temporal understanding, and consistency.

**Data Type**: video (video-instruction / question-answer pairs)

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- ActivityNet-200
- MSRVTT-QA
- MSVD-QA
- TGIF-QA
- ActivityNet-QA
- Video Chat
- Video-LLaMA
- LLaMA Adapter

**Resources**:
- [GitHub Repository](https://github.com/mbzuai-oryx/Video-ChatGPT)
- [GitHub Repository](https://github.com/keplerlab/katna)
- [Resource](https://openai.com/policies/terms-of-use)
- [Resource](https://chat.openai.com)

## 🎯 Purpose and Intended Users

**Goal**: Create a multimodal video conversation model (Video-ChatGPT), provide a large video-instruction dataset of 100,000 pairs for training, and develop a quantitative video conversation evaluation framework for benchmarking video conversation models.

**Tasks**:
- Question Answering
- Text Generation (open-ended video descriptions)
- Video Conversation
- Temporal Reasoning
- Spatial Understanding
- Action Recognition
- Localization
- Object Detection
- Segmentation
- Retrieval
- Tracking

**Limitations**: Model struggles to understand subtle temporal relationships in long videos (>2 minutes) and has difficulty recognizing details of small objects.

## 💾 Data

**Source**: Curated from a subset of the ActivityNet-200 dataset and other video-caption datasets; enriched using off-the-shelf models BLIP-2, GRiT, Tag2Text, and GPT-3.5 via a semi-automatic pipeline plus human-assisted annotation.

**Size**: 100,000 video-instruction pairs

**Format**: N/A

**Annotation**: Human-assisted annotation (expert annotators enrich captions) and semi-automatic annotation (frame-level captions from BLIP-2 and GRiT filtered with Tag2Text tags and merged; GPT-3.5 used to generate coherent video-level captions and question-answer pairs).

## 🔬 Methodology

**Methods**:
- Instruction tuning / fine-tuning of LLM on video-instruction pairs (linear adapter layer trained; rest frozen)
- Video-based Generative Performance Benchmarking (text-generation evaluation)
- Zero-Shot Question-Answer Evaluation on existing QA datasets
- Automated GPT-3.5-based evaluation pipeline (and replication with Vicuna-1.5 for accessibility checks)
- Ablation studies comparing human-only, automatic-only, and combined data

**Metrics**:
- Accuracy
- Relative score (1-5) for: Correctness of Information, Detail Orientation, Contextual Understanding, Temporal Understanding, Consistency

**Calculation**: For generative evaluations, a GPT-3.5-based evaluation pipeline assigns a relative score from 1-5 to model outputs along five aspects (Correctness of Information, Detail Orientation, Contextual Understanding, Temporal Understanding, Consistency). For question-answer datasets (MSVD-QA, MSRVTT-QA, TGIF-QA, ActivityNet-QA), standard Accuracy scores are reported.

**Interpretation**: Higher Accuracy indicates better QA performance. Higher relative scores (on a 1-5 scale) indicate better performance for each aspect (1 = poor, 5 = excellent). The paper interprets higher values as better performance; no additional numeric thresholds are provided.

**Baseline Results**: Zero-shot QA Accuracy (Table 2): Video-ChatGPT: MSVD-QA 64.9, MSRVTT-QA 49.3, TGIF-QA 51.4, ActivityNet-QA 35.2. Generative aspect scores (Table 1): Video-ChatGPT - Correctness 2.40, Detail Orientation 2.52, Contextual Understanding 2.62, Temporal Understanding 1.98, Consistency 2.37. Comparative baselines include Video Chat, LLaMA Adapter, Video-LLaMA, and FrozenBiLM (specific scores reported in paper tables).

**Validation**: Validated via: (1) Blind test distinguishing human vs semi-automatic annotations on 50 sampled videos (52% accuracy in distinguishing sources) to demonstrate consistency of semi-automatic pipeline; (2) Evaluation replication using open-source Vicuna-1.5 (13B) showing similar trends to GPT-3.5 evaluation; (3) Ablation studies showing combined human+automatic data yields best performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Misuse
- Fairness
- Transparency

**Atlas Risks**:
No specific atlas risks defined

**Potential Harm**: ["Residual bias may persist in the dataset and influence the model's understanding and responses.", 'Potential for misuse if model is not handled with caution (explicitly stated).']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The subset of ActivityNet-200 used is distributed under MIT LICENSE; the authors state they will release all datasets created in this work under MIT LICENSE.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
