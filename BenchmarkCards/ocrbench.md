# OCRBench

## 📊 Benchmark Details

**Name**: OCRBench

**Overview**: To facilitate the assessment of Optical Character Recognition (OCR) capabilities in Large Multimodal Models, we propose OCRBench, a comprehensive evaluation benchmark. OCRBench contains 29 datasets and a curated set of 1000 manually filtered and corrected question-answer pairs covering five representative text-related tasks (Text Recognition, Scene Text-Centric VQA, Document-Oriented VQA, Key Information Extraction, and Handwritten Mathematical Expression Recognition). The benchmark and evaluation pipeline are available at https://github.com/Yuliang-Liu/MultimodalOCR .

**Data Type**: multimodal (image and question-answer pairs)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMBench
- MME
- VLMevalkit

**Resources**:
- [GitHub Repository](https://github.com/Yuliang-Liu/MultimodalOCR)

## 🎯 Purpose and Intended Users

**Goal**: Provide a comprehensive evaluation benchmark (OCRBench) to assess the OCR capabilities of Large Multimodal Models across five text-related visual tasks and offer baseline results to guide future zero-shot multimodal method development.

**Tasks**:
- Text Recognition
- Scene Text-Centric Visual Question Answering
- Document-Oriented Visual Question Answering
- Key Information Extraction
- Handwritten Mathematical Expression Recognition

**Limitations**: OCRBench currently lacks comprehensive coverage of image data types and tasks (e.g., multilingual documents, more diverse capture scenarios) and does not include text detection tasks. The benchmark is limited to 1000 manually curated question-answer pairs.

## 💾 Data

**Source**: Compiled from 29 existing OCR-related datasets (examples listed in paper include IIIT5K, SVT, IC13, IC15, SVTP, CT80, COCO-Text, SCUT-CTW1500, Total-Text, WOST, HOST, WordArt, IAM, ReCTS, ORAND-CAR-2014, ST/NST constructed from IIIT5K dictionary, STVQA, TextVQA, OCRVQA, ESTVQA, DocVQA, InfographicVQA, ChartQA, SROIE, FUNSD, POIE, HME100K, etc.). See Table 5 and appendix in the paper for full composition.

**Size**: 1000 question-answer pairs (compiled from 29 datasets); Text Recognition component: 300 images; Scene Text-Centric VQA: 200 questions; Document-Oriented VQA: 200 questions; Key Information Extraction: 200 questions; HMER: 100 images.

**Format**: N/A

**Annotation**: All 1000 question-answer pairs have been manually filtered and corrected; alternative correct answer candidates provided for evaluation.

## 🔬 Methodology

**Methods**:
- Automated metrics (presence-based matching of ground truth in model outputs)
- Manual verification and correction of dataset answers

**Metrics**:
- Presence-based ground truth inclusion (binary match)
- Average Normalized Levenshtein Similarity (ANLS) (mentioned as not suitable for zero-shot LMM outputs)

**Calculation**: A unified criterion: determine whether the ground truth (GT) is present in the model output. Questions with answers containing fewer than 4 symbols are filtered out to reduce false positives. For large datasets, 3000 question instances were sampled for testing where applicable.

**Interpretation**: Higher presence-based match rates indicate better OCR capability of the evaluated model. Results are compared across models and against supervised SOTA references provided in the paper.

**Baseline Results**: Selected OCRBench final scores (Table 3): Gemini: 659; GPT4V: 645; Monkey: 514; mPLUG-Owl2: 366; LLaVAR: 346. (Per-task breakdowns and full model rankings are provided in the paper's tables.)

**Validation**: Dataset answers were manually verified and corrected; alternative correct answer candidates were provided to improve evaluation accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Governance

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Governance**: Lack of testing diversity, Lack of data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
