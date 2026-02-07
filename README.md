# Crack Segmentation

Pre-trained deep learning model for crack segmentation in images of historic churches, developed within the research project <a href=https://aidabim.dieti.unina.it/>AIDaBIM – Artificial Intelligence to assess structural/seismic Damage to historic heritage in a BIM environment</a><br>
This repository provides a ready-to-use solution for crack segmentation in images of historic churches, including:
<ul>
  <li>a pre-trained deep learning model,</li>
  <li>a sample of the reference dataset used for training/validation,</li>
  <li>a minimal example code to perform inference.</li>
</ul>

This repository is intended for research, evaluation, and demonstration purposes. The provided model and dataset are not meant for safety-critical or operational structural assessments.

## Pre-trained Model

Due to file size limitations, the pre-trained crack segmentation model is not stored directly in this repository.
The model is provided as a TorchScript module and can be downloaded from Google Drive: https://drive.google.com/file/d/13AvEer_20VIG60lp6pryh0vJZdHE7njk/view?usp=sharing

## Repository Structure
The repository is organized as follows:
<ul>
  <li> <code>example.py</code>: Minimal inference script demonstrating how to load the model and perform crack segmentation on a sample image.</li>
  <li> <code>requirements.txt</code>```: List of the minimal runtime dependencies required to execute the example script.</li>
  <li> <code>sample_image.jpg</code>: Example input image used to demonstrate the inference pipeline.</li>
  <li> <code>data.zip</code>: Compressed archive containing a sample of the church image dataset, including crack and non-crack samples, used during model development and validation. The dataset is provided for research and evaluation purposes.</li>
</ul>

## Requirements
The example inference script requires the following libraries:
<ul>
  <li>PyTorch</li>
  <li>NumPy</li>
  <li>OpenCV</li>
  <li>OpenCV</li>
</ul>
All required dependencies are listed in requirements.txt and can be installed with:

```bash
pip install -r requirements.txt
```

## License
This project is released under the **MIT License**. See <a href="https://github.com/aidabimprin2022/crack_segmentation/blob/main/LICENSE">LICENSE</a>.

## Acknowledgment
This work was developed within the AIDaBIM research project. This study received funding from the European Union - Next-Generation-EU - National Recovery and Resilience Plan (NRRP) – MISSION 4 COMPONENT 2, INVESTIMENT N. 1.1, CALL PRIN 2022-D.D. 1409 del 14-09-2022 – AIDaBIM CUP No. E53D23016880001, Grant P20225NAMF.
