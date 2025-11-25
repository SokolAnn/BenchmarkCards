# MAGIC BRUSH

## 📊 Benchmark Details

**Name**: MAGIC BRUSH

**Overview**: The first large-scale, manually annotated dataset for instruction-guided real image editing that covers diverse scenarios: single-turn, multi-turn, mask-provided, and mask-free editing. MAGIC BRUSH comprises over 10K manually annotated triplets (source image, instruction, target image) to support training and evaluation of text-guided image editing models.

**Data Type**: image and text (source image, instruction text, target image triplets)

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Oxford-Flower
- CUB-Bird
- EditBench
- InstructPix2Pix

**Resources**:
- [Resource](https://osu-nlp-group.github.io/MagicBrush)
- [GitHub Repository](https://github.com/OSU-NLP-Group/MagicBrush)
- [Resource](https://huggingface.co/datasets/osunlp/MagicBrush)
- [Resource](https://shorturl.at/alHMO)
- [Resource](https://arxiv.org/abs/2306.10012)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale, manually annotated dataset for instruction-guided real image editing to facilitate training and evaluation of text-guided image editing models, supporting single-/multi-turn and mask-provided/mask-free scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Instruction-guided Image Editing
- Mask-provided Image Editing
- Mask-free Image Editing
- Single-turn Image Editing
- Multi-turn Image Editing

**Limitations**: A small portion of edits (<5%) may contain minor extra modifications not mentioned by the instruction or may look slightly unnatural. MAGIC BRUSH does not contain data for global editing (e.g., style transfer) due to annotation built upon DALL-E 2.

**Out of Scope Uses**:
- Annotators are forbidden from creating any identifiable information (e.g., human faces).

## 💾 Data

**Source**: Source images sampled from MS COCO dataset; annotations collected via Amazon Mechanical Turk crowdworkers who interactively synthesize target images using the DALL-E 2 platform and provide edit instructions, global descriptions, and optional free-form masks.

**Size**: 5,313 edit sessions and 10,388 edit turns total. Splits: Train: 4,512 sessions (8,807 turns); Dev: 266 sessions (528 turns); Test: 535 sessions (1,053 turns).

**Format**: N/A

**Annotation**: Manual annotation by trained crowdworkers on Amazon Mechanical Turk (AMT). Workers pass a qualification quiz, propose textual instructions, global descriptions and free-form masks, interact with DALL-E 2 to synthesize target images, and examples undergo manual post-checks and ongoing spot-checks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- L1 (average pixel-level absolute difference)
- L2 (average pixel-level squared difference)
- CLIP-I (cosine similarity between generated image and ground truth using CLIP embeddings)
- DINO (cosine similarity between generated image and ground truth using DINO embeddings)
- CLIP-T (text-image alignment: cosine similarity between local descriptions and generated images' CLIP embeddings)
- 5-point Likert scale for consistency and image quality
- Multi-choice image comparison
- One-on-one pairwise comparison

**Calculation**: L1 and L2 measure average pixel-level differences between generated images and ground truth. CLIP-I and DINO compute cosine similarity between generated images and ground truth in respective embedding spaces. CLIP-T measures cosine similarity between local descriptions and generated images' CLIP embeddings. For mask-provided settings, L1, L2, and CLIP-T are measured over the masked regions only. Human evaluation includes multi-choice selection, one-on-one comparisons, and individual 5-point Likert ratings.

**Interpretation**: Lower L1 and L2 indicate closer pixel-level similarity. Higher CLIP-I, DINO, and CLIP-T indicate better image quality and text-image alignment. Human evaluation preferences and higher Likert scores indicate better perceived consistency and image quality.

**Baseline Results**: Fine-tuning InstructPix2Pix on MAGIC BRUSH significantly improves performance across metrics and human evaluations. Example (mask-free, single-turn): InstructPix2Pix w/ MagicBrush: L1=0.0625, L2=0.0203, CLIP-I=0.9332, DINO=0.8987, CLIP-T=0.2781. Human multi-choice results: Fine-tuned InstructPix2Pix chosen most frequently for consistency (51) and image quality (49) among top methods (Table 4). Individual evaluation (5-point Likert) average image quality: Fine-tuned InstructPix2Pix 3.6 vs InstructPix2Pix 3.2 vs Text2LIVE 2.8 vs GLIDE 2.8 (Table 6).

**Validation**: Data quality evaluated by inviting five AMT workers to review 500 randomly sampled edit turns (each evaluated 100 turns) scoring consistency and image quality on a 1-5 scale; average consistency 4.1/5.0 and image quality 3.9/5.0. Worker selection included qualification quiz, trial grading, ongoing spot-checks, and elimination for quality failures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Misuse
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Spreading disinformation
- **Privacy**: Personal information in data

**Demographic Analysis**: Class-balanced sampling over 80 MS COCO object classes to increase diversity; final distribution includes 34.0% person-included images.

**Potential Harm**: Malicious users could exploit editing tools to create realistic fake or harmful content, leading to the spread of misinformation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotators are forbidden from creating any identifiable information (e.g., human faces). DALL-E 2 also enforces rules to exclude harmful, inappropriate, or sensitive content. The dataset sources images from COCO which focuses on common objects and context to minimize privacy concerns.

**Data Licensing**: Creative Commons Attribution 4.0 (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
