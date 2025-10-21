# Comprehensive Attention Benchmark (CAB)

## 📊 Benchmark Details

**Name**: Comprehensive Attention Benchmark (CAB)

**Overview**: Comprehensive Attention Benchmark (CAB) under a fine-grained attention taxonomy with four distinguishable attention patterns (noncausal self, causal self, noncausal cross, and causal cross). CAB collects seven real-world tasks from different research areas to evaluate efficient attentions under the four attention patterns, validates efficient attentions in eight backbone networks, and benchmarks nine widely-used efficient attention architectures.

**Data Type**: audio (speech waveforms), text (documents and language modeling corpora), time-series (long sequence forecasting), 3D point cloud data, images (low-resolution and high-resolution face images)

**Domains**:
- Computer Vision
- Natural Language Processing
- Speech Processing
- Time Series Forecasting

**Similar Benchmarks**:
- Long Range Arena (LRA)
- SCROLLS

**Resources**:
- [GitHub Repository](https://github.com/Shark-NLP/CAB)
- [Resource](https://arxiv.org/abs/2210.07661)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate efficient attention mechanisms comprehensively under a fine-grained attention taxonomy of four attention patterns (noncausal self, causal self, noncausal cross, causal cross) by collecting seven real-world long-sequence tasks and using eight backbone networks, enabling pattern-wise comparison and exposing fundamental problems of efficient attentions.

**Tasks**:
- Text-to-Speech Synthesis
- Summarization
- Time Series Forecasting
- Point Cloud Completion
- Language Modeling
- Masked Language Modeling
- Image Super-Resolution

**Limitations**: N/A

## 💾 Data

**Source**: Datasets collected for CAB: LJSpeech (TTS), Multi-News (summarization), Electricity Transformer Temperature (ETT) / ECL / Weather (long sequence time-series forecasting), PCN (point cloud completion), PG-19 (language modeling), FFHQ (training for super-resolution) and evaluation on CelebA-HQ (super-resolution).

**Size**: Data lengths from 300 to 16,000 tokens (paper states 'data lengths from 300 to 16,000'). Examples stated: LJSpeech average sequence length 559; Multi-News max source length 4,096 and target 400; PG-19 context length 8,192 for LM experiments; MLM context length 2,048; Super-Resolution uses 16,384 (128x128) input dimension as stated in Table 1; PCC inputs 2,048 points and outputs 14,336 points.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation per task
- Pattern-wise model evaluation across four attention patterns (noncausal self, causal self, noncausal cross, causal cross)
- Compositional Index (CI) aggregation of task metrics
- Efficiency simulation experiments measuring running time and memory on A100 GPU
- Ablation study removing attention mechanism
- Interpolation/extrapolation tests on long-context language modeling

**Metrics**:
- Mean Cepstral Distortion (MCD)
- Mel Spectral Distortion (MSD)
- ROUGE (ROUGE-1, ROUGE-2, ROUGE-L)
- Mean Square Error (MSE)
- Mean Absolute Error (MAE)
- Chamfer Distance (CD)
- F-Score
- Perplexity (PPL)
- Peak Signal-to-Noise Ratio (PSNR)
- Structural Similarity (SSIM)
- Compositional Index (CI)
- Running Time
- Memory Usage
- Efficiency Length

**Calculation**: Compositional Index (CI) calculation: transform metrics so higher is better, normalize each transformed metric with Z-score normalization (using means and standard deviations computed over evaluated models), average normalized metrics within each task, then average across tasks to obtain CI. Efficiency length calculation (Appendix N): fit running time/memory vs sequence length curves (quadratic for vanilla and linear/sub-quadratic for efficient methods) and compute their intersection point; the larger intersection is reported as efficiency length.

**Interpretation**: Higher CI indicates better overall performance across tasks. Efficiency length represents the minimum sequence length where a sub-quadratic efficient model surpasses vanilla attention in running time or memory (smaller efficiency length means the efficient method becomes advantageous at shorter sequence lengths).

**Baseline Results**: Baseline (vanilla attention) results are reported in Table 3. Examples (from Table 3): noncausal self (vanilla) FastSpeech2 MCD 3.475, MSD 1.974; Transformer-TTS MCD 4.095, MSD 2.199; Summarization (Transformer) ROUGE-1 34.61, ROUGE-2 6.35, ROUGE-L 31.66. (Full baseline numbers available in Table 3 of the paper.)

**Validation**: Validation comprised exhaustive experiments across nine efficient attention architectures and eight backbone networks, inter-pattern Pearson correlation analysis of CI, task-to-task correlation analysis, ablation studies, and reporting of means and standard deviations for CI normalization (details in Appendices E, G, H, I).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
