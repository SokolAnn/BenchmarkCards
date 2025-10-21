# Face2Text dataset

## 📊 Benchmark Details

**Name**: Face2Text dataset

**Overview**: An ongoing crowdsourcing effort to collect a corpus of rich textual descriptions of face images taken 'in the wild', aimed at studying how people describe faces and creating a resource to train systems to generate fine-grained, attribute-focused face descriptions.

**Data Type**: image-description pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Flickr8k
- Flickr30k
- VLT2K
- MS COCO
- Caltech-UCSD Birds
- Oxford Flowers-102
- Multi30k
- LFW (Labeled Faces in the Wild)
- MegaFace
- IJB-C
- LFWA
- CelebA

**Resources**:
- [GitHub Repository](https://github.com/mtanti/face2text-dataset/)
- [Resource](http://tamaraberg.com/faceDataset/)
- [Resource](http://rival.research.um.edu.mt/facedesc/)
- [Resource](https://arxiv.org/abs/1803.03827v2)

## 🎯 Purpose and Intended Users

**Goal**: To create a corpus of human face images annotated with rich textual descriptions to investigate how users describe faces and to provide a resource to train systems to generate varied and rich face descriptions.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Vision and Language researchers

**Tasks**:
- Image Captioning
- Image-to-Text Generation
- Natural Language Generation

**Limitations**: Preliminary version; current dataset consists of 400 images and 1,400 descriptions. The annotation category 'inference' showed lower agreement and requires a more precise definition. Ethically problematic descriptions will be filtered prior to dissemination.

**Out of Scope Uses**:
- Identifying recognisable faces by name is prohibited (No recognisable faces are to be identified by name).

## 💾 Data

**Source**: 400 images selected from the Faces in The Wild dataset (Berg et al., 2005); descriptions collected via a custom-made crowdsourcing website.

**Size**: 400 images; 1,400 descriptions collected from 185 participants; all 400 images described at least 3 times (approximately 270 images have 4 descriptions).

**Format**: N/A

**Annotation**: Manual annotation by members of the RIVAL team (8 annotators + 1 control annotator) on a subset of descriptions using yes/no questions about categories (garbage, inferred/external, emotional state, physical attributes, hate speech); agreement measured via Fleiss's kappa.

## 🔬 Methodology

**Methods**:
- Crowdsourcing data collection via a custom website
- Human annotation (yes/no categorical labels) on a subset
- Inter-annotator agreement analysis

**Metrics**:
- Fleiss's kappa (inter-annotator agreement)
- Proportion of positive responses (percentages) per question
- Mean agreement with control annotator (with standard deviations)

**Calculation**: Fleiss's kappa was computed on a shared subset of 20 descriptions annotated by all 9 participants (8 annotators + 1 control). Proportions of positive responses were computed across descriptions (excluding those marked as 'garbage'). Mean agreement with the control annotator was computed for each annotator over their assigned descriptions, with standard deviations reported.

**Interpretation**: Most annotation questions had high levels of agreement (Fleiss's kappa ≥ 0.7) except for the 'inference' question which had lower agreement (kappa = 0.48), indicating that the definition of 'inferred' is open to interpretation.

**Validation**: Validation via a shared subset of 20 descriptions annotated by all annotators; a control annotator annotated these 20 plus an additional 160 descriptions (20 from each annotator) to compute agreement with individual annotators; Fleiss's kappa and mean agreement with the control annotator were used to validate annotation reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Misuse

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Spreading toxicity

**Demographic Analysis**: Participant demographic data collected: gender, age bracket, country of origin, and self-rated English proficiency; authors intend to correlate description features with describer demographics.

**Potential Harm**: ['Detection and filtering of racially or sexually offensive descriptions (hate speech) prior to dissemination']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants were instructed not to identify recognisable faces by name; demographic information (gender, age bracket, country of origin, English proficiency) was collected from participants; authors intend to filter ethically problematic descriptions prior to dissemination.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participation was voluntary; no financial incentives were offered; participants could interrupt and resume the session (session variables saved).

**Compliance With Regulations**: Not Applicable
