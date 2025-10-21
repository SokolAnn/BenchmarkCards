# LVLM-eHub: A Comprehensive Evaluation Benchmark for Large Vision-Language Models

## 📊 Benchmark Details

**Name**: LVLM-eHub: A Comprehensive Evaluation Benchmark for Large Vision-Language Models

**Overview**: This paper presents a comprehensive evaluation of publicly available large multimodal models by building an LVLM evaluation Hub (LVLM-eHub). LVLM-eHub consolidates 8 representative LVLMs and comprises a quantitative capability evaluation (6 categories of multimodal capabilities evaluated on 47 standard text-related visual benchmarks) and an online arena platform (anonymous randomized pairwise human battles) to provide user-level evaluation in open-world question-answering scenarios.

**Data Type**: multimodal (image and text; question-answering pairs, image-caption pairs)

**Domains**:
- Natural Language Processing
- Computer Vision
- Robotics

**Similar Benchmarks**:
- POPE
- ImageNetVC
- GVT

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation benchmark (LVLM-eHub) for large vision-language models by (1) conducting extensive quantitative evaluation across six categories of multimodal capabilities on 47 text-based visual tasks and (2) offering an online LVLM Arena for anonymous pairwise human evaluation in open-world scenarios.

**Tasks**:
- Image Classification
- Object Counting
- Multi-class Identification
- Optical Character Recognition
- Key Information Extraction
- Image Captioning
- Visual Question Answering
- Knowledge-Grounded Image Description
- Visual Entailment
- Visual Commonsense Reasoning
- Embodied Intelligence / Planning

**Limitations**: Online LVLM Arena currently supports only single-round chats due to high computational and memory demands; LVLM Arena requires significant human effort to produce reliable rating results; existing automated metric CIDEr is often unsuitable for LVLM image captioning evaluation due to diverse model outputs.

## 💾 Data

**Source**: Collected from 47 standard text-related visual benchmarks. Datasets explicitly used include ImageNet1K, CIFAR10, Pets37, Flowers102, IIIT5K, IC13, IC15, Total-Text, CUTE80, SVT, SVTP, COCO-Text, WordArt, CTW, HOST, WOST, SROIE, FUNSD, NoCaps, Flickr30K, MSCOCO (COCO-Random/Popular/Adversarial for object hallucination), VQA datasets (DocVQA, TextVQA, STVQA, OCR-VQA, OKVQA, GQA, IconQA, VSR, Visdial), ScienceQA, VizWiz, SNLI-VE, ImageNetVC, VCR, and embodied benchmarks (Minecraft, VirtualHome, Meta-World, Franka Kitchen).

**Size**: 47 benchmarks (40+ datasets). Example evaluation split sizes reported: ImageNet1K 50,000 (val), CIFAR10 10,000 (test), Pets37 3,669 (test), Flowers102 6,149 (test), OCR datasets (varying: IIIT5K 3,000 test, IC13 848 train, IC15 2,077 test, etc.), COCO-derived object-hallucination sets MSCOCO-Random/Popular/Adversarial 3,000 (val) each, ImageNetVC 10,000 (rank), NoCaps 4,500 (val), Flickr-30k 1,000 (test).

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation via prompting
- Question Answering prompting
- Prefix-based score (likelihood-based selection for multi-choice)
- Multi-turn reasoning (Questioner-Answerer-Reasoner pipeline using LLMs and LVLMs)
- User study (human evaluation for embodied tasks)
- LVLM Arena (crowd-sourced pairwise battles with human voting and Elo rating)
- Automated metrics computed per task

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- CIDEr Score
- Mean Reciprocal Rank (MRR)
- Top-1 Accuracy
- Word accuracy
- Entity-level F1
- Prefix-based score
- Elo rating

**Calculation**: Metrics are computed per task as described: accuracy for classification/OC/MCI and hallucination accuracy; word accuracy for OCR; entity-level F1 for KIE; CIDEr for image captioning; MRR for Visdial; top-1 accuracy for most VQA tasks. Average scores for capability categories are obtained by normalizing per-row and averaging. Elo rating is updated from human votes in LVLM Arena. POPE pipeline for object hallucination uses multiple yes/no questions per image and reports accuracy, precision, recall, F1, and probability of answering 'Yes'.

**Interpretation**: Higher metric values indicate better performance per the task metric. Authors note CIDEr can be unsuitable for LVLM caption evaluation due to diverse outputs; Elo rating reflects human preference in open-world scenarios; multi-turn reasoning can improve evaluation reliability for instruction-tuned models and mitigate object hallucination.

**Baseline Results**: Supervised SOTA results are reported for comparison in tables (examples: ImageNet1K S-SOTA 91.10, CIFAR10 S-SOTA 99.70, Pets37 S-SOTA 96.70, Flowers102 S-SOTA 99.64). LVLM model results across tasks are presented in tables (e.g., per-model scores for visual perception, OCR, VQA, object hallucination, embodied tasks).

**Validation**: Validation includes: anonymized randomized pairwise human evaluation (LVLM Arena) with collected votes (634 and 1,425 samples on two dates), user studies (15 participants for embodied tasks), and evaluation on held-out validation/test splits of established datasets. Multi-turn reasoning uses ChatGPT as Reasoner and Questioner for SNLI-VE and VCR evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Potential Harm**: ['Object hallucination (models generating objects inconsistent with target images)', 'Overfitting leading to poor generalization in open-world scenarios']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
