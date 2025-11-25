# VL-CheckList

## 📊 Benchmark Details

**Name**: VL-CheckList

**Overview**: VL-CheckList is a novel explainable framework to understand the capabilities of pre-trained Vision-Language Pretraining (VLP) models. The method divides image-texting ability into three categories (object, attribute, relation), applies a taxonomy to break down these aspects, uses a linguistic-aware negative sampling strategy to generate hard negatives, evaluates models via Image-Text Matching (ITM) without fine-tuning, and provides a toolbox for generating capability-specific evaluation reports.

**Data Type**: image-text pairs (image-text matching pairs)

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- CheckList
- Vision CheckList
- Dynabench
- TIDE

**Resources**:
- [GitHub Repository](https://github.com/om-ai-lab/VL-CheckList)
- [Resource](https://arxiv.org/abs/2207.00221)
- [Resource](https://www.sbert.net/)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate VLP models' fundamental capabilities (object, attribute, relation) using Image-Text Matching (ITM) and a taxonomy-driven, linguistic-aware negative sampling strategy to generate fine-grained, disentangled evaluation reports.

**Target Audience**:
- ML Researchers
- Model Developers
- System Designers
- The research community (users of the open-source toolbox)

**Tasks**:
- Image-Text Matching
- Object presence recognition
- Attribute recognition/classification
- Relation recognition/classification (spatial and action relations)

**Limitations**: The paper states they have not yet comprehensively investigated why high ITM-scored models sometimes achieve lower scores on downstream tasks; for a certain downstream task, how it is fine-tuned may be more critical to model performance.

## 💾 Data

**Source**: Four existing corpora used to build capability-specific evaluation sets: Visual Genome (VG), SWiG, VAW, and HAKE.

**Size**: Visual Genome (VG): 108K examples; VAW: 72K examples; HAKE: 104K examples; SWiG: 126K examples.

**Format**: N/A

**Annotation**: Uses dataset-provided structured annotations: Visual Genome provides attributes, relationships, and region graphs; SWiG provides structured semantic summaries with roles (agent, tool, etc.); HAKE provides relationship annotations between instance activity and body part states; VAW provides attribute annotations.

## 🔬 Methodology

**Methods**:
- Image-Text Matching (ITM) evaluation using pre-trained VLP models' ITM heads (no fine-tuning)
- Linguistic-aware negative sampling to generate hard negative examples by replacing objects/attributes/relations in captions
- Use of structured annotations from VG, SWiG, VAW, HAKE to create capability-specific test sets
- Visualization and analysis including quantitative tables, radar charts, and Grad-CAM attention heatmaps

**Metrics**:
- Accuracy

**Calculation**: Accuracy (acc) is defined as acc = (1/N) * sum_{i=1..N} f(xp_i, xn_i), where f(xp_i, xn_i) = 1 if p(xp_i | I_i) > p(xn_i | I_i) else 0. xp_i is the positive sample, xn_i is the generated negative sample, I_i is the image.

**Interpretation**: A model is counted as correct for a pair if the model's ITM score for the original (positive) text is higher than for the generated negative; accuracy is the fraction of such positive outcomes. Higher accuracy indicates better capability on the tested aspect.

**Baseline Results**: Table 2 (Overall performance) reports average accuracies for seven compared models: LXMERT 72.35, UNITER 72.63, OSCAR 69.31, ViLT 76.82, ALBEF 75.62, TCL 74.57, CLIP 71.65 (per Table 2 in the paper).

**Validation**: Validated by applying VL-CheckList to seven popular VLP models (CLIP, OSCAR, UNITER, LXMERT, ViLT, ALBEF, TCL) using four corpora (VG, SWiG, VAW, HAKE) and showing fine-grained differences and insights not visible from downstream task-only evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Governance**: Lack of testing diversity

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
