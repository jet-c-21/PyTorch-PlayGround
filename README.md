# PyTorch-Playground
The implemented code from [THIS TUTORIAL](https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4) on YouTube

## Environment
- conda
```
conda create --name pytorch python=3.8 -y
```
- Jupyter Kernel
```
conda activate pytorch && \
pip install ipykernel && \
python -m ipykernel install --user --name pytorch --display-name "Pytorch Playground"
```
- torch with GPU
```
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```
