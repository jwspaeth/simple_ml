from hydra.utils import instantiate

from simple_ml.utils import setup_ml


def train(return_validation_result=True, ckpt_path=None, **kwargs):
    data_dict, model, trainer = setup_ml(**kwargs)
    trainer.fit(model, ckpt_path=ckpt_path, **data_dict)

    if return_validation_result:
        return 0