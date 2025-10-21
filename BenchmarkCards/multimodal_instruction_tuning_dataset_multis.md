# MULTimodal InStruction tuning dataset (MULTIS)

## 📊 Benchmark Details

**Name**: MULTimodal InStruction tuning dataset (MULTIS)

**Overview**: A multimodal instruction tuning dataset collected to instruction-finetune ChatBridge. MULTIS covers 16 multimodal task categories and 15 source datasets, and consists of task-specific standardized multimodal QA/captioning samples and open-ended multimodal chat data across image, video, audio, and text modalities to enable instruction-following and zero-shot generalization on multimodal tasks.

**Data Type**: multimodal: image, video, audio, and text (task-specific QA/caption pairs and multimodal chat dialogues)

**Domains**:
- Natural Language Processing
- Computer Vision
- Audio Signal Processing
- Multimodal Interaction

**Languages**:
- N/A

**Similar Benchmarks**:
- LLaVA-Instruct-150K
- ImageBind
- CLIP
- Flamingo
- BLIP-2
- LLaVA
- MiniGPT-4

**Resources**:
- [Resource](https://iva-chatbridge.github.io)
- [Resource](https://arxiv.org/abs/2305.16103)

## 🎯 Purpose and Intended Users

**Goal**: To provide a multimodal instruction tuning dataset (MULTIS) to instruction-finetune multimodal language models (ChatBridge), enabling improved zero-shot multimodal understanding and instruction-following across text, image, video, and audio.

**Target Audience**:
- Researchers
- Developers building multimodal assistants

**Tasks**:
- Question Answering
- Image Captioning
- Video Captioning
- Audio Captioning
- Multimodal Dialogue
- Multimodal Reasoning
- Detailed Description

**Limitations**: 1) Weaknesses in understanding and grounding long-range videos and audios; 2) Framework can be extended to additional modalities (e.g., sketch and point cloud); 3) Frozen modules may lead to insufficient performance and introduce prior biases from pretrained models.

## 💾 Data

**Source**: Compiled from publicly available two-modality language-paired datasets and multimodal sources. The paper lists image-text datasets (MS-COCO, SBU Captions, Conceptual Captions, LAION-115M), video-text pairs (Webvid10M, MSRVTT, VATEX, MSVD), audio-text pairs (WavCaps, AudioCaps, ClothoV2), multimodal datasets (VALOR), and image chat data from LLaVA-Instruct-150K. MULTIS aggregates task-specific datasets (e.g., VQAv2, VG-QA, COCO Caption, MSRVTT QA/Caption, AudioCaps) and multimodal chat data sources (MSRVTT, AudioCaps, VALOR).

**Size**: 4.4M task-specific samples and 209k multimodal chat samples

**Format**: N/A

**Annotation**: Task-specific data transformed from publicly available human-annotated multimodal datasets. For each task, ChatGPT was used to derive 10–15 instruction templates which were manually filtered and refined. Multimodal chat data was constructed using a pipeline that leverages offline open-source models and ChatGPT/GPT-4 in an in-context-learning manner; manual selection/filtering was applied for quality.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation on held-out datasets
- Automated metrics
- Model-based human-quality evaluation using GPT-4 scoring for chat responses

**Metrics**:
- Accuracy
- CIDEr
- BLEU-4
- GPT-4 scoring (1-10 scale assessing helpfulness, relevance, accuracy, and level of detail)

**Calculation**: Accuracy reported for Question Answering tasks. CIDEr reported for captioning tasks. BLEU-4 reported for certain multimodal captioning/dialogue tasks. GPT-4 used to score chat responses on a 1–10 scale for quality dimensions (helpfulness, relevance, accuracy, level of detail).

**Interpretation**: Higher Accuracy, CIDEr, BLEU-4, or GPT-4 score indicates better performance. Instruction tuning with MULTIS improves zero-shot generalization (e.g., 21.8% boost in MSVDQA accuracy; 3.8% improvement in OKVQA; 3.6% improvement in GQA as reported). Incorporating multiple modalities (video+audio) improves performance on multimodal tasks versus unimodal inputs.

**Baseline Results**: Zero-shot evaluation results reported in the paper include: ChatBridge — OKVQA: 45.2 (vs ChatBridge w/o MULTIS 41.4), GQA: 41.8 (vs 37.4), Flickr30k CIDEr: 82.5 (vs 77.7), NoCaps CIDEr: 115.7 (vs 107.5), MSVD QA accuracy: 45.3 (vs 23.5), VATEX CIDEr: 48.9 (vs 47.7), ClothoV2 CIDEr: 26.2 (vs 22.4). Comparative baselines include Flamingo, BLIP-2, and finetuned SoTA numbers listed in Table 1 of the paper.

**Validation**: Hold-out evaluation on 6 datasets from MULTIS's task-specific data for zero-shot testing; GPT-4 used to evaluate multimodal chat response quality; ablations on input modalities performed to validate multimodal capability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
