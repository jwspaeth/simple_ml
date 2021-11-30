from functools import partial
import os
import sys

import hydra
from hydra.utils import instantiate
from omegaconf import OmegaConf


def load_data(data_cfg): # Deprecate
    data_dict = {}
    if "train_dataloader_cfgs" in data_cfg:
        data_dict["train_dataloaders"] = [instantiate(train_dataloader_cfg) for train_dataloader_cfg in data_cfg.train_dataloader_cfgs]

    if "val_dataloader_cfgs" in data_cfg:
        data_dict["val_dataloaders"] = [instantiate(val_dataloader_cfg) for val_dataloader_cfg in data_cfg.val_dataloader_cfgs]

    if "datamodule_cfg" in data_cfg:
        data_dict["datamodule"] = instantiate(data_cfg.datamodule_cfg)

    return data_dict


def setup_ml(model_cfg, data_cfg, trainer_cfg, seed_cfg=None):
    data_dict = instantiate(data_cfg)
    model = instantiate(model_cfg)
    trainer = instantiate(trainer_cfg)

    return data_dict, model, trainer