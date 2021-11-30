from functools import partial
import os
import sys

import hydra
from hydra.utils import instantiate


def setup_ml(model_cfg, data_cfg, trainer_cfg, seed_cfg=None):
    data_dict = instantiate(data_cfg)
    model = instantiate(model_cfg)
    trainer = instantiate(trainer_cfg)

    return data_dict, model, trainer