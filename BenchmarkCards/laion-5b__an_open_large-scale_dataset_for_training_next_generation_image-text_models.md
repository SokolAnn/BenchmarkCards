# LAION-5B: An open large-scale dataset for training next generation image-text models

## 📊 Benchmark Details

**Name**: LAION-5B: An open large-scale dataset for training next generation image-text models

**Overview**: To address this problem and democratize research on large-scale multi-modal models, we present LAION-5B - a dataset consisting of 5.85 billion CLIP-filtered image-text pairs, of which 2.32B contain English language. We show successful replication and fine-tuning of foundational models like CLIP, GLIDE and Stable Diffusion using the dataset, and discuss further experiments enabled with an openly available dataset of this scale. Additionally we provide several nearest neighbor indices, an improved web-interface for dataset exploration and subset generation, and detection scores for watermark, NSFW, and toxic content detection.

**Data Type**: image-text pairs (multimodal)

**Domains**:
- Natural Language Processing
- Computer Vision
- Multimodal Learning

**Languages**:
- English
- Russian
- French
- German
- Spanish
- Chinese
- Unknown

**Similar Benchmarks**:
- MS-COCO
- CC3M
- Visual Genome
- WIT
- CC12M
- RedCaps
- YFCC100M
- CLIP WIT
- ALIGN
- BASIC

**Resources**:
- [Resource](https://arxiv.org/abs/2210.08402)
- [Resource](https://laion.ai/laion-5b-a-new-era-of-open-large-scale-multi-modal-datasets/)
- [Resource](https://knn5.laion.ai/)
- [GitHub Repository](https://github.com/rvencu/crawlingathome-gpu-hcloud)
- [GitHub Repository](https://github.com/rom1504/img2dataset)
- [GitHub Repository](https://github.com/rom1504/clip-retrieval)
- [GitHub Repository](https://github.com/mlfoundations/open_clip)
- [GitHub Repository](https://github.com/laion-ai/laion5b-bias)
- [GitHub Repository](https://github.com/LAION-AI/laionide)
- [Resource](https://huggingface.co/datasets/laion/laion-high-resolution)
- [GitHub Repository](https://github.com/LAION-AI/LAION-5B-WatermarkDetection)
- [Resource](https://laion.ai/dataset-requests/)

## 🎯 Purpose and Intended Users

**Goal**: Make multimodal training more accessible by assembling a public dataset suitable for training large image-text models and to democratize research on large-scale multi-modal models.

**Target Audience**:
- ML Researchers
- Model Developers
- Academic Researchers
- Safety Researchers
- Domain Experts

**Tasks**:
- Image-Text Representation Learning
- Zero-Shot Image Classification
- Image Retrieval
- Text-to-Image Generation
- Image Captioning
- Few-shot / Transfer Learning
- Fine-tuning Pretrained Models

**Limitations**: LAION-5B is not a finished data product: authors recommend academic-research-only use. Explicit limitations discussed include potential overlap with downstream test sets (data contamination), alt-text quality issues (e.g., SEO spam or incoherent captions), biases and flaws introduced by CLIP-based filtering (ViT-B/32), noisy or weakly-related image-text pairs, imperfect safety tags, and the infeasibility of fully curating such a large dataset within a single paper.

**Out of Scope Uses**:
- Use in deployed production systems (authors advise against any applications in deployed systems without careful investigation).
- Military or surveillance tasks (explicitly identified as inappropriate).

## 💾 Data

**Source**: Assembled from Common Crawl HTML (IMG tags / alt-text) and filtered using OpenAI's CLIP ViT-B/32 (English) and a multi-lingual CLIP for other languages; language detection with CLD3; additional tagging via NSFW and watermark detectors and Q16 pipeline. Starting point was ~50 billion images in Common Crawl; filtered to yield LAION-5B.

**Size**: 5.85 billion image-text pairs total; 2.32 billion English image-text pairs; 2.26 billion multilingual image-text pairs; 1.27 billion unknown-language image-text pairs.

**Format**: Metadata files in Apache Parquet format (per-sample attributes); images are provided as URLs to raw image files; precomputed embeddings and KNN indices (FAISS/PQ) are also provided/generated.

**Annotation**: Automatically generated: CLD3 language detection; CLIP-based cosine-similarity filtering (English threshold >= 0.28; other languages >= 0.26); NSFW and watermark scores computed via CLIP-based detectors and specialized classifiers; Q16 pipeline for inappropriate content tagging. Some manual inspection was used for test/validation sets for watermark and NSFW detectors and for training detector datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (CLIP reproduction)
- Zero-shot evaluation
- Retrieval evaluation (nearest-neighbor using embeddings)
- Fine-tuning and generative model evaluation (GLIDE, Stable Diffusion)

**Metrics**:
- Top-1 Accuracy
- Average top-1 Accuracy (VTAB+ over 35 tasks)
- Recall@1
- Recall@5
- Recall@10
- Mean per-class recall
- CIDEr
- SPICE
- BLEU@4

**Calculation**: Zero-shot classification: prompts collected per class, compute class embedding by averaging prompt embeddings, compute cosine similarity between image and class embeddings, assign class with highest similarity, report top-1 accuracy. VTAB+: average top-1 accuracy over 35 tasks. Retrieval: compute cosine similarity between image and text embeddings and report Recall@K. Generative model evaluations include sample quality comparisons and community-shared metrics where applicable.

**Interpretation**: Authors interpret matching or near-matching performance to prior closed datasets (e.g., OpenAI CLIP trained on WIT) on zero-shot, robustness, retrieval, and downstream tasks as evidence that LAION-5B is suitable for training large image-text models; increases in dataset and compute scale generally improve zero-shot transfer and robustness.

**Baseline Results**: Baselines in the paper are OpenAI CLIP models trained on WebImageText (WIT). The paper reports that models trained on LAION subsets (e.g., LAION-400M, LAION-2B-en) match or come close to OpenAI's CLIP performance on ImageNet zero-shot and other benchmarks (e.g., ViT-L/14 trained on LAION-2B-en achieves ~75.4% ImageNet-1k zero-shot top-1 accuracy compared to CLIP WIT ViT-L/14 ~75.6%, as reported in the paper).

**Validation**: Validation by reproducing CLIP models (ViT-B/32, ViT-B/16, ViT-B/16+, ViT-L/14) trained on LAION-400M and LAION-2B-en and evaluating on ImageNet-1k zero-shot, ImageNet distribution shifts, VTAB+ (35 tasks), retrieval on Flickr30K and MSCOCO, few-shot linear probe experiments, and by fine-tuning generative models (GLIDE, Stable Diffusion) on LAION subsets and inspecting generated samples/benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy
- Transparency
- Intellectual Property

**Atlas Risks**:
- **Privacy**: Personal information in data, Reidentification, Exposing personal information
- **Fairness**: Data bias, Output bias
- **Accuracy**: Data contamination, Unrepresentative data
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Intellectual Property**: Data usage rights restrictions, Copyright infringement
- **Value Alignment**: Toxic output, Harmful output
- **Misuse**: Improper usage, Nonconsensual use, Dangerous use
- **Governance**: Lack of data transparency, Lack of system transparency, Incomplete usage definition
- **Explainability**: Inaccessible training data
- **Legal Compliance**: Generated content ownership and IP
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Amplification of social bias', 'Reproduction of discriminatory behavior', 'Exposure of personal/private information', 'Generation of NSFW or otherwise inappropriate content', 'Misuse for identification or surveillance']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset sourced from publicly crawled web links (Common Crawl). Authors note privacy risks (images with people, medical images, personal information). They provide a contact form and email for removal requests, follow Common Crawl robots.txt, do not store raw image data in the release (provide URLs), and provide tools (search UI) to discover links; authors advise academic-use-only and provide safety tag metadata (NSFW, watermark) but note tags are imperfect.

**Data Licensing**: LAION releases metadata under CC-BY-4.0; authors state they do not own the copyright of the images or text themselves.

**Consent Procedures**: Individuals were not directly notified; dataset follows Common Crawl crawling practices and robots.txt of sites. Authors provide a mechanism (contact form and dataset-requests) to request removal/blacklisting of links.

**Compliance With Regulations**: Authors corresponded with the University of Washington Human Subjects Division and determined IRB review was not required for this work; NeurIPS ethics review determined the work has no serious ethical issues. The paper documents privacy concerns and provides removal mechanisms but does not claim broader regulatory compliance guarantees (e.g., GDPR).
