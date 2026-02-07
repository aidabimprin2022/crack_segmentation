# Crack Segmentation

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)

Pre-trained deep learning model for crack segmentation in images of historic churches, developed within the research project <a href=https://aidabim.dieti.unina.it/>AIDaBIM – Artificial Intelligence to assess structural/seismic Damage to historic heritage in a BIM environment</a><br>
This repository provides a ready-to-use solution for crack segmentation in images of historic churches, including:
- a pre-trained deep learning model,
- a sample of the reference dataset used for training/validation,
- a minimal example code to perform inference.

This repository is intended for research, evaluation, and demonstration purposes. The provided model and dataset are not meant for safety-critical or operational structural assessments.

## Pre-trained Deep Learning Model

Due to file size limitations, the pre-trained crack segmentation model is not stored directly in this repository.
The model is provided as a TorchScript module and can be downloaded from Google Drive: https://drive.google.com/file/d/13AvEer_20VIG60lp6pryh0vJZdHE7njk/view?usp=sharing

## Dataset

The file `data.zip` contains a sample of images acquired in the domain of historic churches, used within the AIDaBIM project for training and validation of the crack segmentation model.
The dataset is organized into two main subsets:

- `crack/`: images containing visible cracks or structural lesions;
- `non-crack/`: images showing masonry surfaces without visible damage.

### Crack Subset

The `crack` subset is structured as follows:

- `images/` contains RGB images of masonry surfaces affected by cracks;
- `masks/` contains the corresponding pixel-level crack annotations.

Each image in `images/` has a corresponding mask in `masks/` with the same file name, allowing for straightforward image–mask pairing during training or evaluation.

### Non-crack Subset

The `non-crack` subset contains only the `images/` folder, which includes RGB images of masonry surfaces without visible cracks.
No segmentation masks are provided for the `non-crack` subset, as the corresponding masks would be empty.  
If required by a specific training or evaluation pipeline, empty masks with the same spatial resolution as the input images can be generated programmatically.

## Example Code
The example inference script `example.py` requires a minimal set of runtime dependencies.
All required libraries are listed in `requirements.txt` and can be installed with:

```bash
pip install -r requirements.txt
```

## License
This project is released under the **MIT License**. See <a href="https://github.com/aidabimprin2022/crack_segmentation/blob/main/LICENSE">LICENSE</a>.

## Acknowledgment
This work was developed within the AIDaBIM research project. This study received funding from the European Union - Next-Generation-EU - National Recovery and Resilience Plan (NRRP) – MISSION 4 COMPONENT 2, INVESTIMENT N. 1.1, CALL PRIN 2022-D.D. 1409 del 14-09-2022 – AIDaBIM CUP No. E53D23016880001, Grant P20225NAMF.
