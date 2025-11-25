# Hausa Visual Genome (HaVG)

## 📊 Benchmark Details

**Name**: Hausa Visual Genome (HaVG)

**Overview**: The Hausa Visual Genome (HaVG) is a dataset that contains the description of an image or a section within the image in Hausa and its equivalent in English. The dataset comprises 32,923 images and their descriptions divided into training, development, test, and challenge test sets. HaVG is intended for Hausa-English machine translation, multi-modal research, and image description tasks.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Machine Translation

**Languages**:
- English
- Hausa

**Similar Benchmarks**:
- Hindi Visual Genome (HVG)
- Visual Genome (VG)
- FLoRes evaluation dataset

**Resources**:
- [Resource](https://arxiv.org/abs/2205.01133)
- [GitHub Repository](https://github.com/abumafrim/visual-genome-dataset-creation-tool)
- [Resource](http://hdl.handle.net/11234/1-4749)
- [Resource](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a multimodal dataset (HaVG) suitable for English-to-Hausa machine translation, image captioning, and multimodal research; describe the process of building the dataset and demonstrate sample use cases.

**Target Audience**:
- Researchers
- Model developers

**Tasks**:
- Machine Translation
- Image Captioning
- Multimodal Machine Translation

**Limitations**: Restricted domain (most sentences are in the sports domain, mainly tennis), low lexical diversity (low type-token ratio), and the dataset was created by initial machine translation followed by human post-editing rather than being created from scratch.

**Out of Scope Uses**:
- Commercial use

## 💾 Data

**Source**: Automatically translated from the Hindi Visual Genome (HVG) English captions (derived from the Visual Genome (VG) corpus) using Google Translate, followed by human post-editing by Hausa volunteers using a web-based annotation tool; a secondary manual verification was performed on a sample of 3,500 captions (~10%).

**Size**: 32,923 image-description pairs (Training: 28,930 examples; Development Test: 998 examples; Evaluation Test: 1,595 examples; Challenge Test: 1,400 examples)

**Format**: N/A

**Annotation**: Initial machine translation via Google Translate, followed by post-editing by Hausa volunteers using a web-based annotation tool; a sampled secondary manual verification of 3,500 post-edited captions (~10%) was performed and corrections applied.

## 🔬 Methodology

**Methods**:
- Automated metrics (BLEU Score)
- Human (manual) evaluation of sampled outputs

**Metrics**:
- BLEU Score
- Manual categorization (Correct / Partially correct / Incorrect)

**Calculation**: BLEU scores reported for development (D-Test), evaluation (E-Test), and challenge (C-Test) sets as shown in reported tables. Manual evaluation sampled ~10% of challenge set and categorized outputs as Correct, Partially correct, or Incorrect; separate manual evaluation categories used for image captioning (Match OOI, Match ROI, Other Region, Wrong).

**Interpretation**: Higher BLEU indicates greater n-gram overlap with references. Automatic evaluation showed text-only translation outperforms multimodal translation by BLEU; BLEU for image captioning is low due to diverse valid wordings. Manual evaluation showed multimodal translation resolves lexical ambiguity in a subset (~10%) of sampled cases despite lower BLEU.

**Baseline Results**: Text-to-text translation BLEU: D-Test 31.3, E-Test 46.7, C-Test 17.7. Multimodal translation BLEU: D-Test 15.7, E-Test 22.6, C-Test 8.2. Image captioning BLEU: D-Test 2.6, E-Test 3.1, C-Test 0.7.

**Validation**: Post-editing verification: sampled 3,500 (~10%) of post-edited captions manually verified and corrected. Manual evaluation: ~10% samples from challenge test used to evaluate translation outputs and generated captions, with categorical judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Data Laws**: Data usage restrictions
- **Intellectual Property**: Data usage rights restrictions

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
