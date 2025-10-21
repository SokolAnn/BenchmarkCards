# Multi-Modal, Multilingual Instruction Tuning (M3IT) dataset

## 📊 Benchmark Details

**Name**: Multi-Modal, Multilingual Instruction Tuning (M3IT) dataset

**Overview**: The Multi-Modal, Multilingual Instruction Tuning (M3IT) dataset, designed to optimize VLM alignment with human instructions, comprises 40 carefully curated datasets, including 2.4 million instances and 400 manually written task instructions, reformatted into a vision-to-text structure; key tasks are translated into 80 languages.

**Data Type**: multimodal (vision-to-text instances: image-to-text and video-to-text; question-answering pairs, captioning pairs, image-text pairs)

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- Afrikaans
- Amharic
- Modern Standard Arabic
- Assamese
- Asturian
- Belarusian
- Bulgarian
- Bengali
- Bosnian
- Catalan
- Cebuano
- Czech
- Welsh
- Danish
- German
- Greek
- Spanish
- Estonian
- Finnish
- French
- Nigerian Fulfulde
- Galician
- Gujarati
- Hausa
- Hebrew
- Hindi
- Croatian
- Hungarian
- Armenian
- Indonesian
- Igbo
- Icelandic
- Italian
- Japanese
- Javanese
- Georgian
- Kazakh
- Khmer
- Kannada
- Korean
- Kyrgyz
- Luxembourgish
- Ganda
- Ligurian
- Limburgish
- Lingala
- Lao
- Lithuanian
- Standard Latvian
- Maori
- Macedonian
- Malayalam
- Marathi
- Maltese
- Burmese
- Dutch
- Nyanja
- Occitan
- Eastern Panjabi
- Polish
- Portuguese
- Romanian
- Russian
- Sindhi
- Slovak
- Shona
- Somali
- Serbian
- Swedish
- Tamil
- Telugu
- Tajik
- Thai
- Tagalog
- Turkish
- Ukrainian
- Urdu
- Vietnamese
- Wolof
- Chinese (Simplified)

**Similar Benchmarks**:
- MiniGPT4
- LLaVA
- MultiModalGPT
- MultiInstruct
- InstructBLIP

**Resources**:
- [Resource](https://huggingface.co/datasets/MMInstruction/M3IT)
- [Resource](https://arxiv.org/abs/2306.04387)
- [GitHub Repository](https://github.com/i-Eval/FairEval)
- [Resource](https://paperswithcode.com/)

## 🎯 Purpose and Intended Users

**Goal**: To advance instruction tuning research in the multi-modal domain by introducing an open Multi-Modal Multilingual Instruction Tuning (M3IT) dataset to optimize vision-language model alignment with human instructions and enable the development of general-purpose multi-modal agents.

**Target Audience**:
- ML Researchers
- Vision-Language Researchers

**Tasks**:
- Image Captioning
- Visual Question Answering
- Knowledge-based Visual Question Answering
- Image Classification
- Visual Reasoning
- Visual Generation (e.g., visual storytelling, visual dialog)
- Video Captioning
- Video Question Answering
- Multilingual Vision-Language evaluation

**Limitations**: Multilingual translations in the first version are limited to 80 languages and up to 500 samples per split for selected tasks due to computational resource constraints; some source datasets have Unknown or Custom licenses and users are advised to check the original project pages before use; a small portion (<3%) of answers were not successfully paraphrased by ChatGPT and were filtered or templated.

## 💾 Data

**Source**: Compiled from 40 existing vision-language and video-language datasets reformatted into a unified vision-to-text schema (examples include MS COCO, TextCaps, Image-Paragraph-Captioning, VQA v2, OK-VQA, A-OK-VQA, ViQuAE, CLEVR, NLVR, VCR, ImageNet, MSR-VTT, MSRVTT-QA, ActivityNet-QA, iVQA, MSVD-QA and others).

**Size**: 2,429,264 instances (aggregate across tasks; reported as 2.4 million instances overall); 400 manually written task instructions; 40 tasks.

**Format**: Unified JSON-like instance schema with five fields: Images (base64-encoded strings, optionally with bounding-box visual tags), Instruction (selected from a pool), Inputs (task-specific inputs or empty string), Outputs (ground-truth outputs/paraphrased answers), Meta Data (original ids and metadata).

**Annotation**: Manual instruction writing by eight graduate-student annotators (10 instructions per task), answer paraphrasing using ChatGPT, dataset format unification and preprocessing (e.g., bounding-box tagging, short-answer paraphrasing), quality check by separate annotators, and multilingual translation using NLLB-1.3B with automatic BLEU-based filtering.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Model-based evaluation using GPT-4 as a proxy human evaluator
- Zero-shot transfer evaluation (held-out tasks)

**Metrics**:
- ROUGE-L
- GPT-4 human-proxy ratings (scale 1-10 evaluating accuracy, relevance, naturalness)

**Calculation**: ROUGE-L is computed between model predictions and ground-truth answers to assess consistency. GPT-4 is used to rate pairs of responses: for 300 sampled examples from KVQA datasets, GPT-4 rates responses on a 1-10 scale (accuracy, relevance, naturalness) with multiple prompts and averaged scores used to determine winning responses.

**Interpretation**: Higher ROUGE-L indicates greater overlap/consistency with reference answers for conversational responses; higher GPT-4 scores indicate better overall response quality in terms of accuracy, relevance, and naturalness.

**Baseline Results**: Key reported results: KVQA ROUGE-L (OK-VQA / A-OKVQA / ViQuAE): BLIP2-Flan-T5-XXL: 9.1 / 15.6 / 9.7; MiniGPT4: 23.3 / 21.8 / 24.4; InstructBLIP: 7.1 / 5.9 / 7.3; Ying-VLM (trained on M3IT): 27.5 / 24.5 / 29.6. Zero-shot Chinese tasks ROUGE-L (Flickr-8k-CN / FM-IQA / Chinese-FoodNet): MiniGPT4: 9.6 / 20.1 / 5.0; InstructBLIP: 5.2 / 2.3 / 1.0; Ying-VLM: 20.5 / 33.3 / 49.8. Video-language zero-shot ROUGE-L (various tasks): BLIP-2-Flan-T5-XXL: 8.8/11.1/8.9/10.3/13.2; InstructBLIP: 14.3/6.3/9.3/4.0/7.0; Ying-VLM: 14.2/23.5/21.9/18.3/21.4 (reported per-task in paper).

**Validation**: Held-out evaluation sets (some tasks held-out for evaluation); manual quality checks by annotators sampling examples per split; translation quality filtering using BLEU>20 based on FLORES-101 results; small-scale GPT-4 evaluation (300 examples) to proxy human judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Legal/Intellectual Property
- Governance

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Intellectual Property**: Data usage rights restrictions
- **Governance**: Lack of data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licenses for included source datasets were collected from PapersWithCode; many source datasets have 'Unknown' or 'Custom' licenses and some have explicit licenses (e.g., CC-BY 4.0 for some datasets). The authors advise users to check the original project pages or contact dataset owners before use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
