#!/usr/bin/env python

import os
os.environ["HYDRA_FULL_ERROR"] = "1"
import sys
sys.path.append(os.getcwd())

import hydra
from omegaconf import OmegaConf, open_dict

from simple_ml.train import train


@hydra.main(config_path=None)
def train_from_cfg(cfg):
    OmegaConf.set_struct(cfg, True)
    with open_dict(cfg):
        cfg.pop("experiment_id", None)

    return train(**cfg)

if __name__ == "__main__":
    train_from_cfg()