import numpy as np
from easydict import EasyDict as edict
import torch

config = edict()
config.ANCHOR_SIZE = (400, 600)
config.DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


CFG_FIQA = edict()
CFG_FIQA.THRESHOLD = 40
CFG_FIQA.MODEL_PATH = 'model/SDD_FIQA_checkpoints_r50.pth'
CFG_FIQA.EXTEND_RATE = 0.15


CFG_REG = edict()
CFG_REG.BATCH_SIZE = 32

CFG_REG.KNN = edict()
CFG_REG.KNN.THRESHOLD = 0.8
CFG_REG.KNN.NUM_NEIGHBORS = 5

CFG_REG.CROP = edict()
CFG_REG.CROP.FACE_SIZE = (240, 300)
CFG_REG.CROP.EXTEND_RATE = 0


CFG_SMILE = edict()
CFG_SMILE.MODEL_PATH = 'model/smile_score.h5'


VISUALIZE = edict()

VISUALIZE.HEADER = edict()
VISUALIZE.HEADER.COLOR = [255, 0, 0]
VISUALIZE.HEADER.FONT_SCALE = 3
VISUALIZE.HEADER.THICKNESS = 5
VISUALIZE.HEADER.ORG = (400, 1200)

VISUALIZE.BBOX = edict()
VISUALIZE.BBOX.COLOR = [0, 0, 255]
VISUALIZE.BBOX.THICKNESS = 3

VISUALIZE.NOTATIONS = edict()
VISUALIZE.NOTATIONS.SPACE = 40
VISUALIZE.NOTATIONS.COLOR = [255, 0, 0]
VISUALIZE.NOTATIONS.THICKNESS = 2
VISUALIZE.NOTATIONS.FONT_SCALE = 1

VISUALIZE.BACKGROUND = edict()
VISUALIZE.BACKGROUND.WIDTH_EXTENSION = 20
VISUALIZE.BACKGROUND.COLOR = [0, 0, 0]

