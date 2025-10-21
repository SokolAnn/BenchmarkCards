# LAMM: Language-Assisted Multi-Modal Instruction-Tuning Dataset, Framework, and Benchmark

## 📊 Benchmark Details

**Name**: LAMM: Language-Assisted Multi-Modal Instruction-Tuning Dataset, Framework, and Benchmark

**Overview**: LAMM is an open-source Language-Assisted Multi-Modal instruction-tuning dataset, framework, and benchmark that provides instruction-response data and an evaluation suite to train and evaluate Multi-modal Large Language Models (MLLMs) on 2D (images) and 3D (point cloud) vision tasks. It includes a dataset for instruction tuning, an extensible MLLM training framework, and a benchmark with two novel evaluation strategies (GPT Metric and Binary Locating Metric) and traditional task-specific metrics.

**Data Type**: image instruction-response pairs; point cloud (3D) instruction-response pairs (instruction-response language pairs paired with visual inputs)

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- LLaVA
- MiniGPT4
- mPLUG-owl

**Resources**:
- [Resource](https://openlamm.github.io/)
- [GitHub Repository](https://github.com/OpenLAMM/LAMM)
- [Resource](https://arxiv.org/abs/2306.06687)

## 🎯 Purpose and Intended Users

**Goal**: To establish LAMM as a growing ecosystem for training and evaluating Multi-modal Large Language Models (MLLMs) by providing a Language-Assisted Multi-Modal instruction tuning dataset, an extensible training framework, and the first quantitative benchmark for MLLMs across diverse 2D and 3D vision tasks.

**Target Audience**:
- Academic researchers
- Open research community

**Tasks**:
- Image Classification
- Fine-grained Classification
- Object Detection
- Keypoint Detection
- Visual Question Answering
- Image Captioning
- Object Counting
- Optical Character Recognition
- Facial Classification
- 3D Object Detection
- 3D Visual Grounding
- 3D Visual Question Answering

**Limitations**: Dataset: generated partly via GPT-API which lacks direct access to visual information and can produce factually incorrect or biased outputs; generated data may reflect inherent biases and truthfulness issues of the GPT model used. Benchmark: metrics may fluctuate due to diversity of language outputs; GPT-eval and binary localization are initial attempts and require further research to improve stability. Framework: provided as a primary baseline with potential for further development.

## 💾 Data

**Source**: Images and point clouds collected from publicly available datasets and converted to instruction-response pairs using GPT-API and template conversion. Referenced sources/datasets include: COCO (COCO Captions, COCO DET, COCO Keypoint), Visual Genome, Bamboo, CIFAR10, VOC2012, Flickr30k, FSC147, SVT, CelebA, SQAimage (ScienceQA image subset), 3RScan, CLEVR3D, 3DSSG, ShapeNet, ScanNet, ScanRefer, ScanQA, Locount, TextVQA.

**Size**: 186,098 image-language instruction-response pairs; 10,262 point cloud-language instruction-response pairs. Benchmark: 2D evaluation uses 11 datasets with over 62,439 samples; 3D evaluation uses 3 datasets with over 12,788 samples.

**Format**: Multi-modal training data formatted as text sequences with special vision tokens (<Img>, </Img> for images; <Pcl>, </Pcl> for point clouds) and tokenized with SentencePiece; vision features represented as 256 tokens (CLIP ViT-L/14 for images) and point-cloud tokens encoded (PointNet++ then CLIP encoder). Training objective: next-token prediction loss over response text.

**Annotation**: Instruction-response pairs generated via GPT-API using self-instruction methods and template pools; many pairs are converted from original dataset annotations (captions, bounding boxes, relations, Bamboo knowledge labels). Manual quality control: iterative cold-start manual checks and random 10% manual sampling to filter formatting issues and incorrect answers.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation (out-of-distribution test sets)
- Fine-tuning evaluation on downstream datasets
- Traditional task-specific automated metrics
- Binary Locating Metric (binary localization check)
- GPT-based scoring (GPT Metric) using GPT to rank/score model outputs
- Inference pipeline with Inference Instruction (Task Definition, Output Structure, Query Questions)
- Entity extraction from model text outputs using NLTK and regular expressions
- Manual data quality checks

**Metrics**:
- Accuracy
- Mean Average Precision (mAP@0.5)
- BLEU Score (BLEU-4)
- Mean Absolute Error (MAE)
- Word Accuracy
- Percentage of Correct Keypoints (PCK)
- GPT-based scoring (GPT Metric)
- Binary Locating Metric

**Calculation**: Traditional Metrics: task-specific standard calculations (e.g., Accuracy for classification/VQA, mAP@0.5 for detection, BLEU-4 for captioning, MAE for counting, Word Accuracy for OCR, PCK for keypoints). Binary Locating Metric: predicted location is considered correct if it falls within the object's ground-truth bounding box. GPT Metric: prompt GPT with task definition, question, and candidate model outputs; GPT assigns scores based on accuracy, relevance, fluency, logical coherence, and information richness; average scores used as metric. Entity extraction: use NLTK and regex to extract noun entities, numbers, and bounding-box coordinates from textual outputs for metric calculation.

**Interpretation**: Higher values indicate better performance for each metric (e.g., higher Accuracy, higher mAP, lower MAE). Binary Locating Metric measures coarse localization ability (binary correct/incorrect). GPT Metric measures judged relevance and quality of generated text beyond surface-token overlap, intended to complement or replace BLEU for long/detailed outputs.

**Baseline Results**: Selected baseline (LAMM) results: CIFAR10 Classification (zero-shot) Accuracy 37.9, (finetune) 91.2; VOC2012 Detection mAP@0.5 (zero-shot) 7.20, (finetune) 13.48; SQAimage VQA Accuracy (zero-shot) 49.88, (finetune) 74.27. 3D ScanNet detection mAP@0.5 (zero-shot) 9.3, (finetune) 11.89; ScanQA 3D VQA (zero-shot) 26.54, (finetune) 99.89. Binary-Loc Metric (LAMM baseline) 31.2; GPT Metric (LAMM baseline) 48.44.

**Validation**: Validation includes zero-shot evaluation on datasets with no overlap with training data and fine-tuning experiments on mainstream tasks. Data quality validated via iterative manual cold-start checks and random manual inspection of 10% of generated data. Benchmark validated by running >200 experiments comparing multiple existing MLLMs (e.g., LLaVA, MiniGPT4, mPLUG-owl) and providing analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy
- Robustness
- Legal compliance
- Governance
- Transparency

**Atlas Risks**:
- **Privacy**: Personal information in data, Exposing personal information
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination
- **Data Laws**: Data usage restrictions
- **Intellectual Property**: Data usage rights restrictions
- **Governance**: Incorrect risk testing
- **Transparency**: Lack of training data transparency

**Potential Harm**: ['Privacy risks to individuals in visual data (faces, license plates) — authors plan obfuscation prior to release', 'Propagation of biases and factual errors from GPT-API-generated training data', 'Unreliable outputs / hallucinations leading to incorrect factual information']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors state intention to obfuscate sensitive information (faces and license plates) before publishing the dataset and performed manual sampling to check generated data for alignment with societal values, privacy, security, toxicity, and fairness.

**Data Licensing**: Source datasets compiled are licensed under Creative Commons (CC-BY) as stated; authors indicate adherence to necessary legal protocols for using source data.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
