# Vision-and-Language Navigation using CMA Policy in Habitat Simulator

> Vision-and-Language Navigation (VLN) agent built using Habitat-Lab, CMA Policy, Matterport3D, and R2R-VLNCE datasets for embodied AI navigation tasks.

---
## Authors

- **Syed Naqi Abbas** - 2024AIB1087  
- **Parth** - 2024AIB1012

# Overview

This project implements and evaluates a Vision-and-Language Navigation (VLN) agent using the Cross-Modal Attention (CMA) policy architecture in Habitat Simulator.

The agent learns to navigate realistic indoor 3D environments from natural language instructions by combining:

- Visual perception
- Language understanding
- Cross-modal attention
- Sequential decision making
- Imitation learning

The implementation is based on the VLN-CE framework using Habitat-Lab.

---

# Features

- CMA-based VLN agent
- Habitat-Lab + Habitat-Sim integration
- Matterport3D environment support
- LSTM instruction encoder
- ResNet visual encoder
- Cross-modal attention fusion
- DAgger imitation learning
- Evaluation using SR and SPL metrics
- Ablation and generalization studies

---

# Repository Structure

```text
.
├── habitat_extensions/
├── sbatch_scripts/
├── scripts/
├── vlnce_baselines/
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
├── run.py
├── stats_RandomAgent_val_unseen.json
├── train.log
└── visual.py
````

---

# System Architecture

```text
Instruction
    ↓
Language Encoder (LSTM)

RGB/Depth Observations
    ↓
Visual Encoder (ResNet)

Cross-Modal Attention (CMA)
    ↓
RNN State Encoder
    ↓
Policy Head
    ↓
Navigation Action
```

---

# Datasets Used

## Matterport3D (MP3D)

Realistic indoor 3D scans containing:

* Multiple room layouts
* Navigation meshes
* RGB and depth observations
* Diverse scene structures

## R2R_VLNCE_v1-3_preprocessed

Vision-and-Language Navigation dataset containing:

* Natural language instructions
* Expert trajectories
* Continuous navigation environments

---

# Action Space

| Action       | Description    |
| ------------ | -------------- |
| MOVE_FORWARD | Move ahead     |
| TURN_LEFT    | Rotate left    |
| TURN_RIGHT   | Rotate right   |
| STOP         | End navigation |

---

# Model Components

## Visual Encoder

A pretrained ResNet-based encoder extracts:

* Semantic scene information
* Spatial layouts
* Navigational cues
* Object features

---

## Language Encoder

An LSTM-based encoder converts instructions into contextual embeddings.

Example instruction:

```text
"Turn right near the kitchen"
```

---

## Cross-Modal Attention (CMA)

The CMA module aligns:

* Visual observations
* Language instructions

This enables grounding of instruction words to relevant visual regions.

Example:

```text
"Turn left at the staircase"
```

The model focuses attention on:

* Staircase-related words
* Staircase regions in the environment

---

## Recurrent State Encoder

Maintains temporal memory for:

* Navigation history
* Previous observations
* Instruction progress tracking

---

## Policy Head

Predicts the next navigation action:

* FORWARD
* LEFT
* RIGHT
* STOP

---

# Training Pipeline

The agent is trained using DAgger imitation learning.

```text
Environment Rollout
    ↓
Expert Action Collection
    ↓
Trajectory Aggregation
    ↓
Policy Training
    ↓
Updated Policy
```

---

# Hyperparameters

| Hyperparameter | Value  |
| -------------- | ------ |
| Learning Rate  | 2.5e-4 |
| Batch Size     | 5      |
| Epochs         | 45     |
| Optimizer      | Adam   |
| Hidden Size    | 256    |

---

# Evaluation Metrics

## Success Rate (SR)

Measures whether the agent reaches the goal successfully.

```math
SR = Successful Episodes / Total Episodes
```

## Success weighted by Path Length (SPL)

Measures both success and trajectory efficiency.

```math
SPL = (1/N) Σ Si * (li / max(pi, li))
```

Where:

* `Si` = Success indicator
* `li` = Shortest path length
* `pi` = Agent path length

---

# Results

| Metric            | Seen   | Unseen |
| ----------------- | ------ | ------ |
| Success Rate (SR) | 0.3000 | 0.3600 |
| SPL               | 0.2583 | 0.3393 |

---

# Generalization Study

## Unseen Environment Evaluation

Observations:

* Performance decreases on unseen scenes
* CMA improves robustness
* Scene diversity affects navigation efficiency

---

## Paraphrased Instructions

Example:

```text
Original:
"Turn left at the sofa"

Paraphrased:
"Take a left near the couch"
```

Observations:

* Minor degradation in performance
* Semantic similarity preserved navigation quality

---

## Reduced Training Data

Observations:

* Smaller datasets reduce SR and SPL
* Larger datasets improve generalization

---

# Ablation Study

## Frozen Visual Encoder

Only the following modules were trained:

* Cross-modal attention
* RNN encoder
* Policy head

Observations:

* Faster convergence
* Lower SR and SPL
* Reduced adaptability

This highlights the importance of visual feature fine-tuning.

---

# Installation

## Install Habitat-Lab

This project is developed with Python 3.6. If you are using [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [anaconda](https://anaconda.org/), you can create an environment:

```bash
conda create -n vlnce python=3.6
conda activate vlnce
```

VLN-CE uses [Habitat-Sim](https://github.com/facebookresearch/habitat-sim/tree/v0.1.7) 0.1.7 which can be [built from source](https://github.com/facebookresearch/habitat-sim/tree/v0.1.7#installation) or installed from conda:

```bash
conda install -c aihabitat -c conda-forge habitat-sim=0.1.7 headless
```

Then install [Habitat-Lab](https://github.com/facebookresearch/habitat-lab/tree/v0.1.7):

```bash
git clone --branch v0.1.7 git@github.com:facebookresearch/habitat-lab.git
cd habitat-lab
# installs both habitat and habitat_baselines
python -m pip install -r requirements.txt
python -m pip install -r habitat_baselines/rl/requirements.txt
python -m pip install -r habitat_baselines/rl/ddppo/requirements.txt
python setup.py develop --all
```

## Clone Repository

```bash
git clone https://github.com/syed-naqi-abbas/vlnce
cd vlnce
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---
## Data

#### Scenes: Matterport3D

Matterport3D (MP3D) scene reconstructions are used. The official Matterport3D download script (`download_mp.py`) can be accessed by following the instructions on their [project webpage](https://niessner.github.io/Matterport/). The scene data can then be downloaded:

```bash
# requires running with python 2.7
python download_mp.py --task habitat -o data/scene_datasets/mp3d/
```

Extract such that it has the form `data/scene_datasets/mp3d/{scene}/{scene}.glb`. There should be 90 scenes.

#### Task Dataset

| Dataset | Extract path | Size |
|-------------- |---------------------------- |------- |
| [R2R_VLNCE_v1-3_preprocessed.zip](https://drive.google.com/file/d/1fo8F4NKgZDH-bPSdVU3cONAkt5EW-tyr/view) | `data/datasets/R2R_VLNCE_v1-3_preprocessed` | 250 MB |

##### Encoder Weights

Baseline models encode depth observations using a ResNet pre-trained on PointGoal navigation. Those weights can be downloaded from [here](https://github.com/facebookresearch/habitat-lab/tree/v0.1.7/habitat_baselines/rl/ddppo) (672M). Extract the contents to `data/ddppo-models/{model}.pth`.

## Download Checkpoints

Download pretrained CMA weights from the following Google Drive link:

```text
https://drive.google.com/drive/folders/1KeUseBAxJlHwUd20EzZlZHpuyCZg615T?usp=sharing
```

Place the downloaded weights inside:

```text
data/checkpoints/cma/
```

Example:

```text
data/checkpoints/cma/ckpt.11.pth
```

---

# Training

```bash
python run.py \
  --exp-config vlnce_baselines/config/r2r_baselines/cma.yaml \
  --run-type train
```

---

# Evaluation

```bash
python run.py \
  --exp-config vlnce_baselines/config/r2r_baselines/cma.yaml \
  --run-type eval
```

---

## TensorBoard

```bash
tensorboard --logdir data/tensorboard_dirs/
```

Open:

```text
http://localhost:6006
```

---
# Challenges Faced

* High GPU memory usage
* Large DAgger trajectory storage
* Long training times
* Habitat-Sim dependency conflicts
* Difficulty balancing SR and SPL
* Generalization gap between seen and unseen environments

---

# Limitations

* Computationally expensive training
* Dependence on pretrained visual encoders
* Difficulty handling ambiguous instructions
* Reduced robustness in unseen environments

---

# Future Work

* Transformer-based multimodal fusion
* Larger language models
* Better exploration strategies
* Memory-augmented navigation
* Reinforcement learning fine-tuning

---

# Acknowledgements

* Habitat-Lab
* Habitat-Sim
* Matterport3D
* PyTorch
* Facebook AI Research

---

# References

1. Habitat-Lab: A Platform for Embodied AI Research
3. Matterport3D Dataset
4. Room-to-Room (R2R) Dataset
5. Cross-Modal Attention for Vision-Language Navigation
6. DAgger: Dataset Aggregation for Imitation Learning
