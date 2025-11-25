# SysNoise: Exploring and Benchmarking Training-Deployment System Inconsistency

## 📊 Benchmark Details

**Name**: SysNoise: Exploring and Benchmarking Training-Deployment System Inconsistency

**Overview**: This work introduces SysNoise, a benchmark and framework to quantitatively measure the impact of training-deployment system inconsistency (SysNoise) on model robustness. The benchmark evaluates SysNoise across image classification, object detection, instance/semantic segmentation and natural language processing on 20+ models, measuring how differences in pre-processing, model inference, and post-processing implementations affect performance.

**Data Type**: image (image classification / object detection / segmentation datasets) and text (natural language processing datasets)

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ImageNet-C
- ImageNet-P
- ImageNet-A
- ImageNet-O
- RobustBench
- RobustART
- DEEPSEC
- RealSafe

**Resources**:
- [Resource](https://modeltc.github.io/systemnoise_web)
- [Resource](https://arxiv.org/abs/2307.00280)

## 🎯 Purpose and Intended Users

**Goal**: To identify and systematically evaluate SysNoise (pre-processing, model inference, post-processing) caused by training-deployment system inconsistencies, and to build a benchmark and framework to quantitatively measure its impact on model robustness across vision and NLP tasks.

**Target Audience**:
- Algorithm Researchers
- Hardware Vendors

**Tasks**:
- Image Classification
- Object Detection
- Instance Segmentation
- Semantic Segmentation
- Natural Language Processing
- Text-to-Speech

**Limitations**: The authors note there may still exist other noises not covered by the benchmark and that some noises require specific hardware and are not easy to reproduce. They plan to extend the benchmark to more tasks and real-world systems in future work.

## 💾 Data

**Source**: ImageNet-1K (ImageNet), MS COCO, CitySpace, NLP datasets PIQA, LAMBADA, HellaSwag, WINOGRANDE, LJ Speech (for TTS). The authors also provide generated system-noise variants of ImageNet and COCO validation sets available on the project website.

**Size**: 13,100 audio clips (about 24 hours) for LJ Speech; sizes for ImageNet, COCO, CitySpace, and NLP datasets are not specified in the paper.

**Format**: N/A

**Annotation**: Use original dataset annotations from official releases; system-noise variants are generated from the original datasets.

## 🔬 Methodology

**Methods**:
- Automated evaluation using task metrics (Top-1 accuracy, mAP, mIoU, MSE)
- Controlled system-implementation perturbations across three stages: pre-processing, model inference, post-processing
- Combined-noise (worst-case) analysis by adding multiple SysNoise types
- Comparative analysis with data augmentation methods, adversarial training, and test-time adaptation (TENT)

**Metrics**:
- Top-1 Accuracy
- Mean Average Precision (mAP)
- Mean Intersection over Union (mIoU)
- Mean Square Error (MSE)
- Delta metrics (∆ACC, ∆mAP, ∆mIoU) reported as differences between clean and SysNoise evaluations

**Calculation**: Metric differences are calculated as ∆ACC = ACC_original - ACC_SysNoise (similarly ∆mAP = mAP_original - mAP_SysNoise, ∆mIoU = mIoU_original - mIoU_SysNoise). For SysNoise with multiple options, both mean and max differences are reported; otherwise the single metric difference is reported.

**Interpretation**: Lower ∆ (difference) indicates better robustness to SysNoise. Large positive ∆ values indicate significant performance degradation caused by system inconsistency.

**Baseline Results**: The benchmark evaluates 20+ models. Key reported worst-case impacts include up to 9.97% Top-1 accuracy drop on classification and up to 10.67 mAP drop on detection. Detailed per-model results are reported in Tables 2-5 of the paper.

**Validation**: Reproducibility measures include fixing software versions (torch==1.8.1, opencv==4.1.1.26, Pillow==6.2.1) and setting torch.backends.cudnn.benchmark=True. Selected experiments were repeated multiple times with observed differences <0.0001%. Code and generated datasets are provided on the project website for reproducibility.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Governance**: Lack of system transparency
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Model performance degeneration during deployment due to system-implementation mismatch (e.g., up to 9.97% accuracy drop on classification, 10.67 mAP drop on detection).', 'Reliability issues of models across different deployment platforms; potential to negate architecture or model improvements.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Code released under Apache License 2.0. ImageNet-1K, COCO, and CitySpace datasets used are downloaded from their official releases and generated system-noise datasets follow the licenses of the original datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
